# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # set up variables
    #dictionary
    cache = {}
    #result list
    result = []

    #dictionary of paths
    for path in files:
        #the file is the last name after last / divider
        item = path.split('/')[-1]

        #if item is in dictionary
        if item in cache:
            cache[item].append(path)
        else:
            cache[item] = [path]
    #loop through to check queries (if each one is a key in our dictionary)
    for q in queries:
        #if query is in dictionary 
        if q in cache:
            #put in results
            results = cache[q]
            #we are returning a list into one list
            for path in results:
                #append list of path
                result.append(path)
    else:
        pass

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
