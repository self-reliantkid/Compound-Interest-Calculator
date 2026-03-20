#!/bin/bash
# Get the folder where this script is sitting
DIR=$(dirname "$0")

# Clear the "damaged" attribute from the app in the same folder
xattr -cr "$DIR/compound_interest"

# Give the app permission to run (just in case)
chmod +x "$DIR/compound_interest"

# Launch the app
"$DIR/compound_interest"

# Close the terminal window when the app is closed
exit
