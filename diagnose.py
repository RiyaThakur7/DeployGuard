
import sys

def diagnose(error):
    error = error.lower()

    if "connection refused" in error or "failed to connect" in error:
        print("Diagnosis: Application is not reachable.")
        print("Possible fix: Check whether the Docker container is running.")

    elif "port is already allocated" in error or "address already in use" in error:
        print("Diagnosis: Port conflict detected.")
        print("Possible fix: Use another available host port.")

    elif "no such file or directory" in error:
        print("Diagnosis: A required file or path is missing.")
        print("Possible fix: Check file names and project paths.")

    elif "permission denied" in error:
        print("Diagnosis: Permission problem detected.")
        print("Possible fix: Check file permissions and user access.")

    else:
        print("Diagnosis: Unknown error.")
        print("Next step: Review the deployment logs.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        diagnose(" ".join(sys.argv[1:]))
    else:
        print("Usage: python diagnose.py \"error message\"")
