from math import floor


# bbbbb
class Solution:
    """
    Uses the valid area under the triangle with base start and target
    to find traversable paths. Complexity = (2* (ncls/2 * (ncls/4+1))
    => O(sq(ncls)) where ncls = tgt_col + 1, i.e., the number of columns
    from start to target.
    """

    def __init__(self) -> None:
        self.tgt_row = 0
        self.start = (0, 0)

    # max_dim specifies max valid [0]row and [1]column
    def run(self, max_dim: tuple[int, int], tgt_col: int) -> int:
        print("\ntarget: ", (self.tgt_row, tgt_col))
        if max_dim[1] < tgt_col:
            raise ValueError(f"Target {tgt_col} out of bounds {max_dim} ")
        # base case: 1 path at target
        sol: dict[tuple[int, int], int] = {(self.tgt_row, tgt_col): 1}

        for j in range(tgt_col - 1, floor(tgt_col / 2), -1):
            for i in range(0, min((tgt_col + 1 - j), max_dim[0] + 1)):
                sol[(i, j)] = (
                    sol.get((i + 1, j + 1), 0)
                    + sol.get((i, j + 1), 0)
                    + sol.get((i - 1, j + 1), 0)
                )

        for j in range(floor(tgt_col / 2), 0, -1):
            for i in range(0, min(j + 1, max_dim[0] + 1)):
                sol[(i, j)] = (
                    sol.get((i + 1, j + 1), 0)
                    + sol.get((i, j + 1), 0)
                    + sol.get((i - 1, j + 1), 0)
                )
        sol[self.start] = (
            sol.get(self.start, 0)
            + sol.get((self.start[0], self.start[1] + 1), 0)
            + sol.get((self.start[0] + 1, self.start[1] + 1), 0)
        )
        # print("sol: ", sol)
        return sol[self.start]


def main():
    s = Solution()
    dimensions = (4, 9)
    for i in range(dimensions[1] + 1):
        print("Num paths: ", s.run(dimensions, i))


if __name__ == "__main__":
    main()

"""
aaaaaaa

ccc
"""
