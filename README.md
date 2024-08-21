# Tesutoテスト(from the japanese pronounciation of 'test')
Little template and library for running automated integration tests and get reports as html documents

## Heads up
This is just a prototype, the whole idea is still a work in progress

## Implementations
- [x] [Python](./python.md) 
- [ ] Golang


## How does it work
tesuto is a simple HTTP server with 2 main endpoints:
- /run
- /report

### `GET /run?suite=<suite_name>`
This endpoint is for running a test suite. A test suite is an object with the following structure
```json
{
    "name":"string", //name of the test suite
    "description":"string", //a short description of the suite
    "test_cases": [], //an array containing all the test cases in the suite
    "active":true //whether the suite can be run or not
}
```
Each test case is an object with the following structure
```json
{
    "name":"string", //name of the test case
    "description":"string", //a short description of the test case
    "fn": ()->bool //a function that returns a boolean, the actual test case code
}
```
The test cases must return a boolean that signifies whether they passed or not. An example is provider in each implementation

The `run` endpoint takes in a query parameter named `suite` and it is the name of the test suite you
want to run. An error will be returned if the suite is not found. Please refer to the documentation of the implementation you want to use
for the naming conventions.

### `GET /report?suite=<suite_name>`
This endpoint should be called from a browser. It takes in a query parameter named `suite` and will return the report of the last
run of the corresponding test suite. An error will be returned if the report is not found.
