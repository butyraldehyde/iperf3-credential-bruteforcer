#!/usr/bin/env python3

import argparse
from hashlib import sha256


parser=argparse.ArgumentParser()
parser.add_argument('--username','-u',type=str,help='Username string.')
parser.add_argument('--wordlist',required=True,help='Wordlist path.')
parser.add_argument('--hash',help='Hash string, should just be sha256 hash.')
parser.add_argument('--csv',help='Local CSV path.')
args=parser.parse_args()


def hashcheck(funcUsername,funcHash):
    try:
        with open(args.wordlist, 'r', encoding='ISO-8859-1') as f:
            for password in f:
                # The hash is generated using the bracketed username concatenated with the user password and sha256.
                # It looks like this before hashing: {bob}password1234
                # It looks like this after hashing: 747a7a9a3b80902b64e46e2acabbde92734214dc6d7b3e261a5dca62b59b10c2
                testString = f"{{{funcUsername.strip()}}}{password.strip()}"
                if sha256(testString.encode()).hexdigest() == funcHash:
                    print(f"The password for {funcUsername} is likely {password}")
                    return
            print(f"Couldn't find the password for {funcUsername}")
    except FileNotFoundError:
        print("File not found.")
        exit(1)
    except Exception as Err:
        print(f"Something went wrong. The error is: {Err}")
        exit(1)



if args.csv:
    if args.username:
        print("--csv option cannot be used with --username")
        exit(1)
    if args.hash:
        print("--csv option cannot be used with --hash")
        exit(1)
    try:
        with open(args.csv,'r') as csvfile:
            for row in csvfile:
                if row.startswith('#'): # No comment
                    continue
                if ',' not in row: # Ignore garbage
                    continue
                # TODO: Probably should check for other garbage lines.
                print(f"\nChecking wordlist for credentials for {row}")
                # CSVs for iperf are built using the form "username,hash".
                elements=row.split(',')
                username=elements[0].strip()
                CSVhash=elements[1].strip()
                hashcheck(username,CSVhash)
    except FileNotFoundError:
        print("File not found")
        exit(1)
    except Exception as error:
        print(f"Something went wrong. The error is: {error}")
        exit(1)
else:
    if not args.username:
        args.username = input("Username string: ")
        if not args.username:
            print("No username defined. Defaulting to: 'iperf-user'.")
            args.username = 'iperf-user' # This is 99% of the time not the answer.
    if not args.hash:
        args.hash = input("Hash string: ")
        if not args.hash:
            print("No hash provided. Please define one on the command line with --hash.")
            exit(1)
    print(f"\nChecking wordlist for credentials for {args.username}")
    hashcheck(args.username,args.hash)



exit(0) # Not necessary, but it makes me feel good. That's all that matters.

