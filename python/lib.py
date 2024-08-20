"""
    Contains utility functions
"""
from urllib.parse import urlparse, parse_qs
import importlib


def load_suite(name):
    try:
        module_name = f"suites.{name}"
        module = importlib.import_module(module_name)
        suite = getattr(module, name)
        return suite
    except ModuleNotFoundError:
        return None
    except AttributeError:
        return None


def run_suite(suite_name):
    """
    Run the suite corresponding to the passed name if exists
    If the suite is not found nothing happens
    """
    suite = load_suite(suite_name)
    if suite is None:
        print("Suite not found")
        return
    print(f"About to run suite: {suite_name}")
    for test_case in suite["test_cases"]:
        test_case["fn"]()


def get_reports():
    """
    Returns all the current reports in the database
    """
    print("Getting all the reports")


def get_suite_run_reports(suite_name):
    """
    Returns all the current reports on a specific test suite run
    in the database
    """
    print(f"Getting all reports about suite {suite_name}")


def respond(self, http_status):
    self.send_response(http_status)
    self.send_header("Content-type", "application/json")
    self.end_headers()


def get_query_param(path, param) -> str:
    parsed_path = urlparse(path)
    query_params = parse_qs(parsed_path.query)
    value = query_params.get(param)
    return "" if value is None else value[0]
