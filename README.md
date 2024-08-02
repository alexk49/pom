# pom - Pomodoro Timer

Basic pomodoro timer app with CLI and GUI made with tkinter.

## Usage

If args are passed when executing the script then it will run in the terminal only:

```
# set a 10 minute timer that will make sound on finish
./pom.py --time 10:00 --sound
```

Just running pom.py with no args will open the tkinter GUI.

The timer can be toggled on and off with the enter or spacebar in the GUI mode but in CLI only the enter key works as a toggle.
