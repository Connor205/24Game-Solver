"""Used for computing if the 24 game is solvable. 
   By Connor Nelson
"""
import itertools
import time


def solveable(vals: list) -> bool:
    """If a given list of size 4 is solveable for the 24 game.

    Args:
        vals (int): List of 4 ints

    Returns:
        bool: If the 24 game is solveable with them.
    """

    # This is the list of expressions that can be used in the solution
    # in python form.
    expressions = [
        "+",
        "-",
        "*",
        # "/",
        #"**",
    ]

    # Gets a set of all possible orders of the expressions list
    # with replacement.
    expr_combos = list(itertools.product(expressions, repeat=3))

    # Gets a list of all of the different orderings of the values
    perm_set = list(set(itertools.permutations(vals)))
    # Iterates over all the permutations
    for perm in perm_set:
        a = perm[0]
        b = perm[1]
        c = perm[2]
        d = perm[3]
        for expr in expr_combos:
            # Goes through all of the possible configurations for parens
            test1 = f'(({a} {expr[0]} {b}) {expr[1]} {c} ) {expr[2]} {d}'
            test2 = f'{a} {expr[0]} ( {b} {expr[1]} {c} ) {expr[2]} {d}'
            test3 = f'{a} {expr[0]} (( {b} {expr[1]} {c} ) {expr[2]} {d})'
            test4 = f'{a} {expr[0]} ( {b} {expr[1]} ({c}  {expr[2]} {d}))'
            test5 = f'({a} {expr[0]} {b}) {expr[1]} ({c}  {expr[2]} {d})'
            tests = [test1, test2, test3, test4, test5]
            for test in tests:
                try:
                    # Checks to see if the expression evaluates to 24
                    if eval(test) == 24:
                        return True
                # Deals with various exceptions that can be thrown
                except ZeroDivisionError:
                    pass
                except OverflowError:
                    pass


# Creates a list of all possible lists with the numbers 1-9 with replacement
combos = list(itertools.combinations_with_replacement(range(1, 10), 4))
# Total number of combos
print(len(combos))
# Times the running
start = time.time()
# Gets all combos that are solveable
combos = [x for x in combos if solveable(x)]
#print(combos)
end = time.time()
# number of combos that work
print(len(combos))
print(end - start)
