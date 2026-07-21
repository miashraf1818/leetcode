class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        n = len(t)
        
        # Run-length encode
        blocks = []
        i = 0
        while i < n:
            ch = t[i]
            j = i
            while j < n and t[j] == ch:
                j += 1
            blocks.append((ch, j - i))
            i = j
        
        base = s.count('1')
        best_gain = 0
        
        # Find 0-block, 1-block, 0-block triples
        # Gain = left_zeros + right_zeros (the zeros we turn into 1s)
        # The middle 1s first become 0, but the entire region becomes 1
        # So we gain the two 0-blocks worth of 1s (middle 1s were already counted in base)
        for i in range(1, len(blocks) - 2):
            if blocks[i][0] == '0' and blocks[i+1][0] == '1' and blocks[i+2][0] == '0':
                gain = blocks[i][1] + blocks[i+2][1]
                best_gain = max(best_gain, gain)
        
        return base + best_gain