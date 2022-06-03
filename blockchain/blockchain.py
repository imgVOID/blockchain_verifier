import hashlib
from datetime import datetime
import binascii


# needs to be a metaclass
class Blockchain:
    def __init__(self, genesis: 'Block'):
        self._limit_transactions_per_block = 5
        self.__chain = []
        self.__chain.append(genesis)

    def __repr__(self):
        return self.__chain

    def create_block(self, block: 'Block', nonce: int, previous_hash: str, transactions: list):
        block.nonce, block.previous_block_hash, block.verified_transactions = nonce, previous_hash, transactions
        self.__chain.append(block)
        return block

    def dump_blockchain(self):
        print("Number of blocks in the chain: " + str(len(self.__chain)))
        for x in range(len(self.__chain)):
            block_temp = self.__chain[x]
            print("block # " + str(x))
            print('block hash:', hash(block_temp))
            print('=====================================')
            for transaction in block_temp.verified_transactions:
                self.__display_transaction(transaction)
                print('--------------')
            print('=====================================')

    @staticmethod
    def __display_transaction(transaction: 'Transaction'):
        transaction_dict = transaction.to_dict()
        print("transaction id: " + transaction_dict['id'])
        print('-----')
        print("sender: " + transaction_dict['sender'])
        print('-----')
        print("recipient: " + transaction_dict['recipient'])
        print('-----')
        print("value: " + str(transaction_dict['value']))
        print('-----')
        print("time: " + str(transaction_dict['time']))
        print('-----')

    @property
    def last_block_hash(self):
        return hash(self.__chain[-1])

    @property
    def last_block(self):
        return self.__chain[-1]

    @property
    def last_block_nonce(self):
        return self.__chain[-1].Nonce if self.__chain[-1].Nonce else 0

        # This is the function for proof of work
        # and used to successfully mine the block

    def mine(self):
        previous_proof = self.last_block_nonce
        new_proof = 1
        hash_result = None
        while hash_result is None:
            hash_operation = hashlib.sha256(str(
                new_proof ** 2 - previous_proof ** 2
            ).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                hash_result = hash_operation
            else:
                new_proof += 1
        return new_proof
