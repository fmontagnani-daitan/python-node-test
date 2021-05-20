from unittest.mock import patch, MagicMock
from main import main # pylint: disable=import-error
from src.calculator.calculator import Calculator # pylint: disable=import-error

def test_main():
    with patch.object(Calculator, 'execute_operation', MagicMock()) as mocked_calculator:
        main(0, 1, 1)
        mocked_calculator.assert_called_once_with(0, 1, 1)

def test_main_fail():
    with patch.object(Calculator, 'validate_numbers', MagicMock(side_effect=Exception)):
        try:
            main(0, 1, 'a')
        except Exception as e:
            assert isinstance(e, Exception)
