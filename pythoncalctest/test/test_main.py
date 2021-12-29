import pytest
from unittest.mock import patch, MagicMock
from main import main # pylint: disable=import-error
from src.calculator.calculator import Calculator # pylint: disable=import-error

def test_main():
    with patch.object(Calculator, 'execute_operation', MagicMock()) as mocked_calculator:
        main(0, 1, 1)
        mocked_calculator.assert_called_once_with(0, 1, 1)

def test_main_fail():
    with pytest.raises(TypeError) as ex, \
        patch.object(Calculator, 'validate_options', MagicMock(side_effect=TypeError())):
        main(0, 1, 'a')
    
    assert ex.type is TypeError
