command_Text = {
    "!dev(var)": "prints all variables that are currently defined"
}

plugin_active_message = "developer tools is running..."

def check(ci):
    print(plugin_active_message)
    #this is a dev command list made for developing and fun
    if ci[:5] == "!dev(" and ci[-1] == ")":

        #removes unessicary data
        ci = ci[5:]
        ci = ci[:-1]

        if ci == "var":
            print(dir())