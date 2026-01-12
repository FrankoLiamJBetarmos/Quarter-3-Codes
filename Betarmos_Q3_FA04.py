import numpy as np

names = ["Franko", "Marvoun", "Psalm"]
steps = np.array([
    [4500, 5200, 4800, 5000, 5300], 
    [4000, 4100, 3900, 4200, 4600], 
    [6000, 5800, 5900, 6100, 6200]  
])

totals = np.sum(steps, axis=1)

highest_idx = np.argmax(totals)
highest_name = names[highest_idx]
highest_value = totals[highest_idx]

difference = np.max(totals) - np.min(totals)

print("--- Step Analysis Results ---")
for i in range(len(names)):
    print(f"{names[i]}: {totals[i]} total steps")

print("-" * 30)
print(f"The person with the highest steps is: {highest_name} ({highest_value} steps)")
print(f"Difference between highest and lowest: {difference} steps")