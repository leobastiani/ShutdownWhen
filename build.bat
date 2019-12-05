@ECHO OFF
SETLOCAL EnableDelayedExpansion

pyinstaller -F shutdownWnet.py
pyinstaller -F shutdownWhd.py
pyinstaller -F shutdownWcpu.py



pushd dist
7z a ShutdownWhen.zip shutdownWnet.exe shutdownWhd.exe shutdownWcpu.exe ../shutdownWss/shutdownWss.zip
popd
