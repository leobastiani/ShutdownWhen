py -3 -m py2exe.build_exe shutdownWnet.py -c -b 0 -O
py -3 -m py2exe.build_exe shutdownWhd.py  -c -b 0 -O
py -3 -m py2exe.build_exe shutdownWcpu.py -c -b 0 -O



cd dist
7z a ShutdownWhen.zip shutdownWnet.exe shutdownWhd.exe shutdownWcpu.exe ../shutdownWss/shutdownWss.zip