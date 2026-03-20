# Compound Interest Calculator

A simple command-line app for calculating compound interest. No installation required — just download and run.

---

## What's Inside

```
compound-interest-mac/
├── compound_interest     ← the app
└── run.command           ← double-click this to launch
```

---

## How to Run

1. **Download** the zip file and unzip it
2. **Keep both files in the same folder** — the `run.command` script needs to find `compound_interest` next to it
3. **Double-click** `run.command`

A Terminal window will open and the app will start automatically.

---

## First Time Only — One Extra Step

Because this app isn't from the Mac App Store, macOS may block `run.command` the very first time you open it.

If you see a popup saying *"run.command can't be opened because it is from an unidentified developer"*:

1. **Right-click** (or Control + click) on `run.command`
2. Select **Open**
3. Click **Open** again in the popup

You only need to do this once. After that, double-clicking works normally.

> The app itself (`compound_interest`) is handled silently in the background — you won't see any popups for it.

---

## Troubleshooting

**Terminal opens and closes immediately**
- Make sure both files are in the same folder and haven't been separated.

**"Permission denied" error**
- Open Terminal, navigate to the folder, and run:
  ```bash
  chmod +x run.command
  chmod +x compound_interest
  ```
  Then try double-clicking `run.command` again.

**Nothing happens when I double-click**
- Right-click `run.command` → Open With → Terminal

---

Made with ❤️ — reach out if you run into any issues!
