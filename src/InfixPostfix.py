def split_tokens(string: str) -> list:
    result = []
    val = 0
    val_processing = False
    for c in string:
        if c == " ":
            continue
        if c.isdecimal():
            tmp_num = tmp * 10 + int(c)
            val_processing = True
            continue
        else:
            if val_processing:
                result.append(val)
                val = 0
                val_processing = Fals
            result.append(c)
    if val_processing:
        result.append(val)
    
    return result
    
def infix_to_postfix(token_list):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    operation_stack = []
    postfix_list = []
    for token in token_list:
        if token == ')':
            while operation_stack.peek() != '(':
                postfix_list.append(operation_stack.pop())
            operation_stack.pop()
        elif token in prec:
            while operation_stack and token != '(' and prec[operation_stack[-1] >= prec[token]:
                postfix_list.append(operation_stack.pop())
            operation_stack.append(token)
        else:
            postfix_list.append(token)
    while operation_stack:
        postfix_list.append(operation_stack.pop())
    return postfix_list


def calculate_postfix(token_list):
    stack = []
    prec = {'+', '-', '*', '/'}
    
    for token in token_list:
        if not token in prec:
            stack.append(token)
        else:
            B = stack.pop()
            A = stack.pop()
            if token == '+':
                stack.append(A + B)
            elif token == '-':
                stack.append(A - B)
            elif token == '*':
                stack.append(A * B)
            else:
                stack.append(A / B)
                
    return stack.pop()