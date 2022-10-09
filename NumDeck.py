import array
import random

class NumDeck:
    """ Number Deck from 1 ~ MaxNum """
    def __init__(self, _size) -> None:
        self.Size = _size
        self.NumArray = array.array('i', (i for i in range(1, _size+1)))

    def suffleDeck(self) -> None:
        random.shuffle(self.NumArray)
    
    def printDeck(self) -> None:
        for i in range(self.Size) :
            print("(", i, ",", self.NumArray[i], end = ') ', sep = '')
            if ((i+1) % 20 == 0):
                print()
        print("----------------")
    
    def seekNumber(self, tgt_num) -> bool:
        return self._seekNumber(tgt_num, tgt_num-1, self.Size / 2)

    def _seekNumber(self, tgt_num, arr_idx, ttl) -> bool :
        # print("seekNumber {} in {}, ttl: {}".format(tgt_num, arr_idx, ttl))
        if (ttl <= 0):
            return False
        else:
            if (self.NumArray[arr_idx] == tgt_num):
                return True
            else:
                return self._seekNumber(tgt_num, self.NumArray[arr_idx]-1, ttl-1)
