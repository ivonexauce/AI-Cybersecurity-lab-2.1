import subprocess
import sys

def audit(file_path):
    try:
        result = subprocess.run(
            ["myth", "analyze", file_path],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0 and result.stderr:
            return f"Error: {result.stderr.strip()}"
        return result.stdout or "No issues found."
    except FileNotFoundError:
        return "Error: 'myth' not found. Install mythril."
    except subprocess.TimeoutExpired:
        return "Error: Audit timed out."
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python audit_with_mythril.py <contract.sol>")
        sys.exit(1)
    print(audit(sys.argv[1]))
