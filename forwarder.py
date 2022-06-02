#!/usr/bin/python3
import json, os, re
path = os.path.dirname(os.path.realpath(__file__))

print("Loading forwarder.json")
with open(f"{path}/forwarder.json") as handle:
    config = json.loads(handle.read())

coinsRaw = os.popen("current/spc wallet").read()
if not "Encrypted, Unlocked" in coinsRaw: exit("Wallet Locked")

balance = float(re.findall('Confirmed Balance:.*?([0-9.]+) SCP', coinsRaw , re.MULTILINE | re.DOTALL)[0][0])
print(f"Balance {balance} SCP")
hostRaw = os.popen("current/spc host").read()
storageRaw = re.findall('Storage:.*?([0-9.]+) (GB|TB).*?([0-9.]+) (GB|TB)', hostRaw , re.MULTILINE | re.DOTALL)

totalStorage = float(storageRaw[0][0]) * 1000 if "TB" in storageRaw[0][1] else float(storageRaw[0][0])
usedStorage = float(storageRaw[0][2]) * 1000 if "TB" in storageRaw[0][3] else float(storageRaw[0][2])

availableStorage = totalStorage - usedStorage
price = float(re.findall('Price:.*?([0-9.]+) SCP', hostRaw , re.MULTILINE | re.DOTALL)[0][0])

#Theoretically, but likely way to high since growth is very slow
neededBalanceTheoretically = (availableStorage / 1000) * float(price)
#More likely, 250GB per month at best
neededBalance = round(price / 4)
print(f"Needed Balance {neededBalance}/{neededBalanceTheoretically} SCP")

availableBalance = balance - neededBalance
print(f"Available Balance {availableBalance} SCP")
if availableBalance < 1: exit("Not enough balance")

print(f"Transfering {availableBalance} to {config['destination']}")
os.system(f"current/spc wallet send scprimecoins {availableBalance}SCP {config['destination']}")


