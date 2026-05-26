import sys
import os

if __name__ == "__main__":
    print("  ORACLE STATUS : Reading the Matrix ...  \n")

    try:
        from dotenv import load_dotenv
    except ImportError as e:
        print(f"{e} : Can't import load_dotenv from dotenv.")
        print("Program will exit. Try <pip install python-dotenv>.")
        sys.exit()

    load_dotenv()

    mode: str = os.getenv("MATRIX_MODE")
    database_url: str = os.getenv("DATABASE_URL")
    api_key: str = os.getenv("API_KEY")
    log_level: str = os.getenv("LOG_LEVEL")
    zion_endpoint: str = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded : ")
    print(f"Mode : {mode}")
    print(f"Database : {database_url}")
    print(f"API Access : {api_key}")
    print(f"Log Level : {log_level}")
    print(f"Zion Network : {zion_endpoint}")
