""" Sum of Integers Up To n """


def add_it_up(str_input):
    """ Takes a single integer as input and returns the sum of the integers from zero to the input parameter.
    :param int_input: integer given by the user
    :return: the sum of integers from 0 to the int_input, else 0 if a non-integer is passed in
    """

    try:
        int_input = int(str_input)
        int_sum = 0
        if int_input < 0:  # If the integer is negative
            for i in range(0, int_input - 1, -1):
                int_sum += i
        else:  # If the integer is positive
            for i in range(int_input + 1):
                int_sum += i
        return "The sum is : " + str(int_sum)
    except:
        return 0


if __name__ == '__main__':
    print("Please, enter a number greater or lower than 0 :")
    str_input = input()
    print(add_it_up(str_input))
