

"""
    Selection Sort
    --------------
    A sorting that uses in-place comparison.

    Time Complexity:  O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable: Yes

    Psuedo Code: http://en.wikipedia.org/wiki/Selection_sort

"""


def sort(array):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.

    :param seq: A list of integers
    :rtype: A list of sorted integers
    """
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
          if array[j] < array[i]:
           min = array[j];
           array[j] = array[i];
           array[i] = min;
    return array
