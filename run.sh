#!/bin/bash

# Get the directory where this script lives
DIR="$(cd "$(dirname "$0")" && pwd)"
APP="$DIR/compound_interest"

# Make sure it's executable
chmod +x "$APP"

# Run the app
"$APP"

# Keep Terminal open after exit
echo ""
echo "Press any key to close..."
read -n 1
