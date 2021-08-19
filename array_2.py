def common_elements(list1, list2):
    result=[]
    for i in list1:
        if i in list2:
            result.append(i)
    return result
s1=[1,3,4,6,7,9]
s2=[1,2,4,5,9,10]
print(common_elements(s1,s2))

def common_elements(list1, list2):
    result=[]
    list1.sort()
    list2.sort()
    p1=0
    p2=0
    while p1<len(list1) and p2<len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1 += 1
            p2 += 1
        elif list1[p1] > list2[p2]:
            p2 += 1
        elif list1[p1] < list2[p2]:
            p1 += 1

    return result
s1=[1,3,4,6,7,9]
s2=[1,2,4,5,9,10]
print(common_elements(s1,s2))