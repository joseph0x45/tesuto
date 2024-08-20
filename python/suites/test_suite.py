test_suite = {
    "name": "TestHello",
    "description": "Example test",
    "test_cases": [],
    "active": True
}

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


failing_test = {
    "name": "Failing test",
    "description": "This test fails",
    "fn": None
}


def failing_test_fn():
    print("Hello, I was made to always fail :)")
    return False


failing_test["fn"] = failing_test_fn
test_suite["test_cases"].append(failing_test)
