class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    current_len = i - stack[-1]
                    if current_len > max_len:
                        max_len = current_len
                else:
                    stack.append(i)
        return max_len