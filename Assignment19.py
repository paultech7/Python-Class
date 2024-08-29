# Define a function that sorts an input list of numbers without using any built-in sort functions.
# This is an implementation of a variant of a bubble sort.
# Returns: a list containing the input numbers in ascending order.
def sort_list(input_numbers):

    # Initialize a new list for the output
    sorted_output = list(input_numbers)

    gap = len(sorted_output)

    # Initialize swapped to True to make sure the loop runs regardless of the list length
    swapped = True

    # Keep running while the gap is more than 1 and a swap was made
    while gap > 1 or swapped:

        # Reduce the gap by the shrink factor
        gap = (gap * 10) // 13
        if gap < 1:
            gap = 1

        swapped = False

        # Compare all elements with current gap
        for i in range(0, len(sorted_output) - gap):
            if sorted_output[i] > sorted_output[i + gap]:
                sorted_output[i], sorted_output[i + gap] = sorted_output[i + gap], sorted_output[i]
                swapped = True

    return sorted_output


# Create a list of unsorted numbers
unsorted_list = list()
for i in range(5000, 0, -1):
    unsorted_list.append(i)
# unsorted_list = [102, 67, 53, 53, 45, 6, 3, 8, 23, 8, 0, 13, -9]

# Call the sort function
sorted_list = sort_list(unsorted_list)

# Show the result
print("Sorted list:")
print(sorted_list)
