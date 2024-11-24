from flask import Flask, request
import time

app = Flask(__name__)

# Constants for energy cost calculation
price_per_kWh = 1444.70  # Set the price per kWh in your local currency

input_voltage = 0.0
vout = 0.0
current = 0.0

total_energy = 0.0
total_price = 0.0  # Initialize total price

time_interval_seconds = 1  # Adjust this to your time interval in seconds
start_time = time.time()  # Record the start time

@app.route('/data', methods=['POST'])
def receive_data():
    global input_voltage, vout, current, total_energy, total_price, start_time

    try:
        # Simulated values, replace this with actual data from your ESP32
        data = request.get_json()

        # Extract relevant information
        input_voltage = data.get('inputVoltage', 0.0)
        vout = data.get('vout', 0.0)
        current = data.get('current', 0.0)

        # Calculate instantaneous power in watts
        power = input_voltage * current

        # Calculate energy consumed during the time interval in watt-hours
        energy_interval = power * (time_interval_seconds / 3600)  # Convert seconds to hours

        # Add the energy consumed during this interval to the total energy
        total_energy += energy_interval

        # Calculate the total price in Rp.
        total_price = total_energy * (price_per_kWh / 1000)  # Convert Rp. per kWh to Rp. per Wh

        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)


        # Now you have the values in Python variables
        print(f"Input Voltage: {input_voltage:.2f} V")
        print(f"Vout: {vout:.2f} V")
        print(f"Current: {current:.2f} A")
        print(f"Instantaneous Power: {power:.2f} W")
        print(f"Total Energy: {total_energy:.2f} Wh")
        print(f"Total Price: Rp. {total_price:.2f}")
        print(f"Elapsed Time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")
        print("")
        return "OK", 200
    
    except Exception as e:
        print("Error:", e)
        return "Error processing data", 500
    
if __name__ == '__main__':
    app.run(host='192.168.1.25', port=5000, debug=True)

