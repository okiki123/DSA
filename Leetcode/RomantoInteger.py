class solution:
    def romantointerger(self, s:str) -> int:
        hashmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0
        for i in range(len(s) - 1):
            if hashmap[s[i]] < hashmap[s[i + 1]]:
                number -= hashmap[s[i]]
            else:
                number += hashmap[s[i]]
        return number + hashmap[s[-1]]