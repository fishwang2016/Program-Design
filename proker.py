def poker(hands):

    "Return the best hand: pokder([hand,...]) = > hand"

    return allmax(hands, key = hand_rank)
# similar to max([1,-3,2],key = abs)

def allmax(iterable, key = None):
       "Return a list of all items equal to the max of the iterable."
       result = []
       maxval = None
       
       for hand in iterable:
           xval = key(hand)
       
           if not result or  xval > maxval:
               maxval = xval
               result =[]
               result.append(hand)
           elif xval == maxval:
               result.append(hand)
               
       return result
               
           
      

    

def hand_rank(hand):
    
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    
    if straight(ranks) and flush(hand):
        return (8,max(ranks))
    elif kind(4,ranks):
        return (7, kind(4,ranks),kind(1,ranks))
    elif kind(3,ranks) and kind(2,ranks):
        return (6,kind(3,ranks),kind(2,ranks))
    elif flush(hand):
        return (5,ranks)
    elif straight(ranks):
        return (4,max(ranks))
    elif kind(3,ranks):
        return (3,kind(3,ranks),ranks)
    elif two_pair(ranks):
        return (2,two_pair(ranks),ranks)
    elif kind(2,ranks):
        return (1,kind(2,ranks),ranks)
    else: 
        return (0, ranks)
        
def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    
    
    ranks =['--23456789TJQKA'.index(r) for r, s in cards] # amazing !!!
    ranks.sort(reverse = True)
    
    if ranks ==[14,5,4,3,2]:
        ranks = [5,4,3,2,1]
            
    return ranks
     
def straight(ranks):
     "Return True if th eordered ranks from a 5-card straight"
     
     return (max(ranks)-min(ranks) == 4 ) and (len(set(ranks))== 5)
     
def flush(hand):
    
    "Return True if all the cards have the same suit."
    suits =[s for r, s in hand]
    return len(set(suits)) == 1 # Excellent use of set
    
    

    
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # Your code here.
    for r in ranks:
        if ranks.count(r) == n: return r
            
    return None
    
def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    a =[]
    for r in ranks:
        if ranks.count(r) == 2:
            a.append(r)
      
    a = list(set(a))
    if len(a) ==2:
        
        a = list(a)
        a.sort(reverse = True)
        
        return tuple(a)
        
    else :
        return None
        

    

def test():
    
    "Test cases for the function in poker program"
    
    sf = "6C 7C 8C 9C TC".split() #straight flush
    fk ="9D 9H 9S 9C 7D".split() #  four of a kind
    fh = "TD TC TH 7C 7D".split() # full house
    tp = "5D 5D 9H 9C 6S".split()
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    assert straight(card_ranks(al)) == True 
    
    assert kind(4,fkranks) == 9
    assert kind(3,fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1,fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) ==(9,5)
    
    assert straight([9,8,7,6,5]) == True
    assert straight([9,8,8,6,5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    
    assert card_ranks(sf) == [10,9,8,7,6]
    assert card_ranks(fk) == [9,9,9,9,7]
    assert card_ranks(fh) == [10,10,10,7,7]
    
    assert poker([sf,fk,fh])== [sf]
    assert poker([fk,fh])== [fk]
    assert poker([fh,fh]) == [fh,fh]
    assert poker([sf]) == [sf]
    assert poker([sf]+99*[fh]) == [sf]
    
    # check return value
    assert hand_rank(sf) == (8,10)
    assert hand_rank(fk) == (7,9,7)
    assert hand_rank(fh) ==(6,10,7)
    
    print "tests pass"
    
    return "tests pass"
if __name__ =="__main__":
    test()