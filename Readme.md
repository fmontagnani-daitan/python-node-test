Repository for explaining the differences between Unit Tests for Javascript using Jest and Python using Pytest.

**To set up node-test:**
  * on node-test DIR: npm run build

**To set up pythoncalctest:**
  * on root DIR: make build

**REQUIREMENTS**
  * node v12
  * python 3.8

**NODE APP**
Inside node-test dir, run the following scripts:
  * npm run sum -> Adds numbers 1 and 2
  * npm run subtract -> Subtracts number 2 from number 1
  * npm run multiply -> Adds numbers 1 and 2
  * npm run divide -> Adds numbers 1 and 2
  * npm test -> Run test suite with coverage report (node-test/build/index.html)

**PYTHON APP**
On project's root dir, run the following scripts:
  * make run-main -> Executes main.py
  * make coverage test -> Run test suite with coverage report (pythoncalctest/build/reports/index.html)
