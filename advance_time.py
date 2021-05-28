# Not finished yet..


import argparse
import dates
from datetime import date, timedelta, datetime
import csv
import os
import arguments


# Set an advanced date as perceived as today
def advance_date(args):
    with open("day.csv", "w") as input, open("days.csv", "r") as output:
        day_reader = csv.reader(output)
        day_writer = csv.writer(input)
        is_Added = True

        for line in day_writer:
            if args.advance == None:
                new_date = [date]
                is_Added = True
                writer.writerow(day_reader)