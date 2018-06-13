import stellar_base as ste


def get_account_information():
    mnemonic = (
        'illness spike retreat truth genius clock brain pass '
        'fit cave bargain toe'
    )
    key_pair = ste.Keypair.deterministic(mnemonic)
    address = ste.Address(key_pair.address().decode())
    address.get()
    print("Balances: {}".format(address.balances))
    print("Sequence Number: {}".format(address.sequence))
    print("Flags: {}".format(address.flags))
    print("Signers: {}".format(address.signers))
    print("Data: {}".format(address.data))


if __name__ == "__main__":
    get_account_information()
