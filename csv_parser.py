import csv
from python2Try.firebase_database import write_book_data

with open('BX-Books.csv', newline='') as csvfile: # Change here the wanted csv.
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    data = {}
    
    for id, row in enumerate(spamreader):
        if id == 10:
            break
        
        write_book_data(book_id=..., image_url=..., book_name=...)
        
        print(row)