import subprocess
import pprint
pp = pprint.PrettyPrinter()

# find all devices command
Find_command = 'devcon.exe find *'

#list HW ids of devices
hwIds_command = 'devcon.exe hwids *'

#Enable
Enable_command = 'devcon.exe enable *PID_1016'

#Disable
Disable_command = 'devcon.exe disable *Razer*'

#Find Device
Find_SpecificDevice_command = 'devcon.exe find *Razer*'

find= True
try:
    if find:
        result = subprocess.check_output(Find_SpecificDevice_command,shell=True ,stderr=subprocess.STDOUT)

        print(result)
except subprocess.CalledProcessError as e:
    raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))