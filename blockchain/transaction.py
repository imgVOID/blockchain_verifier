import datetime
import collections
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random
import binascii


class Transaction:
    __GENESIS_KEY = RSA.generate(1024, Random.new().read)

    def __init__(self, sender, recipient, value):
        self.id = None
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict({
            'id': self.id,
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time})

    def sign_transaction(self):
        if self.sender == "Genesis":
            private_key = self.__GENESIS_KEY
        else:
            private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        self.id = binascii.hexlify(signer.sign(h)).decode('ascii')

        return self.id
