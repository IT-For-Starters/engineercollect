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

    
    
    def exe(self):
        print("\033[36m" + "[INFO] Running command: '"+self.cmd+"'")
        command_output = subprocess.check_output(['powershell', '-Command', self.cmd, self.format]).decode('utf-8')
        outputlines = command_output.split("\n")
        finaloutput = ""
        for line in outputlines:
            finaloutput += line
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

with open('config.json', 'r') as f:
    jsoncmd = json.load(f)    



print("\033[36m" + "[INFO] Using JSON for commands, running version", jsoncmd["version"])

for category in jsoncmd['categories']:
    print("\033[36m" + "[INFO] Creating directory for category '"+category['name']+"'")
    newcatdir = os.path.join(new_dir,category['name'])
    os.mkdir(newcatdir)

    for cmd in category["cmds"]:
        cmd = collectCommand(cmd["command"], newcatdir, cmd["friendly"], cmd["format"])
        cmd.exe()




print("\033[36m" + "[INFO] Creating ZIP archive of information called:", dir_name + ".zip")

shutil.make_archive(dir_name, 'zip', new_dir)

print("\033[32m" + "[SUCCESS] Collection Completed and ZIP file generated")

print("\033[0m")

