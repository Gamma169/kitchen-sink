# JP Flight Res System

An implementation of the JP Morgan Flight Reservation System Challenge.

## Running

Requires python3 installed

The file should be able to be run by just calling `./flight-sim.py <ARGS>` as specified.

There may be an issue in translation and marking the file as executable.  If that is the case, just run the file with the `python3` command.  Example:

```shell
python3 ./flight-sim.py BOOK A0 1
```

## Notes

Barring any execution problems as stated above, the program is implemented as required.  It runs on the file `seat_map.txt`.  The program automatically generates this file if it does not exist, and can be deleted to reset the state.

The program can book and cancel reservations for seats A0-T7.

