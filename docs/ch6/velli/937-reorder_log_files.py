from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        num_list = []
        str_list = []
        for log in logs:
            if log.split()[1].isnumeric():
                num_list.append(log)
            else:
                str_list.append(log)

        return sorted(str_list, key=lambda x: (x.split(" ", 1)[1], x.split()[0])) + num_list


if __name__ == "__main__":
    solution = Solution()
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(solution.reorderLogFiles(logs))
