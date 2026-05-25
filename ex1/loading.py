import importlib.util
import importlib.metadata
import sys


def installed_with_poetry() -> bool:
    return "poetry" in sys.executable.lower()


def show_packages() -> None:
    all_installed: bool = True

    print("   -- CHECKING DEPENDENCIES --   ")
    if importlib.util.find_spec("pandas"):
        try:
            import pandas
            print(f"[OK] pandas ({importlib.metadata.version('pandas')}) - Data manipulation ready.")
        except ImportError as e:
            print(f"{e} : pandas not imported. Program exited.")
            sys.exit()
    else:
        print("[ERROR] pandas module not found. Program will stop.")
        all_installed = False

    if importlib.util.find_spec("matplotlib"):
        try:
            import matplotlib
            print(f"[OK] matplotlib ({importlib.metadata.version('matplotlib')}) - Visualization ready.")
        except ImportError as e:
            print(f"{e} : matplotlib not imported. Program exited.")
            sys.exit()
    else:
        print("[ERROR] matplotlib module not found. Program will stop.")
        all_installed = False

    if importlib.util.find_spec("numpy"):
        try:
            import numpy
            print(f"[OK] numpy ({importlib.metadata.version('numpy')}) - Numerical computation ready.")
        except ImportError as e:
            print(f"{e} : numpy not imported. Program exited.")
            sys.exit()
    else:
        print("[ERROR] numpy module not found. Program will stop.")
        all_installed = False

    if all_installed is False:
        if installed_with_poetry():
            print("   (You must run <poetry install> with every module present in pyproject.toml)")
        else:
            print("   (You must run <pip install -r requirements.txt> with every module present in requirements.txt)")


if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print("You're not in a virtual environment, \
thanks for creating one before installing packages.")
        sys.exit()

    if installed_with_poetry():
        print("We are in a Poetry virtual env !")
        print(f"({sys.executable})\n")
    else:
        print("We are in a python virtual env using pip !")
        print(f"({sys.executable})\n")

    show_packages()

    if importlib.util.find_spec("numpy") is None or importlib.util.find_spec("matplotlib") is None or importlib.util.find_spec("pandas") is None:
        sys.exit()

    import pandas
    import matplotlib
    import numpy

    print("  == Analyzing Matrix data ... ==  ")
    
    data_size: int = 1000
    timestamps = numpy.arange(data_size)
    matrix_energy = numpy.random.normal(loc=50, scale=10, size=data_size)
    anomaly_level = numpy.random.randint(0, 100, size=data_size)

    data_frame = pandas.DataFrame({"timestamp": timestamps, "energy": matrix_energy, "anomaly": anomaly_level})
    print(f"Processing {len(data_frame)} data points ...")
    print("Statistics : ")
    print(data_frame.describe())

    print("Generating visualization ...")
    matplotlib.figure(figsize=(10, 5))
    matplotlib.plot(data_frame["timestamp"], data_frame["energy"], color="green", label="Matrix energy")
    matplotlib.title("Matrix Energy Analysis")
    matplotlib.xlabel("Time")
    matplotlib.ylabel("Energy")
    matplotlib.legend()
    matplotlib.savefig("matrix_analysis.png")

    print("\nAnalysis complete !")
    print("Results saved to : matrix_analysis.png")
