def main():

    # Define a function that takes two lists as input and
    # returns a list comprised of the common elements
    # in both input lists.
    def find_common_elements(list1, list2):
        common_list = []
        for item in list1:
            if item in list2:
                common_list.append(item)
        return common_list

    # Create 2 large lists for testing
    test_list1 = []
    test_list2 = []
    for i in range(10000):
        test_list1.append(i)
    for i in range(12, 10000, 10):
        test_list2.append(i)

    # Find the common elements in the two lists.
    common = find_common_elements(test_list1, test_list2)

    # Print the common elements
    print("Common elements are:")
    for _ in common:
        print(f"{_}, ", end="")


main()
