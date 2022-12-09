"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    canAdd = False
    count = len(items)
    frequencies = {}
    newitems = []

    if len(items) == 0:
        return frequencies

    for i in items:
        if not (isinstance(i, str)):
            i = str(i)
            newitems.append(i)
        else:
            newitems.append(i)

    frequencies.update({newitems[0]: 1})

    i = 1

    while count > 1:

        for key in frequencies:
            if key == newitems[i]:
                canAdd = True
                break

        if canAdd:
            new = frequencies.get(newitems[i])
            frequencies[newitems[i]] = new+1
        else:
            frequencies.update({newitems[i]: 1})
        i = i+1
        count = count-1
        canAdd = False

    # Your code goes here
    return frequencies
