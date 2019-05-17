# Ride Cost Calculator
"""
Office Distance *2
Cost Of fuel Per litre
Average of car
"""
distance = int(input())*2
cost = float(input())
average = float(input())

litre_req = distance/average

total_cost = litre_req*cost

print(total_cost)

input()
