# Implemen

# Implement your function below.
def is_one_away(s1, s2):
    if abs(len(s1)-len(s2))>1:
        return False
    elif len(s1)==len(s2):
        return is_one_away_same_length(s1,s2)
    elif len(s1)>len(s2):
        return is_one_away_diff_length(s1,s2)
    elif len(s2)>len(s1):
        return is_one_away_diff_length(s2,s1)


def is_one_away_same_length(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
            if count > 1:
                return False
    return True

# Assumption: len(s1) == len(s2) + 1
def is_one_away_diff_length(s1, s2):
    diff_num=0
    i = 0
    while i < len(s2):
        if s1[i+diff_num]==s2[i]:
            i += 1
        else:
            diff_num += 1
            if diff_num > 1:
                return False
    return True
print(is_one_away("abcde", "abcd") ) # should return True
print(is_one_away("abde", "abcde") ) # should return True
print(is_one_away("a", "a") ) # should return True
print(is_one_away("abcdef", "abqdef") ) # should return True
print(is_one_away("abcdef", "abccef") ) # should return True
print(is_one_away("abcdef", "abcde") ) # should return True
print(is_one_away("aaa", "abc") ) # should return False
print(is_one_away("abcde", "abc")  )# should return False
print(is_one_away("abc", "abcde") ) # should return False
print(is_one_away("abc", "bcc") ) # should return False