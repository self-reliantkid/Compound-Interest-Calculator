#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"
APP="$DIR/compound_interest"

chmod +x "$APP"
"$APP"

echo ""
echo "Press any key to close..."
read -n 1
