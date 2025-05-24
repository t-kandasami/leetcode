class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping_dict = {")": "(", "}": "{", "]": "["}

        for character in s:
            if character in mapping_dict.values():
                stack.append(character)
            elif character in mapping_dict.keys():
                if not stack or mapping_dict[character] != stack.pop():
                    return False
        return not stack


if __name__ == "__main__":
    is_valid = Solution()
    print(is_valid.isValid("()"))          # Output: True
    print(is_valid.isValid("()[]{}"))      # Output: True
    print(is_valid.isValid("(]"))          # Output: False
    print(is_valid.isValid("([)]"))        # Output: False
    print(is_valid.isValid("{[]}"))        # Output: True
    print(is_valid.isValid(""))             # Output: True
    print(is_valid.isValid("{{{{}}}}"))     # Output: True
    print(is_valid.isValid("{{{}}}"))       # Output: True
    print(is_valid.isValid("{{{}}"))        # Output: False
