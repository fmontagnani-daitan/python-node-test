import { add, subtract, multiply, divide } from '../operations.js';

describe('[OPERATIONS MODULE]', () => {
    let num1, num2;

    beforeEach(() => {
        num1 = 1;
        num2 = 2;
    });

    afterEach(() => {
        num1 = 0;
        num2 = 0;
    });

    it('[ADD] - Correctly sums num1 and num2', () => {
        const expected = 3;

        const result = add(num1, num2);

        expect(result).toEqual(expected);
    });

    it('[SUBTRACT] - Correctly subtracts num2 from num1', () => {
        const expected = -1;

        const result = subtract(num1, num2);

        expect(result).toEqual(expected);
    });

    it('[MULTIPLY] - Correctly multiply num1 and num2', () => {
        const expected = 2;

        const result = multiply(num1, num2);

        expect(result).toEqual(expected);
    });
    
    it('[DIVIDE] - Correctly divides num1 by num2', () => {
        const expected = 0.5;

        const result = divide(num1, num2);

        expect(result).toEqual(expected);
    });

    it('[DIVIDE] - Correctly throw error on division by zero', () => {
        num2 = 0;
        const expectedError = new Error('Denominator must not be 0!');
        try {
            divide(num1, num2);
        } catch(error) {
            expect(error).toEqual(expectedError);
        }
    });
});

