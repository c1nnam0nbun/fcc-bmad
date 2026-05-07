import os
import subprocess
from pathlib import Path

def find_project_root(start_path: Path) -> Path:
    current = start_path.resolve()
    while current != current.parent:
        if (current / "_bmad").is_dir():
            return current
        current = current.parent
    return Path.cwd()

def run_setup():
    project_root = find_project_root(Path(__file__))
    skills_root = project_root / "skills"
    print("Skills root:", skills_root)
    
    print("--- FCC MODULE UNIFIED SETUP ---")
    
    # 1. Discover all initialization scripts (scripts/setup.py) in fcc-* skills, excluding fcc-setup itself
    setup_scripts = list(skills_root.glob("fcc-*/scripts/setup.py"))
    setup_scripts = [s for s in setup_scripts if "fcc-setup" not in str(s)]
    
    for script in setup_scripts:
        agent_name = script.parent.parent.name
        print(f"Initializing {agent_name}...")
        subprocess.run(["python", str(script)])

    print("---------------------------------")
    print("FCC Module is fully initialized.")

if __name__ == "__main__":
    run_setup()
