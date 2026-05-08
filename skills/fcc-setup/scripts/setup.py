import os
import sys
import subprocess
from pathlib import Path

def find_project_root(start_path: Path) -> Path:
    current = start_path.resolve()
    while current != current.parent:
        if (current / ".git").exists() or (current / "_bmad").is_dir():
            return current
        current = current.parent
    return Path.cwd()

def install_dependencies(skill_root: Path):
    req_file = skill_root / "assets/requirements.txt"
    if req_file.exists():
        print(f"Installing dependencies from {req_file}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req_file)])
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")

def run_setup():
    skill_root = Path(__file__).parent.parent
    project_root = find_project_root(skill_root)
    
    # Try both possible locations for skills
    skills_search_paths = [project_root / "skills", project_root / ".agents/skills"]
    
    print("--- FCC MODULE UNIFIED SETUP ---")
    
    # 0. Install core dependencies
    install_dependencies(skill_root)
    
    # 1. Discover all initialization scripts (scripts/setup.py) in fcc-* skills
    setup_scripts = []
    for sp in skills_search_paths:
        if sp.exists():
            setup_scripts.extend(list(sp.glob("fcc-*/scripts/setup.py")))
    
    # Exclude this setup script
    setup_scripts = [s for s in setup_scripts if str(s.resolve()) != str(Path(__file__).resolve())]
    
    executed = set()
    for script in setup_scripts:
        script_path = str(script.resolve())
        if script_path in executed:
            continue
            
        agent_name = script.parent.parent.name
        print(f"Initializing {agent_name}...")
        subprocess.run([sys.executable, script_path])
        executed.add(script_path)

    print("---------------------------------")
    print("FCC Module is fully initialized.")

if __name__ == "__main__":
    run_setup()
