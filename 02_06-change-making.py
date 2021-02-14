import math


def change_making(denominations, target):
    cache = {}

    def subproblem(i, t):
        if (i, t) in cache: return cache[(i, t)]  # memoization

        # Compute the lowest number of coins we need if choosing to take a coin
        # of the current denomination.
        val = denominations[i]
        if val > t:
            # current denomination is too large
            choice_take = math.inf
        elif val == t:
            # target reached
            choice_take = 1
        else:
            # take and recurse
            choice_take = 1 + subproblem(i, t - val)

        # Compute the lowest number of coins we need if not taking any more
        # coins of the current denomination.
        if i == 0:
            # not an option if no more denominations
            choice_leave = math.inf
        else:
            # recurse with remaining denominations
            choice_leave = subproblem(i - 1, t)

        optimal = min(choice_take, choice_leave)
        cache[(i, t)] = optimal
        return optimal

    return subproblem(len(denominations) - 1, target)

if __name__ == '__main__':
    print(
        'change_making([1, 5, 12, 19], 16) = '
        f'{change_making([1, 5, 12, 19], 16)}')
