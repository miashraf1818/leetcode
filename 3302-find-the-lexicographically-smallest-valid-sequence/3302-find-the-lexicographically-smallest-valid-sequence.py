from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        # suf[j] stores the maximum (right-most) index in word1 
        # from which the exact suffix word2[j...] can be found.
        suf = [-1] * m
        
        j = m - 1
        for i in range(n - 1, -1, -1):
            if word1[i] == word2[j]:
                suf[j] = i
                j -= 1
                if j < 0:
                    break
                    
        seq = []
        changed = False
        j = 0
        
        # Greedily pick the earliest possible valid indices
        for i in range(n):
            if j == m:
                break
                
            if word1[i] == word2[j]:
                seq.append(i)
                j += 1
            # If characters don't match, use our 1 allowed change only if the remainder of word2 strictly fits
            elif not changed and (j + 1 == m or i < suf[j + 1]):
                changed = True
                seq.append(i)
                j += 1
                
        return seq if len(seq) == m else []