#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    #set the variables
    ##hash table dictionary
    cache = {}
    # route list
    route = []

    for i in tickets:
        cache[i.source] = i.destination

    route.append(cache["NONE"])
    final_destination = cache["NONE"]

    
    

    return route
