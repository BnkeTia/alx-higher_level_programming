#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Create an empty set to store the common items
    common_elem = set()

    # Iterate through the elements in set_1
    for item in set_1:
        # Check if the item is also in set_2
        if item in set_2:
            # If it's in both sets, add it to the common_item
            common_elem.add(item)

    return common_elem
