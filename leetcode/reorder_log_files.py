'''
Reorder Log Files
Source : https://leetcode.com/problems/reorder-log-files/

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

Note:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.

'''


class Solution:
    aresult = []

    def reorderLogFiles(self, logs):

        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        letters = []
        # divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: x.split()[0])  # when suffix is tie, sort by identifier
        letters.sort(key=lambda x: x.split()[1:])  # sort by suffix
        self.aresult = letters + digits  # put digit logs after letter logs

        for log in self.aresult:
            print(log)
        return self.aresult

if __name__ == "__main__":
    logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    sol = Solution().reorderLogFiles(logs)
    # sol.reorderLogFiles(logs)

