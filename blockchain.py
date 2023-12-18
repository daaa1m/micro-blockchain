import hashlib as hasher
from datetime import datetime
from typing import TypedDict


class TxnData(TypedDict):
    sender: str
    recipient: str
    amount: int


class BlockData(TypedDict):
    proof: int
    transactions: list[TxnData]


class Block:
    def __init__(
        self, index: int, time_stamp: datetime, data: BlockData, prior_hash: str
    ) -> None:
        self.index = index
        self.time_stamp = time_stamp
        self.data = data
        self.prior_hash = prior_hash
        self.hash = self.hash_block()

    def data_to_str(self) -> str:
        return ", ".join(f"{value}" for value in self.data.items())

    def hash_block(self) -> str:
        def data_to_str(self) -> str:
            return ", ".join(f"{value}" for value in self.data.items())

        data_as_str = data_to_str(self)

        phrase = (
            str(self.index) + str(self.time_stamp) + data_as_str + str(self.prior_hash)
        )
        sha = hasher.sha256()
        sha.update(phrase.encode())

        return sha.hexdigest()


def create_genesis_block() -> Block:
    genesis_transactions = [TxnData(sender="NSA", recipient="satoshi", amount=1)]
    genesis_data = BlockData(proof=7, transactions=genesis_transactions)
    return Block(0, datetime.now(), genesis_data, "")


def proof_of_work(prior_proof: int) -> int:
    incrementor = prior_proof + 1

    # keep incrementing until the incrementor is divisible by 7 and prior proof
    while not (incrementor % 7 == 0 and incrementor % prior_proof == 0):
        incrementor += 1

    return incrementor


def create_next_block(
    last_block: Block, next_proof: int, updated_txns: list[TxnData]
) -> Block:
    new_data = BlockData(proof=next_proof, transactions=updated_txns)

    return Block(last_block.index + 1, datetime.now(), new_data, last_block.hash)
