#!/usr/bin/env python3

import sys

def fail():
    print('FAIL')
    sys.exit(1)

FILE_NAME = 'seat_map.txt'
MAX_COLS = 8
MAX_ROWS = 20
SEAT_FILLED = '1'
SEAT_EMPTY = '0'

# Step 1: Initialize the seat map
seat_map = []

try:
    with open(FILE_NAME, 'r') as f:
        lines  = f.readlines()
        seat_map = [list(line.strip()) for line in lines]
except:
    for _ in range(MAX_ROWS):
        seat_map.append([SEAT_EMPTY]*MAX_COLS)


# Step 2: Read and parse the command line arguments
try:
    args = sys.argv[1:]
    action = args[0]
    starting_seat = args[1]
    num_seats = int(args[2])
except:
    fail()


# Step 3: Check the validity of the starting seat
row = ord(starting_seat[0]) - 65
col = int(starting_seat[1:])
if row < 0 or row > MAX_ROWS-1 or col < 0 or col >= MAX_COLS:
    fail()


# Step 4: Perform Action
if action == 'BOOK':
    
    # Step 5: Handle multiple seat reservations
    end_col = col + num_seats - 1
    if end_col >= MAX_COLS:
        fail()
    for i in range(col, end_col+1):
        if seat_map[row][i] == SEAT_FILLED:
            fail()
    for i in range(col, end_col+1):
        seat_map[row][i] = SEAT_FILLED

elif action == 'CANCEL':
    # Step 6: Handle seat cancellations
    end_col = col + num_seats - 1
    if end_col >= MAX_COLS:
        fail()
    for i in range(col, end_col+1):
        if seat_map[row][i] == SEAT_EMPTY:
            fail()
    for i in range(col, end_col+1):
        seat_map[row][i] = SEAT_EMPTY

else:
    fail()


# Step 7: Update the state of reserved seats in the file
# with open('seat_map.txt', 'w') as f:
with open(FILE_NAME, 'w') as f:
    for row in seat_map:
        f.write(''.join([str(val) for val in row]) + '\n')

print('SUCCESS')
