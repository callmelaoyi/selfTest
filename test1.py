

A_dict = {
    'a':2,
    'b':1,
    'c':4,
    'd':3
}

print(A_dict)
print(A_dict.values())

a_sort = sorted(A_dict,key= lambda x: A_dict[x])
for i in a_sort:
    print("key = ", i, "value = ", A_dict[i])    


"""
n阶台阶
每次一个台阶或者两个台阶
爬到n层有多少走法
"""

def getFloor(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return getFloor(n-1) + getFloor(n-2)

print(getFloor(5))