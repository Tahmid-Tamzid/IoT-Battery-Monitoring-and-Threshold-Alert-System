import socket
import time
import random

# Function to simulate battery voltage measurement
def measure_battery_voltage():
    # Simulated battery voltage range (between 10V and 15V)
    min_voltage = 10.0
    max_voltage = 15.0
    
    # Generate a random voltage within the defined range
    voltage = random.uniform(min_voltage, max_voltage)
    
    return voltage

# Function to simulate electrical current measurement
def measure_electrical_current():
    # Simulated electrical current range (between 0A and 5A)
    min_current = 0.0
    max_current = 5.0
    
    # Generate a random current within the defined range
    current = random.uniform(min_current, max_current)
    
    return current

# Function to check voltage thresholds and log messages
def check_thresholds(voltage):
    messages = []
    if voltage < 10:
        messages.append("Battery Voltage is low")
    elif voltage > 14:
        messages.append("Battery Voltage is high")
    return messages

# Function to check electrical current threshold and log message
def check_current_threshold(current):
    if current > 3:
        return "Electrical Current Threshold is crossed"
    return None

# Function to send data to the server via socket
def send_data_to_server(data):
    HOST = '127.0.0.1'  
    PORT = 21        
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data.encode())

# Main function
def main():
    while True:
        # Measure battery voltage and electrical current
        voltage = measure_battery_voltage()
        current = measure_electrical_current()

        # Check voltage thresholds and log messages
        voltage_messages = check_thresholds(voltage)
        
        # Check electrical current threshold and log message
        current_message = check_current_threshold(current)

        # Combine all messages
        messages = voltage_messages + ([current_message] if current_message else [])

        # Send data to server
        data = f"ADN=12344556 & CTD=45678 & BatteryVoltage={voltage} & ElectricalCurrent={current} & Messages={','.join(messages)}"
        send_data_to_server(data)

        # Wait for some time before repeating
        time.sleep(3) 

if __name__ == "__main__":
    main()
