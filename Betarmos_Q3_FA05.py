import numpy as np

names = ["Franko", "Marvoun", "Psalm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300], 
    [4000, 4100, 3900, 4200, 4600], 
    [6000, 5800, 5900, 6100, 6200]  
])

print("--- Daily Activity Analysis ---")

daily_totals = np.sum(steps, axis=0)

for i in range(len(days)):
    print(f"{days[i]}: {daily_totals[i]} total steps")

best_day_idx = np.argmax(daily_totals)
best_day_name = days[best_day_idx]
best_day_value = daily_totals[best_day_idx]

print("-" * 30)
print(f"The most active day overall was {best_day_name} with {best_day_value} steps!")