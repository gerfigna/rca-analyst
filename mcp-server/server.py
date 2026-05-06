"""Minimal MCP server exposing tools over SSE transport."""

import os
import pandas as pd
from pathlib import Path

from mcp.server.fastmcp import FastMCP

DATA_ROOT = Path(os.environ.get("DATA_ROOT", "/data/skills"))
DATA_PATH = Path(os.environ.get("DATA_PATH", "/data/data"))

_host = os.environ.get("MCP_HOST", "0.0.0.0")
_port = int(os.environ.get("MCP_PORT", "8000"))
mcp = FastMCP("file-server", host=_host, port=_port)


def _resolve_data(filename: str) -> Path:
    """Resolve a relative path inside DATA_PATH, rejecting traversal attempts."""
    if not filename or filename in (".", "/", ""):
        return DATA_PATH
    # Strip leading slashes so Path("/etc/passwd") doesn't escape the root
    relative = Path(filename.lstrip("/"))
    resolved = (DATA_PATH / relative).resolve()
    if not resolved.is_relative_to(DATA_PATH.resolve()):
        raise ValueError(f"Path '{filename}' is outside the allowed data directory.")
    return resolved


def _resolve(path: str | None) -> Path:
    """Resolve a relative path inside DATA_ROOT, rejecting traversal attempts."""
    if not path or path in (".", "/", ""):
        return DATA_ROOT
    # Strip leading slashes so Path("/etc/passwd") doesn't escape the root
    relative = Path(path.lstrip("/"))
    resolved = (DATA_ROOT / relative).resolve()
    if not resolved.is_relative_to(DATA_ROOT.resolve()):
        raise ValueError(f"Path '{path}' is outside the allowed data directory.")
    return resolved


# @mcp.tool()
def list_files(path: str = "") -> list[dict]:
    """List files and directories inside the shared folder.

    Args:
        path: Sub-path within the shared folder (optional, defaults to root).

    Returns:
        A list of entries, each with 'name', 'type' ('file'|'directory'), and 'size' (bytes, files only).
    """
    target = _resolve(path)
    if not target.exists():
        raise FileNotFoundError(f"Path does not exist: {path!r}")
    if not target.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {path!r}")

    entries = []
    for entry in sorted(target.iterdir()):
        item: dict = {"name": entry.name, "type": "directory" if entry.is_dir() else "file"}
        if entry.is_file():
            item["size"] = entry.stat().st_size
        entries.append(item)
    return entries


@mcp.tool()
def load_skill(name: str) -> str:
    """Load a skill's instructions by name.

    Args:
        name: Skill name (e.g. 'kt-analysis', 'ishikawa', '5-whys', 'rca-prioritization', 'ping').

    Returns:
        The skill's Markdown content as a UTF-8 string.
    """
    target = _resolve(f"{name}.md")
    if not target.exists():
        available = [p.stem for p in DATA_ROOT.glob("*.md")]
        raise FileNotFoundError(
            f"Skill '{name}' not found. Available skills: {available}"
        )
    return target.read_text(encoding="utf-8")


@mcp.tool()
def describe_csv(filename: str) -> str:
    """
    Returns a statistical summary of a CSV file in the data directory.
    Includes: shape, column types, descriptive stats, Pearson correlation matrix,
    and defect rates grouped by defect columns (columns starting with 'defect_').
    Use this to understand the raw process data and find relationships between variables.
    filename: relative path inside the data directory, e.g. 'injection_process_data.csv'
    """
    path = _resolve_data(filename)
    df = pd.read_csv(path, sep=None, engine="python", encoding="utf-8-sig", decimal=",")
    parts = []
    parts.append(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    parts.append(f"Columns: {list(df.columns)}")
    parts.append("\n--- Descriptive Statistics ---")
    parts.append(df.describe().to_string())
    numeric_df = df.select_dtypes(include="number")
    parts.append("\n--- Pearson Correlation Matrix ---")
    parts.append(numeric_df.corr().round(3).to_string())
    defect_cols = [c for c in df.columns if c.startswith("defect_")]
    for col in defect_cols:
        parts.append(f"\n--- Defect Rates by {col} (mean of numeric vars) ---")
        parts.append(df.groupby(col)[numeric_df.columns].mean().round(3).to_string())
    return "\n".join(parts)


@mcp.tool()
def sample_csv(filename: str, n: int = 50, defect_filter: str = "") -> str:
    """
    Returns a sample of rows from a CSV file in the data directory.
    Use this to inspect raw process data and reason about specific cases.
    filename: relative path inside the data directory, e.g. 'injection_process_data.csv'
    n: number of rows to return (default 50, max 200)
    defect_filter: optional column name to filter rows where that column == 1,
                   e.g. 'defect_warp' to see only warp defect cases.
                   Leave empty to get a random sample.
    """
    path = _resolve_data(filename)
    df = pd.read_csv(path, sep=None, engine="python", encoding="utf-8-sig", decimal=",")
    n = min(n, 200)
    if defect_filter and defect_filter in df.columns:
        df = df[df[defect_filter] == 1]
    sample = df.sample(min(n, len(df)), random_state=42)
    return sample.to_string(index=False)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
