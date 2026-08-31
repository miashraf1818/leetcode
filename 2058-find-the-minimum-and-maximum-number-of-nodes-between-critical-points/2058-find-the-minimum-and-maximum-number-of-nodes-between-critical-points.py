class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next

        pos = 1
        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:
            # Check for local maximum or local minimum
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                if first == -1:
                    first = pos
                else:
                    min_dist = min(min_dist, pos - last)

                last = pos

            prev = curr
            curr = curr.next
            pos += 1

        # Less than 2 critical points
        if first == -1 or first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]