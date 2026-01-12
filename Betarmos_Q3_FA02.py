import numpy as np

step_data = np.array([
    [4500, 5200, 4800, 5000, 5300], 
    [4000, 4100, 3900, 4200, 4600], 
    [6000, 5800, 5900, 6100, 6200] 
])

print(f"Psalm's steps on Wednesday: {step_data[2, 2]}")

print(f"My steps... {step_data[0].tolist()}")

print("Updating my Thursday steps to 5500.")
step_data[0, 3] = 5500

print(f"My updated steps: {step_data[0].tolist()}")