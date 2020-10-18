"""
Get The English Only Lyrics

This script is used to get the English only lyrics from the two Eurovision lyric files
by getting the intersection between the two files.

This script requires eurovision-en.txt and eurovision-full.txt 
"""

with open('compareData/eurovision-en.txt', 'r') as file1:
    with open('compareData/eurovision-full.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('intersection.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

