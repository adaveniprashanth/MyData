if 0:
    # lambda function within filter,map,reduce functions
    my_list = [1, 2, 3, 4, 5, 6]

    # filter syntax filter(function,iterables)
    new_list = list(filter(lambda a: a % 2 == 0, my_list))
    print(new_list)  # contains only values satisfies the function

    # map syntax map(function,iterables)
    new_list1 = list(map(lambda a: a % 2 == 0, my_list))
    print(new_list1)  # return the list after satisfies condition

    my_list1 = [2, 3, 4, 5, 6]
    new_list1 = list(map(lambda a, b: a * b, my_list, my_list1))
    print(new_list1)

    # reduce syntax reduce(function,iterables,initial)
    # the function in reduce needs 2 parameters
    from functools import reduce

    my_data = range(1, 7)
    summarized_value = reduce(lambda a, b: a * b, my_data)
    # print(summarized_value)
