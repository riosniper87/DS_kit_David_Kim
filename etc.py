#Anything that used during works, but (might be) helpful :) 
import subprocess

def git_commit_push(repo_path, file_path, commit_message):
    try:
        # Change to the repository directory
        subprocess.run(['git', 'checkout', 'main'], cwd=repo_path)

        # Stage the changes to the specific file
        subprocess.run(['git', 'add', file_path], cwd=repo_path)

        # Commit changes with the given commit message
        subprocess.run(['git', 'commit', '-m', commit_message], cwd=repo_path)

        # Push changes to the main branch
        subprocess.run(['git', 'push', 'origin', 'main'], cwd=repo_path)

        print("Changes committed and pushed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
