class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        total_flip = 0

        index = n - 2

        Flag = True

        while Flag:

            if k == 1:
                return (0 + total_flip) % 2
            elif k == 2:
                return (1 + total_flip) % 2

            if k > pow(2, index):
                total_flip += 1
                k -= pow(2, index)

            index -= 1