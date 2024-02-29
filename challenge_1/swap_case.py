def swap_case(s):
    lst = list(s)
    for i in range(len(s)):
        lst[i] = lst[i].lower() if lst[i].isupper() else lst[i].upper()
    return "".join(lst)


def swap_case2(s):
    temp = ""
    for i in range(len(s)):
        temp += s[i].lower() if s[i].isupper() else s[i].upper()
    return temp


def swap_case3(s):
    temp = ""
    for ch in s:
        temp += ch.lower() if ch.isupper() else ch.upper()
    return temp
