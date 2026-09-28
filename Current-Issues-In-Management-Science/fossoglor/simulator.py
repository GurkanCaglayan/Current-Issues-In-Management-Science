import random
from parameters import *
from basic_rule import simple_rule

def draw_demand(i): #standart sapmayla gerçekleşen talebi çektim
  demand = AVG_demands[i]
  deviation = CV[i] * AVG_demands[i]
  demand = random.gauss(demand, deviation)
  demand = round(demand)
  demand = max(0, demand)
  return demand

def run_twelve_weeks(): #basic rule'u 12 haftalık run ettim
  stock = starting_inventory.copy() 
  total_cost = 0
  for week in range(weeks):
    production = simple_rule(stock)
    for i in range(len(products)):
      stock[i] = production[i] + stock[i]
      if production[i] > 0:
        total_cost = total_cost + setup_cost[i]
      stock[i] = stock[i] - draw_demand(i)
      if stock[i] > 0:
        total_cost = total_cost + stock[i] * holding_cost[i]
      if stock[i] < 0:
        total_cost = total_cost + abs(stock[i]) * penalty_cost[i]
  return total_cost
import time

costs = []
start = time.time()
for k in range(1, 101):
  random.seed(k)
  costs.append(run_twelve_weeks())
duration = time.time() - start

print("Average:", sum(costs) / len(costs))
print("Highest:", max(costs))
print("Time (s):", duration)
