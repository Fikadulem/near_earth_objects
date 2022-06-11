"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(filename="/Users/fikadu.balcha/Training/near_earth_objects/workspace/data/neos.csv"):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    neos = []
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        for line in reader:
            neos.append(line)
        #lens = len(neos)
        #print(lens)
        print(f"There are {len(neos)} rows in this file")
        print(header)
        #print(neos)
        #filename.close()
   # TO DO: add
    #return neos
load_neos()


def load_approaches(filename="C://Training//Udacity//project//workspace//data//cad.json"):
    """Read close approach data from a JSON file.
    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:

            return approaches

    approaches
    # TODO: Load close approach data from the given JSON file.
    # return ()
