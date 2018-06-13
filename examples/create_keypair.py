import requests
from stellar_base import Keypair


def create_keypair_determinist_english():
    mnemonic = (
        'illness spike retreat truth genius clock brain pass '
        'fit cave bargain toe'
    )
    key_pair = Keypair.deterministic(mnemonic, index=21)
    public_key = key_pair.address_str
    print("Public key / Account address:\n", public_key)
    print("Seed / Your secret to keep it on local:\n",
          key_pair.seed().decode())
    r = requests.get('https://friendbot.stellar.org/?addr=' + public_key)
    print("Send Friend bot the public key\n", r.text)


if __name__ == "__main__":
    create_keypair_determinist_english()
