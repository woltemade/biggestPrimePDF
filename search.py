# search_sequence.py
# takes a very long time +- 6 hours
def search_sequence(big_number, sequence):
    """
    Search for a sequence of numbers within a big number.

    :param big_number: The large number as a string.
    :param sequence: The sequence to search for as a string.
    :return: The starting index of the sequence if found, otherwise -1.
    """
    return big_number.find(sequence)

if __name__ == "__main__":
    # Calculate the prime number
    prime_number = str(2**136279841 - 1)

    # Define the sequence to search for
    sequence = "123456789101112"  # Replace with the sequence you want to search for

    # Search for the sequence
    index = search_sequence(prime_number, sequence)

    if index != -1:
        print(f"Sequence found at index: {index}")
    else:
        print("Sequence not found")