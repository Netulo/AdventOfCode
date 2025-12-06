
def print_solution(part, method: str, *args):
    print(f"\n*-----------PART {part}-------------")
    if method == "": print("|")
    else: print(f"| METHOD -> {method}")

    for val in args:
        print(val)

    print("|")
    print("*------------------------------\n")