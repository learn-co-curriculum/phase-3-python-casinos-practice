class Bid:

    all=[]

    def __init__(self,gambler,dealer,amount):
        self.gambler=gambler
        self.dealer=dealer
        self.amount=amount
        self.all.append(self)

    @property
    def gambler(self):
        return self._gambler
    
    @gambler.setter
    def gambler(self,gambler):
        from lib.Gambler import Gambler
        if(type(gambler)!=Gambler):
            raise ValueError("Gambler must be a Gambler instance")
        self._gambler=gambler

    @property
    def dealer(self):
        return self._dealer
    
    @dealer.setter
    def dealer(self,dealer):
        from lib.Dealer import Dealer
        if(type(dealer)!=Dealer):
            raise ValueError("Dealer must be a Dealer instance")
        self._dealer=dealer

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self,amount):
        if(not(type(amount) in (int,float) and amount>0)):
            raise ValueError("Amount must be an integer or float greater than 0")
        self._amount=amount