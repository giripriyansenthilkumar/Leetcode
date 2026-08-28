from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.comb=list(combinations(characters,combinationLength))
        self.i=0

    def next(self) -> str:
        # print(self.comb)
        if self.i<len(self.comb):
            curr=self.comb[self.i]
            self.i+=1
            return ''.join(curr)

    def hasNext(self) -> bool:
        if self.i<len(self.comb):
            return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()