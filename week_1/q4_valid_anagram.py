class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t

if __name__ == "__main__":
    is_anagram = Solution()
    print(is_anagram.isAnagram("anagram", "nagaram"))  # Output: True
    print(is_anagram.isAnagram("rat", "car"))          # Output: False
    print(is_anagram.isAnagram("listen", "silent"))    # Output: True
    print(is_anagram.isAnagram("hello", "world"))      # Output: False
    print(is_anagram.isAnagram("", ""))                 # Output: True