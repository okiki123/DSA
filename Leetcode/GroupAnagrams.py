def groupAnagrams(self, strs:list[str]) -> list[list[str]]:
    res = defaultdict(list)
    for c in strs:
        count = [0] * 26
        for a in c:
            count[ord(a) - ord("a")] += 1
        res[tuple[count]].append(c)
    return res.value()
