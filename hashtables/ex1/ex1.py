

def get_indices_of_item_weights(weights, length, limit):
  
    #set cache
    cache = {}
    
    # Checks list of weights by index
    for i in range(length):
        #store each weight as a key
        weight = weights[i]
        #print(f'key and value:{i, weight}')
        if weight in cache:
            #store the weight index as the value
            value = cache[weight]
            #return tuple
            return(i, value)
            
        
        #calculate the difference
        difference = limit - weight
        #add to cache
        cache[difference] = i
        #print(difference)
    return None


if __name__ == "__main__":
    print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))