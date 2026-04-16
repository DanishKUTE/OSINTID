import os
import subprocess

print("[*] OSINTID GitHub Auto Setup Starting...")

# Step 1: Create requirements.txt
requirements = """colorama
dnspython
python-whois
requests
psutil
"""

with open("requirements.txt", "w") as f:
    f.write(requirements)

print("[+] requirements.txt created")

# Step 2: Create .gitignore
gitignore = """__pycache__/
*.pyc
osintid_data/
*.db
.env
"""

with open(".gitignore", "w") as f:
    f.write(gitignore)

print("[+] .gitignore created")

# Step 3: Initialize Git
def run(cmd):
    print(f"[*] Running: {cmd}")
    subprocess.call(cmd, shell=True)

run("git init")
run("git add .")
run('git commit -m "Initial commit - OSINTID framework"')

# Step 4: Ask for GitHub repo
repo_url = input("\nEnter your GitHub repo URL (e.g. https://github.com/username/OSINTID.git): ").strip()

# Step 5: Connect and push
run(f"git remote add origin {repo_url}")
run("git branch -M main")
run("git push -u origin main")

print("\n[✅] DONE! Your project is now on GitHub.")