# Given two strings s and t, return true if t is an anagram of s, and false otherwise

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        key = "".join(sorted(s))
        value = "".join(sorted(t))
        if key == value:
            return True
        return False

if __name__ == '__main__':
    answer = Solution()
    print(answer.isAnagram("rats", "star"))

# rats, star, cars, arcs etc
