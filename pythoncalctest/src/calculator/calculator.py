from src.operations.operations import soma, subtract, multiply, divide # pylint: disable=import-error

class Calculator():
    def __init__(self) -> None:
        self._sum = soma
        self._subtract = subtract
        self._multiply = multiply
        self._divide = divide
    
    def validate_numbers(self, num1, num2) -> bool:
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise TypeError('Error: Operands must be numbers')
        return True
    
    def execute_operation(self, operation_code, num1, num2):
        if self.validate_numbers(num1, num2):
            if operation_code == 0:
                return self._sum(num1, num2)
            elif operation_code == 1:
                return self._subtract(num1, num2)
            elif operation_code == 2:
                return self._multiply(num1, num2)
            elif operation_code == 3:
                return self._divide(num1, num2)
            else:
                raise ValueError(message='Operation code must be between 0 and 3')
