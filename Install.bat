# Installer for Microsoft Windows
mkdir C:\Temp
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe" -OutFile "C:\Temp\python-3.7.0.exe"
C:\Temp\python-3.7.0.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
python.exe -m pip install -r .\requirements.txt
