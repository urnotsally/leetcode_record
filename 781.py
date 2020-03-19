class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        tmp = {}
        total = 0
        for i in range(len(answers)):
            total_of_one = answers[i] + 1
            if not tmp.get(total_of_one, 0):
                tmp[total_of_one] = answers[i]
                total += total_of_one
            else:
                if tmp[total_of_one] == 0:
                    total += answers[i]
                else:
                    tmp[total_of_one] -= 1

        return total

if __name__ == '__main__':
    Solution().numRabbits([1,1,2])