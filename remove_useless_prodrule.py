import re

# CFG, G = (V, T, S, P) where V = {S, A, B, C} and T = {a, b}
# Production rule is given by user


# Main fucntion.
# Get the production rule from user
if __name__ == "__main__" :
    
    description = "Input production rules of the CFG G = (V, T, S, P) where V = {S, A, B, C} and T = {a, b}"
    V = {'S', 'A', 'B', 'C'}
    T = {'a', 'b'}
    P = []
    
    print(description)
    n_of_rules = int(input("1. Input the number of production rule : "))

    print("2. Input the production rules of the form 'A -> ab'")

    # regex of input format
    p = re.compile('[SABC]{1}\s->\s[SABCab]+')
    
    for i in range(1, n_of_rules+1):
        while(True):
            input_str = input(str(i) + ') ')
            m = p.match(input_str)
            if m:
                rule = [x.strip() for x in input_str.split('->')]
                P.append(rule)
                break
            else:
                print("Format not matched. Input proudction should be of the form 'A -> ab'. Check variables and terminal symbols too.")
            

    # step 1: Eliminate variables which do not derive terminal symbol
    
    V_1 = set()

    for i in range(n_of_rules):
        for rule in P:
            if set(rule[1]).issubset(T | V_1):
                V_1.add(rule[0])

    # Eliminate useless production rules
    useless_V = V - V_1
    P_1 = []

    for rule in P:
        is_uesless = False
        for x in rule[1]:
            if x in useless_V:
                is_uesless = True
        
        if rule[0] in useless_V or is_uesless:
            continue
        else:
            P_1.append(rule)
    

    # step 2: Eliminate non reachable varibles
    n_of_rules = len(P_1)
    V_2 = {'S'}

    for i in range(n_of_rules):
        for rule in P_1:
            # For the rule A -> x1x2...xi where A in V_1 and xi in T | V_1 for all i,
            # if A is in V_2, then add xi in V_1 to V_2 which implies it is reachable variable
            if rule[0] in V_2:
                for x in rule[1]:
                    if x in V_1:
                        V_2.add(x)

    # Eliminate useless production rules
    useless_V = V_1 - V_2
    P_2 = []

    for rule in P_1:
        is_uesless = False
        for x in rule[1]:
            if x in useless_V:
                is_uesless = True
        
        if rule[0] in useless_V or is_uesless:
            continue
        else:
            P_2.append(rule)

        
    print("Before elminating useless production : ")
    for rule in P:
        print('{0} -> {1}'.format(rule[0], rule[1]))
    

    print('---------------------------------------')
    print("After elminating useless production : ")
    for rule in P_2:
        print('{0} -> {1}'.format(rule[0], rule[1]))


                
            

