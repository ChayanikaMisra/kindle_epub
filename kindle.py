import epub
import re
book  =  epub . open_epub ( 'Metamorphosis-jackson.epub' )
#from nltk import word_tokenize

data1=book.read_item('OEBPS/chapter-002-chapter-ii.html')

#print(data1)
#from epub_conversion.utils import open_book

#book1= open_book("Metamorphosis-jackson.epub")

#lines = convert_epub_to_lines(book1)


book1=  epub . open_epub ('The-Problems-of-Philosophy-LewisTheme.epub')
#item  =  book . read_item ( 'OEBPS/chapter-002-chapter-ii.html' ) 
    #if  linear :
        #print(item_id)
        ##print('Linear item ')
        #print(item . href) 
    #else : 
        ##print('Non-linear item')
        ##print(item . href) 
    # read the content 
    ##data  =  book . read_item( item )
for  item_id ,  linear  in  book1 . opf . spine . itemrefs : 
    item1  =  book1 . get_item ( item_id )
    #print(item1)
    if  linear :
        print(item_id)



print('first paragraph: \n')
        
from bs4 import BeautifulSoup as BSHTML
BS = BSHTML(data1,"html5lib")
print(BS.body.p.string)
#print(BS.body.contents[0].strip())
