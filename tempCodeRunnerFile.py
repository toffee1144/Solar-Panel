data = request.get_json()

        # Extract relevant information
        input_voltage = data.get('inputVoltage', 0.0)
        current = data.get('current', 0.0)

        # Display the information
        print(f"Input Voltage: {input_voltage:.2f} V")
        print(f"Current: {current:.2f} A")

        # Process the data as needed