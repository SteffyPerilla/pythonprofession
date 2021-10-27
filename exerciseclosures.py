from typing import Generic, TypeVar

T = TypeVar('T')

def make_divisor(n:int) -> Generic[T]:
    def numerator(x:int) -> int:
        assert n != 0, 'You cannot divide by zero'
        return x//n
    return numerator

def main():
    divided_by_2 = make_divisor(18)
    print(divided_by_2(54))

if __name__ == '__main__':
    main()