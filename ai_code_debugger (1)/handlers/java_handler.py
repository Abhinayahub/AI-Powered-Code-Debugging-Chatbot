import tempfile
import os
import subprocess

def run_java_code(code):
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "Main.java")
        with open(filepath, "w") as f:
            f.write(code)
        compile_proc = subprocess.run(["javac", filepath], capture_output=True, text=True)
        if compile_proc.returncode != 0:
            return f"❌ Java Compile Error:\n{compile_proc.stderr}"
        run_proc = subprocess.run(["java", "-cp", tmpdir, "Main"], capture_output=True, text=True)
        if run_proc.returncode != 0:
            return f"❌ Java Runtime Error:\n{run_proc.stderr}"
        return "✅ Output:\n" + (run_proc.stdout.strip() or "[No output]")