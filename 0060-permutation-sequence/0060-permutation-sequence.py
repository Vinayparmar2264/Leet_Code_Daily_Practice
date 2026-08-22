
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        # Store numbers: [1, 2, 3, ..., n]
        numbers = []

        # (n-1)!
        fact = 1

        for i in range(1, n):
            fact *= i
            numbers.append(i)

        numbers.append(n)

        # Convert k to 0-based indexing
        k -= 1

        ans = ""

        while True:

            # Find which number should come at this position
            index = k // fact

            ans += str(numbers[index])

            # Remove the selected number
            numbers.pop(index)

            # If no numbers are left, we are done
            if len(numbers) == 0:
                break

            # Find position inside the selected block
            k = k % fact

            # Calculate factorial for remaining numbers
            fact = fact // len(numbers)

        return ans