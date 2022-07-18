## Problem Solving Basic HackerRank Test
## This is 2 Question  I got at Problem Solving Basic HackerRank Test

## TODO: Nearly Similar Rectangles
from collections import defaultdict

def nearlySimilarRectangles(sides):
    biggest = lambda a, b: biggest(b, a % b) if b > 0 else a
    d = defaultdict(int)
    for i, j in sides:
        k = biggest(i, j)
        d[(i // k, j // k)] += 1
    return sum((x * (x - 1)) // 2 for x in d.values())


##FIXME : Antoher Logic, but erorr at compile and submit at hackerank, because  the runtime is O(n^2) not O(n). But its work 😃.

# def nearlySimilarRectangles(sides):
    # result = 0

    # for i in range(0, len(sides)-1):
    #     x = sides[i]

    #     for j in range(i + 1, len(sides)):
    #         y = sides[j]

    #         if x[0]/y[0] == x[1]/y[1]:
    #             result = result + 1

    # return result

## TODO: Password Decryption
def decryptPassword(s):
    s = list(s)
    i = 0
    while i < len(s) and s[i].isdigit() and s[i] !="0":
        i += 1
    for j,k in enumerate([l for l in range(i,len(s)) if s[l]=="0"]):
        s[k] = s[i-j-1]
    for j in range(i, len(s)):
        if s[j] == "*":
            s[j-1], s[j-2] = s[j-2],s[j-1]
    return "".join(s[i:]).replace("*","")