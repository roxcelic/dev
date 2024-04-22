# welcome to my python programme

```py
import urllib.request

print("if you would like to know more about this file and script please check out \"https://github.com/roxcelic/dev/python/README.md \" ")
input = input("- running this will download a file called script.py to your computer in this directory, is that okay (y/n) -")
if input.lower() == "y":
    url = "https://dev.roxcelic.love/python/index.py"
    file_name = "script.py"
    urllib.request.urlretrieve(url, file_name)

    import script
else: print("no worrys, its always good to stay safe")
```

this code is my way of sharing a constantly updating python script
it will firstly download [this file](index.py) to your pc as "script.py" and then run it
all of the code is completely open source and you should not need to change anything at all to get it to work

it downloads the file using 'urllib.request' which from my knoledge comes with most modern python installs, but i may be wrong

if you are uncomfortable with this in any way i understand, that being another reason why this code is completely public.

so please, ENJOY!