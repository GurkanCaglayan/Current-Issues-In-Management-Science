from parameters import * #parametreleri al

def basic_rule(current_stock):
  candidates = []
  for i in range(len(param_products)): #aynı sekilde ürün sayısı arttırılırsa diye
    if current_stock[i] < param_avg_demand[i]:
      candidates.append([current_stock[i], i])
  candidates.sort()
  production_planned_this_week = [0] * len(param_products)
  hours_left = param_weekly_time
  for candidate in candidates:
    i = candidate[1]
    target_production = 3 * param_avg_demand[i] - current_stock[i]
    required_hours = param_setup_time[i] + target_production * param_production_time[i]
    if required_hours <= hours_left:
      production_planned_this_week[i] = target_production
      hours_left = hours_left - param_setup_time[i] - param_production_time[i] * production_planned_this_week[i]
    else: #saat yetmeyecekse
      if hours_left >= param_setup_time[i] + param_production_time[i]: #bir tane de olsa üretim yapılabilecekse
        production_planned_this_week[i] = int((hours_left - param_setup_time[i]) / param_production_time[i])
      break
  return production_planned_this_week
