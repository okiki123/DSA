class solution:
    def replaceelement(self, arr:list[int]) -> list[int]:
        rightmax = -1
        for i in range(len(arr) - 1, -1, -1):
            newmax = max(rightmax,arr[i])
            arr[i] = rightmax
            rightmax = newmax