'''
Runtime: 36 ms, faster than 56.09% of Python3 online submissions for Reorder Data in Log Files.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Reorder Data in Log Files.
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # split letter logs and digit logs
        let_logs, dig_logs = [], []
        for log in logs:
            id_, cont = log.split(' ', 1)
            # if it is a letter log, split by space
            if cont[0].isalpha():
                let_logs.append([id_, cont])
            else:
                dig_logs.append(log)
      
        # sort letter log
        sorted_let_logs = sorted(let_logs, key=lambda l:(l[1], l[0]))
        return [' '.join(sll) for sll in sorted_let_logs] + dig_logs
