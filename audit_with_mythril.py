 # audit_with_mythril.py
        import subprocess

        def audit(file_path):
            result = subprocess.run(["myth", "analyze", file_path], capture_output=True, text=True)
            return result.stdout