import numpy as np
import json
import pickle

# Global variable to hold the model
model = None

# Load the column names from the JSON file
with open("columns.json", "r") as file:
    data_col = json.load(file)
Columns = data_col["columns"]

def load_model():
    global model
    with open("model.pkl", 'rb') as f:
        model = pickle.load(f)

def price_predict(airline, source, destination, duration, seat, stops, days_left, dep_time, arr_time):
    # Ensure Columns is a list of column names
    airline_col = f"airline_{airline}"
    source_col = f"source_city_{source}"
    destination_col = f"destination_city_{destination}"
    dep_col = f"departure_time_{dep_time}"
    arr_col = f"arrival_time_{arr_time}"

    # Find the index of each column name in Columns
    airline_index = Columns.index(airline_col) if airline_col in Columns else -1
    source_index = Columns.index(source_col) if source_col in Columns else -1
    destination_index = Columns.index(destination_col) if destination_col in Columns else -1
    dep_index = Columns.index(dep_col) if dep_col in Columns else -1
    arr_index = Columns.index(arr_col) if arr_col in Columns else -1

    # Prepare the feature vector
    x = np.zeros(len(Columns))
    x[0] = stops
    x[1] = seat
    x[2] = duration
    x[3] = days_left

    if airline_index >= 0:
        x[airline_index] = 1
    if source_index >= 0:
        x[source_index] = 1
    if destination_index >= 0:
        x[destination_index] = 1
    if dep_index >= 0:
        x[dep_index] = 1
    if arr_index >= 0:
        x[arr_index] = 1

    x = x.reshape(1, -1)
    return model.predict(x)[0]

# Set example input values
airline = "Vistara"
source = "Delhi"
destination = "Mumbai"
duration = 1.5
seat = 0
stops = 0
days_left = 45
dep_time = "Evening"
arr_time = "Morning"


