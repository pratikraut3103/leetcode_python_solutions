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
