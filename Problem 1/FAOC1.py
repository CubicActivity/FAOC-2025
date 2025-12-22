# Week 1: Capybara Picnic Groups
# Capybaras are planning a picnic. Each capybara has a "friendliness score".
#
# A group of capybaras is valid if:
#
#     The group contains at least 2 capybaras.
#
# The difference between the maximum and minimum friendliness scores in the group is at most K.
# Input Format:
# The first line contains the integer K.
# The second line contains the list of friendliness scores separated by commas.
#
# Your Task:
# Return the maximum number of capybaras that can attend a single valid picnic group. If no valid group can be formed, return 0.
#
# Example Input:
#
# 2
# 3,5,2,7,4
#
# Explanation:
# Sorted scores: [2, 3, 4, 5, 7]
# Valid groups with diff <= 2: [2,3,4], [3,4,5], [5,7], etc.
# The largest group is [2, 3, 4] (size 3).
# Output: 3

def largestGroupSize(K, NotSortedScores):
    SortedScores = sorted(NotSortedScores)
    left = 0
    max_size = 0

    for right in range(len(SortedScores)):
        while SortedScores[right] - SortedScores[left] > K:
            left += 1
        group_size = right - left + 1
        if group_size >= 2:
            max_size = max(max_size, group_size)
    return max_size

if __name__ == "__main__":
    with open("user_input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    K = int(lines[0])
    scores = list(map(int, lines[1].split(",")))
    result = largestGroupSize(K, scores)
    print(result)
