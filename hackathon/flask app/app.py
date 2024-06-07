from flask import Flask, render_template, request
from joblib import load

app = Flask(__name__)

# Load the trained model
model = load('trained_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    engine_speed = float(request.form['engine_speed'])
    vehicle_speed = float(request.form['vehicle_speed'])
    fuel_level = float(request.form['fuel_level'])
    acc_pedal_position = float(request.form['acc_pedal_position'])
    engine_coolant_temp = float(request.form['engine_coolant_temp'])

    # Make prediction using the loaded model
    prediction = model.predict([[engine_speed, vehicle_speed, fuel_level, acc_pedal_position, engine_coolant_temp]])

    # Prepare message based on prediction
    if prediction[0] == 1:
        message = "Neutral driving behavior detected! You can now shift to an appropriate gear for optimal fuel efficiency and vehicle control."
    else:
        message = "Neutral driving behavior not detected."

    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
