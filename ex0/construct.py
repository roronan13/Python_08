import sys
import os
import site

if __name__ == "__main__":
    print("Matrix status : ", end="")
    if sys.prefix == sys.base_prefix:
        print("you're still plugged in.")
    else:
        print("welcome to the construct.")

    print(f"\nCurrent python : {sys.executable}")
    if sys.prefix != sys.base_prefix:
        print(f"Virtual environment : {os.path.basename(sys.prefix)}")
        print(f"Environment path : {sys.prefix}")
    else:
        print("Virtual environment : NONE")

    if sys.prefix == sys.base_prefix:
        print("\nWARNING : you're in the global environment !")
        print("\nTo enter the construct, run : ")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate")
        print("\nThen run this program again.")
    else:
        print("\nSUCCESS : you're in a isolated environment !")
        print("Package installation path : ", end="")
        print(f"{site.getsitepackages()[0]}")
        print("\n(run deactivate to leave this virtual env)")
