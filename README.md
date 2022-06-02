# scp-forwarder

## Work in Progress

**Dependencies**<br />
Python 3.7 or higher<br />
```
apt-get install -y git python3 python3-pip && pip3 install Southxchange==1.3
```

**Prepare**<br />
```
git clone https://github.com/Ne00n/scp-forwarder.git && cd scp-forwarder
cp forwarder.example.json forwarder.json
sed -i -e 's/address/YOURWALLET/g' config.json
```

**Test**<br />
```
python3 forwarder.py
```