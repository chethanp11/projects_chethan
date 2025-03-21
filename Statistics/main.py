import statistics
from collections import Counter

def get_statistics(data):
    try:
        numeric_data = list(map(float, data))
        mean_value = statistics.mean(numeric_data)
        median_value = statistics.median(numeric_data)
        mode_value = statistics.mode(numeric_data)
        return {
            "Mean": mean_value,
            "Median": median_value,
            "Mode": mode_value
        }
    except ValueError:
        return None

def get_character_statistics(data):
    count = len(data)
    unique_values = set(data)
    most_common = Counter(data).most_common(1)[0]
    return {
        "Count": count,
        "Unique Values": unique_values,
        "Most Common": most_common
    }

def main():
    user_input = input("Enter your observations (comma separated): ")
    observations = [item.strip() for item in user_input.split(",")]

    print("\nStatistics for Numerical Data:")
    numeric_stats = get_statistics(observations)
    if numeric_stats:
        for key, value in numeric_stats.items():
            print(f"{key}: {value}")
    else:
        print("No valid numerical data found.")

    print("\nStatistics for Character Data:")
    char_stats = get_character_statistics(observations)
    for key, value in char_stats.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()