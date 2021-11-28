from brownie import OurToken
from web3 import Web3
from scripts.helpful_scripts import get_account

INITIAL_SUPPLY = Web3.toWei(1000, "ether")


def deploy():
    account = get_account()
    our_token = OurToken.deploy(INITIAL_SUPPLY, {"from": account})
    print(f"token name: {our_token.name()}")
    print(f"our balance: {our_token.balanceOf(account)}")


def main():
    deploy()
