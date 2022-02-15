"""
Given two different positions on a chess board, find the least number of moves it would take a knight 
to get from one to the other. The positions will be passed as two arguments in algebraic notation. 
For example, knight("a3", "b5") should return 1.


- Convert input
- Calculate shortest path length
- Output shortest path (positive integer)


array row -     chessboard row
0         -     8
1         -     7
2         -     6
3         -     5
4         -     4
5         -     3
6         -     2
7         -     1

we want to map any given chessboard row number onto its corresponding array row number (ideally with some simple expression)

1 - 8 = -7
|1 - 8| = 7

array_row = abs(chessboard_row - 8)

"""


def convert_input(location, destination):
    print("convert_input() called")
    # Array[location[0]][location[1]]
    loc_r = abs(8 - int(location[1]))
    loc_c = ord(location[0]) - 97 # returns numbered place of a given letter in the alphabet. Alphabet letters start at element 97 in Unicode, minus one more for array indexing
    print(loc_r)
    print(loc_c)

    dest_r = abs(8 - int(destination[1]))
    dest_c = ord(destination[0]) - 97
    print(dest_r)
    print(dest_c)

def find_shortest_path():
    print("find_shortest_path() called")

def output_shortest_path():
    print("output_shortest_path() called")

convert_input("a3", "b5")