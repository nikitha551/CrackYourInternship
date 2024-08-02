class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        rules={")":"(","]":"[","}":"{"}
        for c in s:
            if c in rules:
                if st and st[-1]==rules[c]:
                    st.pop()
                else:
                    return False 
            else:
                st.append(c)
        return True if not st else False

        
