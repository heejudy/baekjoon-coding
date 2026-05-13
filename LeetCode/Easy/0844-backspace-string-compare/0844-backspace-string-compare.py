class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        while '#' in s:
            idx = s.find('#')

            if idx == 0:
                s = s[1:]
            else:
                s = s[:idx-1] + s[idx+1:]

        while '#' in t:
            idx = t.find('#')

            if idx == 0:
                t = t[1:]
            else:
                t = t[:idx-1] + t[idx+1:]
        
        if s == t:
            return True
        else:
            return False