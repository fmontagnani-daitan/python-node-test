from src.calculator.calculator import Calculator

def main(operation_code: int, num1: int, num2: int) -> None:
    calculator = Calculator()
    try:
        result = calculator.execute_operation(operation_code, num1, num2)
        print(f'Result is: {result}')
    except Exception as e:
        print(e)
        raise e


if __name__ == '__main__':
    main(0, 1, 1)   # pragma: no cover
    main(1, 1, 1)   # pragma: no cover
    main(2, 1, 1)   # pragma: no cover
    main(3, 1, 1)   # pragma: no cover
    main(3, 1, 'e') # pragma: no cover
