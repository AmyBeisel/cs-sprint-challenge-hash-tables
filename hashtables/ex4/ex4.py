def has_negatives(a):
    """
    YOUR CODE HERE
    """
    
    #set up variables
    #hash table dictionary
    cache = {}
    #result list
    result = [] 
    

    #loop through the list
    for nums in a:
        cache[nums] = nums
        
        #if number not 0 or in dictionary. 
        if nums != 0 and - nums in cache: 
            #return number as positive (absolute number) and append in list
            result.append(abs(nums))
    return result


if __name__ == "__main__":

    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
