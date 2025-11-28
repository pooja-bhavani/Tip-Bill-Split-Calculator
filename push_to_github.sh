#!/bin/bash

# Initialize git repository
git init

# Add remote repository
git remote add origin https://github.com/pooja-bhavani/The-Tip-Bill-Split-Calculator-.git

# Add all files
git add .

# Commit with message
git commit -m "Initial commit: Tip & Bill Split Calculator with Flask backend and glassmorphism UI"

# Push to GitHub
git branch -M main
git push -u origin main

echo "✅ Successfully pushed to GitHub!"
