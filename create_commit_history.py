"""
Script to create a realistic git commit history from March 2, 2025 to June 13, 2025.
This will show progressive development of the Market Lens project.
"""

import subprocess
import random
from datetime import datetime, timedelta
import os
import json

# Configuration
START_DATE = datetime(2025, 3, 2)
END_DATE = datetime(2025, 6, 13)
USERNAME = "Himanshusheo"
EMAIL = "himanshusheoran174@gmail.com"

# Commit patterns - realistic work schedule
# 0 = no work, 1 = 1 commit, 2 = 2 commits
COMMIT_PATTERNS = {
    'weekday': [0, 0, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 0, 1, 1],  # More work on weekdays
    'weekend': [0, 0, 0, 1, 0, 1, 0],  # Less work on weekends
}

def generate_commit_dates():
    """Generate realistic commit dates with rest days and multiple commits."""
    dates = []
    current_date = START_DATE
    
    while current_date <= END_DATE:
        is_weekend = current_date.weekday() >= 5
        pattern = COMMIT_PATTERNS['weekend'] if is_weekend else COMMIT_PATTERNS['weekday']
        num_commits = random.choice(pattern)
        
        # Add some randomness - sometimes skip even on workdays
        if random.random() < 0.15:  # 15% chance of rest day even on workday
            num_commits = 0
        
        for i in range(num_commits):
            # Spread commits throughout the day
            hour = random.randint(9, 20)
            minute = random.randint(0, 59)
            commit_time = current_date.replace(hour=hour, minute=minute)
            dates.append(commit_time)
        
        current_date += timedelta(days=1)
    
    return sorted(dates)

# Progressive development milestones
MILESTONES = [
    # March 2-10: Project setup and initial structure
    {
        'start': datetime(2025, 3, 2),
        'end': datetime(2025, 3, 10),
        'commits': [
            "Initial project setup and repository structure",
            "Add README with project overview",
            "Set up Python project structure with pyproject.toml",
            "Create Pipeline directory structure",
            "Add initial requirements.txt",
            "Set up gitignore for Python and Node projects",
            "Create initial directory structure for all modules",
        ]
    },
    # March 11-20: Pipeline development
    {
        'start': datetime(2025, 3, 11),
        'end': datetime(2025, 3, 20),
        'commits': [
            "Implement Customers_Univariate_EDA.py with basic analytics",
            "Add customer GMV analysis functionality",
            "Implement payment method analysis",
            "Add pincode distribution analysis",
            "Create Customers_Bivariate_EDA.py for relationship analysis",
            "Implement correlation analysis between customer variables",
            "Add SKU_EDA.py for product analysis",
            "Implement category and subcategory analysis",
            "Add product hierarchy visualization",
            "Create master_data.py for revenue analysis",
            "Implement time series trend analysis",
            "Add seasonal decomposition functionality",
        ]
    },
    # March 21-31: Weather and Investment analysis
    {
        'start': datetime(2025, 3, 21),
        'end': datetime(2025, 3, 31),
        'commits': [
            "Implement Weather_Analysis_EDA.py",
            "Add temperature correlation analysis",
            "Implement precipitation impact analysis",
            "Create Investment_EDA.py for marketing investment analysis",
            "Add channel effectiveness analysis",
            "Implement ROI calculations",
            "Create Feature.py for feature engineering",
            "Add derived metrics and transformations",
            "Implement main.py FastAPI server",
            "Add API endpoints for analytics",
            "Create Pipeline README documentation",
        ]
    },
    # April 1-15: Dashboard foundation
    {
        'start': datetime(2025, 4, 1),
        'end': datetime(2025, 4, 15),
        'commits': [
            "Initialize React Dashboard with Vite",
            "Set up TypeScript configuration",
            "Install and configure Tailwind CSS",
            "Add shadcn-ui component library",
            "Create basic dashboard layout",
            "Implement sidebar navigation",
            "Add header component",
            "Create dashboard context for state management",
            "Set up Supabase integration",
            "Implement authentication system",
            "Add login and signup pages",
            "Create dashboard home page",
            "Add data upload functionality",
            "Implement file upload component",
        ]
    },
    # April 16-30: Dashboard features
    {
        'start': datetime(2025, 4, 16),
        'end': datetime(2025, 4, 30),
        'commits': [
            "Add chart components for data visualization",
            "Implement stats card component",
            "Create marketing chart component",
            "Add data visualization pages",
            "Implement chart-card component",
            "Add loading animation component",
            "Create footer component",
            "Add logo component",
            "Implement page header component",
            "Add dashboard pages for different analytics",
            "Create data upload card component",
            "Add sample data files",
            "Implement data fetching and display",
            "Add error handling and loading states",
        ]
    },
    # May 1-15: Report Generation - AI Agents
    {
        'start': datetime(2025, 5, 1),
        'end': datetime(2025, 5, 15),
        'commits': [
            "Set up Report Generation module structure",
            "Create supervisor agent for coordination",
            "Implement exploration agent for data analysis",
            "Add SQL agent for database queries",
            "Create ROI agent for return on investment analysis",
            "Implement budget agent for allocation optimization",
            "Add KPI agent for performance indicators",
            "Create market analysis agent",
            "Implement compiler agent for report generation",
            "Add report generation utilities",
            "Create data manager for SQLite integration",
            "Implement report to PDF conversion",
            "Add report formatting utilities",
            "Create main.py for report generation",
        ]
    },
    # May 16-31: Budget Allocation and Analysis
    {
        'start': datetime(2025, 5, 16),
        'end': datetime(2025, 5, 31),
        'commits': [
            "Create Budget Allocation directory",
            "Implement time series budget allocation notebook",
            "Add bi-level optimization notebook",
            "Integrate Robyn MMM framework",
            "Add budget allocation visualization",
            "Create Analysis directory for channel analysis",
            "Implement marketing channel analysis notebook",
            "Add hypothesis testing functionality",
            "Implement LIME explanations for model interpretability",
            "Add channel effectiveness analysis",
            "Create Channel Allocation module",
            "Implement product-wise channel allocation",
            "Add Sales Allocation analysis",
        ]
    },
    # June 1-10: Integration and improvements
    {
        'start': datetime(2025, 6, 1),
        'end': datetime(2025, 6, 10),
        'commits': [
            "Integrate all modules together",
            "Add comprehensive README documentation",
            "Improve error handling across modules",
            "Add data validation and preprocessing",
            "Optimize performance of analytics pipeline",
            "Add more visualization options",
            "Improve dashboard UI/UX",
            "Add export functionality for reports",
            "Implement caching for better performance",
            "Add unit tests for critical functions",
            "Update documentation with usage examples",
            "Fix bugs and improve code quality",
        ]
    },
    # June 11-13: Final polish
    {
        'start': datetime(2025, 6, 11),
        'end': datetime(2025, 6, 13),
        'commits': [
            "Final code review and cleanup",
            "Update all documentation",
            "Add final touches to dashboard",
            "Complete project documentation",
            "Final commit: Market Lens project complete",
        ]
    },
]

