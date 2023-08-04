class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        hashmap = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in hashmap.keys():
                if stack != [] and stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack == []:
            return True
        else:
            return False
