#!/bin/bash
# Move to the folder where this script is located
cd "$(dirname "$0")"

echo "------------------------------------------"
echo "   Checking for Updates on GitHub...     "
echo "------------------------------------------"

# This command fetches the latest version tag from your GitHub API
# Replace 'YOUR_USERNAME' and 'YOUR_REPO' with your actual details
LATEST_VERSION=$(curl -s https://api.github.com/repos/self-reliantkid/Compound-Interest-Calculator/releases/latest | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')

echo "Latest Version available: $LATEST_VERSION"
echo "Launching your local app..."
echo "------------------------------------------"

# 1. Clear the "damaged" flag
xattr -cr compound_interest

# 2. Ensure the app has permission
chmod +x compound_interest

# 3. Launch the app
./compound_interest
