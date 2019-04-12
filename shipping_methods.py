#cost of normal ground shipping
def ground_cost(weight):
  if weight <= 2:
    return (weight * 1.50 + 20.00)
  elif (weight <= 6 and weight > 2):
    return (weight * 3.00 + 20.00)
  elif (weight > 6 and weight <= 10):
    return (weight * 4.00 + 20.00)
  else:
    return (weight * 4.75 + 20.00)
print(ground_cost(4.8))

#cost of premium ground shipping
premium_ground_cost = 125.00 
print(premium_ground_cost)

#cost of drone shipping
def drone_cost(weight):
  if weight <= 2:
    return weight * 4.50
  elif (weight > 2 and weight <= 6):
    return weight * 9.00
  elif (weight > 6 and weight <= 10):
    return weight * 12.00 
  else:
    return weight * 14.25
print(drone_cost(4.8))


#calculate the cheapest way of shipping
def cheapest_shipping(weight):
  ground = ground_cost(weight)
  premium = premium_ground_cost
  drone = drone_cost(weight)
  
  if ground < premium and ground < drone:
    return "You should ship using ground shipping, it will cost " + str(ground)
  elif premium < ground and premium < drone:
    return "You should be using premium ground shipping, it will cost " + str(premium)
  else:
    return "You should be using drone shipping, it will cost " + str(drone)
  
# testing the cheapest_cost function

print(cheapest_shipping(17))
print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))
