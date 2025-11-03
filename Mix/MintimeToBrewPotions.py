"""
You are given two integer arrays, skill and mana, of length n and m, respectively.
In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].
Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​
Return the minimum amount of time required for the potions to be brewed properly.
Example 1:
Input: skill = [1,5,2,4], mana = [5,1,4,2]
Output: 110
Explanation:
Potion Number	Start time	Wizard 0 done by	Wizard 1 done by	Wizard 2 done by	Wizard 3 done by
0	0	5	30	40	60
1	52	53	58	60	64
2	54	58	78	86	102
3	86	88	98	102	110
As an example for why wizard 0 cannot start working on the 1st potion before time t = 52, consider the case where the wizards started preparing the 1st potion at time t = 50. At time t = 58, wizard 2 is done with the 1st potion, but wizard 3 will still be working on the 0th potion till time t = 60.
Example 2:
Input: skill = [1,1,1], mana = [1,1,1]
Output: 5
Explanation:
Preparation of the 0th potion begins at time t = 0, and is completed by time t = 3.
Preparation of the 1st potion begins at time t = 1, and is completed by time t = 4.
Preparation of the 2nd potion begins at time t = 2, and is completed by time t = 5.
"""
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        if n == 0 or m == 0:
            return 0

        # prefix time for first potion
        prev_pref = [0] * n
        cum = 0
        for i in range(n):
            cum += skill[i] * mana[0]
            prev_pref[i] = cum

        start = 0  # start time of current potion

        # iterate over next potions
        for j in range(1, m):
            curr_pref = [0] * n
            cum = 0
            for i in range(n):
                cum += skill[i] * mana[j]
                curr_pref[i] = cum

            # compute minimal gap required between s[j-1] and s[j]
            gap = float('-inf')
            for i in range(n):
                a = prev_pref[i]              # sum_{k=0..i} t[k][j-1]
                b = curr_pref[i-1] if i > 0 else 0  # sum_{k=0..i-1} t[k][j]
                gap = max(gap, a - b)

            start += gap
            prev_pref = curr_pref  # move to next potion

        # makespan = start time of last potion + total processing time of it
        return start + prev_pref[-1]
