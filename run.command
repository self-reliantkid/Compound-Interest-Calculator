#!/bin/bash
# Move to the folder where this script is located
cd "$(dirname "$0")"

# --- SET YOUR CURRENT VERSION HERE ---
CURRENT_VERSION="v1.2" 

clear
echo "=========================================="
echo "    Interest Calculator: $CURRENT_VERSION"
echo "=========================================="

# Fetch the latest version tag from GitHub
# Replace YOUR_USERNAME and YOUR_REPO below!
LATEST=$(curl -s https://api.github.com/repos/self-reliantkid/Compound-Interest-Calculator/releases/latest | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')

if [ -z "$LATEST" ]; then
    echo "[!] Could not check for updates (Offline)."
elif [ "$LATEST" != "$CURRENT_VERSION" ]; then
    echo "[UPDATE AVAILABLE]"
    echo "Current: $CURRENT_VERSION"
    echo "Latest:  $LATEST"
    echo "------------------------------------------"
    echo "Opening download page..."
    # This opens the Mac's browser to your releases page
    open "https://github.com/YOUR_USERNAME/YOUR_REPO/releases/latest"
    echo "------------------------------------------"
    sleep 2
else
    echo "[✓] You are running the latest version."
fi

echo "Launching app..."

# The "Magic Fix" for the 'Damaged' error
xattr -cr compound_interest
chmod +x compound_interest
./compound_interest
