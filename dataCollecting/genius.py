import lyricsgenius as lg
from scraper import *

clientAccess = '2zKmiJ6oqawQGviEFgOm5adOGUn8d9ohY6axrCyV_jLpSW-rHSy7QOGFji5nR150cDr-xLEkdMzDMLZSm0_HJA'
genius = lg.Genius(clientAccess, 
                    skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                    remove_section_headers=True)

artists = getArtists()
