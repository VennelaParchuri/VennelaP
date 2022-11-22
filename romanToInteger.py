# LeetCode problem 13 Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        self.strn1 = s
        value = 0
        strn2 = ''
        strn3= ''
        x=0
        dic1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if self.strn1 in dic1.keys():
            return dic1[self.strn1]
        else:
            while x< len(self.strn1):
                strn2 = self.strn1[x]
                if(x+1 < len(self.strn1)):
                    strn3 = self.strn1[x+1]
                    if dic1[strn2] >= dic1[strn3]:
                        value = value+ dic1[strn2]
                        x+=1
                    else:
                        value = value + dic1[strn3] - dic1[strn2]
                        x+=2
                else:
                    value= value + dic1[strn2]
                    x+=1
            return value