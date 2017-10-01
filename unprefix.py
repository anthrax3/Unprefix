#!c:/Python36/python.exe

import os
import argparse

parser = argparse.ArgumentParser(description='[ Unprefix Version 0.1 ] ')
parser.add_argument(
    "--path", help=r"python --path C:\Users\TrustedSec\Downloads", required=True)
args = parser.parse_args()
files = os.listdir(args.path)

banner = """
███    █▄  ███▄▄▄▄      ▄███████▄    ▄████████    ▄████████    ▄████████  ▄█  ▀████    ▐████▀
███    ███ ███▀▀▀██▄   ███    ███   ███    ███   ███    ███   ███    ███ ███    ███▌   ████▀
███    ███ ███   ███   ███    ███   ███    ███   ███    █▀    ███    █▀  ███▌    ███  ▐███
███    ███ ███   ███   ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄      ▄███▄▄▄     ███▌    ▀███▄███▀
███    ███ ███   ███ ▀█████████▀  ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀▀███▀▀▀     ███▌    ████▀██▄
███    ███ ███   ███   ███        ▀███████████   ███    █▄    ███        ███    ▐███  ▀███
███    ███ ███   ███   ███          ███    ███   ███    ███   ███        ███   ▄███     ███▄
████████▀   ▀█   █▀   ▄████▀        ███    ███   ██████████   ███        █▀   ████       ███▄
                                    ███    ███
								[ Developed By: @0xSecGuy ]
		"""

print(banner)

try:
    for f in files:
        if not f.startswith('WWW.DOWNVIDS.NET-'):
            continue
        else:
            os.rename(os.path.join(args.path, f),
                      os.path.join(args.path, f[17:]))
            print('Video has been renamed: ' + (f[17:]))

except Exception as e:
    print(str(e))

print('\n[+] Mission Completed')
print('[+] Have a nice day!')
