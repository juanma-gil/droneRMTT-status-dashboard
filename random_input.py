import random

x_values = [0]
y_values = [0]
z_values = [0]

bat_values = [100]

# Function to generate random drone data
def generate_random_drone_data():
    x_values.append(x_values[-1] + random.uniform(-1, 1))
    y_values.append(y_values[-1] + random.uniform(-1, 1))
    z_values.append(z_values[-1] + random.uniform(-1, 1))

    bat_values.append(bat_values[-1] + random.uniform(-1, 0))

    return {
        "mid": random.randint(-2, 100),  # Simulate mission pad detection
        "x": x_values[-1],
        "y": y_values[-1],
        "z": z_values[-1],
        "mpry": [ random.uniform(-180, 180), #pitch
            random.uniform(-180, 180), #roll
            random.uniform(-180, 180), #yaw
        ],
        "vgx": random.uniform(-10, 10),
        "vgy": random.uniform(-10, 10),
        "vgz": random.uniform(-10, 10),
        "templ": random.uniform(20, 50),
        "temph": random.uniform(50, 80),
        "tof": random.uniform(0, 200),
        "h": random.uniform(0, 200),
        "bat": bat_values[-1],
        "baro": random.uniform(0, 10),
        "time": random.uniform(0, 600),
        "agx": random.uniform(-10, 10),
        "agy": random.uniform(-10, 10),
        "agz": random.uniform(0, 20),
    }
