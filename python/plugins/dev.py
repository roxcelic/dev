import urllib
import os
import requests

command_Text = {
    ".plugin_install(<a plugin link>)": "replace '<a plugin link> with a plugin you would like to install'",
    ".plugin_delte(<a local url>)": "replace '<a local url>' with a local file path to a plugin",
    ".plugin_list": "prints an each plugin installed",
    ".plugin_check": "prints plugin location values"
}

plugin_active_message = "plugin cleanup is active"

#plugin management data
folder_name = 'plugins/'
folder_path = os.path.join(os.getcwd(), folder_name)

file_paths = []

plugin_paths = []

if os.path.isfile("pluginloc.config"):
    with open('pluginloc.config', 'r') as file:
        plugin_paths = [line.strip() for line in file]

if os.path.isfile("plugin.config"):
    with open('plugin.config', 'r') as file:
        file_paths = [line.strip() for line in file]

def check_url_exists(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False
    
#plugin install script
def install_plugins(url):
    if (check_url_exists(url)):
        global plugin_paths, file_paths
        if url not in plugin_paths:
            plugin_paths.append(url)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            file_name = url[8:].replace("/", ".")
            file_name = folder_path + file_name
            urllib.request.urlretrieve(url, file_name)
            file_name = file_name.replace(os.getcwd(), "").replace("\\", "")
            file_paths.append(file_name)
            with open('pluginloc.config', 'w') as file:
                for item in plugin_paths:
                    file.write(f"{item}\n")
            with open('plugin.config', 'w') as file:
                for item in file_paths:
                    file.write(f"{item}\n")
            print("plugin installed")
    else:
        print("the link had no content to access")

#plugin delete script
def delete_plugins(local_ci):
    if local_ci in plugin_paths:
        plugin_paths.remove(local_ci)
        file_paths.remove(folder_name + local_ci[8:].replace("/", "."))
        with open('pluginloc.config', 'w') as file:
            for item in plugin_paths:
                file.write(f"{item}\n")
        with open('plugin.config', 'w') as file:
            for item in file_paths:
                file.write(f"{item}\n")
        os.remove(folder_name + local_ci[8:].replace("/", "."))
    else:
        print("sorry that plugin wasnt found")

def start():
    print("start")

def end():
    print("end")

def check(ci):
    if ci[:16] == ".plugin_install(" and ci[-1:] == ")":
        ci = ci[16:]
        ci = ci[:-1]
        install_plugins(ci)

    if ci[:15] == ".plugin_delete(" and ci[-1:] == ")":
        ci = ci[15:]
        ci = ci[:-1]
        delete_plugins(ci)

    if ci == ".plugin_list":
        print(plugin_paths)
        for item in plugin_paths:
            print(item)
    
    if ci == ".plugin_check":
        print("plugin_paths: ",plugin_paths)
        print("file_paths: ",file_paths)