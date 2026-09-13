from collections import Counter

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Step 1: Extract coordinates of all '1's in both images
        ones_img1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones_img2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Step 2 & 3: Count the frequency of each translation vector required to map a 1 to a 1
        translation_counts = Counter()
        for r1, c1 in ones_img1:
            for r2, c2 in ones_img2:
                # The required shift to move (r1, c1) to (r2, c2)
                shift_vector = (r2 - r1, c2 - c1)
                translation_counts[shift_vector] += 1
                
        # Step 4: The maximum overlap is the most frequent shift, or 0 if no 1s exist
        return max(translation_counts.values()) if translation_counts else 0