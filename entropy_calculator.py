import numpy as np

n = 10000
ps = np.linspace(0.0, 1.0, num=11)

for p in ps:
    sequence = ""
    for i in range(n):
        if np.random.rand() < p:
            sequence += "1"
        else:
            sequence += "0"

    frequency_0 = 0
    frequency_1 = 0
    for digit in sequence:
        if digit == "0":
            frequency_0 += 1
        else:
            frequency_1 += 1

    prob_0 = frequency_0 / n
    prob_1 = frequency_1 / n

    entropy_val = 0.0
    if prob_0 != 0 and prob_1 != 0:
        entropy_val = -prob_0 * np.log2(prob_0) - prob_1 * np.log2(prob_1)

    print("p: {:.1f} - Entropy: {:.4f}".format(p, entropy_val))
