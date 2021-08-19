def non_repeating(given_string):
    mp = {}
    count = 0
    for i in given_string:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
    for i, j in mp.items():
        if j == 1:
            count += 1
            return i

    return None


# NOTE: The following input values will be used for testing your solution.
print(non_repeating("abcab"))  # should return 'c'
print(non_repeating("abab"))  # should return None
print(non_repeating("aabbbc"))  # should return 'c'
print(non_repeating("aabbdbc"))  # should return 'd'

def non_repeating(given_string):
    mp = {}
    count = 0
    for i in given_string:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
    for i in given_string:
        if mp[i]==1:
            return i

    return None


# NOTE: The following input values will be used for testing your solution.
print(non_repeating("abcab"))  # should return 'c'
print(non_repeating("abab"))  # should return None
print(non_repeating("aabbbc"))  # should return 'c'
print(non_repeating("aabbdbc"))  # should return 'd'