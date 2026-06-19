# myModule.py

def add_mul(op, *args):
    if op == 'add':
        total = 0
        for arg in args:
            total += arg  
    elif op == 'mul':
        total = 1         
        for arg in args:
            total *= arg  
    else:
        raise ArithmeticError
    return total

if __name__ == "__main__":
    print(add_mul('add', 1, 2, 3, 4, 5))
    print(add_mul('mul', 1, 2, 3, 4, 5))

    