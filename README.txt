This project was created by Stephen Hayden April 2020 to aid in the migration between LibraryThing and LibraryWorld 
for the Tanner Library, part of the depeartment of Philosophy at the University of Michigan. 

The ultimate goal was to create a list of items with multiple authors, a common case which did not migrate properly
as part of the exported MARC from LibraryThing. 

(1)

Step one was to use "lib_thing_scrape.py" to compile the urls of each item in the LibraryThing catalog.
This step required Selenium to scrape through 

https://www.librarything.com/catalog_bottom.php?view=UMPhilosophy&offset=0

as beautiful soup was only capable of returning the first page out of the 155 needed to return all links.
These links were then written into "catalog_page_urls.txt"

(2)
That file was then read into "get_item_urls.py," which took each of those urls looked through each item for a link
within each page to the "details" page, which could then be used later. Those details pages were then written to
"work_details_urls.txt"


(3)
Then, that file was read into "get_item_details.py," which looked through the "book details" page for each item and
gathered the book's title, author, other authors, publication date, and call number, then wrote each of those details
into a dictionary and then appended that to a list which was then used to write three different json files pending
the item's conditionals. One file was made containing the details of all 7,717 items, one list was created if and
only if the item had multiple authors, and a third list was created if the item, for whatever reason, did not have a
call number attached to it. These files were then used to cross reference when correcting by hand the new LibraryWorld
Catalog.



 
