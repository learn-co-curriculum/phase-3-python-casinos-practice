class Dealer:

    all=[]

    def __init__(self,name):
        self.name=name
        Dealer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if(hasattr(self,"name") or not type(name)==str):
            raise ValueError("Name must be a string and cannot be changed")
        self._name=name

    def bids(self):
      from lib.Bid import Bid
      return [bid for bid in Bid.all if bid.dealer==self]

    def gamblers(self):
        return list(set([bid.gambler for bid in self.bids()]))
    
    def bid_amounts(self):
        return list(set([bid.amount for bid in self.bids()]))
    
    def gambler_types(self):
        return [gambler.gambler_type for gambler in self.gamblers()]

    def average_bid_amount(self,gambler):
      bid_amounts=[bid.amount for bid in self.bids() if bid.gambler==gambler]
      if(len(bid_amounts)==0): return 0
      return sum(bid_amounts)/len(bid_amounts)
   
    def highest_gambler(self):
      max=0
      max_gambler=None
      for gambler in self.gamblers():
         avg=self.average_bid_amount(gambler)
         if(avg>max):
            max=avg
            max_gambler=gambler
      return max_gambler


