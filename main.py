def count_ones(n):
    """Counts the number of 1s in the binary representation of an integer."""
    count = 0
    while n > 0:
        count += n & 1  # Check if the last bit is 1
        n >>= 1        # Right shift to check the next bit
    return count

# Example usage
number = 25
ones_count = count_ones(number)
print(f"The number of 1s in the binary representation of {number} is: {ones_count}")