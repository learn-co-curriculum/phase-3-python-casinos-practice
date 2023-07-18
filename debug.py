#!/usr/bin/env python3
import ipdb;

from lib.Gambler import Gambler
from lib.Dealer import Dealer
from lib.Bid import Bid


if __name__ == '__main__':
    print("Testing....")
    
    #gamblers
    maurice=Gambler("Maurice","heavy")
    sam=Gambler("Sam","light")
    
    #dealers
    bob=Dealer("Bob")
    steve=Dealer("Steve")

    #bids
    maurice.make_bid(bob,200)
    maurice.make_bid(steve,200)
    maurice.make_bid(steve,200)
    sam.make_bid(bob,10)

    print(maurice.highest_dealer())



    ipdb.set_trace()
