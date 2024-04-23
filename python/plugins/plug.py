#this is the dict which lists the plugins commands and what they do
command_Text = {
    ".hey": "returns plugin status"
}

#this is the message that will print when the plugin is put in the active state
plugin_active_message = "hey"

#add the commands here
def check(input):
    if input == ".hey": print(print(plugin_active_message))