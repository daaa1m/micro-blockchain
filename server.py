import json
from datetime import datetime
from typing import List

from flask import Flask, request

import blockchain as bc
from blockchain import Block, TxnData

miner_address = "6969420-blaze-it"

# initialise our node
node = Flask(__name__)


# initialise our SmolCoin chain which is a list of Blocks
prime = bc.create_genesis_block()
SmolCoin = [prime]

# this node stores a list of txns which starts with the first grant
this_node_txns: List[TxnData] = prime.data["transactions"]


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

    print("node txn's are now\n", this_node_txns)

    return "confirmed\n"


@node.route("/mine", methods=["GET"])
def mine() -> str:
    last_block = SmolCoin[-1]
    proof = bc.proof_of_work(last_block.data["proof"])

    this_node_txns.append(TxnData(sender="server", recipient=miner_address, amount=1))

    mined_block = bc.create_next_block(last_block, proof, this_node_txns)

    SmolCoin.append(mined_block)

    # print(vars(SmolCoin[-1]))

    return "mine succesful\n"


def datetime_serializer(obj) -> str:
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convert datetime to ISO 8601 string
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


@node.route("/blocks", methods=["GET"])
def get_blocks() -> str:
    SmolCoin_dict = [block.__dict__ for block in SmolCoin]

    return json.dumps(SmolCoin_dict, indent=4, default=datetime_serializer)


node.run()
