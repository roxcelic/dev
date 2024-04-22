#all libs
import urllib.request

#this keeps the script running
cont = True

#basic Literal values
help_Text = '''
    here is some basic information about this script:
        this is for me (roxcelic) to share my python finds and fun, it is fully open source and i am happy to share the code

        here are some commands you can use to get started:
'''
intro_Text = '''
    hello, welcome to my program and congrats on using it. If you need any help please use the '?help' command
'''

#basic dicts
command_Text = {
    "?help": "this command prints the help literal giving the user information",
    ".hangman": "runs hangman from another downloaded script which should be located at 'extra.py'",
    ".end": "this command ends the script"
}

#imports
def import_lib(url):
    url = url
    file_name = "extra.py"
    urllib.request.urlretrieve(url, file_name)
    import extra

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
        input = input.replace(input[:6], '')
        input = input[:-1]

        #checks if assistance can be provided (if the given value exists in the 'command_Text dict')
        if input in command_Text:
            print(command_Text[input])
        else:
            print("sorry there is no help for command: ", input)
        
    #imports another script
    elif input == ".hangman":
        import_lib("https://dev.roxcelic.love/python/hangman.py")

    #ends the script
    elif input == ".end": return False

    #always returns true unless the script is ended
    return True

#runs the code
print(intro_Text)
while cont:
    ci = input("-")
    cont = check(ci);