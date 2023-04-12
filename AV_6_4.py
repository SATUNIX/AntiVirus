#12/4/2023
'''
THIS PROGRAM SUPPLYS BASIC CONFIG TO CLAM AV AND SENDS EMAIL UPDATES
RUNS ON A NETWORKED KALI MACHINE FOR AV SCANNING OF RELATED SERVERS 

STRAIGHT THROUGH CABLE

AACSOLUTIONS
https://www.aacsolutions.com.au/
ANTHONY GRACE
https://github.com.au/SATUNIX
'''
#TODO: Networked quarantine to seperate machine 
import time
import configparser
import subprocess
import smtplib
import argparse
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Constants
CONFIG_FILE = 'config.ini'
WAIT_TIME = 60 * 60 * 6

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class ClamAVScanner:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.subnet_address = self.config.get('Network', 'subnet_address')
        self.quarantine_dir = self.config.get('ClamAV', 'quarantine_dir')
        self.scan_options = self.config.get('ClamAV', 'scan_options')   
        self.email_address = self.config.get('Outlook', 'email_address')
        self.email_password = self.config.get('Outlook', 'email_password')
        self.recipient_emails = self.config.get('Outlook', 'recipient_email')
        self.excluded_machine = self.config.get('Network', 'excluded_machine')

    def network_scan(self):
        scan_command = ['sudo', 'clamscan', self.scan_options, self.subnet_address, f'--exclude={self.excluded_machine}']
        scan_output = subprocess.run(scan_command, capture_output=True, text=True)
        logger.info(scan_output.stdout)

        # Quarantine infected files
        quarantine_command = ['sudo', 'clamscan', '-r', f'--move={self.quarantine_dir}', self.subnet_address]
        quarantine_output = subprocess.run(quarantine_command, capture_output=True, text=True)
        logger.info(quarantine_output.stdout)
        return quarantine_output

    def email_message(self, quarantine_output):
        if quarantine_output.returncode != 0:
            sender_email = self.email_address
            recipient_emails = self.recipient_emails.split(',')
            message = MIMEMultipart()
            # Message configuration
            message['From'] = sender_email
            message['Subject'] = "Clam AV Alert"
            body = "Clam AV has detected infected files on your network and quarantined them."
            message.attach(MIMEText(body, 'plain'))
            outlook_server = smtplib.SMTP('smtp.office365.com', 587)

            try:
                outlook_server.starttls()
                # Log in to your Outlook account
                outlook_server.login(sender_email, self.email_password)
                for recipient_email in recipient_emails:
                    message['To'] = recipient_email.strip()  # Remove any leading/trailing whitespace
                    # Send the email message
                    outlook_server.sendmail(sender_email, recipient_email, message.as_string())
                logger.info("Email notification sent successfully.")
            except Exception as e:
                logger.error("Error sending email notification:", e)
            finally:
                # Quit the SMTP server
                outlook_server.quit()

    def get_user_input(self):
        while True:
            input_declaration = input("Run AV based on previous config.ini or do you want to change config.ini? (run/edit): ").lower()
            if input_declaration == "run":
                return True
            elif input_declaration == "edit":
                subprocess.run("nano config.ini", shell=True)
            else:
                logger.error("Invalid input. Please enter 'run' or 'edit'.")

    def run_av(self):
        if self.get_user_input():
            logger.info("Running default configurations: ")
            subprocess.run("cat config.ini", shell=True)
        # rest of the code
    def print_ascii_art():
        ascii_art = r"""
####       ####   ###  ##  ##  ###  ##  ##              ##     ##  ###  #### ##   ## ##
 ##         ##      ## ##  ##   ##  ### ##               ##    ##   ##  # ## ##  ##   ##
 ##         ##     # ## #  ##   ##   ###               ## ##   ##   ##    ##     ##   ##
 ##         ##     ## ##   ##   ##    ###              ##  ##  ##   ##    ##     ##   ##
 ##         ##     ##  ##  ##   ##     ###             ## ###  ##   ##    ##     ##   ##
 ##  ##     ##     ##  ##  ##   ##  ##  ###            ##  ##  ##   ##    ##     ##   ##
### ###    ####   ###  ##   ## ##   ##   ##           ###  ##   ## ##    ####     ## ##
                                                                                                   
  ##     ###  ##  #### ##    ####            ### ###    ####   ### ##   ##  ###   ## ##
   ##      ## ##  # ## ##     ##              ##  ##     ##     ##  ##  ##   ##  ##   ##
 ## ##    # ## #    ##        ##              ##  ##     ##     ##  ##  ##   ##  ####
 ##  ##   ## ##     ##        ##              ##  ##     ##     ## ##   ##   ##   #####
 ## ###   ##  ##    ##        ##              ### ##     ##     ## ##   ##   ##      ###
 ##  ##   ##  ##    ##        ##               ###       ##     ##  ##  ##   ##  ##   ##
###  ##  ###  ##   ####      ####               ##      ####   #### ##   ## ##    ## ##
    """
        print(ascii_art)

if __name__ == '__main__':
    # Initialize ClamAVScanner
    scanner = ClamAVScanner(CONFIG_FILE)
    # Call the function to print the ASCII art
    scanner.print_ascii_art()
    while True:
        # Call functions to get user input and run AV
        scanner.run_av()

        # Network scan
        quarantine_output = scanner.network_scan()

        # Update virus definitions every day
        for i in range(4):
            subprocess.run(['sudo', 'freshclam'])

        # Send notifications
        scanner.email_message(quarantine_output)

        # Wait for 6 hours
        time.sleep(WAIT_TIME)
