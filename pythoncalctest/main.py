from src.calculator.calculator import Calculator # pylint: disable=import-error

def main(operation_code, num1, num2):
    calculator = Calculator()
    try:
        result = calculator.execute_operation(operation_code, num1, num2)
        print(f'Result is: {result}')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main(0, 1, 1)
    main(1, 1, 1)
    main(2, 1, 1)
    main(3, 1, 1)
    main(3, 1, 'e')
