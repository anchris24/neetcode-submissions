class Solution:
    def checkValidString(self, s: str) -> bool:
        paran = []
        stars = []

        for i in range(len(s)):
            if s[i] == '(':
                paran.append(i)
            elif s[i] == '*':
                stars.append(i)
            else:
                if paran:
                    paran.pop()
                elif stars:
                    stars.pop()
                else:                   
                    return False
        
        if not paran and not stars:
            return True
        
        if len(stars) < len(paran):
             return False

        starid = 0
        for i in range(len(paran)):
            while starid < len(stars) and stars[starid] < paran[i]:
                starid += 1
            
            if starid == len(stars):
                return False
            # if stars[starid] < paran[i]:
            #     return False
            starid += 1
        
        return True
            