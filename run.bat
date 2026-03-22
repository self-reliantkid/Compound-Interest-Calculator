@echo off
cd /d "%~dp0"

echo Starting Compound Interest Calculator...
echo.

compound_interest.exe

echo.
pause
```

---

## Your Repo Should Look Like This
```
your-repo/
├── .github/
│   └── workflows/
│       └── build.yml
├── compound_interest.py
├── run.command
├── run.sh
├── run.bat
└── README.md
