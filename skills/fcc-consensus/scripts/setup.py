import os
from pathlib import Path

def find_project_root(start_path: Path) -> Path:
    current = start_path.resolve()
    while current != current.parent:
        if (current / ".git").exists() or (current / "_bmad").is_dir():
            return current
        current = current.parent
    return Path.cwd()

if __name__ == "__main__":
    project_root = find_project_root(Path(__file__))
    consensus_output = project_root / "_bmad" / "output" / "consensus"
    os.makedirs(consensus_output, exist_ok=True)
    print(f"Ensured consensus output directory: {consensus_output}")
