// const { defaults } = require('jest-config');

module.exports = {
  verbose: true,
  coverageDirectory: './build',
  collectCoverageFrom: [
    '**.js',
  ],
  coverageThreshold: {
    global: {
      branches: 95,
      functions: 95,
      lines: 95,
      statements: 95
    }
  },
  coveragePathIgnorePatterns: [
    '/node_modules/',
    'jest.config.js',
  ],
  coverageReporters: [
    'text',
    'text-summary',
    'html',
    'jest-junit',
  ],
};
