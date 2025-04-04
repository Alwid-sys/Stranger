import configparser
import shutil
import os
import argparse

SETTINGS_FILE = "settings.ini"
BACKUP_SETTINGS = "settings.ini.bak"

def create_default_setting(): # Skapa settings.ini med innehåll för funktionalitet
    """Create a default settings file for testing"""
    if not os.path.exists(SETTINGS_FILE):
        print(f"Creating default settings file {SETTINGS_FILE}")

        config = configparser.ConfigParser()
        config["network"] = {
            'hostname' : 'test-device',
            'ip_adress' : '192.168.1.100',
            'subnet_mask' : '255.255.255.0'
        }
        with open(SETTINGS_FILE, "w") as f:
            config.write(f)

        print("Default settings created!")

def back_up_setting(): # Skapa backup, körs vid create (för säkerhetsskull) eller som eget argument
    shutil.copy(SETTINGS_FILE, BACKUP_SETTINGS)
    print("Backup created")

def update_user_IP(new_IP): # Editera IPadress
    config = configparser.ConfigParser()
    config.read(SETTINGS_FILE)

    old_IP = config['network']['ip_adress']
    config['network']['ip_adress'] = new_IP
    with open(SETTINGS_FILE, 'w') as f:
        config.write(f)

    print(f"Updated IP adress from {old_IP} to {new_IP}")

def update_host_name(new_host): # Editera hostname
    config = configparser.ConfigParser()
    config.read(SETTINGS_FILE)

    old_host = config['network']['hostname']
    config['network']['hostname'] = new_host
    with open(SETTINGS_FILE, 'w') as f:
        config.write(f)

    print(f"Updated hostname from {old_host} to {new_host}")

def update_subnet_mask(new_mask): # Editera subnätmasken
    config = configparser.ConfigParser()
    config.read(SETTINGS_FILE)

    old_mask = config['network']['subnet_mask']
    config['network']['subnet_mask'] = new_mask
    with open(SETTINGS_FILE, 'w') as f:
        config.write(f)
    print(f"Updated subnet mask from {old_mask} to {new_mask}")

def restore_profile(): # Återställ innehållet från backup
    if os.path.exists(BACKUP_SETTINGS):
        shutil.copy(BACKUP_SETTINGS, SETTINGS_FILE)
        print("Settings restored from backup")
    else:
        print("Alert, no backup found!")

def show_settings(): # Visa innehållet i settings.ini
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as show:
            config = configparser.ConfigParser()
            config.read_file(show)
            for section in config.sections():
                print(f"[{section}]")
            for key, value in config[section].items():
                print(f"{key} = {value}")
    else:
        print("The file does not exist yet...")

# Argument för argparse            
parser = argparse.ArgumentParser(description="My own little settings program, edit, backup, create and whatnot.")

parser.add_argument(
    "--create",
    action="store_true",
    help="Create a default settings file")

parser.add_argument(
    "--show",
    action='store_true',
    help="Show settings file")

parser.add_argument(
    "--restore",
    action="store_true",
    help="Restore settings from backup,")

parser.add_argument(
    "--backup",
    action='store_true',
    help="Create backup")

parser.add_argument(
    "--hostname",
    type=str,
    help="Declare new hostname")

parser.add_argument(
    "--ip",
    type=str,
    help="Declare new ip adress")

parser.add_argument(
    "--submask",
    type=str,
    help="Declare new subnet mask")

args = parser.parse_args()

# trolig ordning för att undvika buggar med argparse

if args.create:
    create_default_setting()
    back_up_setting()

if args.backup:
    back_up_setting()

if args.hostname:
    update_host_name(args.hostname)

if args.ip:
    update_user_IP(args.ip)

if args.submask:
    update_subnet_mask(args.submask)

if args.restore:
    restore_profile()

if args.show:
    show_settings()

