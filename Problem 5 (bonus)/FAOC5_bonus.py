# BONUS: System Override: The Kernel Panic
# FATAL ERROR.
#
# The Dean's message is trapped inside the Kernel's execution layer. You have dumped the raw function calls from the memory stack.
#
# To retrieve the message, you must implement an interpreter for the FINKI Kernel Language (FKL).
#
# Supported Functions:
#
#     HEX(s): Decodes a Hexadecimal string into ASCII. (e.g., HEX(4869) -> "Hi")
#
# REV(s): Reverses the string. (e.g., REV(ABC) -> "CBA")REP(n, s): Repeats the string s, n times.CAT(s1, s2, ...): Concatenates multiple strings.Nesting: Functions can be nested arbitrarily deep.
# Input Format:
# A single string representing a nested function call.
#
# Input Example:
# CAT(REP(2, REV(HEX(4f454e))), _WAKE_UP)
#
# Execution Trace:
#
#     HEX(4f454e) -> "NEO"
#
# REV("NEO") -> "OEN"REP(2, "OEN") -> "OENOEN"CAT("OENOEN", "_WAKE_UP") -> "OENOEN_WAKE_UP"
# Your Task:
# Evaluate the expression and return the final string.
# Example Input:
# CAT(REP(2,REV(HEX(4f454e))),_WAKE_UP)
# output:
# Explanation: OENOEN_WAKE_UP



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
