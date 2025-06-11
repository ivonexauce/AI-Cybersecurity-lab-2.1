# audit_with_slither.py
        import subprocess

        def audit(file_path):
            result = subprocess.run(["slither", file_path], capture_output=True, text=True)
            return result.stdout