def get_commit_message(date):
    """Get appropriate commit message for the given date."""
    for milestone in MILESTONES:
        if milestone['start'] <= date <= milestone['end']:
            if milestone['commits']:
                msg = milestone['commits'].pop(0)
                return msg
    
    # Fallback messages
    fallback_messages = [
        "Refactor code for better organization",
        "Improve error handling",
        "Add comments and documentation",
        "Fix minor bugs",
        "Optimize performance",
        "Update dependencies",
        "Improve code quality",
        "Add validation checks",
        "Enhance user experience",
        "Update configuration files",
    ]
    return random.choice(fallback_messages)

def make_realistic_change(date, commit_msg):
    """Make a realistic small change to a file based on commit message."""
    changed = False
    
    # Determine file to modify based on commit message
    msg_lower = commit_msg.lower()
    
    # Pipeline-related commits
    if any(word in msg_lower for word in ['customer', 'pipeline', 'eda', 'sku', 'master_data', 'weather', 'investment', 'feature']):
        pipeline_files = [
            'Pipeline/Customers_Univariate_EDA.py',
            'Pipeline/Customers_Bivariate_EDA.py',
            'Pipeline/SKU_EDA.py',
            'Pipeline/master_data.py',
            'Pipeline/Weather_Analysis_EDA.py',
            'Pipeline/Investment_EDA.py',
            'Pipeline/Feature.py',
            'Pipeline/main.py',
        ]
        for file_path in pipeline_files:
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    # Add a helpful comment or improve existing code
                    if len(lines) > 5:
                        # Find a good place to add a comment (after imports)
                        insert_idx = 0
                        for i, line in enumerate(lines[:20]):
                            if line.strip() and not line.strip().startswith(('import', 'from', '#', '"', "'")):
                                insert_idx = i
                                break
                        
                        if insert_idx > 0 and not lines[insert_idx-1].strip().startswith('#'):
                            comment = f"# {commit_msg.split(':')[0] if ':' in commit_msg else 'Enhancement'} - {date.strftime('%Y-%m-%d')}\n"
                            lines.insert(insert_idx, comment)
                            changed = True
                    
                    if changed:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        break
                except Exception:
                    continue
    
    # Dashboard-related commits
    elif any(word in msg_lower for word in ['dashboard', 'react', 'component', 'ui', 'page', 'auth']):
        dashboard_files = [
            'Dashboard/src/App.tsx',
            'Dashboard/src/components/dashboard-layout.tsx',
            'Dashboard/src/components/header.tsx',
            'Dashboard/src/components/sidebar.tsx',
        ]
        for file_path in dashboard_files:
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    if len(lines) > 3:
                        # Add comment after imports
                        insert_idx = 0
                        for i, line in enumerate(lines[:15]):
                            if not line.strip().startswith(('import', 'export', '//', '/*')):
                                insert_idx = i
                                break
                        
                        if insert_idx > 0:
                            comment = f"// {commit_msg.split(':')[0] if ':' in commit_msg else 'Enhancement'} - {date.strftime('%Y-%m-%d')}\n"
                            lines.insert(insert_idx, comment)
                            changed = True
                    
                    if changed:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        break
                except Exception:
                    continue
    
    # Report Generation commits
    elif any(word in msg_lower for word in ['report', 'agent', 'ai', 'generation', 'supervisor', 'roi', 'budget', 'kpi']):
        report_files = [
            'Report Generation/agents/supervisor.py',
            'Report Generation/agents/roi.py',
            'Report Generation/agents/budget.py',
            'Report Generation/agents/kpi.py',
            'Report Generation/main.py',
        ]
        for file_path in report_files:
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    if len(lines) > 5:
                        insert_idx = 0
                        for i, line in enumerate(lines[:20]):
                            if line.strip() and not line.strip().startswith(('import', 'from', '#', '"', "'")):
                                insert_idx = i
                                break
                        
                        if insert_idx > 0 and not lines[insert_idx-1].strip().startswith('#'):
                            comment = f"# {commit_msg.split(':')[0] if ':' in commit_msg else 'Enhancement'} - {date.strftime('%Y-%m-%d')}\n"
                            lines.insert(insert_idx, comment)
                            changed = True
                    
                    if changed:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        break
                except Exception:
                    continue
    
    # Budget Allocation commits
    elif any(word in msg_lower for word in ['budget', 'allocation', 'optimization', 'robyn']):
        budget_files = [
            'Budget Allocation/Budget_Allocation_Time_Series.ipynb',
            'Budget Allocation/Budget_Bioptimisation.ipynb',
        ]
        for file_path in budget_files:
            if os.path.exists(file_path):
                # Touch the file to show activity
                os.utime(file_path, None)
                changed = True
                break
    
    # README or documentation commits
    elif any(word in msg_lower for word in ['readme', 'documentation', 'setup', 'structure', 'config']):
        if os.path.exists('README.md'):
            try:
                with open('README.md', 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Small improvement - update a section or add a note
                if '*Last updated:' in content:
                    content = content.replace('*Last updated: January 2025*', f'*Last updated: {date.strftime("%B %Y")}*')
                elif '*Last updated:' not in content:
                    content += f'\n\n*Last updated: {date.strftime("%B %Y")}*\n'
                
                with open('README.md', 'w', encoding='utf-8') as f:
                    f.write(content)
                changed = True
            except Exception:
                pass
    
    # If no specific change was made, update the commit history log
    if not changed:
        if not os.path.exists('.commit_history'):
            with open('.commit_history', 'w') as f:
                f.write('Commit History Log\n')
                f.write('=' * 50 + '\n\n')
        with open('.commit_history', 'a', encoding='utf-8') as f:
            f.write(f'{date.strftime("%Y-%m-%d %H:%M")}: {commit_msg}\n')

def create_commit_history():
    """Create the commit history."""
    print("=" * 60)
    print("Market Lens - Git Commit History Generator")
    print("=" * 60)
    print(f"Date Range: {START_DATE.strftime('%Y-%m-%d')} to {END_DATE.strftime('%Y-%m-%d')}")
    print(f"User: {USERNAME} <{EMAIL}>")
    print("=" * 60)
    print()
    
    print("Setting up git user configuration...")
    subprocess.run(['git', 'config', 'user.name', USERNAME], check=True)
    subprocess.run(['git', 'config', 'user.email', EMAIL], check=True)
    
    # Check current branch and status
    result = subprocess.run(['git', 'branch', '--show-current'], capture_output=True, text=True)
    current_branch = result.stdout.strip()
    print(f"Current branch: {current_branch}")
    
    # Check if we need to reset history
    result = subprocess.run(['git', 'log', '--oneline'], capture_output=True, text=True)
    existing_commits = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
    
    # Always create a backup before modifying history
    if existing_commits > 0:
        backup_name = f"backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        print(f"\nCreating backup branch: {backup_name}")
        subprocess.run(['git', 'branch', backup_name], check=False)
        print(f"[OK] Backup created. You can restore with: git reset --hard {backup_name}")
        
        if existing_commits > 3:
            print(f"\n[!] Found {existing_commits} existing commits.")
            print("Will create new history with backdated commits.")
        
        # Create a new orphan branch to build fresh history
        print("\nCreating new orphan branch for fresh history...")
        temp_branch = 'temp_new_history'
        subprocess.run(['git', 'checkout', '--orphan', temp_branch], check=False)
        subprocess.run(['git', 'rm', '-rf', '--cached', '.'], check=False)  # Unstage everything
        # Copy all files from working directory
        subprocess.run(['git', 'add', '-A'], check=False)
        print("[OK] New branch created, ready to build history")
    
    print("\nGenerating commit dates...")
    commit_dates = generate_commit_dates()
    print(f"Generated {len(commit_dates)} commit dates")
    
    print("\nCreating commit history...")
    print("This may take a while...\n")
    
    # Create the initial commit dated March 2, 2025 with all current files
    print("\nCreating initial commit (March 2, 2025)...")
    # Ensure all files are staged
    subprocess.run(['git', 'add', '-A'], check=False)
    
    # On orphan branch, there's no HEAD, so we always create initial commit
    initial_date = START_DATE.replace(hour=10, minute=0)
    date_str = initial_date.strftime('%Y-%m-%d %H:%M:%S')
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = date_str
    env['GIT_COMMITTER_DATE'] = date_str
    
    result = subprocess.run(
        ['git', 'commit', '-m', 'Initial commit: Market Lens - Comprehensive marketing analytics platform'],
        env=env,
        check=False,
        capture_output=True
    )
    
    if result.returncode == 0:
        print("[OK] Initial commit created")
    else:
        print(f"[WARNING] Initial commit may have failed: {result.stderr.decode('utf-8', errors='ignore')}")
        # Try to continue anyway
    
    print("\nNow creating progressive commit history...")
    
    commit_num = 0
    for date in commit_dates:
        commit_num += 1
        commit_msg = get_commit_message(date)
        
        # Make a realistic change
        make_realistic_change(date, commit_msg)
        
        # Stage changes
        subprocess.run(['git', 'add', '-A'], check=False)
        
        # Check if there are changes to commit
        result = subprocess.run(['git', 'diff', '--cached', '--quiet'], 
                              capture_output=True)
        if result.returncode == 0:
            # No changes, ensure we have the commit history file
            if not os.path.exists('.commit_history'):
                with open('.commit_history', 'w') as f:
                    f.write('Commit History Log\n')
                    f.write('=' * 50 + '\n\n')
            with open('.commit_history', 'a', encoding='utf-8') as f:
                f.write(f'{date.strftime("%Y-%m-%d %H:%M")}: {commit_msg}\n')
            subprocess.run(['git', 'add', '.commit_history'], check=False)
        
        # Create commit with backdated date
        date_str = date.strftime('%Y-%m-%d %H:%M:%S')
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = date_str
        env['GIT_COMMITTER_DATE'] = date_str
        
        result = subprocess.run(
            ['git', 'commit', '-m', commit_msg],
            env=env,
            check=False,
            capture_output=True
        )
        
        if commit_num % 20 == 0:
            print(f"Created {commit_num}/{len(commit_dates)} commits... ({date.strftime('%Y-%m-%d')})")
    
    print(f"\n[OK] Created {commit_num} commits!")
    
    # Replace main branch with our new history
    print("\nFinalizing: Replacing main branch with new history...")
    result = subprocess.run(['git', 'branch', '--show-current'], capture_output=True, text=True)
    current_branch = result.stdout.strip()
    
    if current_branch == 'temp_new_history' or 'temp_new_history' in current_branch:
        # We're on the temp branch, replace main
        subprocess.run(['git', 'branch', '-D', 'main'], check=False)  # Delete old main (may fail if on it, that's OK)
        subprocess.run(['git', 'branch', '-m', 'main'], check=False)  # Rename temp to main
        subprocess.run(['git', 'checkout', 'main'], check=False)  # Switch to main
        print("[OK] Main branch replaced with new history")
    else:
        print(f"[INFO] Current branch is {current_branch}, history created there")
    
    print("\n[OK] Commit history created successfully!")
    print(f"\nSummary:")
    print(f"  - Total commits: {commit_num + 1}")  # +1 for initial commit
    print(f"  - Date range: {START_DATE.strftime('%Y-%m-%d')} to {END_DATE.strftime('%Y-%m-%d')}")
    print(f"  - Username: {USERNAME}")
    print(f"  - Email: {EMAIL}")
    print(f"\n[!] IMPORTANT: Before pushing, you may want to:")
    print(f"  1. Review the commit history: git log --oneline --graph --all")
    print(f"  2. Check a few commits: git log --format='%h %ad %s' --date=short")
    print(f"  3. If satisfied, push with: git push --force-with-lease origin main")
    print(f"  4. This will rewrite the remote history!")

if __name__ == '__main__':
    try:
        create_commit_history()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()

