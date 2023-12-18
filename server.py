from typing import List, TypedDict

from flask import Flask, request


class TxnData(TypedDict):
    sender: str
    recipient: str
    amount: int


node = Flask(__name__)  # creating a new Flask class called node

# this node stores a list of txns
this_node_txns: List[TypedDict] = []


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


node.run()
