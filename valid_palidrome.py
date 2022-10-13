# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        flag = 0
        for char in s:
            if char.isalnum():
                flag = 1
        if flag == 0:
            return True
                
        if len(s) == 1:
            return True
        result = "".join(c for c in s if c.isalnum())
        result = result.lower()
        res_arr = list(result)

        if len(res_arr) % 2 != 0:
            upper = res_arr[:(len(res_arr)//2)]
            lower = res_arr[((len(res_arr)//2) + 1):]
            sub = lower[:]
            check = []
            for i in sub:
                check.append(lower.pop())
            check = "".join(check)
            upper = "".join(upper)
            if (check == upper):
                return True

        if len(res_arr) % 2 == 0:            
            upper = res_arr[:((len(res_arr)//2))]
            lower = res_arr[(len(res_arr)//2):]
            sub = lower[:]
            check = []
            for i in sub:
                check.append(lower.pop())
            check = "".join(check)
            upper = "".join(upper)
            if (check == upper):
                return True

           # aaaa 

if __name__ == '__main__':
    answer = Solution()
   # print(answer.isPalindrome("A man, a plan, a canal: Panama"))
   # print(answer.isPalindrome("race a car"))
    print(answer.isPalindrome("aaaa"))
   # print(answer.isPalindrome(" "))
   # print(answer.isPalindrome("a"))
   # print(answer.isPalindrome(".,"))
