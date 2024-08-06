# RSA Cryptotrojan

#### Disclaimer
###### This project is for educational purposes only. I have used a ~40 bit rsa encryption schema to demonstrate how a kleptographic backdoor can be put in RSA. It is not suitable for any practical applications in its current form. Also it somehow fails to obtain the private key back about ~20% of the times and I dont know why. If you do figure it out let me know. I AM NOT RESPONSIBLE FOR HOW YOU USE THIS PIECE OF SOFTWARE.

## Installation
- git clone https://github.com/0x-Apollyon/RSA-Backdoor.git
- cd RSA-Backdoor
- python -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

## How to use

The folder "victim device" simulates the victim environment and "attacker device" simulates the attackers environment.
Steps to use the trojan are as follows
- Generate an attacker RSA keypair using attacker keygen.
- Put the public key in the victim device folder
- Now generate a victim RSA keypair using victim keygen
- Copy the victims PUBLIC key over to the attacker environment
- Use the reverser script to obtain the private key of the victim

# Features
- Cryptographically indistinguisable output compared to a non backdoored RSA implementation
- Trivial timing difference, the average time taken to generate a non backdoored RSA keypair using this implementation is 6.6854 ms compared to the backdoored implementation of 17.1556 ms. The 9 ms time difference is practically undetectable.
- Backward and forward security

## Theory

This attack is based on a technique described in the lecture "Kleptography:
Old Warnings New Threats!!" by Moti Yung and Adam Young.
[If you want to learn more about it you can find the lecture here](https://ciencias.medellin.unal.edu.co/eventos/cryptoco/images/presentaciones/CryptoCO_-_Yung_-_Lecture1.pdf)

Also credits to Yannic Hemmer for his klepto-python-rsa code which helped a lot in its development.
[You can find that code here](https://github.com/MeNoSmartBrain/kelpto-python-rsa)

## Improvements to be made

Several improvements can be made both in the algorithm and in the code itself.

### Code
- Better and faster prime generation
- Removal of that 20% failure rate

### Algorithm
- Faster key generation
- Currently the attacker has half the security compared to the user, this can be worked upon

## Contact

If you wish to contribute to this project, just open a pull request. If you wish to contact me regarding anything you can do so below
- [X](https://x.com/0xApollyon) : 0xApollyon
- Discord : 0xapollyon
