'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

https://leetcode.com/problems/koko-eating-bananas/description/

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

'''
import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        res = 1
        mi = 1
        ma = max(piles)
        while mi <= ma:
            k = (mi + ma) // 2
            c = 0
            for pile in piles:
                if pile <= k:
                    c+=1
                else:
                    c+=math.ceil(float(pile)/k)
            if c <= h:
                ma = k - 1
                res = k
            else:
                mi = k + 1

        return res
       