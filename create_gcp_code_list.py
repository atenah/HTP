# Program: create_gcp_code_list.py
#
# Version: 0.1 Initial Version
#
# This program will generate a text file containing all possible combinations 4 letter alphabetic codes
# with no repeated letters which will be used to identify a ground control point.
#
# This file can be imported into the database in order to create placeholder records for all codes.
#
#
from itertools import product
from itertools import combinations
from string import ascii_uppercase
import random
import sys

__author__ = 'mlucas'

#gcp_codes=[''.join(i) for i in product(ascii_uppercase, repeat = 4)]
gcp_codes=[''.join(i) for i in combinations(ascii_uppercase, 4)]
random.shuffle(gcp_codes)
print 'Number of codes generated ', len(gcp_codes)

index=1
with open ('gcp_file.txt','w') as f:
    for code in gcp_codes:
        print>>f,index,',',code
        index+=1

sys.exit()
