a = [["a"], ["d"], ["h"], ["a"], ["a"], ["h"]]
print("".join(sum(a, [])).count("a"))
print(("".join(sum(a, [])).count("a") + "".join(sum(a, [])).count("h")) % 2)
