# 121 123 321
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        reverse = []
        non_reverse = []
        popper = []
        if num < 0:
            return False

        while(num > 0):
            mod_val = num % 10
            reverse.append(mod_val)
            popper.append(mod_val)
            num = num // 10
        print(reverse)
        for i in range(len(reverse)):
            non_reverse.append(popper.pop((len(popper)-1)))
        print(non_reverse)
        print("why")
        print(reverse)
        for j in range(len(non_reverse)):
            print("I'm here")
            print(j)
            if (reverse[j] != non_reverse[j]):
                print("am I here")
                return False
        return True  
        
solution = Solution()
answer = solution.isPalindrome(1010)
print(f"ans: {answer}")
