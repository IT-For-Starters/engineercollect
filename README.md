# Engineer Collector
There seem to be multiple collection programs and scripts that engineers can use to gather information about a client's machine. However, these are either unnecessarily complicated, hidden, fixed (can't be customised) or cost human money. This is just my way of gathering lots of info of a client machine in a quick and easy program that engineers can run themselves, or that they can distribute to end users to run and send the results of.

**:exclamation: This is still in alpha, please use at own risk**

## How does this work?
It's nice and simple:
- The program will run a number of powershell commands that you specify
- Each command will generate an output, that is saved to a text file
- You can specify which commands you want to run from a single ```config.json``` file
    - If you don't provide one in the same directory as the program, it will automatically pull the default one from my repo.
- Once all commands are ran, all outputs are neatly put into a single ZIP file, which is stored in the same directory as the program.

## Features
:white_check_mark: All commands are ran locally, and no outputs are sent to anyone  
:white_check_mark: The commands to run are entirely customisable  
:white_check_mark: Specify whether you want to output the result as default, table or list

### Tell me more about the JSON
The ```config.json``` file is used to store all of the commands that the program will run.
Commands are filtered into "categories". Each category will get its own folder in the ZIP file, containing the outputs of all commands in their own text files.