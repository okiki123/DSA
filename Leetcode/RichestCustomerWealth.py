class solution:
    def richestcustomer(self, accounts:list[list[int]]) -> int:
        maxsum = 0
        for i in range(len(accounts)):
            eachsum = 0
            for j in range(len(accounts[i])):
                eachsum += accounts[i][j]
                maxsum = max(maxsum, eachsum)
        return maxsum