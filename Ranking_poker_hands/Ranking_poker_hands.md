# Ranking Poker Hands
Create a poker hand that has a method to compare itself to another pokerhand:

```python
compare_with(self, other_hand)
```
 A poker hand has a constructor that accepts a string containing 5 cards:

`PokerHand("KS 2H 5C JD TD")`

The characterisctic of the string of cards are:
- Each card consists of two characters:
    - the 1st character is the value of the card: `2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)`
    - the 2nd character represents the suit: `S(pades), H(earts), D(iamonds), C(lubs)`
- A space is used as card separator between cards

The result of your poker hand compare can be one of these 3 options: <br>
`['Win', 'Tie', 'Loss']` <br>

## Notes
- Apply Texas Hold'em rules for ranking the cards.
- Low aces are not valid in this kata
- There is no ranking for the suits

A hand consists of **5** cards and are ranked from lowest to highest, in the following
way:
- **High card**: Highest value card.
- **One pair**: Two cards of the same value.
- **Two pairs** Two different pairs.
- **Three of a Kind**: Three cards of the same value.
- **Straight**: All cards are consecutive values.
- **Flush**: All cards of the same suit.
- **Full House**: Three of a kind and a pair.
- **Four of a kind**: Four cards of the same value.
- **Straight Flush**: All cards are consecutive values of the same suit
- **Royal Flush**: Ten, Jack, Queen, King, Ace, in same suit.

If two players have the same ranked hands then the rank made up of the highest values wins;
But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hands are compared; if the highest cards tie then the next highest cards are compared, and so on.

## Algorithm
1. Estimate combination of **player1** and **player2**; <br>
1. if **player1** and **player2** combinations are equal: <br>
- if it is `'Royal flush`: return `'Tie'`
- else:
    - sum the value indices of combination cards:
        - if `player1.sum > player2.sum`: return `'Win'`
        - if `player1.sum < player2.sum`: return `'Lose'`
        - else: compare highest **non-combinational** card <br>
        if they are equal: `move to the next card` etc.
3. if **player1** combination > **player2** combination: return `'Win'` <br>
else: return `'Lose'`.








