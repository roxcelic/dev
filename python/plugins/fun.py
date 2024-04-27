import warnings
import time

plugin_active_message = "nice to see you again, twinkle toes"

command_Text = {
    ".yes(<text>)": "yes"
}

def check(ci):
    if ci[:5] == ".yes(" and ci[-1:] == ")":
        warnings.warn("you cant stop this without ending the script :3")
        warnings.warn("for anyone who needs extra help its 'ctrl + c'")
        time.sleep(1)
        ci = ci[5:]
        ci = ci[:-1]
        a = True
        while a:
            print(ci, end="")