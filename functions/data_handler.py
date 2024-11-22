import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.txt')

def display_data():
    """

    """
    try:
        with open(DATA_FILE, 'r') as file:
            data = file.read()
            print("\n--- Data Contents ---")
            print(data if data else "No data available.")
            print("---------------------\n")
    except FileNotFoundError:
        print("Data file not found.")
    except Exception as e:
        print(f"An error occurred while reading the data file: {e}")

def add_data(entry):
    """

    :param entry:
    """
    try:
        with open(DATA_FILE, 'a') as file:
            file.write(entry + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the data file: {e}")
