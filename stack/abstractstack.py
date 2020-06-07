
from stack.abstractcollection import AbstrackCollection

class AbstrackStack(AbstrackCollection):
    def __init__(self, sourceCollection):
        AbstrackCollection.__init__(self, sourceCollection)


    def add(self, item):
        self.push(item)
