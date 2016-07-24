def poker(hands):

    "Return the best hand: pokder([hand,...]) = > hand"

    return max(hands, key = hand_rank)
# similar to max([1,-3,2],key = abs)

def hand_rank(hand):

    return None 
