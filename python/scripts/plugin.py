import urllib.request
import os

folder_name = 'plugins/'
folder_path = os.path.join(os.getcwd(), folder_name)

file_paths = []

plugin_paths = []

if os.path.isfile("pluginloc.config"):
    with open('pluginloc.config', 'r') as file:
        plugin_paths = [line.strip() for line in file]

def install_plugins(url):
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

install_plugins(input("link-"))