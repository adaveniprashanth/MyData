#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 17:17:14 2022

@author: pj
"""
if 0:
    class Solution:
        def maxSumRangeQuery(self, nums, requests):
            l = nums
            l.sort(reverse=True)
            total = 0
            for i in requests:
                p1 = l[i[0]:i[1]+1]
                for j in p1:
                    total+=j
            return total
    
    s = Solution()
    m = s.maxSumRangeQuery([1,2,3,4,5],[[1,3],[0,1]])
    print(m)


'''

 given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

def solution(A):
    # write your code in Python 3.6
    val = 0
    for i in A:
        if val < i:
            val = i
    if val < 0:
        return 1
    elif (val -1) not in A:
        return val -1
    else:
        return val+1

'''

