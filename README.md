# Shutdown Scheduler using Python and Tkinter

This Python script allows you to schedule a system shutdown and cancel scheduled shutdowns using a graphical user interface (GUI) built with Tkinter.

## Prerequisites

- Python 3.x installed on your computer.
- Tkinter library (usually included with Python standard library).

## How to Use

1. Run the script.
2. Enter the time in seconds after which you want the computer to shut down in the "Shutdown Time (in seconds)" field.
3. Click the "Schedule Shutdown" button to schedule the shutdown. You will receive a confirmation message.
4. To cancel a scheduled shutdown, click the "Cancel Shutdown" button. If there are no scheduled shutdowns, you will be notified.

## Script Details

- The script uses the `subprocess` module to run system commands.
- `shutdown -s -t {time_str}` is used to schedule a shutdown, where `{time_str}` is the time in seconds.
- `shutdown -a` is used to cancel a scheduled shutdown.
- The GUI is created using Tkinter, a Python library for creating graphical interfaces.
- Input validation is included to ensure that a valid time in seconds is entered.
- Messages are displayed using `messagebox` from Tkinter.

## Important Notes

- Be cautious when scheduling shutdowns, as they will force the computer to shut down after the specified time, potentially causing unsaved work to be lost.

## Author

This script was created by **MohammedHank91**

## License

This script is open-source and available under the [MIT License](LICENSE).
