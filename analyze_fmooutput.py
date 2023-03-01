# Author: Roshan Mammen Regy
# Email ID: roshanm.regy@gmail.com
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--fmooutput",required=True,help="Output log from GAMESS FMO",type=str)
parser.add_argument("--fmoinput",required=True,help="GAMESS FMO input file",type=str)
parser.add_argument("--output",required=False,help="Output file name",default='PIEDAoutput',type=str)
args = parser.parse_args()
import concurrent.futures
import numpy as np 
import re
import json
from fmofile_parser import *
from fmo_classes import * 
from helper_functions import *


outputlines = open(args.fmooutput).readlines()
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = []
    outputvalues = {}
    for lno, line in enumerate(outputlines):
        result = output_parser(line, lno)
        if result!=None:
            outputvalues[result[-1]] = result[:-1]


inputlines = open(args.fmoinput).readlines()
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = []
    inputvalues = {}
    for lno,line in enumerate(inputlines):
        result = input_parser(line,lno)
        if result != None:
            inputvalues[result[-1]] = result[:-1]


fragments = get_frag_stats(outputvalues['Fragment statistics'][0],outputlines)
fragments = add_atoms2frags(fragments, inputvalues['INDAT'][0],inputlines)
dimers = get_dimer_data(outputvalues["Two-body FMO properties"][0],outputlines,fragments)
fragments_to_csv(fragments)
dimers_to_csv(dimers)
