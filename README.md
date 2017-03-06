# py36_test
Testing PyInstaller with Python 3.6 on Windows 10. Tested with PyInstaller develop branch (PyInstaller 3.3.dev): https://github.com/pyinstaller/pyinstaller/commit/98e4482ac3a72bcce9e41aef90bc9392129d6b59

## Steps to reproduce
On a Windows development machine:
- Download and install Windows 10 SDK ([download here](https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk))
- Add `C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64` to [system Path](http://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10)
- From a Windows Python 3.6 virtualenv with PyInstaller develop branch installed, run: `pyinstaller test.spec`.
- Test the executable works: `dist\test\test`:

`INFO:py36_test.hello:Hello World`

On a Windows testing machine with a fresh Windows 10 installation:
- Run: `dist\test\test`:

`Error loading Python DLL: X:\.local\src\py36_test\dist\test\python36.dll (error code 126)`


## Notes
- Rebuilding with Python 3.5 and PyInstaller 3.2 on the development machine, the testing machine fails with the same error (except python35.dll is referenced). 
- Rebuilding with Python 3.5 and PyInstaller 3.2 on the development machine, the testing machine succeeds, logging 'Hello World' to stdout.
- `cl` output is:
`Microsoft (R) C/C++ Optimizing Compiler Version 19.00.24210 for x64`
- Not reproducible in a *nix environment.
