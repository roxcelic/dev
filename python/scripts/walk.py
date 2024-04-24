#imports
import time

#messages
MESSAGES = [
    "this script is made to allow python code to be shared across the web by users",
    "it is designed to be lightweight and quick",
    "the code in the main downloaded script is well documented, you can see it by going to https://github.com/roxcelic/dev/python",
    "the scripts that it uses for inbuilt extra functions are not commented or presented as well but they can be accessed with: ",
    "https://github.com/roxcelic/dev/python/scripts",
    "this script also supports plguins, one of its main purposes.",
    "these plugins allow extra commands and code to be ran in the script, the ones ive made can be found here:",
    "https://github.com/roxcelic/dev/python/plugins",
    "plugins are not deleted as with other files as I found it was easier to keep them around, saving a lot of startup time",
    "but I have a plugin which deletes them on start so if you dont like it like that then it can easily be changed",
    "the main script has config files which are using in the extra program config to help display data for things such as \"whats new\"",
    "if there are any more questions feel free to message me any way you see fit, and there will be a blog post on my website that contains more data on this script",
    "thank you for downloading this and please dont forget to",
    "ENJOY!"
]

#Main script
wait = float(input("input a float for the time between messages to allow you to read them -"))
for item in MESSAGES:
    print(item)
    time.sleep(wait)