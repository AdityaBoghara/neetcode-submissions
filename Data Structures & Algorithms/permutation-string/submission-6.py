class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        freq2 = {}

        if len(s1) > len(s2):
            return False


        for i in range(len(s1)):
            freq1[s1[i]] = 1 + freq1.get(s1[i], 0)
            freq2[s2[i]] = 1 + freq2.get(s2[i], 0)


        l, r = 0, len(s1)

        while r<len(s2):
            if freq1 == freq2:
                return True
            freq2[s2[l]] -= 1
            if freq2[s2[l]] == 0:
                del freq2[s2[l]]
            l+=1
            freq2[s2[r]] = 1 + freq2.get(s2[r], 0)
            r += 1

        return freq1 == freq2
            








        