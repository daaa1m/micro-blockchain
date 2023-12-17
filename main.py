import hashlib as hasher
from datetime import datetime


class Block:
    def __init__(
        self, index: int, time_stamp: datetime, data: str, prior_hash: str
    ) -> None:
        self.index = index
        self.time_stamp = time_stamp
        self.data = data
        self.prior_hash = prior_hash
        self.hash = self.hash_block()

    def hash_block(self) -> str:
        encoded_phrase = (
            str(self.index)
            + str(self.time_stamp)
            + str(self.data)
            + str(self.prior_hash)
        )
        sha = hasher.sha256()
        sha.update(bytes(encoded_phrase, "utf-8"))

        return sha.hexdigest()


def create_genesis_block() -> Block:
    return Block(0, datetime.now(), "SBF is guilty", "0")


def create_next_block(last_block: Block) -> Block:
    data = f"i am block {last_block.index + 1}"
    return Block(last_block.index + 1, datetime.now(), data, last_block.hash)


# init the blockchain
blockchain = [create_genesis_block()]
prior_block = blockchain[0]

for i in range(1, 25):
    prior_block = blockchain[i - 1]
    new_block = Block(i, datetime.now(), f"i am index number {i}", prior_block.hash)
    blockchain.append(new_block)
    print(f"Block {new_block.index} has been added to the blockchain!")
    print(f"Hash: {new_block.hash}")

# TODO create a server using Flask
