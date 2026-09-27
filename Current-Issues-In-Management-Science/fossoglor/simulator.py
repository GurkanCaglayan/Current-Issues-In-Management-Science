import random
from parameters import *

# Draws one week's demand for product i
def draw_demand(i):
  demand = AVG_demands[i]                  # average weekly demand of product i
  sapma = CV[i] * AVG_demands[i]           # standard deviation = CV x average
  demand = random.gauss(demand, sapma)     # draw one number from the normal distribution
  demand = round(demand)                   # round to the nearest whole number
  demand = max(0, demand)                  # demand cannot be negative: below 0 becomes 0
  return demand                            # give the drawn demand back to the caller

# Simple starting rule: decides this week's production for all 8 products
# stock = list of current stock levels (8 numbers, negative = waiting orders)
def simple_rule(stock):
  planned_SKUs =  []                       # candidates to produce this week, starts empty
  for i in range(8):                       # look at every product, i = 0, 1, ..., 7
    if stock[i] < AVG_demands[i]:          # less than one week of stock?
      planned_SKUs.append([stock[i], i])   # add it as a [stock, product index] pair
  planned_SKUs.sort()                      # sort pairs by the first number: least stock first
  production = [0, 0, 0, 0, 0, 0, 0, 0]    # this week's production per product, starts at 0
  hours_left = weekly_time                 # line hours still free this week
  for pair in planned_SKUs:                # take the candidates one by one, least stock first
    i = pair[1]                            # second element of the pair = product index
    units_produced = 3 * AVG_demands[i] - stock[i]           # bring stock up to three weeks of demand
    hours_needed = setup_time + units_produced * prod_time   # setup hours + production hours
    print(hours_needed)                    # TEMPORARY: check the hours, delete later

print(simple_rule(starting_inventory))     # TEST: run the rule on week 1 stock
