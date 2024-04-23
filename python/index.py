#all libs
import urllib.request
import shutil
import os

#this keeps the script running
cont = True

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
    ".hangman": "runs hangman from another downloaded script which should be located at 'extra.py'",
    ".plugin": "allows you to install a 3rd party plugin",
    ".local_plugin": "allows you to install a 3rd party plugin from local storage",
    ".end": "this command ends the script"
}

#imports

def import_lib(url):
    local_input = input("- this will download an extra lib as extra.py are you sure you would like to do this (y/n) -")
    if local_input.lower() == "y":
        url = "https://dev.roxcelic.love/python/scripts/" + url
        file_name = "extra.py"
        urllib.request.urlretrieve(url, file_name)
        import extra
    else: print("- the option is always available -")

def import_plugin(url):
    local_input = input("- this will download the python file for the plugin and run it, please be safe with the code you download, would you like to continue? (y/n) -")
    if local_input.lower() == "y":
        file_name = "plug.py"
        urllib.request.urlretrieve(url, file_name)
        globals()["plug"] = __import__("plug")

    else: print("- the option is always available -")

#commands
def check(ci):

    #ends the script
    if ci == ".end": return False

    #provides user assistance
    elif ci == "?help":
        #prints the help Literal
        print(help_Text)
        #prints commands and what they do
        for key, value in command_Text.items():
            print(f"{key}: {value}")

    #this is the help command which will return a value from command_Text relating to the command which was inquired about
    elif ci[:6] == "?help(" and ci[-1] == ")":
        #removes unessicary data
        ci = ci[6:]
        ci = ci[:-1]

        #checks if assistance can be provided (if the given value exists in the 'command_Text dict')
        if ci in command_Text:
            print(command_Text[ci])
        else:
            print("sorry there is no help for command: ",'"',ci,'"')
    
    #allows plugins to be inputted
    elif ci == ".plugin":
        global plugin_is_active
        local_input = input("please input the url to your plugin - ")
        import_plugin(local_input)
        print("loading plugin data...")
        command_Text.update(plug.command_Text)
        plugin_is_active = True
        print("plugin loaded, to check new content run '?help' to list all commands")

    elif ci == ".local_plugin":
        local_input = input("please enter the name and location of the file -")
        shutil.copy(local_input, "plug.py")
        globals()["plug"] = __import__("plug")
        print("loading plugin data...")
        command_Text.update(plug.command_Text)
        plugin_is_active = True
        print("plugin loaded, to check new content run '?help' to list all commands")


    #imports another script
    elif ci == ".hangman":
        import_lib("hangman.py")

    elif (plugin_is_active):
        plug.check(ci)

    #always returns true unless the script is ended
    return True

#runs the code
print(intro_Text)
import_lib("config.py")
while cont:
    print("-" *15)
    ci = input("-")
    cont = check(ci);

#removes the files and data
if os.path.exists("/__pycache__/") and os.path.isdir("/__pycache__/"):
    shutil.rmtree("/__pycache__/")
if os.path.exists("script.py"):
        os.remove("script.py")
if os.path.exists("extra.py"):
        os.remove("extra.py")
if os.path.exists("plug.py"):
        os.remove("plug.py")