# Shuffle

CashShuffle is a plugin for the [Electron Cash](https://electroncash.org/) BCH wallet. It allows users to make shuffled transactions using [CoinJoin](https://en.wikipedia.org/wiki/CoinJoin).

## Installation

Ubuntu users can install using the following command. This command will install the latest version of Electron Cash with CashShuffle in your home directory.

```
cd ~/ && wget https://electroncash.org/downloads/3.0/win-linux/ElectronCash-3.0.tar.gz && tar -xvzf ElectronCash-3.0.tar.gz && rm -rf ElectronCash-3.0.tar.gz && wget https://github.com/cashshuffle/cashshuffle-electron-cash-plugin/archive/master.zip && unzip master.zip && rm -rf master.zip && mv cashshuffle-electron-cash-plugin-master/shuffle 'Electron Cash-3.0/plugins' && rm -rf cashshuffle-electron-cash-plugin-master && sed -i "s/'electroncash_plugins.virtualkeyboard',/'electroncash_plugins.virtualkeyboard', 'electroncash_plugins.shuffle',/" 'Electron Cash-3.0/setup.py' && cd 'Electron Cash-3.0' && sudo python3 setup.py install
```

Otherwise, use the following instructions:

1. Place the `shuffle` folder `cashshuffle-electron-cash-plugin-master/shuffle` into the Electron Cash plugins folder `Electron Cash-3.0/plugins`
2. Open the `setup.py` file `Electron Cash-3.0/setup.py` and find the line that contains the text `'electroncash_plugins.virtualkeyboard'`. Replace this text with

```'electroncash_plugins.virtualkeyboard', 'electroncash_plugins.shuffle',```

3. Change directories into Electron Cash, and re-install `sudo python3 setup.py install`

## Getting started

1. Enable plugin from 'tools/plugins' menu

![Settings](/images/settings.png)

2. Press `Settings` and enter the server connection string

![Server settings](/images/server_settings.png)

3. Close the settings dialog window. The shuffle tab will appear

![Server settings](/images/shuffle_tab.png)

## Making shuffle

1. Form `Shuffle input address` choose coin which you want to shuffle. The list of coins formed from utxo's of your wallet.

2. From `Shuffle change address` choose the address for the change. You can leave default setting if you don't want to get any change back.

3. From `Shuffle output address` choose the address for shuffled output

4. In the amount block choose the amount of coins for shuffling.

5. Fee is fixed and unchanged  

6. If amount of coins in input grater then sum of shuffling amount fee then `Shuffle` button will become enabled

7. Pressing the `Shuffle` will start shuffling process. After 5 players registered on server shuffling process will starts.

8. If all goes good you will see the outputs and transaction dialog window in the end. If something goes wrong you will see the errors in output.

9. In this version of protocol one of the players should press `broadcast` on transaction dialog window.    
