class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r=""
        carry=0
        a,b=a[::-1],b[::-1]
        for i in range(max(len(a),len(b))):
            A=ord(a[i])-ord("0") if i<len(a) else 0
            B=ord(b[i])-ord("0") if i<len(b) else 0

            t=A+B+carry
            char=str(t%2)
            r=char+r
            carry=t//2
        
        if carry:
            r="1"+r
        return r
