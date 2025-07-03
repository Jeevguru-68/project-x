def bracketmatching(expr):
    stack=[]
    for char in expr:
        if char in ["(","{","["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char=stack.pop()
            if current_char=='(':
                if char!=")":
                    return False
            if current_char=='{':
                if char!="}":
                    return False
            if current_char=='[':
                if char!="]":
                    return                                                                                                                                                  0
    if stack:
        return False
    return True
expr="{()}[]"
if bracketmatching(expr):
    print("matching")
else:
    print("not matching")
                
            