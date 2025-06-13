'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

https://neetcode.io/problems/string-encode-and-decode?list=blind75

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
'''

class Solution:

    def encode(self, strs):
        s = ""
        for word in strs:
            s += str(len(word)) + "$" + word
        return s
    def decode(self, s: str):
        l = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j+=1
            lenght = int(s[i:j])
            l.append(s[j+1:j+1+lenght])
            i = j + lenght + 1
        return l
