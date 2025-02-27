from itertools import permutations
from math import sqrt

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    selected_items = []
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories, total_cost = 0, 0
    
    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_calories += details['calories']
            total_cost += details['cost']
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    food_list = list(items.keys())
    costs = [items[item]['cost'] for item in food_list]
    calories = [items[item]['calories'] for item in food_list]
    n = len(food_list)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Definition of selected dishes
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(food_list[i - 1])
            w -= costs[i - 1]
    
    return selected_items, dp[n][budget]

# Test
budget = 60
print("Greedy Algorithm Result:", greedy_algorithm(items, budget))
print("Dynamic Programming Result:", dynamic_programming(items, budget))
