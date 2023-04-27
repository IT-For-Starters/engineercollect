# Engineer Collector
There seem to be multiple collection programs and scripts that engineers can use to gather information about a client's machine. However, these are either unnecessarily complicated, hidden, fixed (can't be customised) or cost human money. This is just my way of gathering lots of info of a client machine in a quick and easy program that engineers can run themselves, or that they can distribute to end users to run and send the results of.

## How does this work?
It's nice and simple:
- The program will run a number of powershell commands that you specify
- Each command will generate an output, that is saved to a text file
- You can specify which commands you want to run from a single ```config.json``` file
    - If you don't provide one in the same directory as the program, it will automatically pull the default one from my repo.
- Once all commands are ran, all outputs are neatly put into a single ZIP file, which is stored in the same directory as the program.

## Features
:white_check_mark: All calculations are local only, so no sharing data with servers  
:white_check_mark: Bi-Directional comparisons mean that you can check for missing addresses on both sides  
:white_check_mark: Specify either a semi-colon or plus symbol as your delimiter for proxy addresses  

## Prerequisites
To run this application, you will need:
- A web server to host the app
- 2 CSV files/data with UserPrincipalName and ProxyAddresses columns