"""
run.py - GENBOT Entry Point
"""

import os
import sys
import subprocess

def main():
    # Ensure dependencies are available
    # Run streamlit
    print("🚀 Launching GENBOT Modular Architecture...")
    
    # Get directory of this script
    root_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(root_dir, "app", "main.py")
    
    # Streamlit requires PYTHONPATH to include the root to find core/modules etc.
    env = os.environ.copy()
    env["PYTHONPATH"] = root_dir + os.pathsep + env.get("PYTHONPATH", "")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", app_path], env=env, check=True)
    except KeyboardInterrupt:
        print("\n👋 Stopping GENBOT.")
    except Exception as e:
        print(f"\n❌ Failed to launch: {e}")

if __name__ == "__main__":
    main()
