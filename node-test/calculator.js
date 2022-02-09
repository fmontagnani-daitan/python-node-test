import { add, subtract, multiply, divide } from './operations.js';

const OPERATIONS = {
    0: add,
    1: subtract,
    2: multiply,
    3: divide,
};

const _validateOptions = (operationId, num1, num2) => {
    if (!(operationId in OPERATIONS)) {
        throw new Error('Operation code must be between 0 and 3')
    }

    if (isNaN(num1) || isNaN(num2)) {
        throw new Error('Operands must be numbers')
    }
    return OPERATIONS[operationId];
};

const calculator = {
    execute: (operationId, num1, num2) => {
        const operation = _validateOptions(operationId, num1, num2);
        return operation(num1, num2);
    },
};

export default calculator;
