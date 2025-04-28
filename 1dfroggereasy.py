"""
Frogger is a classic 2-D video game that challenges the player to move a frog character safely across a traffic-filled road and a hazardous river. What is not well known is that Frogger actually began as a prototype board game based on a 2-D concept at a now-defunct toy company.¹ After spending millions of dollars following the advice of consultants, company executives realized that the resulting game was almost completely deterministic, and therefore not much fun to play,² so they sold all Frogger rights to a video game company in an attempt to recoup some of the development costs. The rest, as they say, is video game history.

The original 2-D Frogger design, however, makes for good programming competition problems. Here is how the game works: The board is a row of n squares, each of which contains a non-zero integer. These squares are indexed 1 to n, from left to right. To start the game, the player rolls an n-sided die with one of the distinct indices on each side and places a frog token on the board square with the resulting index. The player then randomly selects a card from a deck of cards with integers written on them (one per card); the integer on each card is contained in at least one board square. The number on the selected card is the magic number (or goal number) for this instance of the game.

The player then applies the following rule as many times as necessary until the game ends: If the frog is on a square containing a positive integer x, the frog makes a length-x hop to the right. (Hop distance is measured in board square units.) If the frog is on a square containing a negative integer x, the frog makes a length-|x| hop to the left (note the absolute value).

The game ends as soon as the frog encounters one of the following four fates:

The frog lands on a square containing the magic number. This is the only winning outcome for the player. Note that if the frog starts on a square containing the magic number, the player wins immediately (i.e., after 0 hops).

The frog falls off the left end of the board.

The frog falls off the right end of the board.

The frog hops onto a square where the frog has been before, and therefore is trapped in a cycle.

Let h be the number of hops the frog makes before the game ends. Given an instance of the game, your task is to determine the frog’s fate and the corresponding value of h.

Input:
The first line of input contains three space-separated integers, n, startIndex, and magicNumber, where n is the number of board squares, startIndex is the index of the frog’s starting square, and magicNumber is the magic number. This is followed by a line containing n space-separated non-zero integers. These are the numbers in the board squares in order from left to right. Each board square number is in the interval [-10⁹, 10⁹], and the magic number is guaranteed to be one of the board square numbers.

Output:
Output two lines. The first line contains a word indicating the fate of the frog, one of ‘magic’, ‘left’, ‘right’, ‘cycle’, corresponding to the four fates listed above, respectively. The second line contains the integer h, the number of hops the frog makes before encountering its fate.

Sample Input 1:
6 4 42
-9 1 42 -2 -3 -3

Sample Output 1:
magic
2

Sample Input 2:
8 2 13
7 5 4 2 13 -2 -3 6

Sample Output 2:
cycle
4
"""

n, startIdx, magicNum = map(int, input().split())
board = list(map(int, input().split()))
pos = startIdx

if board[pos - 1] == magicNum:
    print("magic")
    print(0)
    exit()

visited = {pos}
hops = 0

while True:
    val = board[pos - 1]
    newPos = pos + val
    hops += 1

    if newPos < 1:
        print("left")
        print(hops)
        break

    if newPos > n:
        print("right")
        print(hops)
        break

    if board[newPos - 1] == magicNum:
        print("magic")
        print(hops)
        break

    if newPos in visited:
        print("cycle")
        print(hops)
        break

    visited.add(newPos)
    pos = newPos
