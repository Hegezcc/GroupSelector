# GroupSelector

A small command line program to group input file to small batches, possibly by also randomizing entries.

    usage: main.py [-h] [-s SIZE] [-d DELIMITER] [-r] [-o OUTPUT]
                   [files [files ...]]

    Group given input file(s) with given group size and delimiter

    positional arguments:
      files                 input file, default is standard input

    optional arguments:
      -h, --help            show this help message and exit
      -s SIZE, --size SIZE  set group size, default is 3
      -d DELIMITER, --delimiter DELIMITER
                            group delimiter, default is empty string
      -r, --randomize       randomize entries before grouping them
      -o OUTPUT, --output OUTPUT
                            set output file, default is standard output
