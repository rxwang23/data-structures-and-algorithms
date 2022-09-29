def shift(lst, k, direction="left"):
    """
    :param lst: list of N numbers
    :param k: positive integer k (where k < N)
    :param direction: shifted numbers circularly k steps to the left (default) o right
    :return:
    """
    if direction == "right":
        k = len(lst) - k
    for shift_num in range(k):
        lst.append(lst.pop(0))


# lst = [1,2,3,4,5,6]
# shift(lst, 2)
# print(lst)
#
# lst = [1,2,3,4,5,6]
# shift(lst, 2, "right")
# print(lst)