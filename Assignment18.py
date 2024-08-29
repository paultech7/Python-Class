# Define a function that takes two tuples and creates a new tuple containing all elements from both tuples.
# Returns: a tuple with all the elements from both input tuples.
def concat_tuples(tuple_in1, tuple_in2):
    return tuple_in1 + tuple_in2


# Set test tuples
test_tuple1 = (1, 3, 10)
test_tuple2 = (20, 34, 40, 51, 78)

# Concatenate the two tuples
new_tuple = concat_tuples(test_tuple1, test_tuple2)

# Show the result
print("For tuples ", test_tuple1, " and ", test_tuple2, ",")
print("result is ", new_tuple)
