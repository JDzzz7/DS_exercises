# 121 123 321
class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack = []
        rev = []
        str_x = str(x)
        original = list(str_x)
        stack = list(str_x)
        print(stack)
        for i in range(len(original)):
            print("here")
            rev.append(stack.pop((len(stack)-1)))

        for i in range(len(original)):
            if rev[i] != original[i]:
                print(f"rev{i}: {rev[i]}")
                print(f"original{i}: {original[i]}")
                return False
        return True

solution = Solution()
answer = solution.isPalindrome(121)
print(f"ans: {answer}")
