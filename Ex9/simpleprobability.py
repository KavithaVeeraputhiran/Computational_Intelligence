# Probability of getting sum = 9 when 2 dice are tossed

total_outcomes = 0
favorable_outcomes = 0

# Loop through all possible dice values
for dice1 in range(1, 7):
    for dice2 in range(1, 7):
        total_outcomes += 1
        
        if dice1 + dice2 == 9:
            favorable_outcomes += 1
            print(f"Favorable outcome: ({dice1}, {dice2})")

# Calculate probability
probability = favorable_outcomes / total_outcomes

print("\nTotal outcomes:", total_outcomes)
print("Favorable outcomes:", favorable_outcomes)
print("Probability of getting sum = 9:", probability)