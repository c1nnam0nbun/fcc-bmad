
from pathlib import Path


def find_project_root(start_path: Path) -> Path:
    current = start_path.resolve()
    while current != current.parent:
        if (current / "_bmad").is_dir():
            return current
        current = current.parent
    return Path.cwd()