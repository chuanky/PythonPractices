'''传奇加了一句话'''
'''MG加了一句话'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == None or s == '': return s

        max_word = ''
        for index in range(len(s)):
            curr_word = s[index]
            left = index
            right = index
            while right + 1 < len(s) and s[index] == s[right + 1]:
                right += 1
                curr_word = s[index:right+1]

            curr_word = self.expand(s, index, left, right, curr_word)
            if len(max_word) < len(curr_word):
                max_word = curr_word

        return max_word

    def expand(self, s, index, left, right, curr_word):
        if left < 0 or left >= len(s) or right < 0 or right >= len(s):
            return curr_word
        
        if s[left] == s[right]:
            return self.expand(s, index, left - 1, right + 1, s[left:right+1])
        else:
            return curr_word

solution = Solution()
r = solution.longestPalindrome("ccc")
print(r)