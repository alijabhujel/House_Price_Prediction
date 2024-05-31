import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)
data = pd.read_csv('final_dataset.csv')

def predict():
    bedrooms = request.form.get('beds')
    bathrooms = request.form.get('baths')
    size = request.form.get('size')

try:
    # Ensure the file path is correct
    data = pd.read_csv("train.csv")
    # Display the first few rows of the dataframe
    print("First few rows of the dataframe:")
    print(data.head())
    # Display the last few rows of the dataframe
    print("\nLast few rows of the dataframe:")
    print(data.tail())
    print(data.info())
except FileNotFoundError:
    print("Error: The file 'train.csv' was not found.")
except pd.errors.EmptyDataError:
    print("Error: The file 'train.csv' is empty.")
except pd.errors.ParserError:
    print("Error: There was an error parsing the file 'train.csv'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    app.run(debug=True, port=5000)