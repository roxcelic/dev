#all libs
import urllib.request

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
        file_name = "plugin/plug.py"
        urllib.request.urlretrieve(url, file_name)
        import plugin.plug as plugin
    else: print("- the option is always available -")
#commands
def check(input):

    #provides user assistance
    if input == "?help":
        #prints the help Literal
        print(help_Text)
        #prints commands and what they do
        for key, value in command_Text.items():
            print(f"{key}: {value}")

    #this is the help command which will return a value from command_Text relating to the command which was inquired about
    elif input[:6] == "?help(" and input[-1] == ")":
        #removes unessicary data
        input = input[6:]
        input = input[:-1]

        #checks if assistance can be provided (if the given value exists in the 'command_Text dict')
        if input in command_Text:
            print(command_Text[input])
        else:
            print("sorry there is no help for command: ",'"',input,'"')
    
    #allows plugins to be inputted
    elif input == ".plugin":
        local_input = input("please input the url to your plugin - ")
        import_plugin(local_input)
        print("loading plugin data...")
        command_Text.update(plugin.command_Text)
        plugin_is_active = True
        print("plugin loaded, to check new content run '?help' to list all commands")

    #imports another script
    elif input == ".hangman":
        import_lib("hangman.py")

    #ends the script
    elif input == ".end": return False

    if (plugin_is_active):
        plugin.check(input)
    #always returns true unless the script is ended
    return True

#runs the code
print(intro_Text)
import_lib("config.py")
while cont:
    print("-" *15)
    ci = input("-")
    cont = check(ci);