class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        re=[]
        r = []
        while columnNumber > 0:
            columnNumber -= 1
            r.append(chr((columnNumber % 26) + ord('A')))
            columnNumber //= 26
        re.append(''.join(r[::-1]))
        for i in re:
            return i
