# PasswordGenerator
A simple Password Generator written in Python
![Screenshot of the Password Generator in Action](screenshot.png)

## How to run
- Clone Repository `git clone git@github.com:AaronBeier/PasswordGenerator.git`
- Enter Directory `cd PasswordGenerator`
- Create VirtualEnv `python -m venv .`
- Activate VirtualEnv `.\Scripts\Activate.ps1` (Windows)
- Install Requirements `pip install -r requirements.txt`
- Run `python main.py`

## How to package
- Install Requirements `pip install -r installer_requirements.txt`
- Run PyInstaller `pyinstaller --clean --onefile --noconsole --icon=NONE --optimize=2 main.py`

## Known Issues
- Icon does not work when exporting as a singular executable using PyInstaller