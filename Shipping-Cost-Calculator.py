groundShippingFlat = 20.00
premiumGroundShipping = 125.00
# Ground Shipping
def cost_of_ground_shipping(weight):
  if (weight <= 2.0):
    cost = weight * 1.50 + groundShippingFlat
    return(cost)
  elif (weight <= 6.0):
    cost = weight * 3.00 + groundShippingFlat
    return(cost)
  elif (weight <= 10.0):
    cost = weight * 4.00 + groundShippingFlat
    return(cost)
  elif (weight > 10.0):
    cost = weight * 4.75 + groundShippingFlat
    return(cost)
  else:
    print('Shipping is not possible')

# Testing the function

print(cost_of_ground_shipping(8.4))

# Drone Shipping
def cost_of_drone(weight):
  if (weight <= 2.0):
    cost = weight * 4.50
    return(cost)
  elif (weight <= 6.0):
    cost = weight * 9.00
    return(cost)
  elif (weight <= 12.0):
    cost = weight * 4.00
    return(cost)
  elif (weight > 10.0):
    cost = weight * 14.25
    return(cost)
  else:
    print('Shipping is not possible')
print(cost_of_drone(1.5))

# The cheapest method

def cheapest_method(weight):

  ground = cost_of_ground_shipping(weight)
  premium = premiumGroundShipping
  drone = cost_of_drone(weight)

  #Using if statements to tell the cheapest option

  if (ground < premium) and (premium < drone):
    method = "Premium Ground"
    cost = premium 
  else:
    method = "Drone"
    cost = drone

  print("The cheapest option avaiable is $%.2f with %s shipping."
  % (cost,method)
  )
#Calling my function 
cheapest_method(4.8)
