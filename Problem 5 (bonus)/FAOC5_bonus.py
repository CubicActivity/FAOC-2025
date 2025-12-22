#just strips the expression from white space
def evaluate(expr):
    expr = expr.strip()

#convert hex to text
    if expr.startswith("HEX("):
        return bytes.fromhex(expr[4:-1]).decode()

#reverse string
    if expr.startswith("REV("):
        return evaluate(expr[4:-1])[::-1]

#repeat string n times,
    if expr.startswith("REP("):
        inner = expr[4:-1]
        depth = 0
        for i, c in enumerate(inner):
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            elif c == ',' and depth == 0:
                n_str = inner[:i]
                s_expr = inner[i+1:]
                break
        n = int(n_str.strip())
        return evaluate(s_expr) * n

#concatenate strings once we reach the comma separator
    if expr.startswith("CAT("):
        inner = expr[4:-1]
        args = []
        depth = 0
        last_index = 0
        for i, c in enumerate(inner):
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            elif c == ',' and depth == 0:
                args.append(inner[last_index:i])
                last_index = i + 1
        args.append(inner[last_index:])
        return ''.join(evaluate(arg) for arg in args)

    return expr.strip().strip('"')


def main():
    with open("user_input.txt", "r") as f:
        expr = f.read().strip()
    print(evaluate(expr))


if __name__ == "__main__":
    main()
