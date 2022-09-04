import hashlib
# importing this library to access function which will generate hashes

def hashGenerator(data):
    # sha256 algorithm to convert any data into 64 decimal characters
    result=hashlib.sha256(data.encode())
    #converting into hexa decimal
    return result.hexdigest()

class Block:
    def __init__(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash

# genesis block is the first blok of blockchain

class Blockchain:
    def __init__(self):
        # prev hash
        hashLast=hashGenerator('gen_last')
        # current hash
        hashStart=hashGenerator('gen_start')

        # adding values to genesis block
        genesis=Block('gen-data',hashStart,hashLast)
        # connecting this genesis block
        self.chain=[genesis]

    def add_block(self,data):
        # getting last block's hash
        prev_hash=self.chain[-1].hash
        # to generate unique hashes
        hash=hashGenerator(data+prev_hash)
        block = Block(data,hash,prev_hash)
        self.chain.append(block)


bc=Blockchain()
bc.add_block('1')
bc.add_block('2')
bc.add_block('3')

# converting this blockchain into dictionary
for block in bc.chain:
    print(block.__dict__)

    
