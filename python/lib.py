"""
    Contains utility functions
"""
from urllib.parse import urlparse, parse_qs
import importlib

report_template_upper = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Centered Table with Status Colors</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        table {
            border-collapse: collapse;
            width: 50%;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
        .status {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            display: inline-block;
        }
        .passed {
            background-color: green;
        }
        .failed {
            background-color: red;
        }
    </style>
</head>
<body>
    <table>
        <tr>
            <th>Name</th>
            <th>Status</th>
        </tr>
"""

report_template_lower = """
  </table>
</body>

</html>
"""


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


def generate_html_report(results) -> str:
    report_table = ""
    for k, v in results.items():
        report_table = f"""
            {report_table}
            <tr>
                <td>{k}</td>
                <td><span class="status {'passed' if v else 'failed'}"></span></td>
            </tr>
        """
    full_report = f"{report_template_upper}{report_table}{report_template_lower}"
    return full_report


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
    results = {}
    for test_case in suite["test_cases"]:
        result: bool = test_case["fn"]()
        results[test_case["name"]] = result
    report = generate_html_report(results)
    with open(f"{suite_name}.html", "w") as file:
        file.write(report)


def get_suite_run_reports(suite_name) -> str:
    """
    Returns the latest report for the specified test suite
    """
    print(f"Getting all reports about suite {suite_name}")
    try:
        with open(f"{suite_name}.html", 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"<h1>No report found for test suite '{suite_name}'</h1>"
    except Exception as e:
        return f"<h1>Error while reading report: {str(e)}</h1>"


def respond(self, http_status):
    self.send_response(http_status)
    self.send_header("Content-type", "application/json")
    self.end_headers()


def get_query_param(path, param) -> str:
    parsed_path = urlparse(path)
    query_params = parse_qs(parsed_path.query)
    value = query_params.get(param)
    return "" if value is None else value[0]
