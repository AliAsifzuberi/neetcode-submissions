class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        count_s = {}
        left = 0
        have = 0
        need = len(count_t)

        min_len = float("inf")
        best_window = ""

        for right in range(len(s)):
            char = s[right]
            count_s[char] = count_s.get(char, 0) + 1

            if char in count_t and count_s[char] == count_t[char]:
                have += 1

            while have == need:
                current_len = right - left + 1

                if current_len < min_len:
                    min_len = current_len
                    best_window = s[left:right + 1]

                left_char = s[left]
                count_s[left_char] -= 1

                if (
                    left_char in count_t
                    and count_s[left_char] < count_t[left_char]
                ):
                    have -= 1

                left += 1

        return best_window