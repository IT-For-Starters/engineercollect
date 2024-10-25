import subprocess
import os
import json
import datetime
import shutil
import requests

now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")


class collectCommand:
    def __init__(self, cmd, filedir, friendly, format = "table"):
        self.cmd = cmd
        self.filedir = filedir
        self.friendly = friendly
        if format == "list":
            self.format = "| Format-List"
        elif format == "none":
            self.format = ""
        else:
            self.format = "| Format-Table"

    
    
    def exePS(self):
        print("\033[36m" + "[INFO][PS] Running command: '"+self.cmd+"'")
        try:
            command_output = subprocess.check_output(['powershell', '-Command', self.cmd, self.format]).decode('utf-8', errors='replace')
            outputlines = command_output.split("\n")
            finaloutput = ""
            for line in outputlines:
                finaloutput += line
        except Exception as e:
            print("\033[31m" + f"An unexpected error occurred: {e}")
            finaloutput = f"{e}"
        
        file_name = self.friendly + '.txt'
        file_path = os.path.join(self.filedir, file_name)
        with open(file_path, 'w') as file:
            file.write(finaloutput)
        print("\033[32m" + "[SUCCESS] Command output saved as '"+self.friendly+".txt'")

    def exeCMD(self):
        print("\033[36m" + "[INFO][CMD] Running command: '"+self.cmd+"'")
        try:
            command_output = subprocess.check_output(self.cmd, shell=True).decode('utf-8', errors='replace')
            outputlines = command_output.split("\n")
            finaloutput = ""
            for line in outputlines:
                finaloutput += line
        except Exception as e:
            print("\033[31m" + f"An unexpected error occurred: {e}")
            finaloutput = f"{e}"
        file_name = self.friendly + '.txt'
        file_path = os.path.join(self.filedir, file_name)
        with open(file_path, 'w') as file:
            file.write(finaloutput)
        print("\033[32m" + "[SUCCESS] Command output saved as '"+self.friendly+".txt'")



dir_name = "EngineerCollect_" + timestamp
temp_dir = os.environ.get('TEMP')
new_dir = os.path.join(temp_dir, dir_name)

if not os.path.exists(new_dir):
    os.mkdir(new_dir)


if not os.path.isfile("config.json"):
    print("\033[33m" + "[WARN] No config file found in working directory. Will download the default")
    confurl = "https://github.com/CallMeSteve297/engineercollect/raw/main/config.json"
    confresponse = requests.get(confurl)
    if confresponse.status_code == 200:
        # File found, proceed with download
        with open("config.json", "wb") as f:
            f.write(confresponse.content)
            print("\033[32m" + "[SUCCESS] Default Config File Retrieved")
        with open('config.json', 'r') as f:
            jsoncmd = json.load(f)
    else:
        # File not found or other error
        print("Error:", confresponse.status_code)
else:
    with open('config.json', 'r') as f:
        jsoncmd = json.load(f)




print("\033[36m" + "[INFO] Using JSON for commands, running version", jsoncmd["version"])

for category in jsoncmd['categories']:
    print("\033[36m" + "[INFO] Creating directory for category '"+category['name']+"'")
    newcatdir = os.path.join(new_dir,category['name'])
    os.mkdir(newcatdir)

    for cmd in category["cmds"]:
        if cmd["type"] == "cmd":
            cmd = collectCommand(cmd["command"], newcatdir, cmd["friendly"], "none")
            cmd.exeCMD()
        elif cmd['type'] == "ps":
            cmd = collectCommand(cmd["command"], newcatdir, cmd["friendly"], cmd["format"])
            cmd.exePS()
        else:
            print("\033[91m" + "[ERROR] No Type Specified for Command", cmd["command"])




print("\033[36m" + "[INFO] Creating ZIP archive of information called:", dir_name + ".zip")

shutil.make_archive(dir_name, 'zip', new_dir)

print("\033[32m" + "[SUCCESS] Collection Completed and ZIP file generated")

print("\033[0m")

