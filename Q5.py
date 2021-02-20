'''
    Given a string s, return the longest palindromic substring in s.

    Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

    Input: s = "cbbd"
    Output: "bb"

    Input: s = "a"
    Output: "a"

    Input: s = "ac"
    Output: "a"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = s
        my_list = []
        if s == s[::-1]:
            return s
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s == s[::-1]:
                return s
            else:
                return s[0]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    temp = s[i : j+1]
                    if temp == temp[::-1]:
                        my_list.append(temp)
        if len(my_list) > 0:
            value = [len(x) for x in my_list]
            max_value = max(value)
            for _ in range(len(value)):
                if value[_] == max_value:
                    return my_list[_]
        else:
            return s[0]

if __name__ == '__main__':
    so = Solution()
    print(so.longestPalindrome("babad"))
