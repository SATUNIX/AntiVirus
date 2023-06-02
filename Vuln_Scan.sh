#!/bin/bash
#Anthony Grace 
#TCD - GPL3.0 
#This software comes with absolutely no warranty

function root_scan {
    echo "---- Finding world writable files from root ----"
    find / -type f -perm -002 -exec dirname {} \; | sort -u
    sleep 0.2
    echo "---- Finding world executable files from root ----"
    find / -type f -perm -001 -exec dirname {} \; | sort -u
    sleep 0.2
    echo "---- Finding world writable files from user home directories ----"
    find /home/* -type f -perm -002 -exec dirname {} \; | sort -u
    sleep 0.2
    echo "---- Finding SGID/GUID files in the home directory ----"
    find ~ -type f \( -perm -4000 -o -perm -2000 \) -exec dirname {} \; | sort -u
    sleep 0.2
}

function user_scan {
    echo "---- Finding world writable files in the home directory ----"
    find ~ -type f -perm -002 -exec dirname {} \; | sort -u
    sleep 0.2
    echo "---- Finding world executable files in the home directory ----"
    find ~ -type f -perm -001 -exec dirname {} \; | sort -u
    sleep 0.2
    echo "---- Finding unowned files in the home directory ----"
    find ~ -nouser -exec dirname {} \; | sort -u
    sleep 0.2
    echo "---- Finding SGID/GUID files in the home directory ----"
    find ~ -type f \( -perm -4000 -o -perm -2000 \) -exec dirname {} \; | sort -u
    sleep 0.2
}

timestamp=$(date "+%Y%m%d%H%M%S")

if [[ $EUID -eq 0 ]]; then
    root_scan | tee "Vuln_Scan_Results_${timestamp}.txt"
else
    user_scan | tee "Vuln_Scan_Results_${timestamp}.txt"
fi

exit 0
