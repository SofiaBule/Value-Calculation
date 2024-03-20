def expected_value(values, probabilities):
    return sum(value * probability for value, probability in zip(values, probabilities))

values = [1, 2, 3, 4, 5, 6]
probabilities = [1/6] * 6  # Assuming fair dice
expected_val = expected_value(values, probabilities)
print(f"Expected value of a fair dice roll: {expected_val}")
