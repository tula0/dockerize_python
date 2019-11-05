#%%
import falcon
from wsgiref.simple_server import make_server
from wsgiref.validate import validator
import generic_midware
#%%

if(__name__=='__main__'):
    app=generic_midware.simple_app()
    val=generic_midware.validator_app


"""
Executing code failed : Error: Activating Python 3.7.4 64-bit ('py37env': conda) to run Jupyter failed with Error: 
Command failed: C:/ProgramData/Anaconda3/activate && conda activate py37env && echo 'e8b39361-0157-4923-80e1-22d70d46dee6' \
 && python c:/Users/OLWENY/.vscode/extensions/ms-python.python-2019.10.41019/pythonFiles/printEnvVariables.py
'C:/ProgramData/Anaconda3/activate' is not recognized as an internal or external command,
operable program or batch file.
.

"_CONDA_EXE": "C:\\ProgramData\\Anaconda3\\Scripts\\conda.exe"
"_CONDA_ROOT": "C:\\ProgramData\\Anaconda3"
C:\ProgramData\Anaconda3\Scripts\activate
C:\ProgramData\Anaconda3\Scripts\activate.bat


####------Hacks
install:
    jupyter-notebook : not installed
    jupyter lab      : not installed
    ipywidgets       : not installed
"""
dict={"ALLUSERSPROFILE": "C:\\ProgramData", "APPDATA": "C:\\Users\\OLWENY\\AppData\\Roaming", "COMMONPROGRAMFILES": "C:\\Program Files\\Common Files", 
"COMMONPROGRAMFILES(X86)": "C:\\Program Files (x86)\\Common Files", "COMMONPROGRAMW6432": "C:\\Program Files\\Common Files", "COMPUTERNAME": "DESKTOP-6M92GLE", 
"COMSPEC": "C:\\Windows\\system32\\cmd.exe", "DRIVERDATA": "C:\\Windows\\System32\\Drivers\\DriverData", "GOOGLE_DEFAULT_CLIENT_ID": "no", "GOOGLE_DEFAULT_CLIENT_SECRET": "no", "HOMEDRIVE": "C:", "HOMEPATH": "\\Users\\OLWENY", "LOCALAPPDATA": "C:\\Users\\OLWENY\\AppData\\Local", "LOGONSERVER": "\\\\DESKTOP-6M92GLE", "NUMBER_OF_PROCESSORS": "4", "NVM_HOME": "C:\\Users\\OLWENY\\AppData\\Roaming\\nvm", "NVM_SYMLINK": "C:\\Program Files\\nodejs", "ONEDRIVE": 
"C:\\Users\\OLWENY\\OneDrive", "OS": "Windows_NT", "PATH": "C:\\ProgramData\\DockerDesktop\\version-bin;C:\\Program Files\\Docker\\Docker\\Resources\\bin;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files\\Git\\cmd;C:\\Users\\OLWENY\\AppData\\Roaming\\nvm;C:\\Program Files\\nodejs;C:\\Users\\OLWENY\\AppData\\Roaming\\nvm\\v12.10.0;C:\\ProgramData\\Anaconda3\\envs\\py37env\\Scripts;C:\\ProgramData\\Anaconda3\\envs\\py37env;C:\\ProgramData\\Anaconda3;C:\\ProgramData\\Anaconda3\\condabin;C:\\ProgramData\\Anaconda3\\Scripts;C:\\Program Files\\nodejs\\node_modules\\project-copy;C:\\Program Files\\MariaDB 10.1\\bin;C:\\ProgramData\\CPPBuildTools\\bin;C:\\Users\\OLWENY\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\OLWENY\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Users\\OLWENY\\AppData\\Roaming\\nvm;C:\\Program Files\\nodejs", "PATHEXT": ".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC", "PROCESSOR_ARCHITECTURE": "AMD64", "PROCESSOR_IDENTIFIER": "Intel64 Family 6 Model 61 Stepping 4, GenuineIntel", "PROCESSOR_LEVEL": "6", "PROCESSOR_REVISION": "3d04", "PROGRAMDATA": "C:\\ProgramData", "PROGRAMFILES": "C:\\Program Files", "PROGRAMFILES(X86)": "C:\\Program Files (x86)", "PROGRAMW6432": "C:\\Program Files", "PROMPT": "$P$G", "PSMODULEPATH": "C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules", "PUBLIC": "C:\\Users\\Public", "SESSIONNAME": "Console", "SYSTEMDRIVE": "C:", "SYSTEMROOT": "C:\\Windows", "TEMP": "C:\\Users\\OLWENY\\AppData\\Local\\Temp", "TMP": "C:\\Users\\OLWENY\\AppData\\Local\\Temp", "USERDOMAIN": "DESKTOP-6M92GLE", "USERDOMAIN_ROAMINGPROFILE": "DESKTOP-6M92GLE", "USERNAME": "OLWENY", "USERPROFILE": "C:\\Users\\OLWENY", 
"WINDIR": "C:\\Windows", "__COMPAT_LAYER": "DetectorsMessageBoxErrors", "TERM_PROGRAM": "vscode", "TERM_PROGRAM_VERSION": "1.39.2", "LANG": "en_US.UTF-8", "COLORTERM": "truecolor"}


import sys

sys.executable

#Two issues
#1. Why VSCODE python interactive does not use my Select Python Interpreter
#2. My Anaconda3 folder doesn't contain conda and activate file.

