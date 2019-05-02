"""
    Cocktail Sort
    -------------
    A bidirectional bubble sort. Walks the elements bidirectionally, swapping
    neighbors if one should come before/after the other.

    Time Complexity: O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable: Yes

    Psuedo Code: http://en.wikipedia.org/wiki/Cocktail_sort

"""
def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.

    :param seq: A list of integers
    :rtype: A list of sorted integers
    """
    for i in range(len(seq) - 1, 0, -1):
        swapped = False

        for j in range(i, 0, -1):
            if seq[j] < seq[j - 1]:
                seq[j], seq[j - 1] = seq[j - 1], seq[j]
                swapped = True

        for j in range(i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                swapped = True

        if not swapped:
            return seq
