from transform import run_transform
from load import load_to_database

def run_pipeline():
    run_transform()
    load_to_database()

if __name__ == "__main__":
    run_pipeline()