# Function to perform Insertion Sort in monotonically decreasing order
def insertion_sort_descending(numbers):
    """
    Sorts a list of numbers in monotonically decreasing order
    using the Insertion Sort algorithm.
    """

    # Start from the second element since the first element
    # is already considered sorted
    for current_index in range(1, len(numbers)):

        # Store the value to be placed in the correct position
        current_value = numbers[current_index]

        # Initialize index for comparing elements to the left
        previous_index = current_index - 1

        # Shift all elements that are smaller than current_value
        # one position to the right to make space
        while previous_index >= 0 and numbers[previous_index] < current_value:
            numbers[previous_index + 1] = numbers[previous_index]
            previous_index -= 1

        # Insert the current_value at its correct position
        numbers[previous_index + 1] = current_value


# Main block to test the function
if __name__ == "__main__":

    # Example array to demonstrate sorting
    sample_array = [12, 11, 13, 5, 6]

    # Display the original array
    print("Original Array:", sample_array)

    # Call the insertion sort function
    insertion_sort_descending(sample_array)

    # Display the sorted array
    print("Sorted Array in Decreasing Order:", sample_array)
