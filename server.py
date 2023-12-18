from typing import List, TypedDict

from flask import Flask, request

import blockchain as bc


class TxnData(TypedDict):
    sender: str
    recipient: str
    amount: int


# initialise our node
node = Flask(__name__)

# this node stores a list of txns
this_node_txns: List[TypedDict] = []  # TODO think about moving this inside the function
miner_address = "random-miner-address-69-420"

# initialise our SmolCoin
SmolCoin_blockchain = [bc.create_genesis_block()]
prior_block = SmolCoin_blockchain[0]


@node.route("/txn", methods=["POST"])
def transaction() -> str:
    # get txn data that is being posted and add to list of txn's
    new_txn = request.get_json()
    this_node_txns.append(new_txn)

    print("New transaction has been made")

    sender = new_txn["sender"]
    print(f"from {sender}")

    recipient = new_txn["recipient"]
    print(f"to {recipient}")

    amount = new_txn["amount"]
    print(f"to {amount}")

    return "confirmed\n"


@node.route("/mine", methods=["GET"])  # TODO: create the mine endpoint
def mine():
    last_block = SmolCoin_blockchain[len(SmolCoin_blockchain) - 1]
    last_proof = last_block

    return "Done mining\n"


node.run()
