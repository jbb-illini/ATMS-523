import subprocess
import sys

def run_git_command(command):
    """
    Runs a git command in the terminal and prints its output.
    """
    try:
        # Use subprocess.run to execute the command.
        # It's better than subprocess.call or os.system for security and output handling.
        result = subprocess.run(command, check=True, text=True, capture_output=True, shell=True)
        print("Standard Output:")
        print(result.stdout)
        
        if result.stderr:
            print("Standard Error:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print("Standard Error:")
        print(e.stderr)

# --- Your Git Workflow ---

# 1. Stage all changes for the next commit
# Equivalent to: git add .
print("--- Staging files ---")
run_git_command("git add .")

# 2. Commit the staged changes
# Equivalent to: git commit -m "Your descriptive commit message here"
# You'll need to change the message to describe your work.
commit_message = "Adds and updates files for Module 1"
print(f"--- Committing with message: '{commit_message}' ---")
run_git_command(f'git commit -m "{commit_message}"')

# 3. Pull remote changes to get your local branch in sync
# Equivalent to: git pull --rebase
print("--- Pulling latest changes from GitHub ---")
run_git_command("git pull --rebase")

# 4. Push local changes to the remote repository
# Equivalent to: git push
print("--- Pushing commits to GitHub ---")
run_git_command("git push")

print("\n--- Git workflow complete ---")