import hashlib
from typing import List
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Block(): # no inheritence
    shares: str
    buyer_id: int
    seller_id: int
    trade_time: str=datetime.utcnow().strftime('%H:%M:%S')
    prev_hash: str='0'
    
    def hash_block(self): 
        sha=hashlib.sha256()
        trade_time_encoded=self.trade_time.encode()
        sha.update(trade_time_encoded)
        sha.update(str(self.shares).encode())
        sha.update(self.prev_hash.encode())
        return sha.hexdigest()
    
@dataclass
class StockChain(): 
    chain: List[Block]
        
    def add_block(self, block): 
        self.chain+=[block]