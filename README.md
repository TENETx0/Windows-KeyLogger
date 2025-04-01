# Malware-Developement
Developing malwares and Ransomwares for learning purposes !

**🚨 Disclaimer: This project is intended strictly for educational and ethical cybersecurity research purposes. Unauthorized deployment on devices without explicit consent is illegal and violates privacy laws. Use this tool only in controlled environments like virtual machines or test labs.**

 **📌 About This Project**

This project is a Windows-based keylogger designed for cybersecurity professionals, ethical hackers, and researchers to analyze keylogging behavior, test detection techniques, and enhance security awareness.

**🛠️ Setup & Usage (For Research Purposes Only!)**

🔹 Installation

```
pip install pyHook pythoncom
```

🔹 Run the Keylogger (Ethically)
```
python keylogger.py local
```
🔹 Retrieve Logs

    Check keylogs.txt for recorded keystrokes.

    If using email/FTP, logs will be sent to the configured destination.
    
# Fixing Errors :

**Install Pip, Swig, PyWin32 andd PyHook as Requirements before running the file**

**Pip Installation  :**

1) Ensure pip is Installed
```
python -m ensurepip --default-pip
python -m pip install --upgrade pip
```
2) Add Python and Scripts Folder to PATH
Sometimes, pip is installed but not recognized. Try thi
```
setx PATH "%PATH%;C:\Python312\Scripts\;C:\Python312\"

```
3) Then, restart PowerShell and try running:
```
pip --version 
```
**Install pyWinhook**

1) 🔧 Fix: Install SWIG & Build Tools

1️⃣ Install SWIG

You need to install SWIG manually:

    Download SWIG from the official site:
    🔗 SWIG Download

    Extract it and copy the path of the swig.exe file (e.g., C:\swigwin-4.1.1\swig.exe).

    Add SWIG to your system PATH:

        Open Environment Variables (Win + R → type "sysdm.cpl" → Advanced → Environment Variables).

        Under System Variables, find Path → Edit.

        Click New and add the path to swig.exe (e.g., C:\swigwin-4.1.1\).

        Click OK and Restart your system.

2️⃣ Install Microsoft C++ Build Tools

Since pyWinhook requires C++ compilation, install the necessary tools:

    Download and install Build Tools for Visual Studio:
    🔗 Visual Studio Build Tools

    During installation, check:

        C++ Build Tools

        Windows SDK

        MSVC v142 or v143 (depending on your system)

3️⃣ Verify SWIG Installation

Run the following in PowerShell or CMD:

```
swig -version
```

If SWIG is installed correctly, it should display the version.


4️⃣ Try Installing pyWinhook Again

Once SWIG is installed, retry installing pyWinhook:
```
pip install pyWinhook
```
