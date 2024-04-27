import warnings
import time

plugin_active_message = "nice to see you again, twinkle toes"

command_Text = {
    ".yes(<text>)": "yes"
}

def check(ci):
    warnings.warn("you cant stop this without ending the script :3")
    time.sleep(1)
    if ci[:5] == ".yes(" and ci[-1:] == ")":
        ci = ci[5:]
        ci = ci[:-1]
        print(ci, end="")