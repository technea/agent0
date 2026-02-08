import sys
import os
import subprocess

print(f"Python Executable: {sys.executable}")
print(f"Python Version: {sys.version}")

try:
    import pip
    print(f"Pip Version: {pip.__version__}")
    print("✅ Pip module is installed!")
except ImportError:
    print("❌ Pip module is NOT installed.")
    print("Please reinstall Python and ensure 'pip' is checked during installation.")
    sys.exit(1)

print("\nAttempting to install dependencies via subprocess...")
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("\n✅ Dependencies installed successfully!")
except subprocess.CalledProcessError as e:
    print(f"\n❌ Installation failed with exit code {e.returncode}")
    print("Try running this command manually:")
    print(f"{sys.executable} -m pip install -r requirements.txt")
except Exception as e:
    print(f"\n❌ Unexpected error: {e}")

print("\nPress Enter to exit...")
input()
