def is_operator(token):
    return token in ['+', '-', '*', '/']

def evalueer_postfix(expressie):
    stapel = []    
    for token in expressie:
        if is_operator(token):
            op2 = stapel.pop()
            op1 = stapel.pop()
            if token == '+':
                stapel.append(op1 + op2)
            elif token == "-":
                stapel.append(op1 - op2)
            elif token == "*":
                stapel.append(op1 * op2)
            elif token == "/":
                stapel.append(op1 / op2)
            else:
                raise ValueError("Onbekende operator") # Should not happen
        else:
            stapel.append(float(token))
    
    assert len(stapel) == 1, "Verkeerde postfix uitdrukking" # Should not happen

    return stapel[0]

def prioriteit(token): # kan ook met een dict --> {'*': 2, '/': 2 ... }
    if token in ['+', '-']:
        return 1
    if token in ['*', '/']:
        return 2
    if token == '(':
        return 0 # haakje heeft laagtste prioriteit
    return None # zou niet mogen gebeuren

def infix_naar_postfix(expressie):
    stapel = []
    postfix = []
    for token in expressie:
        if is_operator(token):
            while len(stapel) > 0 and prioriteit(stapel[-1]) >= prioriteit(token):
                postfix.append(stapel.pop())
            # len(stapel) == 0 or prioriteit(stapel[-1]) < prioriteit(token)   
            stapel.append(token)
            
        elif token == '(':
            stapel.append(token)
        elif token == ')':
            while stapel[-1] != '(':
                postfix.append(stapel.pop())
            stapel.pop()            
        else:
            postfix.append(token)
    
    while len(stapel) > 0:
        postfix.append(stapel.pop())

    return postfix


def parse_expressie(expressie):
    return expressie.split()

def rekenmachine(s):
    expressie = parse_expressie(s)
    postfix = infix_naar_postfix(expressie)
    return evalueer_postfix(postfix)

if __name__ == "__main__":
    print(evalueer_postfix(["3", "5", "+"]))
    print(evalueer_postfix(["3", "5", "-"]))
    print(evalueer_postfix(["3", "5", "*"]))
    print(evalueer_postfix(["3", "5", "/"]))

    print(infix_naar_postfix(["3", "+", "5"]))
    print(infix_naar_postfix(["3", "+", "5" , "*", "2"]))
    print(infix_naar_postfix(["(", "3", "+", "5" , ")", "*", "2"]))

    print("Geef expressie")
    exp = input()
    tokens = parse_expressie(exp)
    postfix = infix_naar_postfix(tokens)
    print(f"{exp} = {evalueer_postfix(postfix)}")