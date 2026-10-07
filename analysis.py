import random


def random_sequence(length):
    """Generate a random sequence containing 0s and 1s."""
    return [random.randint(0, 1) for _ in range(length)]


def alternation_rate(sequence):
    """Return the proportion of consecutive values that are different."""
    if len(sequence) < 2:
        return 0

    changes = 0
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i - 1]:
            changes += 1

    return changes / (len(sequence) - 1)


def longest_streak(sequence):
    """Return the length of the longest streak of equal values."""
    if not sequence:
        return 0

    longest = 1
    current = 1

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return longest


def random_comparison(human_sequence, simulations=1000):
    """Compare a human sequence with many random sequences."""
    random_alternations = []
    random_streaks = []

    for _ in range(simulations):
        sequence = random_sequence(len(human_sequence))
        random_alternations.append(alternation_rate(sequence))
        random_streaks.append(longest_streak(sequence))

    average_alternation = sum(random_alternations) / simulations
    average_streak = sum(random_streaks) / simulations

    return average_alternation, average_streak


human = [
    0, 1, 0, 1, 1, 0, 1, 0, 0, 1,
    0, 1, 1, 0, 1, 0, 1, 0, 0, 1
]

human_alternation = alternation_rate(human)
human_streak = longest_streak(human)
random_alternation, random_streak = random_comparison(human)

print("Human sequence:", human)
print()
print("Human alternation rate:", round(human_alternation, 3))
print("Average random alternation rate:", round(random_alternation, 3))
print()
print("Human longest streak:", human_streak)
print("Average random longest streak:", round(random_streak, 3))
