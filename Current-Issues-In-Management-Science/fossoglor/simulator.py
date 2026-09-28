import random
import time #hesaplama süresini ölçmek için
from parameters import *
from basic_rule import basic_rule

def generate_demand(i): #gerceklesecek talebi çektim
  std_dev = param_CV[i] * param_avg_demand[i] #standart sapma hesabı
  observed_demand = random.gauss(param_avg_demand[i], std_dev) #normal dağılımdan talep çek
  observed_demand = round(observed_demand) #tam sayı olması lazım
  observed_demand = max(0, observed_demand) #negatif talep olmaz
  return observed_demand #haftanın gerceklesen talebi

def run_horizon():
  current_stock = param_starting_inventory.copy() #başlangıç stoğunun kopyası asıl liste bozulmasın diyeymis ai önerisi
  total_cost = 0 #run ın maliyeti
  for week in range(param_weeks):
    production_planned_this_week = basic_rule(current_stock) #pazartesi eyleme geçen kural o haftanın üretimini belirler
    for i in range(len(param_products)): #ürün sayısı değişirse diye
      current_stock[i] = production_planned_this_week[i] + current_stock[i] #üretileni stoğa ekliyor
      if production_planned_this_week[i] > 0:
        total_cost = total_cost + param_setup_cost[i]
      current_stock[i] = current_stock[i] - generate_demand(i)
      if current_stock[i] > 0:
        total_cost = total_cost + current_stock[i] * param_holding_cost[i]
      if current_stock[i] < 0: #backlog durumunda
        total_cost = total_cost + abs(current_stock[i]) * param_penalty_cost[i]
  return total_cost

costs_from_runs = [] #her run ın toplam maliyeti
start = time.time()
for seed in range(1, 101):
  random.seed(seed)
  costs_from_runs.append(run_horizon())
duration = time.time() - start

print("Average:", sum(costs_from_runs) / len(costs_from_runs))
print("Highest:", max(costs_from_runs))
print("Time (s):", duration)
