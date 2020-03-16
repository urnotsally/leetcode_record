class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = [[0 for i in range(len(s))] for j in range(len(s))]

        for a in range(len(s)):
            for i in range(len(s)):
                j = i + a
                if j >= len(s):
                    break
                if i > j:
                    ans[i][j] = 0
                    continue
                if i == j:
                    ans[i][j] = 1
                    continue
                if s[i] == s[j]:
                    ans[i][j] = 2 + ans[i + 1][j - 1]
                    continue
                if s[i] != s[j]:
                    ans[i][j] = max(ans[i + 1][j], ans[i][j - 1])
                    continue

        return ans[0][len(s) - 1]


if __name__ == '__main__':
    print Solution().longestPalindromeSubseq("bbbab")