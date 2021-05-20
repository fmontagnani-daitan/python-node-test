export const add = (num1, num2) => num1 + num2;

export const subtract = (num1, num2) => num1 - num2;

export const multiply = (num1, num2) => num1 * num2;

export const divide = (num1, num2) => {
    if (num2 === 0) {
        throw new Error('Denominator must not be 0!');
    }
    return num1 / num2;
};
