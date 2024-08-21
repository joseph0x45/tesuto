## Heads up
This work is still in progres, this is just a prototype

# Getting started
Clone the project or just copy the python folder found at the root of the project.

The directory has the following structure:
```
├── lib.py
├── main.py
└── suites
    ├── init.py
    └── test_suite.py
```
The `lib.py` file contains some utilities that tesuto uses to run and save the reports. Don't touch that file unless you know what you are doing

The  `main.py` file contains the server, now again do not touch that file unless you know what you are doing 

You will be writing your test suites in the `suites` directory.

## Test suites
An example implementation should be present when you clone or copy the python folder. Each test suite should be defined in it's own file that should be named after
the test suite. As in the example provider, the `test_suite` is defined inside the `test_suite` file.
```py
# in suites/test_suite.py
test_suite = {
    "name": "TestHello",
    "description": "Example test",
    "test_cases": [],
    "active": True
}
```
Once your suite ready you can now start writing test cases and append them to the test suite. Here is a sample code from the provided example:
```py
passing_test = {
    "name": "Passing test",
    "description": "This test just passes",
    "fn": None
}
def passing_test_fn():
    print("Hello, I was born to pass")
    return True
passing_test["fn"] = passing_test_fn
test_suite["test_cases"].append(passing_test)
```

That's it. After that, you can start running your test suite by sending a GET request to `/run?suite=<your_suite>` and get the report by visiting `/report?suite=<your_suite>`
in a browser.
