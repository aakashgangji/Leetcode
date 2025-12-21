class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if not A or len(A) <= 1:
            return 0
        num_strings = len(A)
        string_length = len(A[0])
        deleted_columns = 0
        sorted_pairs = [False] * num_strings
        for col in range(string_length):
            should_delete = False
            for row in range(num_strings - 1):
                if not sorted_pairs[row] and A[row][col] > A[row + 1][col]:
                    deleted_columns += 1
                    should_delete = True
                    break  
            if should_delete:
                continue
            for row in range(num_strings - 1):
                if A[row][col] < A[row + 1][col]:
                    sorted_pairs[row] = True
        return deleted_columns