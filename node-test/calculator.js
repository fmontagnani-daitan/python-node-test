import { add, subtract, multiply, divide } from './operations.js';

const _validateNumbers = (num1, num2) => {
    if (isNaN(num1) || isNaN(num2)) {
        throw new Error('Operands must be numbers')
    }
};

const _executeOperation = (operation, num1, num2) => {
    _validateNumbers(num1, num2);
    return operation(num1, num2);
};

const calculator = {
    0: (num1, num2) => _executeOperation(add, num1, num2),
    1: (num1, num2) => _executeOperation(subtract, num1, num2),
    2: (num1, num2) => _executeOperation(multiply, num1, num2),
    3: (num1, num2) => _executeOperation(divide, num1, num2),
};

export default calculator;
