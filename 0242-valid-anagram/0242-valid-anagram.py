class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a=list(s)
        b=list(t)
        a.sort()
        b.sort()
        return a==b