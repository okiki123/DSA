#s = BLOOMBERG

class solution:
    def firstUniqueChar(self, s: str) -> int:
        st_map = {}
        for i in range(len(s)):
            