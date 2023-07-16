def groupAnagrams(self, strs:list[str]) -> list[list[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(a) - ord("a")] += 1
        res[tuple(count)].append(c)
    return res.values()
