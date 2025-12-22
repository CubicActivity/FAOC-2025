# Week 2: Stella's Diary
# Stella keeps a meticulous diary. Every day, she rates her "Vibe Score" as an integer (positive for great days, negative for terrible days).
#
# Stella wants to look back and find her "Golden Era". A "Golden Era" is defined as a contiguous sequence of days where the sum of Vibe Scores is maximized.
#
# Input Format:
# A single line containing a list of integers (Vibe Scores) separated by commas.
#
# Your Task:
# Return the sum of the "Golden Era" (the maximum sum of any contiguous subarray).
# Note: If all numbers are negative, the solution is the single largest number (closest to 0).
# Example input:  10,-5,40,-60,15
# Explanation: The sequence [10, -5, 40] sums to 45. The sequence [15] is 15. The max is 45.

def golden_era(vibe_scores):
    max_sum = current_sum = vibe_scores[0]
    for score in vibe_scores[1:]:
        current_sum = max(score, current_sum + score)
        max_sum = max(max_sum, current_sum)
    return max_sum

def main():
    with open("user_input.txt", "r") as file:
        line = file.readline().strip()
        scores = list(map(int, line.split(',')))
    print(golden_era(scores))

if __name__ == "__main__":
    main()
