from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        not_palindrome, palindrome, pairs = {}, {}, defaultdict(set)

        for w in words:
            if w == w[::-1]: palindrome[w] = palindrome.get(w, 0) + 1
            else: not_palindrome[w] = not_palindrome.get(w, 0) + 1

        # print("before palindrome: ", palindrome)
        # print("not_palindrome: ", not_palindrome)

        for k in not_palindrome.keys():
            if not_palindrome.get(k[::-1], 0) != 0:
                pairs[(k, k[::-1])] = min(not_palindrome[k], not_palindrome[k[::-1]])
             
        # print("pairs: ", pairs)

        n, palindrome_w_max_len_cnt_1 = 0, 0
        for k, v in palindrome.items():
            if v > 1:
                cnt = v // 2
                palindrome[k] -= cnt*2
                v = palindrome[k]
                # print("k: ", k, " cnt: ", cnt*2, " increment: ", len(k)*cnt)
                n += len(k)*cnt*2
            if v == 1: palindrome_w_max_len_cnt_1 = max(palindrome_w_max_len_cnt_1, len(k))
        n += palindrome_w_max_len_cnt_1

        # print("after palindrome: ", palindrome)

        m = 0
        for k, v in pairs.items(): m += v*len(k[0])

        return n + m