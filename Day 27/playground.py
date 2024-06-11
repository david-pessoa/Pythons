def add(*args):
    soma = 0
    for num in args:
        soma += num
    return soma

def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs.get("add"))
    print(kwargs.get("multiply"))
    print(n)

calculate(2, multi = 3)