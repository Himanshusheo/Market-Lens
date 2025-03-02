"""
Script to push the backdated commit history to GitHub.
This will push commits with their original dates preserved.
"""

import subprocess
import sys
import os

def check_git_status():
    """Check if we're in a git repository and have commits."""
    try:
        # Check if we're in a git repo
        result = subprocess.run(['git', 'rev-parse', '--git-dir'], 
                              capture_output=True, check=True)
        
        # Check if we have commits
        result = subprocess.run(['git', 'log', '--oneline'], 
                              capture_output=True, text=True)
        if not result.stdout.strip():
            print("[ERROR] No commits found! Please run create_commit_history.py first.")
            return False
        
        commits = result.stdout.strip().split('\n')
        print(f"[OK] Found {len(commits)} commits")
        return True
    except subprocess.CalledProcessError:
        print("[ERROR] Not in a git repository!")
        return False
    except Exception as e:
        print(f"[ERROR] {e}")
        return False

def check_remote():
    """Check if remote repository is configured."""
    try:
        result = subprocess.run(['git', 'remote', '-v'], 
                              capture_output=True, text=True, check=True)
        if 'origin' in result.stdout:
            # Extract the remote URL
            for line in result.stdout.split('\n'):
                if 'origin' in line and 'fetch' in line:
                    remote_url = line.split()[1]
                    print(f"[OK] Remote 'origin' found: {remote_url}")
                    return True, remote_url
        print("[WARNING] No 'origin' remote found")
        return False, None
    except Exception as e:
        print(f"[ERROR] {e}")
        return False, None

def push_to_github(force=False):
    """Push commits to GitHub with backdated dates preserved."""
    print("=" * 60)
    print("Push Backdated Commits to GitHub")
    print("=" * 60)
    print()
    
    # Check git status
    if not check_git_status():
        return False
    
    # Check remote
    has_remote, remote_url = check_remote()
    if not has_remote:
        print("\n[INFO] No remote repository configured.")
        print("To add a remote repository, run:")
        print("  git remote add origin https://github.com/USERNAME/REPO.git")
        print("  or")
        print("  git remote add origin git@github.com:USERNAME/REPO.git")
        return False
    
    # Get current branch
    result = subprocess.run(['git', 'branch', '--show-current'], 
                          capture_output=True, text=True)
    current_branch = result.stdout.strip() or 'main'
    
    print(f"\nCurrent branch: {current_branch}")
    print(f"Remote: {remote_url}")
    
    # Show recent commits with dates
    print("\nRecent commits (showing dates):")
    result = subprocess.run(['git', 'log', '--format=%h %ad %s', '--date=short', '-10'], 
                          capture_output=True, text=True)
    print(result.stdout)
    
    # Confirm before pushing
    print("\n" + "=" * 60)
    print("IMPORTANT WARNINGS:")
    print("=" * 60)
    print("1. This will rewrite the remote repository history!")
    print("2. If others are working on this repo, coordinate with them first")
    print("3. The commit dates will be preserved as backdated")
    print("4. You'll need to use --force-with-lease or --force")
    print("=" * 60)
    print()
    
    response = input("Do you want to proceed with pushing? (yes/no): ").strip().lower()
    if response not in ['yes', 'y']:
        print("Cancelled.")
        return False
    
    # Ask about force push
    print("\nChoose push method:")
    print("1. --force-with-lease (safer, recommended)")
    print("2. --force (more aggressive)")
    print("3. Cancel")
    
    choice = input("Enter choice (1/2/3): ").strip()
    
    if choice == '3':
        print("Cancelled.")
        return False
    
    # Build push command
    push_cmd = ['git', 'push']
    if choice == '1':
        push_cmd.append('--force-with-lease')
        print("\n[INFO] Using --force-with-lease (safer option)")
    elif choice == '2':
        push_cmd.append('--force')
        print("\n[WARNING] Using --force (will overwrite remote history)")
    else:
        print("Invalid choice. Cancelled.")
        return False
    
    push_cmd.extend(['origin', current_branch])
    
    print(f"\nPushing to {remote_url}...")
    print(f"Command: {' '.join(push_cmd)}")
    print()
    
    try:
        result = subprocess.run(push_cmd, check=True, capture_output=True, text=True)
        print("[SUCCESS] Commits pushed successfully!")
        print("\nYour backdated commit history is now on GitHub!")
        print(f"View it at: {remote_url.replace('.git', '')}/commits/{current_branch}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Push failed!")
        print(f"Error: {e.stderr}")
        print("\nPossible reasons:")
        print("1. Remote branch has commits you don't have locally")
        print("2. Authentication failed (check your GitHub credentials)")
        print("3. No write access to the repository")
        print("\nTry:")
        print("  - Check your GitHub authentication: git config --list | grep credential")
        print("  - Verify you have push access to the repository")
        return False
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return False

def main():
    """Main function."""
    try:
        success = push_to_github()
        if success:
            print("\n" + "=" * 60)
            print("SUCCESS! Your commits are now on GitHub with backdated dates!")
            print("=" * 60)
        else:
            print("\nPush was not completed.")
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()

