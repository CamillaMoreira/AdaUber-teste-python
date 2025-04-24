def evaluate_polish(expression: str) -> int:
    tokens = expression.split()[::-1]  
    stack = []

    for token in tokens:
        if token in "+-*/":
            a = stack.pop()
            b = stack.pop()
            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = int(a / b)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack[0]


print(evaluate_polish("+ 3 4"))  
print(evaluate_polish("* + 2 3 4"))  
print(evaluate_polish("- * 7 4 + 2 3"))  
print(evaluate_polish("/ * 8 4 2"))  
