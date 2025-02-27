import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(n_rolls=1000000):
    sums_count = {i: 0 for i in range(2, 13)}  
    for _ in range(n_rolls):
        roll1 = random.randint(1, 6) 
        roll2 = random.randint(1, 6)  
        dice_sum = roll1 + roll2
        sums_count[dice_sum] += 1
    
    # Calculating probabilities
    probabilities = {s: count / n_rolls for s, count in sums_count.items()}
    return probabilities

def analytical_probabilities():
    return {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 4/36, 7: 6/36,
            8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}

def compare_results(simulated, analytical):
    print("Sum | Monte-Carlo | Analytical")
    print("--------------------------------")
    for i in range(2, 13):
        print(f" {i:2}  | {simulated[i]:.4f}   | {analytical[i]}")

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.bar(sums, probs, color='skyblue', edgecolor='black')
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability')
    plt.title('Monte Carlo Simulation of Two Dice Rolls')
    plt.xticks(range(2, 13))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    for i, v in enumerate(probs):
        plt.text(sums[i], v + 0.002, f'{v:.3f}', ha='center')
    
    plt.show()

# Test
num_rolls = 1000000
probabilities = simulate_dice_rolls(num_rolls)
analytical_probs = analytical_probabilities()
compare_results(probabilities, analytical_probs)
plot_probabilities(probabilities)
