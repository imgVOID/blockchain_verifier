from client import Client
from transaction import Transaction
from block import Block
from blockchain import Blockchain

transactions = []
Dinesh = Client()
Ramesh = Client()
Seema = Client()
Vijay = Client()
t1 = Transaction("Genesis", Dinesh.identity, 15.0)
transactions.append(t1)
t2 = Transaction(Dinesh, Seema.identity, 6.0)
t2.sign_transaction()
transactions.append(t2)
t3 = Transaction(Ramesh, Vijay.identity, 2.0)
t3.sign_transaction()
transactions.append(t3)
t4 = Transaction(Seema, Ramesh.identity, 4.0)
t4.sign_transaction()
transactions.append(t4)
t5 = Transaction(Vijay, Seema.identity, 7.0)
t5.sign_transaction()
transactions.append(t5)
t6 = Transaction(Ramesh, Seema.identity, 3.0)
t6.sign_transaction()
transactions.append(t6)
t7 = Transaction(Seema, Dinesh.identity, 8.0)
t7.sign_transaction()
transactions.append(t7)
t8 = Transaction(Seema, Ramesh.identity, 1.0)
t8.sign_transaction()
transactions.append(t8)
t9 = Transaction(Vijay, Dinesh.identity, 5.0)
t9.sign_transaction()
transactions.append(t9)
t10 = Transaction(Vijay, Ramesh.identity, 3.0)
t10.sign_transaction()
transactions.append(t10)

blockchain = Blockchain(Block(first_transaction=t1))

blockchain.create_block(
    block=Block(), nonce=blockchain.mine(),
    previous_hash=blockchain.last_block_hash, transactions=[t2, t3, t4]
)

blockchain.dump_blockchain()
