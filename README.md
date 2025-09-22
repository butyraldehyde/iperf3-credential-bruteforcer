# iperf3-credential-bruteforcer
Python script for taking iperf3 credential CSVs or username and hash combinations and brute forcing with a wordlist.

USAGE:

```
$: python3 iperfbrute.py --wordlist /home/bob/Downloads/rockyou.txt --csv /home/bob/Downloads/iperfcsv.csv                                          

Checking wordlist for credentials for testuser,6d30222cf5cb9f09b0175e1dbfbc0b6fef34fc08c2fdf02682e0c2450c9c7170

The password for testuser is likely testpass

$:
```

```
$: python3 iperfbrute.py --wordlist /home/bob/Downloads/rockyou.txt \
--hash 6d30222cf5cb9f09b0175e1dbfbc0b6fef34fc08c2fdf02682e0c2450c9c7170 --username testuser

Checking wordlist for credentials for testuser
The password for testuser is likely testpass

$:

```

