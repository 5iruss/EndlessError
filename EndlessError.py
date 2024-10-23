import tkinter as tk
import time
import random
import threading

stop_flag = False
error_messages = [("TechSino", "#00FF00"), ("Unreal.VC", "red")]

def show_multiple_errors():
    global stop_flag
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    counter = 0

    while not stop_flag:
        for _ in range(5):
            x_position = random.randint(0, screen_width - 200)
            y_position = random.randint(0, screen_height - 100)
            error_message, text_color = error_messages[counter % 2]
            counter += 1
            
            popup = tk.Toplevel(root)
            popup.geometry(f"200x100+{x_position}+{y_position}")
            popup.config(bg="black")
            
            neon_bg = "black"
            if error_message == "TechSino":
                shadow_label = tk.Label(popup, text=error_message, fg="#39FF14", bg=neon_bg, font=("Arial", 14, "bold"))
            else:
                shadow_label = tk.Label(popup, text=error_message, fg="#FF2B2B", bg=neon_bg, font=("Arial", 14, "bold"))
            
            shadow_label.place(x=2, y=2)
            label = tk.Label(popup, text=error_message, fg=text_color, bg=neon_bg, font=("Arial", 14, "bold"))
            label.pack(expand=True, fill='both')
        
        time.sleep(0.2)

def stop_loop():
    global stop_flag
    stop_flag = True

root = tk.Tk()
root.withdraw()
threading.Thread(target=show_multiple_errors).start()
threading.Timer(5, stop_loop).start()
root.mainloop()
