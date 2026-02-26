import engine_core

print("Engine Version:", engine_core.get_version())

amount = 6000
points = engine_core.calculate_points(amount)

print(f"Purchase: {amount} THB")
print(f"Earned Points: {points}")