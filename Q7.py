'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



    Example 1:

    Input: x = 123
    Output: 321

    Example 2:
    Input: x = -123
    Output: -321

    Example 3:
    Input: x = 120
    Output: 21

    Example 4:
    Input: x = 0
    Output: 0
'''
class Solution:
    def reverse(self, x: int) -> int:
        revs_number = 0
        number = x
        temp = ''
        if number < 0 :
            number = abs(number)
            temp = '-'
        while (number > 0):
            remainder = number % 10
            revs_number = (revs_number * 10) + remainder
            number = number // 10
        if x < 0 :
            revs_number = - revs_number
        if abs(revs_number) < 2**31 and revs_number != 2**31 - 1:
            return revs_number
        else:
            return 0

if __name__ == '__main__':
    so = Solution()
    print(so.reverse(1534236469))
