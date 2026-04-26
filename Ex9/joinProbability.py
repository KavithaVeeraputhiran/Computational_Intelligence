# Joint probability table
prob_table = {
    "A0": {"B0": 0.10, "B1": 0.15},
    "A1": {"B0": 0.05, "B1": 0.15},
    "A2": {"B0": 0.15, "B1": 0.10},
    "A3": {"B0": 0.05, "B1": 0.11}
}

# Step 1: P(A1, B0)
p_A1_B0 = prob_table["A1"]["B0"]

# Step 2: P(B0)
p_B0 = sum(prob_table[a]["B0"] for a in prob_table)

# Step 3: Conditional probability
p_A1_given_B0 = p_A1_B0 / p_B0

print("P(A1 | B0) =", p_A1_given_B0)