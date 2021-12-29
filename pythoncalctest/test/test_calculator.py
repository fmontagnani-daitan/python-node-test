import pytest
from unittest import TestCase
from unittest.mock import patch, call, MagicMock
from src.calculator.calculator import Calculator

class TestCalculator(TestCase):
    calculator = None   #useless: just to demonstrate

    def setUp(self):
        if self.calculator is None: #useless: just to demonstrate
            self.calculator = Calculator()

        self.num1 = 1
        self.num2 = 2

    def test_validate_options_operand_error(self):
        try:
            self.calculator.validate_options(0, 'a', 2)
        except Exception as e:
            assert isinstance(e, TypeError)
            assert str(e) == 'Error: Operands must be numbers'

    def test_validate_options_option_error(self):
        try:
            self.calculator.validate_options(5, 1, 2)
        except Exception as e:
            assert isinstance(e, ValueError)
            assert str(e) == 'Operation code must be between 0 and 3'

    def test_calculator_soma(self):
        with patch('src.calculator.calculator.soma', MagicMock()) as mocked_operation:
            # it will fail since self.calculator was instantiated outside scope
            # self.calculator.execute_operation(0, self.num1, self.num2)
            calculator = Calculator()
            calculator.execute_operation(0, self.num1, self.num2)
            
            assert mocked_operation.mock_calls == [call(1, 2)]
    
    def test_calculator_subtract(self):
        with patch('src.calculator.calculator.subtract', MagicMock()) as mocked_operation:
            calculator = Calculator()
            calculator.execute_operation(1, self.num1, self.num2)
            
            assert mocked_operation.mock_calls == [call(1, 2)]

    def test_calculator_multiply(self):
        with patch('src.calculator.calculator.multiply', MagicMock()) as mocked_operation:
            calculator = Calculator()
            calculator.execute_operation(2, self.num1, self.num2)
            
            assert mocked_operation.mock_calls == [call(1, 2)]
    
    def test_calculator_divide(self):
        with patch('src.calculator.calculator.divide', MagicMock()) as mocked_operation:
            calculator = Calculator()
            calculator.execute_operation(3, self.num1, self.num2)
            
            assert mocked_operation.mock_calls == [call(1, 2)]

    def tearDown(self):
        self.num1 = 0
        self.num2 = 0
