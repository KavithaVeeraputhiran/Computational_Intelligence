import math

# -------- ACTIVATION FUNCTIONS -------- #
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def threshold(x):
    return 1 if x >= 0 else 0

def tanh(x):
    return math.tanh(x)

def activate(yin, func):
    if func == "sigmoid":
        return sigmoid(yin)
    elif func == "threshold":
        return threshold(yin)
    elif func == "tanh":
        return tanh(yin)
    else:
        raise ValueError("Invalid activation")

# -------- MAIN TRAIN FUNCTION -------- #
def train():
    n = int(input("Enter number of inputs: "))
    m = int(input("Enter number of training samples: "))

    X = []
    T = []

    print("\nEnter inputs and target:")
    for i in range(m):
        while True:
            x = list(map(int, input(f"Sample {i+1} inputs: ").split()))
            if len(x) != n:
                print(f" Enter exactly {n} inputs!")
            else:
                break

        t = int(input(f"Target for sample {i+1}: "))
        X.append(x)
        T.append(t)

    alpha = float(input("\nEnter learning rate (alpha): "))
    max_epochs = int(input("Enter max epochs: "))
    activation = input("Choose activation (sigmoid/threshold/tanh): ").lower()

    weights = [0] * n
    b = 0

    for epoch in range(1, max_epochs + 1):

        print(f"\n========== EPOCH {epoch} ==========")

        header = " ".join([f"x{j+1}" for j in range(n)])
        dw_header = " ".join([f"dw{j+1}" for j in range(n)])
        w_header = " ".join([f"w{j+1}" for j in range(n)])

        print(f"{header} | t | yin | f(yin) | y | {dw_header} | {w_header} | b")
        print("-" * 90)

        # 🔹 Store old weights for comparison
        old_weights = weights.copy()
        old_b = b

        for i in range(m):
            x = X[i]
            t = T[i]

            yin = sum(x[j] * weights[j] for j in range(n)) + b
            y = activate(yin, activation)

            if activation == "sigmoid":
                y_out = 1 if y >= 0.5 else 0
            elif activation == "tanh":
                y_out = 1 if y >= 0 else 0
            else:
                y_out = y

            if y_out == t:
                dW = [0] * n
                db = 0
            else:
                dW = [alpha * x[j] * t for j in range(n)]
                db = alpha * t

                for j in range(n):
                    weights[j] += dW[j]
                b += db

            x_str = " ".join(map(str, x))
            dw_str = " ".join(map(str, dW))
            w_str = " ".join(map(str, weights))

            print(f"{x_str} | {t} | {yin:5.2f} | {y:7.4f} | {y_out} | {dw_str} | {w_str} | {b}")

        #  Convergence check (STRICT)
        if weights == old_weights and b == old_b:
            print(f"\n Training stopped: No weight change in epoch {epoch}")
            break

    else:
        print(f"\nMaximum epochs reached")

    print("\nFinal Weights:", weights)
    print("Final Bias:", b)

# -------- RUN -------- #
train()