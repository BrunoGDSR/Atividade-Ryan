def parenteses_balanceados(expr):
    pilha = []
    pares = {')':'(', ']':'[', '}':'{'}
    for ch in expr:
        if ch in "([{":
            pilha.append(ch)
        elif ch in ")]}":
            if not pilha or pilha[-1] != pares[ch]:
                return False
            pilha.pop()
    return len(pilha) == 0

print(parenteses_balanceados("(a+b)*(c-d)"))
print(parenteses_balanceados("(a+b]*c"))