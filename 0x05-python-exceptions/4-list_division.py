#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element 2 lists
    Args:
        my_list-1: The list containing the dividends
        my_list-2: The list containing the divisors
        list_length: The length of both lists
    Returns:
        A new list containing the division result
    """

    new_list = []

    for i in range(list_length):

        try:
            new_list.append(my_list_1[i] / my_list_2[i])

        except IndexError:
            print("out of range")

            new_list.append(0)

        except (TypeError, ValueError):
            print("wrong type")

            new_list.append(0)

        except ZeroDivisionError:
            print("division by 0")

            new_list.append(0)

        finally:
            pass

    return new_list
