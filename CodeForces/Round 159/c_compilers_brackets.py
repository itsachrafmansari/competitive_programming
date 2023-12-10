def isValid(text: str) -> str:
    stack = []

    for char in text:
        if char == "{":
            stack.append(char)
        elif char == "}":
            if len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                return "invalid"

    if len(stack) == 0:
        return "valid"
    else:
        return "invalid"


case = input()
print(isValid(case))
