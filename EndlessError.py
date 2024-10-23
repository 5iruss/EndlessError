import tkinter as tk
import time
import random
import threading
import win32file
import win32api

stop_flag = False
popups = []
error_messages = [("TechSino", "#00FF00"), ("Unreal.VC", "red")]

def show_multiple_errors():
    global stop_flag
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    counter = 0

    while not stop_flag:
        for _ in range(10):
            x_position = random.randint(0, screen_width - 200)
            y_position = random.randint(0, screen_height - 100)
            error_message, text_color = error_messages[counter % 2]
            counter += 1
            
            popup = tk.Toplevel(root)
            popup.geometry(f"200x100+{x_position}+{y_position}")
            popup.config(bg="black")
            popups.append(popup)
            
            neon_bg = "black"
            if error_message == "TechSino":
                shadow_label = tk.Label(popup, text=error_message, fg="#39FF14", bg=neon_bg, font=("Arial", 14, "bold"))
            else:
                shadow_label = tk.Label(popup, text=error_message, fg="#FF2B2B", bg=neon_bg, font=("Arial", 14, "bold"))
            
            shadow_label.place(x=2, y=2)
            label = tk.Label(popup, text=error_message, fg=text_color, bg=neon_bg, font=("Arial", 14, "bold"))
            label.pack(expand=True, fill='both')
        
        time.sleep(0.1)

def stop_loop():
    global stop_flag
    stop_flag = True
    for popup in popups:
        popup.destroy()
    popups.clear()

def detect_usb():
    while True:
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        for drive in drives:
            if win32file.GetDriveType(drive) == win32file.DRIVE_REMOVABLE:
                threading.Thread(target=show_multiple_errors).start()
                time.sleep(20)
                stop_loop()
                return

root = tk.Tk()
root.withdraw()
threading.Thread(target=detect_usb).start()
root.mainloop()
