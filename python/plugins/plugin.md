#welcome to the plugins
```py
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
#must also return the current input
def update(ci):
    print("update")
    return ci;

#ran every run through of the main loop at the end
def dem():
    print("dem")

#ran through at the end of the script
def end():
    print("end")
```

in this folder you will find the file displayed above as [plug.py](https://github.com/roxcelic/dev/python/plugins/plug.py)
it is a templete for a basic plugin, please be kind with this and dont make anything bad
but i cant really stop you

please enjoy it though!

if you need any help feel free to contact me any way that seems fit