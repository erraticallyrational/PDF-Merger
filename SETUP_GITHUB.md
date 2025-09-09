# Setting Up GitHub for PDF Merger Project

## Step 1: Install Git

### Option A: Download Git for Windows
1. Go to https://git-scm.com/download/win
2. Download the latest version for Windows
3. Run the installer with default settings
4. Restart your terminal/PowerShell

### Option B: Install via Chocolatey (if you have it)
```powershell
choco install git
```

### Option C: Install via Winget (Windows 10/11)
```powershell
winget install --id Git.Git -e --source winget
```

## Step 2: Configure Git (First time setup)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Step 3: Initialize Repository and Push to GitHub

### 3.1 Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial commit: PDF Merger Web Application"
```

### 3.2 Create GitHub Repository
1. Go to https://github.com
2. Click the "+" icon in the top right
3. Select "New repository"
4. Name it: `pdf-merger-app` (or your preferred name)
5. Add description: "A simple web application for merging PDF files built with Flask and PyPDF2"
6. Make it Public or Private (your choice)
7. **DO NOT** initialize with README, .gitignore, or license (we already have these)
8. Click "Create repository"

### 3.3 Connect Local Repository to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/pdf-merger-app.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 4: Verify Upload
1. Go to your GitHub repository
2. Verify all files are uploaded correctly
3. Check that the README.md displays properly

## Alternative: Using GitHub Desktop
If you prefer a GUI:
1. Download GitHub Desktop from https://desktop.github.com/
2. Install and sign in with your GitHub account
3. Click "Add an Existing Repository from your Hard Drive"
4. Select this folder: `C:\Users\atlas\OneDrive\Desktop\PDF MERGER`
5. Click "Publish repository" to create it on GitHub

## Project Structure
Your repository will contain:
```
pdf-merger-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web interface
├── .gitignore         # Git ignore rules
├── README.md          # Project documentation
└── SETUP_GITHUB.md    # This setup guide
```

## Next Steps After Upload
1. Add a license file (MIT, Apache, etc.)
2. Create issues for future enhancements
3. Set up GitHub Pages if you want to host the app
4. Add GitHub Actions for CI/CD if needed

## Troubleshooting
- If you get authentication errors, you may need to set up a Personal Access Token
- Make sure your repository name doesn't contain spaces or special characters
- Ensure all files are committed before pushing
