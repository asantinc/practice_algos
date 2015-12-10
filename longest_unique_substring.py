'''
Find length of longest substring with unique characters
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: #empty string
            return 0
            
        start, i, max_len = 0, 0, 1
        unique = {}
        i = 0
        
        for i, char in enumerate(s):
            if char in unique and unique[char] >= start:
                if max_len < i-start:
                    max_len = i-start
                start = unique[char]+1
            unique[char] = i

        max_len = max(max_len, i+1-start)
        return max_len

if __name__ == '__main__':
    a = ''
    b = 'aa'
    c = 'abc'
    d = 'abac'
    e = 'bbbc'

    s = Solution()
    assert s.lengthOfLongestSubstring(a) == 0
    assert s.lengthOfLongestSubstring(b) == 1
    assert s.lengthOfLongestSubstring(c) == 3
    assert s.lengthOfLongestSubstring(d) == 3
    assert s.lengthOfLongestSubstring(e) == 2
