weight = 41.5
cost_ground_premium = 125

# Ground Shipping
if weight <= 2:
    cost_ground = 20 + (1.50 * weight)
elif 2 < weight <= 6:
    cost_ground = 20 + (3.00 * weight)
elif 6 < weight <= 10:
    cost_ground = 20 + (4.00 * weight)
else:
    cost_ground = 20 + (4.75 * weight)

#Drone Shipping
if weight <= 2:
  cost_drone = 4.5 * weight
elif 2 < weight <= 6:
  cost_drone = 9 * weight
elif 6 < weight <= 10:
  cost_drone = 12 * weight
else:
  cost_drone = 14.25 * weight

print("Ground Shipping $", cost_ground)
print("Premium Ground Shipping $", cost_ground_premium)
print("Drone Shipping $", cost_drone)