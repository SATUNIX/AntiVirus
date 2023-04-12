AV_6_4.py / ClamAVScanner
A Continuous Network Virus Scanner

ClamAVScanner - A continuous network virus scanning and email notification tool
Synopsis

arduino

python ClamAVScanner.py [config.ini]

Description:

ClamAVScanner is a Python script designed to continuously scan a specified network subnet for viruses using ClamAV, quarantine infected files, and send email notifications when infected files are detected.
Features

    Scans a network subnet for viruses using ClamAV
    Quarantines infected files
    Sends email notifications when infected files are detected
    Updates virus definitions regularly
    Allows users to change configurations

Configuration:

The configuration is managed through the config.ini file, which should be located in the same directory as the ClamAVScanner.py script. The file contains the following sections: (Make sure your quarantine directory is setup correctly) (see below)  

    Network: Specifies the subnet_address and excluded_machine
    ClamAV: Specifies the quarantine_dir and scan_options
    Outlook: Specifies the email_address, email_password, and recipient_email

Configuration of quarantine DIR: 

Choose a location where you want to create the quarantine directory. For example, you can create a directory named "quarantine" in the /var directory. To do this, open your terminal and run the following command:

    bash

sudo mkdir /var/quarantine

This command creates a new directory named "quarantine" in the /var directory. Make sure to set appropriate permissions for the directory so that ClamAV can move files into it:

bash

sudo chown clamav:clamav /var/quarantine
sudo chmod 750 /var/quarantine

Replace "clamav:clamav" with the appropriate user and group that ClamAV is running under on your system.

Specify the quarantine directory when running ClamAV:
When running ClamAV, use the --move option followed by the path to your quarantine directory to move infected files to the quarantine directory. For example:

bash

    sudo clamscan -r --move=/var/quarantine /path/to/scan

    This command scans the /path/to/scan directory recursively and moves any infected files it finds to the /var/quarantine directory.

In the ClamAVScanner script you provided earlier, the quarantine directory is specified in the config.ini file. You can set the quarantine directory path in the ClamAV section like this:

csharp

[ClamAV]
quarantine_dir = /var/quarantine

This path will be used in the network_scan() method when running the quarantine_command.
Installation: 

cd 
mkdir apps 
cd apps 
#(Or wherever you keep your git apps)
git clone {gitclone url}
sudo chmod +x *
pip install -r requirements.txt 

Usage:

To run the ClamAVScanner script, simply execute the following command:

bash

python AV_6_4.py

The script will prompt the user to choose whether to run the AV based on the existing config.ini file or edit the file before running. If the user selects 'edit', the script will open the config.ini file using the 'nano' text editor.

The main loop of the script will perform the following actions:

    Scan the network for viruses using ClamAV
    Quarantine any infected files
    Update virus definitions
    Send email notifications if infected files are detected
    Wait for 6 hours before repeating the process

Requirements:

    Python 3.6 or later
    ClamAV
    An email account with SMTP access

Bugs:

Please report any bugs to the developer.
anthony.grace@outlook.com

[ANTHONY JOSEPH GRACE]
[AAC SOLUTIONS]

Copyright No Rights Reserved
GPL
The GPL (GNU General Public License) is a widely used free software license, which guarantees end users the freedom to run, study, share, and modify the software. The GPL was created by Richard Stallman and is maintained by the Free Software Foundation.

Copyright (c) [2023]. All rights reserved.
