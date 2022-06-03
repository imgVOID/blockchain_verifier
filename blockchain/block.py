class Block:
    def __init__(self, first_transaction=None):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = None

        if first_transaction:
            first_transaction.sign_transaction()
            self.verified_transactions.append(first_transaction)
            self.previous_block_hash = None
            self.Nonce = 0
