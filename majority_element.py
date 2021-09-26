""" Majority element """

import random


def floor(number_list):
    """ The majority element is defined as the element that appears more than floor(n / 2) times,
    where n is the length of the list.
    :param number_list:  list of int
    :return: the majority element
    """

    max_count = 0
    count = 0
    index = 0
    half_size = len(number_list) // 2

    for i in range(len(number_list)):
        for j in range(len(number_list)):
            if number_list[j] == number_list[i]:
                count += 1
                if count > max_count:
                    max_count = count
                    index = i
        count = 0

    if max_count > half_size:  # The element appears more than n/2 times
        return "The majority element is " + str(number_list[index])
    else:
        return "No majority element"


if __name__ == '__main__':
    randomList = []
    for i in range(0, 5):  # List size of 5
        n = random.randint(1, 5) # Random number between 1 and 5
        randomList.append(n)
    print("Input list : %s " % randomList)
    print(floor(randomList))
