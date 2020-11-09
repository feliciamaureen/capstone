"""
Export Results

This script is used call the exporting functions from words.py, bigrams.py, trigrams.py.
This script can be run on its own to run all of the other classes.

This script requires words.py, bigrams.py, trigrams.py
"""

from words import exportWordsExcel
from bigrams import exportBigramsExcel
from trigrams import exportTrigramsExcel

#export all results to excel
exportWordsExcel()
exportBigramsExcel()
exportTrigramsExcel()