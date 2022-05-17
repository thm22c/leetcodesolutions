#problem:
#is the given number valid
#eg 1e-10 is valid
# e is not
#and so on


class Solution:
    def isDigit(self, s):
        if s in "0123456789":
            return True
        return False

    def digitIn(self, s):
        for i in s:
            if self.isDigit(i):
                return True
        return False

    def isSign(self, s):
        if s in "+-" and not"":
            return True
        return False

    def isPureNum(self, s, strict):
        if len(s)==0:
            return True
        ss = s
        if self.isSign(s[0]) and not strict:
            ss = s[1:]

        for i in ss:
            if not self.isDigit(i):
                return False
        return True


    def isNumber(self, s):
        #check if not more than 1 dot
        if s == ".":
            return False
        if not self.digitIn(s):
            return False

        splitsDots = s.split(".")
        if(len(splitsDots)>2):
            return False


        #if valid number of dots
        #and no e's are present
        #each splitDots should be pure number

        if "e" in s or "E" in s:
            if len(s)<3:
                return False
            splitsE = s.split("e")
            if(len(splitsE)==1):
                splitsE = s.split("E")
            if(len(splitsE)!=2):
                return False
            if splitsE[0] in [".", "", "+", "-"]:
                return False
            # recheck everything for first list
            # second list: nunstrict number
            if not self.isPureNum(splitsE[1], False) or splitsE[1] in "+-":
                return False
            splitsDots = splitsE[0].split(".")
            if (len(splitsDots) > 2):
                return False

        if len(splitsDots) == 1:
            return (self.isPureNum(splitsDots[0], False))
        else:
            return (self.isPureNum(splitsDots[0], False)) and (self.isPureNum(splitsDots[1], True))

