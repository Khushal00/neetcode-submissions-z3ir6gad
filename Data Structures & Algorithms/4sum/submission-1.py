class Solution:
    def fourSum(self, a: List[int], target: int) -> List[List[int]]:
        a.sort()
        res = []

        for i in range(len(a)):
            if i > 0 and a[i] == a[i-1]:
                continue
            for j in range(i+1, len(a)):
                if j > i+1 and a[j] == a[j-1]:
                    continue
                l, r = j + 1, len(a) - 1
                while l < r:
                    sumReq = a[i] + a[j] + a[l] + a[r]
                    if sumReq == target:
                        res.append([a[i], a[j], a[l], a[r]])
                        l += 1
                        r -= 1
                        while l < r and a[l] == a[l-1]:
                            l += 1
                    elif sumReq < target:
                        l += 1
                    else:
                        r -= 1
                    

        return res