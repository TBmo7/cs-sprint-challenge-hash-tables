def has_negatives(a):
    """
    YOUR CODE HERE
    take in elements and add to hash table 
    search number is the current element multiplied by -1
    if that number exists
    add to array, check for duplicates
    
    """
    # Your code here

    numbers = {}
    result = []
    for element in a:
        if element != 0:
            
            numbers[element] = element
            search_num = element * -1
            if search_num in numbers:
                if search_num < 0:
                    search_num *= -1
                if search_num not in result:
                    result.append(search_num)
            




    return result


if __name__ == "__main__":
    print(has_negatives([0,-1, -2, 1, 2, 3, 4, -4,0]))
