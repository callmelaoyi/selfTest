# import math

# def Pow(x, n):
#     # return x^n
    
#     # if n >=0:
#     #     ret = x
#     #     a = int(math.log2(n))
#     #     b = n - a
#     #     for i in range(a):
#     #         ret = ret^2
#     #     if b != 0:
#     #         for i in range(b):
#     #             ret = ret * x
#     #     # return x^n
#     # else:
#     #     b = 1/x
#     #     return b^(-n)
#     if n<=0:
#         x = 1/x
#         n = -n
#     index = 1
#     while index^index <= n:
#         index+=1
#     index -=1
#     b = n - index
#     ret = x
#     for i in range(index):
#         ret = ret^index
#     if b != 0:
#         for j in range(b):
#             ret *=x
#     return ret

# print(pow(3, -11))


'''
输入：s = "babad"
输出："bab" 或 “aba”
最长回文子串
'''
def maxReturnSubStr(str1):
    ret = str1[0]
    for i in range(len(str1)):
        prePtr = i-1
        nextPtr = i+1
        while prePtr >=0 and nextPtr <=len(str1)-1 and  str1[prePtr] ==str1[nextPtr]:
            prePtr -=1
            nextPtr +=1
        nextPtr-=1
        prePtr+=1
        if (nextPtr-prePtr) >= len(ret):
            ret = str1[prePtr:nextPtr+1]
    return ret

print(maxReturnSubStr("abcdcbd"))