import subprocess
import tkinter as tk
from tkinter import messagebox

process = None

def schedule_shutdown():
    global process

    time_str = entry_time.get()
    if not time_str.isdigit():
        messagebox.showerror("Error", "Please enter a valid time in seconds.")
        return
    
    command = f"shutdown -s -t {time_str}"
    process = subprocess.Popen(command, shell=True)
    messagebox.showinfo("Shutdown Scheduled", f"Computer will shut down in {time_str} seconds.")

def cancel_shutdown():
    time_str = entry_time.get()
    try:
        output = subprocess.check_output("shutdown -a", shell=True)
        messagebox.showinfo("Running Scheduled Shutdowns", f"Scheduled shutdowns {time_str} sec have been cancelled.")
    except subprocess.CalledProcessError:
        messagebox.showinfo("Running Scheduled Shutdowns", "There are no running scheduled shutdowns.")

# Create the main window
window = tk.Tk()
window.title("Shutdown Scheduler")

# Create and position the GUI elements
label_time = tk.Label(window, text="Shutdown Time (in seconds):")
label_time.pack()

entry_time = tk.Entry(window)
entry_time.pack()

button_schedule = tk.Button(window, text="Schedule Shutdown", command=schedule_shutdown)
button_schedule.pack()

button_cancel = tk.Button(window, text="Cancel Shutdown", command=cancel_shutdown)
button_cancel.pack()


# Start the main event loop
window.mainloop()
