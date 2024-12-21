class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if not s[i] in dic:
                dic[s[i]] = t[i]
                # print(dic[s[i]])
            else:
                if dic[s[i]] != t[i]:
                    return False
        # print(dic)
        return True
