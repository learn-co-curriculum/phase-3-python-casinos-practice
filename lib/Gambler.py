class Gambler:
    
   def __init__(self,name,gambler_type):
      self.name=name
      self.gambler_type=gambler_type

   @property
   def name(self):
      return self._name
   
   @name.setter
   def name(self,name):
      if(hasattr(self,"name") or not type(name)==str):
         raise ValueError("Name must be a string and cannot be changed")
      self._name=name

   @property
   def gambler_type(self):
      return self._gambler_type
   
   @gambler_type.setter
   def gambler_type(self,gambler_type):
      if(not(type(gambler_type)==str and (gambler_type=="light" or gambler_type=="moderate" or gambler_type=="heavy"))):
         raise ValueError("Gambler type must be a string and must be light,moderate, or heavy")
      self._gambler_type=gambler_type

   def bids(self):
      from lib.Bid import Bid
      return [bid for bid in Bid.all if bid.gambler==self]

   def dealers(self):
      return list(set([bid.dealer for bid in self.bids()]))
   
   def make_bid(self,dealer,amount):
      from lib.Bid import Bid
      Bid(self,dealer,amount)

   def average_bid_amount(self,dealer):
      bid_amounts=[bid.amount for bid in self.bids() if bid.dealer==dealer]
      if(len(bid_amounts)==0): return 0
      return sum(bid_amounts)/len(bid_amounts)
   
   def highest_dealer(self):
      return max(self.dealers(),key=lambda dealer: sum(dealer.bid_amounts())/len(dealer.bid_amounts()))

      # max=0
      # max_dealer=None
      # for dealer in self.dealers():
      #    avg=self.average_bid_amount(dealer)
      #    if(avg>max):
      #       max=avg
      #       max_dealer=dealer
      # return max_dealer
