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

    #starting destination
    for i in tickets:
        cache[i.source] = i.destination

    #get the tickets for first flights
    route.append(cache["NONE"])
    #finial flight
    final_flight = cache["NONE"]

    #if final flight not equal to NONE 
    while final_flight != "NONE":
        
        if final_flight == "NONE":
            continue
        else:
            route.append(cache[final_flight])
            final_flight = cache[final_flight]
    

    return route
