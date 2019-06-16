# Removing useless production from CFG

In order to make it simple, I do not care lambda productions and unit productions.

Let G = (V, T, S, P) be CFG, where V = {S, A, B, C} and T = {a, b}. (You can change these variables and symbols) Take production rules from user input and return production rules after removing useless productions. 


## Language

python3

## Usage

Run DFA.py

    python DFA.py

First input : number of production rules

Example: 

    Input production rules of the CFG G = (V, T, S, P) where V = {S, A, B, C} and T = {a, b}
    1. Input the number of production rule : 6

Second input : production rule of the form 'A -> ab'

Example: 

    2. Input the production rules of the form 'A -> ab'
    1) S -> aS
    2) S -> A
    3) S -> C
    4) A -> a
    5) B -> aa
    6) C -> aCb

Return production rules before/after removing useless production rules

    Before elminating useless production : 
    S -> aS
    S -> A
    S -> C
    A -> a
    B -> aa
    C -> aCb
    ---------------------------------------
    After elminating useless production : 
    S -> aS
    S -> A
    A -> a
