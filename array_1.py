def most_frequent(s):
    mp={}
    for i in s:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
    max_times=max(mp.values())
    for i, j in mp.items():
        if j == max_times:
            return i

s=[1,2,3,4,5,1,2,3,1,1]
print(most_frequent(s))

def most_frequent(s):
    mp={}
    max_times = 0
    max_num = 0
    for i in s:
        if i in mp:
            mp[i] += 1
            if mp[i] > max_times:
                max_times = mp[i]
                max_num = i
        else:
            mp[i] = 1

    return max_num
s=[1,2,3,4,5,1,2,3,1,1]
print(most_frequent(s))

def most_frequent(s):
    mp={}
    max_times = 0
    max_num = 0
    for i in s:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
        if mp[i] > max_times:
            max_times = mp[i]
            max_num = i
    return max_num
s=[1,2,3,4,5,1,2,3,1,1]
print(most_frequent(s))