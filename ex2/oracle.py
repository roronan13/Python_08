import sys
import os

if __name__ == "__main__":
    print("  ORACLE STATUS : Reading the Matrix ...  \n")

    try:
        from dotenv import load_dotenv
    except ImportError as e:
        print(f"{e} : Can't import load_dotenv from dotenv.")
        print("Program will exit. Try <pip install python-dotenv> (in a virtual env if possible).")
        sys.exit()

    load_dotenv()

    mode: str = os.getenv("MATRIX_MODE")
    database_url: str = os.getenv("DATABASE_URL")
    api_key: str = os.getenv("API_KEY")
    log_level: str = os.getenv("LOG_LEVEL")
    zion_endpoint: str = os.getenv("ZION_ENDPOINT")

    missing_variables: list[str] = []
    if mode is None:
        missing_variables.append("MATRIX_MODE")
    if database_url is None:
        missing_variables.append("DATABASE_URL")
    if api_key is None:
        missing_variables.append("API_KEY")
    if log_level is None:
        missing_variables.append("LOG_LEVEL")
    if zion_endpoint is None:
        missing_variables.append("ZION_ENDPOINT")

    if len(missing_variables):
        print("WARNING : some variables are not set : ")
        print(f"{missing_variables}")

    print("\n  Configuration loaded : ")
    print(f"Mode : {mode}")
    print(f"Database : {database_url}")
    print(f"API Access : {api_key}")
    print(f"Log Level : {log_level}")
    print(f"Zion Network : {zion_endpoint}")

    if mode == "development":
        print("You're in development mode !")
    elif mode == "production":
        print("You're are in production mode !")
    else:
        print(f"Careful the mode you're in is weird ({mode}).")
