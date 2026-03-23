import ast
import sys
import io
from unittest.mock import patch

def run_python_code(code, raw_inputs):
    try:
        ast.parse(code)
    except SyntaxError as e:
        return f"❌ Python Syntax Error: {e.msg} at line {e.lineno}"

    inputs = raw_inputs.strip().split('\n')
    input_iter = iter(inputs)

    def mock_input(prompt=''):
        try:
            return next(input_iter)
        except StopIteration:
            raise Exception("⚠ Not enough inputs provided.")

    old_stdout = sys.stdout
    redirected_output = io.StringIO()
    sys.stdout = redirected_output

    try:
        with patch('builtins.input', mock_input):
            exec(code, {})
    except Exception as e:
        sys.stdout = old_stdout
        return f"❌ Python Runtime Error: {e}"

    sys.stdout = old_stdout
    return "✅ Output:\n" + (redirected_output.getvalue().strip() or "[No output]")