def get_middle(s):
    length = len(s)
    middle = length // 2

    if length % 2 == 0:
        return s[middle - 1: middle + 1]
    else:
        return s[middle]
print(get_middle("test"))

