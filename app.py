from flask import Flask,render_template,request
import numpy as np
import json
import pickle

model=None


app=Flask(__name__)

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

@app.route('/')
def home():
    load_model()
    return render_template('1.html')

@app.route('/predict_price', methods=['POST'])
def predict_price():
    
    # Extract data from the form
    airline = request.form.get('Airline')
    source = request.form.get('Source')
    destination = request.form.get('Destination')
    duration = float(request.form.get('Duration'))
    seat = int(request.form.get('class'))
    stops = int(request.form.get('Stops'))
    days_left = int(request.form.get('daysDifference'))
    dep_time = request.form.get('Departure')
    arr_time = request.form.get('Arrival')

    # Call your price prediction function
    price = price_predict(airline, source, destination, duration, seat, stops, days_left, dep_time, arr_time)

    # Render the HTML template with the predicted price
    return render_template('1.html', price=price)

if __name__ == '__main__':
    load_model()
    app.run(debug=True)