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
    #hash table dictionary
    cache = {}
    # create an empty list in which we will save the airports
    route = []

    # hash each ticket such that source is the key and destination is value
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # The first flight is the one that has source=None
    route.append(cache["NONE"])
    #finial flight  
    final_flight = cache["NONE"]

    #add in route each flight 
    
    while final_flight != "NONE":
        #is it the first flight? If so, move on
        if final_flight == "NONE":
            continue
        #add the next flight
        else:
            route.append(cache[final_flight])
            final_flight = cache[final_flight]
    

    return route

tickets = [
    Ticket("PIT", "ORD" ),
    Ticket("XNA", "CID" ),
    Ticket("SFO", "BHM" ),
    Ticket("FLG", "XNA" ),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO" ),
    Ticket("CID", "SLC" ),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT" ),
    Ticket("BHM", "FLG" )
]

print(reconstruct_trip(tickets, 10))