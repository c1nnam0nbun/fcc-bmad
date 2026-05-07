import os
from pathlib import Path

def find_project_root(start_path: Path) -> Path:
    """Traverse up to find the project root marked by the _bmad directory."""
    current = start_path.resolve()
    while current != current.parent:
        if (current / "_bmad").is_dir():
            return current
        current = current.parent
    # Fallback to current working directory if _bmad not found
    return Path.cwd()

def init_sanctum():
    # Dynamically find project root
    project_root = find_project_root(Path(__file__))
    fcc_root = project_root / "_bmad" / "memory" / "fcc"
    
    # Required Subdirectories
    subdirs = [
        fcc_root / "daily",
        fcc_root / "clients",
        fcc_root / "curated",
        fcc_root / "internal" / "fcc-agent-kyc" / "sessions"  # Agent's private sanctum
    ]
    
    for subdir in subdirs:
        subdir.mkdir(parents=True, exist_ok=True)
        print(f"Verified directory: {subdir}")

    # Initialize Index if it doesn't exist
    index_file = fcc_root / "index.md"
    if not index_file.exists():
        with open(index_file, "w", encoding="utf-8") as f:
            f.write("# FCC Compliance Index\n\nTracked reviews and module status.\n\n## Active Client Reviews\n\n(None)\n")
        print(f"Initialized shared index: {index_file}")

if __name__ == "__main__":
    init_sanctum()
