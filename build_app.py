import os
import sys
import subprocess

def main():
    print("Locating MediaPipe package...")
    try:
        import mediapipe
    except ImportError:
        print("ERROR: mediapipe is not installed in the current environment.")
        sys.exit(1)
        
    mediapipe_dir = os.path.dirname(mediapipe.__file__)
    mediapipe_modules = os.path.join(mediapipe_dir, "modules")
    
    if not os.path.exists(mediapipe_modules):
        print(f"ERROR: MediaPipe modules directory not found at: {mediapipe_modules}")
        sys.exit(1)
        
    print(f"Found MediaPipe modules at: {mediapipe_modules}")
    
    # We will build the application using PyInstaller.
    # Using sys.executable guarantees we run PyInstaller within this virtual environment.
    add_data_flag = f"{mediapipe_modules}{os.path.pathsep}mediapipe/modules"
    
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--name=HandGesturePuzzle",
        f"--add-data={add_data_flag}",
        "main.py"
    ]
    
    print("\nRunning PyInstaller command:")
    print(" ".join(cmd))
    
    try:
        subprocess.run(cmd, check=True)
        print("\nBuild completed successfully!")
        print("You can find the standalone executable at: dist/HandGesturePuzzle.exe")
    except subprocess.CalledProcessError as e:
        print(f"\nERROR: PyInstaller execution failed: {e}")
        sys.exit(e.returncode)

if __name__ == "__main__":
    main()
