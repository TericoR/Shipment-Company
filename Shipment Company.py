
def ground_shipping_cost(weight):
  if weight <= 2:
    cost = weight * 1.50 + 20.00
    return cost
  elif weight > 2 or weight<= 6:
    cost = weight * 3.00 + 20.00
    return cost
  elif weight > 6 or weight <= 10:
    cost = weight * 4.00 + 20.00
    return cost
  else:
    cost = weight * 4.75 + 20.00
    return cost
premium_ground_shipping = 125.00

def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.50 + 0.00
    return cost
  elif weight > 2 or weight <= 6:
    cost = weight * 9.00 + 0.00
    return cost
  elif weight > 6 or weight <= 10:
    cost = weight * 12.00 + 0.00
    return cost
  else:
    cost = weight * 14.25 + 0.00
    return cost
def cheapest_shipping(weight):
  ground = ground_shipping_cost(weight)
  prem = premium_ground_shipping
  drone = drone_shipping(weight)
  if ground < prem and ground < drone:
    return f"The cheapest shipping method is ground shipping. Price: ${ground}"
  elif drone < prem and drone < ground:
    return f"The cheapest shipping method is drone shipping. Price: ${drone}"
  else:
    return f"The cheapest shipping method is premium. Price: ${prem}"

print(cheapest_shipping(41.5))