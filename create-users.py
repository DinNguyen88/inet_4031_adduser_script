#!/usr/bin/env python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        # Skip comments and empty lines
        if line.startswith('#') or not line.strip():
            continue

        # Use re.match to check for lines starting with a hash (#)
        match = re.match(r'^#', line)

        # Split the line into fields
        fields = line.strip().split(':')

        # Check if the line starts with a # or doesn't have exactly 5 fields
        if match or len(fields) != 5:
            continue  # Skip to the next iteration if true

        # Extract user details
        username, password, last_name, first_name, groups_str = fields

        # Format for the GECOS field
        gecos = f"{first_name} {last_name},,,"

        # Split groups by comma, ignore if '-'
        groups = [] if groups_str == '-' else groups_str.split(',')

        # User creation command
        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        os.system(cmd)

        # Set user password
        print(f"==> Setting the password for {username}...")
        cmd = f"echo '{username}:{password}' | sudo chpasswd"
        os.system(cmd)

        # Assign user to specified groups
        for group in groups:
            if group:
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/usermod -a -G {group} {username}"
                os.system(cmd)

if __name__ == '__main__':
    main()

