import calculator from '../calculator.js';
import { add, subtract, multiply, divide } from '../operations.js';

jest.mock('../operations.js', () => ({
    add: jest.fn(),
    subtract: jest.fn(),
    multiply: jest.fn(),
    divide: jest.fn(),
}));


describe('[CALCULATOR OBJECT]', () => {
    let num1, num2;

    beforeEach(() => {
        num1 = 1;
        num2 = 2;
    });

    afterEach(() => {
        num1 = 0;
        num2 = 0;
    });
    
    it('should call an add operation with correct params', () => {
        calculator.execute(0, num1, num2);

        expect(add).toHaveBeenCalledWith(num1, num2);
    });

    it('should call an subtract operation with correct params', () => {
        calculator.execute(1, num1, num2);

        expect(subtract).toHaveBeenCalledWith(num1, num2);
    });

    it('should call an multiplication operation with correct params', () => {
        calculator.execute(2, num1, num2);

        expect(multiply).toHaveBeenCalledWith(num1, num2);
    });

    it('should call an divide operation with correct params', () => {
        calculator.execute(3, num1, num2);

        expect(divide).toHaveBeenCalledWith(num1, num2);
    });

    it('should throw error on invalid param', () => {
        num1 = 'a'
        try{
            calculator.execute(0, num1, num2);
        } catch (error) {
            expect(error.toString()).toEqual('Error: Operands must be numbers');
        }
    });

    it('should throw error on invalid option', () => {
        try{
            calculator.execute('a', num1, num2);
        } catch (error) {
            expect(error.toString()).toEqual('Error: Operation code must be between 0 and 3');
        }
    });
});
