def printData(data, level=0):
    for item in data:
        if isinstance(item, list):
#            for items in item:
#                print(items)
            printData(item, level+1)
        else:
            for i in range(level):
                print("\t", end='')
            print(item)