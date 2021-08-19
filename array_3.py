# Implement your function below.
def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    first=list1[0]
    if first in list2:
        k=list2.index(first)
    else:
        return False
    n=len(list1)
    ans=[0]*n


    for i in range(n):
        j = (i+k)%n
        ans[j]=list1[i]
    if ans == list2:
        return True
    else:
        return False



# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
print(is_rotation(list1, list2a)) #should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
is_rotation(list1, list2b)
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
is_rotation(list1, list2c)
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
is_rotation(list1, list2d)
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
is_rotation(list1, list2e)
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
is_rotation(list1, list2f)
# is_rotation(list1, list2f) should return True.
list2g = [7, 1, 2, 3, 4, 5, 6]
is_rotation(list1, list2g)
# is_rotation(list1, list2g) should return True.

