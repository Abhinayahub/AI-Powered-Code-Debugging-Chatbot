import tempfile
import os
import subprocess

def run_cpp_code(code):
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "program.cpp")
        exepath = os.path.join(tmpdir, "program")
        with open(filepath, "w") as f:
            f.write(code)
        compile_proc = subprocess.run(["g++", filepath, "-o", exepath], capture_output=True, text=True)
        if compile_proc.returncode != 0:
            return f"❌ C++ Compile Error:\n{compile_proc.stderr}"
        run_proc = subprocess.run([exepath], capture_output=True, text=True)
        if run_proc.returncode != 0:
            return f"❌ C++ Runtime Error:\n{run_proc.stderr}"
        return "✅ Output:\n" + (run_proc.stdout.strip() or "[No output]")