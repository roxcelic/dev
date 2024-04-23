#this is the dict which lists the plugins commands and what they do
command_Text = {
    ".hey": "returns plugin status"
}

#this is the message that will print when the plugin is put in the active state at the start of the script
plugin_active_message = "hey"

#add the commands here
def check(input):
    global plugin_active_message
    if input == ".hey": print(print(plugin_active_message))

#ran at the start of the script
def start():
    print("start")

#ran every run through at the start of the main check
def update():
    print("update")

#ran every run through of the main loop
def dem():
    print("dem")

#ran through at the end of the script
def end():
    print("end")