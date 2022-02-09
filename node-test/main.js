import calculator from './calculator.js';

export const main = () => {
    const args = process.argv.slice(2);
    const operationNum = Number(args[0]);
    const num1 = Number(args[1]);
    const num2 = Number(args[2]);

    try {
        const result = calculator.execute(operationNum, num1, num2);
        console.log('Result is: ', result);
    } catch (error) {
        console.log(error.toString());
    }
}

main();
