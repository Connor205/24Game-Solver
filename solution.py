"""Used for computing if the 24 game is solvable. 
"""
import itertools
import time


def solveable(vals: list) -> bool:
    expressions = [
        "+",
        "-",
        "*",
        # "/",
        #"**",
    ]
    expr_combos = list(itertools.product(expressions, repeat=3))
    #print(expr_combos)
    perm_set = list(set(itertools.permutations(vals)))
    for perm in perm_set:
        a = perm[0]
        b = perm[1]
        c = perm[2]
        d = perm[3]
        for expr in expr_combos:
            test1 = f'(({a} {expr[0]} {b}) {expr[1]} {c} ) {expr[2]} {d}'
            test2 = f'{a} {expr[0]} ( {b} {expr[1]} {c} ) {expr[2]} {d}'
            test3 = f'{a} {expr[0]} (( {b} {expr[1]} {c} ) {expr[2]} {d})'
            test4 = f'{a} {expr[0]} ( {b} {expr[1]} ({c}  {expr[2]} {d}))'
            test5 = f'({a} {expr[0]} {b}) {expr[1]} ({c}  {expr[2]} {d})'
            tests = [test1, test2, test3, test4, test5]
            for test in tests:
                #print(test)
                try:
                    if eval(test) == 24:
                        #print(test)
                        return True
                except ZeroDivisionError:
                    pass
                except OverflowError:
                    pass


# hard = [13, 12, 10, 8]
# hard2 = [5, 1, 1, 1]
# solveable(hard2)
combos = list(itertools.combinations_with_replacement(range(1, 10), 4))
#print(combos)
print(len(combos))
start = time.time()
combos = [x[:2] for x in combos if solveable(x)]
new_combos = []
for x in combos:
    if solveable(x):
        new_combos.append(x)
print(combos)
end = time.time()
print(len(combos))
print(end - start)
