import sys

def process_values(values):
    try:
        values = [float(val) for val in values]
    except ValueError:
        return "Error"

    if any(value < 0 for value in values):
        return "Error"

    avg = sum(values) / len(values)
    avg_message = "Greater than 50." if avg > 50 else "NOt greater then 50."

    positive_count = sum(1 for value in values if value > 0)
    parity_message = "Even." if positive_count % 2 == 0 else "Odd"

    greater_than_10 = sorted([value for value in values if value > 10])

    output = (
        f"original: {', '.join(map(str, values))}\n"
        f": {', '.join(map(str, greater_than_10))}\n"
        f"{avg_message}\n"
        f"{parity_message}"
    )
    return output

if __name__ == "__main__":
    input_values = sys.argv[1:]
    result = process_values(input_values)
    print(result)
