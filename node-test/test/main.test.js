import calculator from '../calculator.js';

process.argv = ['node', 'jest', '0', '1', '3']

import { main } from '../main.js';

jest.mock('../calculator.js', () => ({
    execute: jest.fn(),
}));

describe('[MAIN]', () => {
    it('calls correctly operation', () => {
        main();

        expect(calculator.execute).toHaveBeenCalledWith(0, 1, 3);
    });

    it('correctly handles exception', () => {
        calculator.execute.mockReturnValue(new Error('foo'));
        try {
            main();
        } catch(error) {
            expect(error.toString()).toEquals('foo')
        }
    });
});
