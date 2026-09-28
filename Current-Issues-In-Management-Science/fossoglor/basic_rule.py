from parameters import *

def simple_rule(stock):
  planned_SKUs =  []
  for i in range(len(products)):
    if stock[i] < AVG_demands[i]:
      planned_SKUs.append([stock[i], i])
  planned_SKUs.sort()
  production = [0] * len(products)
  hours_left = weekly_time
  for pair in planned_SKUs:
    i = pair[1]
    units_produced = 3 * AVG_demands[i] - stock[i]
    hours_needed = setup_time[i] + units_produced * prod_time[i]
    if hours_needed <= hours_left:
      production[i] = units_produced
      hours_left = hours_left - setup_time[i] - prod_time[i] * production[i]
    else:
      if hours_left >= setup_time[i] + prod_time[i]:
        production[i] = int((hours_left - setup_time[i]) / prod_time[i])
      break
  return production
