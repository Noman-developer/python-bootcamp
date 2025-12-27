
"""
Python Warm-Up: One-Page Bootcamp Script
---------------------------------------
Concepts covered:
- functions
- lists & dictionaries
- loops
- conditionals
- error handling
- simple CLI interaction
"""

def get_numbers():
    """Ask the user for numbers and return them as a list."""
    raw = input("Enter numbers separated by spaces: ")
    try:
        return [float(n) for n in raw.split()]
    except ValueError:
        print("❌ Please enter valid numbers.")
        return []


def analyze(numbers):
    """Return basic statistics about a list of numbers."""
    if not numbers:
        return None

    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "average": sum(numbers) / len(numbers),
    }


def display(stats):
    """Pretty-print the results."""
    print("\n📊 Analysis Results")
    print("-" * 20)
    for key, value in stats.items():
        print(f"{key.capitalize():>8}: {value}")


def main():
    print("🔥 Python Warm-Up Bootcamp 🔥")
    numbers = get_numbers()

    stats = analyze(numbers)
    if stats:
        display(stats)
    else:
        print("No data to analyze. Try again!")


if __name__ == "__main__":
    main()
