#problem:
#have some patterns of valid pws
#give the number of steps necessary to fix

import numpy as np
import random
#6-20 characters
#least 1 lowercase 1 upper 1 digit
#never 3 consecutive repeats
upper = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
lower = "abcdefghijklmnopqrstuvxyz"
digits = "1234567890"
extra = ".!"
allInput = upper+lower+digits+extra
def notInStr(str):
    result = ""
    for x in allInput:
        if not x in str:
            result += x
    return result

def anyXinY(x, y):
    for yy in y:
        if yy in x:
            return True
    return False

def generateMask(str):
    maskL = np.array([0 for i in str])
    maskU = np.array([0 for i in str])
    maskD = np.array([0 for i in str])
    maskR = np.array([0 for i in str])
    for i in range(0, len(str)):
        if str[i] in lower:
            maskL[i] = 1;
            break
    for i in range(0, len(str)):
        if str[i] in upper:
            maskU[i] = 1;
            break
    for i in range(0, len(str)):
        if str[i] in digits:
            maskD[i] = 1;
            break
    for i in range(0,len(str)-1):
        if str[i] == str[i+1]:
            if i-2 >=0:
                if str[i] == str[i-2]:
                    maskR[i-1] = 1
            if i+3 < len(str):
                if str[i+1] == str[i+3]:
                    maskR[i+2] = 1
    print(str)
    print(maskU)
    print(maskL)
    print(maskD)
    print(maskR)
    return maskR+maskD+maskU+maskL

def beTriplets(pw):
    for i in range(0,len(pw)-2):
        if pw[i] == pw[i+1] and pw[i] == pw[i+2]:
            return False
    return True

def idxTriplets(pw):
    for i in range(0, len(pw) - 2):
        if pw[i] == pw[i + 1] and pw[i] == pw[i + 2]:
            return i+2
    return -1

def lenStreak(str, i):
    start = i
    for j in range(i, len(str)):
        if str[i] != str[j]:
            return (j-1)-i
    return len(str)-start


def gibStreaksPop(str):
    res = []
    i = 0
    while i <(len(str) - 2):
        if str[i] == str[i + 1] and str[i] == str[i + 2]:

            res.append([i, lenStreak(str,i)])
            i += lenStreak(str, i)
        i+=1
    #now the best streak: with len == mod 3
    #print(res)
    random.shuffle(res)
    if res == []:
        return -1
    return res[0][0]+2

def correctPW(str):
    lowerT = anyXinY(str, lower)
    upperT = anyXinY(str, upper)
    digitT = anyXinY(str, digits)
    tripp = beTriplets(str)
    if len(str)>=6 and len(str)<=20:
        return True, lowerT,upperT,digitT,tripp
    else:
        return False, lowerT,upperT,digitT,tripp
class Solution:    
    def strongPasswordChecker(self,pw):
        res = [strongPasswordCheckerIn(pw) for i in range(0, 10)]
        return min(res)

    
    


def strongPasswordCheckerIn(pw):
    a, b, c, d, e = correctPW(pw)
    steps = 0
    while (not a) or (not b) or (not c) or (not d) or (not e):
        a, b, c, d, e = correctPW(pw)
        # triplets need to be broken up first bc its a double-tap
        # eg aaabbb takes 2 steps to be valid a1abAb
        if not e:
            steps +=1
            # all 3 cases here
            # too long with triplets: just delete bc cant drop other categories
            # too short with triplets: insert best between them eg missing digit
            idx = idxTriplets(pw)
            if len(pw) <6:
                if not b:
                    pw = pw[:idx] + 'a' + pw[idx:]
                    continue
                if not c:
                    pw = pw[:idx] + 'A' + pw[idx:]
                    continue
                if not d:
                    pw = pw[:idx] + '1' + pw[idx:]
                    continue
                pw = pw[:idx] + (notInStr(pw)[0]) + pw[idx:]
                continue
            if len(pw) <= 20:
                if not b:
                    s = list(pw)
                    s[idx] = "a"
                    pw = "".join(s)
                    continue
                if not c:

                    s = list(pw)
                    s[idx] = "A"
                    pw = "".join(s)
                    continue
                if not d:

                    s = list(pw)
                    s[idx] = "1"
                    pw = "".join(s)
                    continue
                s = list(pw)
                s[idx] = notInStr(pw)[0]
                pw = "".join(s)
                continue
            else:
                idx = gibStreaksPop(pw)
                pw = pw[:idx]+pw[idx+1:]
                continue


        # ez case all other criteria are met but too short:
        if len(pw) < 6 :
            if  b and c and d:
                steps += 1
                pw +=notInStr(pw)[0]
                continue
            if not b:
                steps += 1
                pw +="a"
                continue
            if not c:
                steps += 1
                pw +="A"
                continue
            if not d:
                steps += 1
                pw += "1"
                continue
        if len(pw) > 20:
            # no possible double-tap from delete -> no wider checks

            steps += 1
            mask = generateMask(pw)
            for i in range(0, len(mask)):
                if mask[i] == 0:
                    pw = pw[:i]+pw[i+1:]
                    break
            continue
        else:
            #acceptable length but other factors wrong? but not streaking
            if not b:
                steps += 1
                mask = generateMask(pw)
                for i in range(0, len(mask)):
                    if mask[i] == 0:
                        s = list(pw)
                        s[i] = "a"
                        pw = "".join(s)
                        break
                continue
            if not c:
                steps += 1
                mask = generateMask(pw)
                for i in range(0, len(mask)):
                    if mask[i] == 0:
                        s = list(pw)
                        s[i] = "A"
                        pw = "".join(s)
                        break
                continue
            if not d:
                steps += 1
                mask = generateMask(pw)
                for i in range(0, len(mask)):
                    if mask[i] == 0:
                        s = list(pw)
                        s[i] = "1"
                        pw = "".join(s)
                        break
                continue
    #print(pw)
    return steps

        
