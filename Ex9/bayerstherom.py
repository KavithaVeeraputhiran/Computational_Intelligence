# Bayes Theorem for 3 coins

# Sample space
sample_space = [
    "HHH", "HHT", "HTH", "HTT",
    "THH", "THT", "TTH", "TTT"
]

# Event A: exactly two heads
A = [s for s in sample_space if s.count('H') == 2]

# Event B: first coin is head
B = [s for s in sample_space if s[0] == 'H']

# Intersection A ∩ B
A_intersection_B = [s for s in A if s in B]

# Probabilities
P_A = len(A) / len(sample_space)
P_B = len(B) / len(sample_space)
P_A_given_B = len(A_intersection_B) / len(B)

# Output
print("Sample Space:", sample_space)
print("\nEvent A (Exactly 2 Heads):", A)
print("Event B (First coin is Head):", B)
print("A ∩ B:", A_intersection_B)

print("\nP(A):", P_A)
print("P(B):", P_B)
print("P(A|B):", P_A_given_B)