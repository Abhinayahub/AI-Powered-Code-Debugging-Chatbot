import subprocess
import tempfile
import os

def run_javascript_code(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".js", mode='w') as tmpfile:
        tmpfile.write(code)
        filepath = tmpfile.name
    run_proc = subprocess.run(["node", filepath], capture_output=True, text=True)
    os.unlink(filepath)
    if run_proc.returncode != 0:
        return f"❌ JavaScript Error:\n{run_proc.stderr}"
    return "✅ Output:\n" + (run_proc.stdout.strip() or "[No output]")