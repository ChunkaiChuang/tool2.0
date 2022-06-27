import os 
import subprocess

def get_device_sn():
    output_list=[]
    devices=[]
    output_str=subprocess.check_output("adb devices".split())[25:].decode()
    for item in output_str.split("\n"):
        if item == "":
            pass
        else:
            output_list.append(item)
    for item in output_list:
        devices.append(item.split("\t")[0])
    return devices

def name():                          #Back up (first name and last name)
    devices=get_device_sn()
    for x in devices:
        os.system(f'''adb -s {x} shell input text  "AlwaysTwoFiveTwoThree"''')
        os.system(f'''adb -s {x} shell input keyevent KEYCODE_TAB''')
        os.system(f'''adb -s {x} shell input text  "PassNineFourThreeNine"''')
        os.system(f'adb -s {x} shell input keyevent KEYCODE_TAB')
        os.system(f'adb -s {x} shell input keyevent KEYCODE_ENTER')
def base():                          #Back up (Base information)
    devices=get_device_sn()
    for x in devices:
        os.system(f'adb -s {x} shell input keyevent KEYCODE_TAB')
        os.system(f'adb -s {x} shell input keyevent KEYCODE_ENTER')
        os.system(f'adb -s {x} shell sleep 1')
        os.system(f'adb -s {x} shell input keyevent KEYCODE_TAB')
        os.system(f'adb -s {x} shell input keyevent KEYCODE_ENTER')
        os.system(f'adb -s {x} shell input keyevent KEYCODE_TAB')
        os.system(f'''adb -s {x} shell input text  "26"''')
        os.system(f'adb -s {x} shell input keyevent KEYCODE_TAB')
        os.system(f'''adb -s {x} shell input text  "1996"''')
        os.system(f'adb -s {x} shell input keyevent KEYCODE_TAB')
        os.system(f'adb -s {x} shell input keyevent KEYCODE_ENTER')
        os.system(f'adb -s {x} shell sleep 1')
        os.system(f'adb -s {x} shell input keyevent KEYCODE_TAB')
        os.system(f'adb -s {x} shell input keyevent KEYCODE_ENTER')
        os.system(f'adb -s {x} shell input keyevent KEYCODE_TAB')
        os.system(f'adb -s {x} shell input keyevent KEYCODE_ENTER')

def LDAP():
    devices=get_device_sn()
    for x in devices:
        os.system(f'''adb -s {x} shell input text  ""''')

def L_password():
    devices=get_device_sn()
    for x in devices:
        os.system(f'''adb -s {x} shell input text  ""''')

def QA():
    devices=get_device_sn()
    for x in devices:
        os.system(f'''adb -s {x} shell setprop debug.betterbug.qa true''')

def Test():
    devices=get_device_sn()
    for x in devices:
        os.system(f'''adb -s {x} shell input text "Test"''')

def OTA():
    os.system('adb root')
    os.system('''adb shell am broadcast -a 'com.google.android.gms.phenotype.FLAG_OVERRIDE' \
  --es package "com.google.android.platform.ota" \
  --es user "\*" \
  --esa flags "server_based_ror_enabled" \
  --esa values "true" \
  --esa types "boolean" \
  com.google.android.gms        # Run complete command''')
    os.system('adb shell device_config get ota server_based_ror_enabled')

def reboot():
    devices=get_device_sn()
    for x in devices:
        os.system(f'''adb -s {x} reboot''')

def before():
        os.system('adb shell dumpsys lock_settings')

def lock():
        os.system('adb shell dumpsys activity | grep state=RUNNING')

def account():
    devices=get_device_sn()
    for x in devices:
        os.system(f'''adb -s {x} shell input text ""''')
        
def password():
    devices=get_device_sn()
    for x in devices:
        os.system(f'''adb -s {x} shell input text ""''')

