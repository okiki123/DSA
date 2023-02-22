#s = BLOOMBERG

class solution:
    def firstUniqueChar(self, s: str) -> int:
        st_map = {}
        for i in range(len(s)):
            if s[i] not in st_map:
                st_map[s[i]] = True
            else:
                st_map[s[i]] = False
        for i in range(len(s)):
            if st_map[s[i]] == True:
                return i
        return -1
