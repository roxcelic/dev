#all libs
import urllib.request
import importlib.util
import shutil
import os

#removes all 'bad' data
def clean():
    if os.path.exists("__pycache__") and os.path.isdir("__pycache__"):
        shutil.rmtree("__pycache__")
    if os.path.exists("plugins/__pycache__") and os.path.isdir("plugins/__pycache__"):
        shutil.rmtree("plugins/__pycache__")
    if os.path.exists("script.py"):
            os.remove("script.py")
    if os.path.exists("extra.py"):
            os.remove("extra.py")
    if os.path.exists("plug.py"):
            os.remove("plug.py")

clean()

#list of plugins
plugin_paths = []

#this keeps the script running
cont = True

#checks for concent
concent = 0

#this checks if a plugin is installed
plugin_is_active = False

#basic Literal values
intro_Text = '''
    hello, welcome to my program and congrats on using it.
    after each line it will print "-" 15 times to show you that you are out of any command menu
    all of this code is fully open source if you would like to check whats happening at "https://github.com/roxcelic/dev"
    
    If you need any help please use the '?help' command
'''

help_Text = '''
    here is some basic information about this script:
        this is for me (roxcelic) to share my python finds and fun, it is fully open source and i am happy to share the code

        here are some commands you can use to get started:
'''

#basic dicts
command_Text = {
    "?help": "this command prints the help literal giving the user information",
    "?help(<a command>)": "swapping out '<a command>' for a command you would like to search for will tell you about that command and only that command",
    "?walkThrough": "runs a walkthrough of the script and all of its functions, goals and abilties",
    ".hangman": "runs hangman from another downloaded script which should be located at 'extra.py'",
    ".plugin": "allows you to install a 3rd party plugin",
    ".concent": "applys concent automatically, only works during the run it was ran due to saftey",
    ".end": "this command ends the script"
}

#imports

def import_from_path(path):
    module_name = os.path.basename(path).replace('.py', '')
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def import_lib(url):
    if concent == 1: local_input = "y"
    else: local_input = input("- this will download an extra lib as extra.py are you sure you would like to do this (y/n) -")
    if local_input.lower() == "y":
        url = "https://dev.roxcelic.love/python/scripts/" + url
        file_name = "extra.py"
        urllib.request.urlretrieve(url, file_name)
        import_from_path("extra.py")
    else: print("- the option is always available -")

def help():
    command_Text2 = command_Text
    for path in plugin_paths:
        if os.path.isfile(path):
            module = import_from_path(path)
            if hasattr(module, 'command_Text'):
                command_Text2.update(module.command_Text)
    
    print(help_Text)

    for key, value in command_Text.items():
        print(f"{key}: {value}")

def help2(ci):
    command_Text2 = command_Text
    for path in plugin_paths:
        if os.path.isfile(path):
            module = import_from_path(path)
            if hasattr(module, 'command_Text'):
                command_Text2.update(module.command_Text)

    if ci in command_Text2:
        print(command_Text2[ci])
    else:
        print("sorry there is no help for command: ",'"',ci,'"')
    

#installs all loaded plugins
if os.path.isfile("plugin.config"):
    with open('plugin.config', 'r') as file:
        plugin_paths = [line.strip() for line in file]

for path in plugin_paths:
    module = import_from_path(path)
    if hasattr(module, 'start'):
        module.start()

#commands
def check(ci):
    global plugin_paths

    #runs the update function in all of the installed plugins
    for path in plugin_paths:
        if os.path.isfile(path):
            module = import_from_path(path)
            if hasattr(module, 'update'):
                module.update()

    #ends the script
    if ci == ".end": return False

    #provides user assistance
    elif ci == "?help":
        help()

    #this is the help command which will return a value from command_Text relating to the command which was inquired about
    elif ci[:6] == "?help(" and ci[-1] == ")":
        #removes unessicary data
        ci = ci[6:]
        ci = ci[:-1]

        #checks if assistance can be provided (if the given value exists in the 'command_Text dict')
        help2(ci)
    
    #runs the script walkthrough
    elif ci == "?walkThrough":
        import_lib("walk.py")
    
    #allows plugins to be inputted
    elif ci == ".plugin":
        import_lib("plugin.py")
        
    #imports another script
    elif ci == ".hangman":
        print("hanf")
        import_lib("hangman.py")

    if ci == ".concent":
        local_input = input("would you like to automatically give concent to all downloads? (n/y) ")
        if local_input.lower() == "y":
            concent = 1
            with open('main.config',"r") as file:
                localread = [line.strip() for line in file]
            localread[2] = concent
            with open('main.config',"w") as file:
                for item in localread:
                    file.write(str(item) + "\n")


    if os.path.isfile("plugin.config"):
        with open('plugin.config', 'r') as file:
            plugin_paths = [line.strip() for line in file]

    #runs the check function in all installed plugins
    for path in plugin_paths:
        if os.path.isfile(path):
            module = import_from_path(path)
            if hasattr(module, 'check'):
                module.check(ci)

    #always returns true unless the script is ended
    return True

#runs the code
print(intro_Text)
print("attempting to import the required data to update the config data...")
import_lib("config.py")

#prints the plugin active message for each installed plugin
for path in plugin_paths:
    module = import_from_path(path)
    if hasattr(module, 'plugin_active_message'):
        print(module.plugin_active_message)

while cont:
    #resets all loaded plugin location data
    if os.path.isfile("plugin.config"):
        with open('plugin.config', 'r') as file:
            plugin_paths = [line.strip() for line in file]

    print("-" *15)

    ci = input("-")
    cont = check(ci);

    #runs the dem function in each installed plugin
    for path in plugin_paths:
        if os.path.isfile(path):
            module = import_from_path(path)
            if hasattr(module, 'dem'):
                module.dem()

#runs the end function once the script is ended
for path in plugin_paths:
    if os.path.isfile(path):
        module = import_from_path(path)
        if hasattr(module, 'end'):
            module.end()

#cleans the excess files/folders
clean()
