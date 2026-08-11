class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()

        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        for i, ch in enumerate(s):

            if ch in seen:
                continue

            # Remove bigger characters if they appear again later
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(ch)
            seen.add(ch)
        print(last)
        return ''.join(stack)