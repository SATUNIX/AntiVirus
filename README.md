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

The configuration is managed through the config.ini file, which should be located in the same directory as the ClamAVScanner.py script. The file contains the following sections:

    Network: Specifies the subnet_address and excluded_machine
    ClamAV: Specifies the quarantine_dir and scan_options
    Outlook: Specifies the email_address, email_password, and recipient_email

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
