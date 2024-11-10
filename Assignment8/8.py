import time
import random

def sensor_data():
    timestamp = 0
    while True:
        temperature = random.uniform(-10, 50)
        yield (timestamp, temperature)
        timestamp += 1
        time.sleep(0.1)

def filter_by_threshold(data_stream, min_temp=0, max_temp=40):
    for timestamp, temperature in data_stream:
        if min_temp <= temperature <= max_temp:
            yield (timestamp, temperature)

def smooth_temperature(data_stream):
    window = []
    for timestamp, temperature in data_stream:
        window.append(temperature)
        if len(window) > 3:
            window.pop(0)
        if len(window) == 3:
            smoothed_temp = sum(window) / 3
            yield (timestamp, smoothed_temp)

def convert_to_fahrenheit(data_stream):
    for timestamp, temperature in data_stream:
        temperature_fahrenheit = (temperature * 9/5) + 32
        yield (timestamp, temperature_fahrenheit)

def main():
    data = sensor_data()
    filtered_data = filter_by_threshold(data)
    smoothed_data = smooth_temperature(filtered_data)
    fahrenheit_data = convert_to_fahrenheit(smoothed_data)

    for _ in range(20):
        print(next(fahrenheit_data))

if __name__ == "__main__":
    main()
