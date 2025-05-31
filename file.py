import sys

def get_file_text(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        print("There was an error during runtime")
        sys.exit(1)