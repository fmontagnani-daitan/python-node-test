from typing import Union
from src.operations.operations import soma, subtract, multiply, divide

class Calculator():
    def __init__(self) -> None:
        self._sum = soma
        self._subtract = subtract
        self._multiply = multiply
        self._divide = divide
        self._operations = [0, 1, 2, 3]

    def validate_options(self, operation_code: int, num1: int, num2: int) -> bool:
        if operation_code not in self._operations:
            raise ValueError('Operation code must be between 0 and 3')

        if not isinstance(num1, int) or not isinstance(num2, int):
            raise TypeError('Error: Operands must be numbers')

        return True

    def execute_operation(self, operation_code: int, num1: int, num2: int) -> Union[int, float]:    # pylint: disable=inconsistent-return-statements
        is_valid_options = self.validate_options(operation_code, num1, num2)

        if is_valid_options:
            if operation_code == 0:
                return self._sum(num1, num2)
            if operation_code == 1:
                return self._subtract(num1, num2)
            if operation_code == 2:
                return self._multiply(num1, num2)
            if operation_code == 3:
                return self._divide(num1, num2)
