from bs4 import BeautifulSoup
import requests
import re
import os
import csv
import unittest


def get_titles_from_search_results(filename):
    """
    Write a function that creates a BeautifulSoup object on "search_results.htm". Parse
    through the object and return a list of tuples containing book titles (as printed on the Goodreads website) 
    and authors in the format given below. Make sure to strip() any newlines from the book titles and author names.

    [('Book title 1', 'Author 1'), ('Book title 2', 'Author 2')...]
    """
    source_dir = os.path.dirname(__file__)
    url = os.path.join(source_dir, filename)
    #page = requests.get(url)
    with open(url, 'r') as f:
        content = f.read()
    #if page.ok:
       # soup = BeautifulSoup(page.content,'html.parser')
    soup = BeautifulSoup(content,'html.parser')
    #dictionary = {}
    tags = soup.find('div', {'class': 'mainContentFloat'})
    x = tags.find_all('a', {'class': 'bookTitle'})
    y = tags.find_all('a', {'class': 'authorName'})

    titles_lst = []
    authors_lst = []
    for title in titles:
        titles_lst.append(title.text.strip())
    for author in authors:
        authors_lst.append(author.text.strip())
    tuple_lst = []
    for i in range(len(titles_lst)):
        tuple_lst.append((titles_list[i], authors_lst[i]))
    return tuple_lst
    

    #pass


def get_search_links():
    """
    Write a function that creates a BeautifulSoup object after retrieving content from
    "https://www.goodreads.com/search?q=fantasy&qid=NwUsLiA2Nc". Parse through the object and return a list of
    URLs for each of the first ten books in the search using the following format:

    ['https://www.goodreads.com/book/show/84136.Fantasy_Lover?from_search=true&from_srp=true&qid=NwUsLiA2Nc&rank=1', ...]

    Notice that you should ONLY add URLs that start with "https://www.goodreads.com/book/show/" to 
    your list, and , and be sure to append the full path to the URL so that the url is in the format 
    “https://www.goodreads.com/book/show/kdkd".

    """

    r = requests.get('https://www.goodreads.com/search?q=fantasy&qid=NwUsLiA2Nc')
    soup = BeautifulSoup(r.text, 'html.parser')
    book_list = soup.find_all('a', class_ = 'bookTitle')

    lst = []

    for i in book_list[:10]:
        link = i['href']
        if link.startswith('/book/show/'):
            lst.append('https://www.goodreads.com' + str(link))
    return lst

    #pass


def get_book_summary(book_url):
    """
    Write a function that creates a BeautifulSoup object that extracts book
    information from a book's webpage, given the URL of the book. Parse through
    the BeautifulSoup object, and capture the book title, book author, and number 
    of pages. This function should return a tuple in the following format:

    ('Some book title', 'the book's author', number of pages)

    HINT: Using BeautifulSoup's find() method may help you here.
    You can easily capture CSS selectors with your browser's inspector window.
    Make sure to strip() any newlines from the book title and number of pages.
    """

    #pass

    resp = requests.get(book_url)
    soup = BeautifulSoup(resp.content, 'html.parser')

    title = soup.find('h1', id = 'bookTitle')
    author = soup.find('a', class_ = 'authorName')
    pages = soup.find('span', itemprop = 'numberOfPages')

    nums = '0123456789'
    num = ''
    for char in pages.text.strip():
        if char in nums:
            num += char
    int_num = int(num)

    return (title.text.strip(), author.text.strip(), int_num)

def summarize_best_books(filepath):
    """
    Write a function to get a list of categories, book title and URLs from the "BEST BOOKS OF 2020"
    page in "best_books_2020.htm". This function should create a BeautifulSoup object from a 
    filepath and return a list of (category, book title, URL) tuples.
    
    For example, if the best book in category "Fiction" is "The Testaments (The Handmaid's Tale, #2)", with URL
    https://www.goodreads.com/choiceawards/best-fiction-books-2020, then you should append 
    ("Fiction", "The Testaments (The Handmaid's Tale, #2)", "https://www.goodreads.com/choiceawards/best-fiction-books-2020") 
    to your list of tuples.
    """
    #pass
    with open(filepath) as f:
        content = f.read()
    #if page.ok:
       # soup = BeautifulSoup(page.content,'html.parser')
    soup = BeautifulSoup(content,'html.parser')

    tags = soup.find('div', {'class': 'clearFix'})
    
    x = tags.find('div', {'category': 'clearFix'})

    for item in x:

        genre = item.find('h4', class_ = 'category__copy')
        title = item.find('div', {'class': 'category__winerImageContainer'})
        url = item.find('a', item[href]) #how do you extract this 
    tup = (genre, title, url)
    return tup 

    




   tags = soup.find_all('table', {'class': 'data-table'})[2]
    #print(tags)
    x = tags.find_all('td', {'class':'cell-name'})
    #print(x)
    for item in x:
        k = item.find('a', {'class': 'ent-name'}).text.strip()
        lst.append(k)
    print(lst)
    return lst


def write_csv(data, filename):
    """
    Write a function that takes in a list of tuples (called data, i.e. the
    one that is returned by get_titles_from_search_results()), writes the data to a 
    csv file, and saves it to the passed filename.

    The first row of the csv should contain "Book Title" and "Author Name", and
    respectively as column headers. For each tuple in data, write a new
    row to the csv, placing each element of the tuple in the correct column.

    When you are done your CSV file should look like this:

    Book title,Author Name
    Book1,Author1
    Book2,Author2
    Book3,Author3
    ......

    This function should not return anything.
    """
    pass


def extra_credit(filepath):
    """
    EXTRA CREDIT

    Please see the instructions document for more information on how to complete this function.
    You do not have to write test cases for this function.
    """
    pass

class TestCases(unittest.TestCase):

    # call get_search_links() and save it to a static variable: search_urls
    search_urls = get_search_links()


    def test_get_titles_from_search_results(self):
        # call get_titles_from_search_results() on search_results.htm and save to a local variable
        list_books = get_titles_from_search_results('search_results.htm')

        # check that the number of titles extracted is correct (20 titles)
        self.assertEqual(len(list_books), 20)

        # check that the variable you saved after calling the function is a list
        self.assertTrue(type(list_books), list)

        # check that each item in the list is a tuple
        for item in list_books:
            self.assertTrue(type(item), tuple)

        # check that the first book and author tuple is correct (open search_results.htm and find it)
        self.assertEqual(list_books[0], ('Harry Potter and the Dealthy Hollows (Harry Potter, #7)', 'JK Rowling'))

        # check that the last title is correct (open search_results.htm and find it)
        self.assertEqual(list_books[-1], ('Harry Potter: The Prequel (Harry Potter, #0.5)', 'Julian Harrison'))
        self.assertEqual(list_books[19][0], ('Harry Potter: The Prequel (Harry Potter, #0.5)'))

    def test_get_search_links(self):
        # check that TestCases.search_urls is a list
        self.assertEqual(type(TestCases.search_urls), list)
        # check that the length of TestCases.search_urls is correct (10 URLs)
        self.assertEqual(len(TestCases.search_urls), 10)

        # check that each URL in the TestCases.search_urls is a string
        for item in TestCases.search_urls:
            self.assertTrue(type(item), str)
        # check that each URL contains the correct url for Goodreads.com followed by /book/show/
            #DO THIS 

    def test_get_book_summary(self):
        # create a local variable – summaries – a list containing the results from get_book_summary()
        # for each URL in TestCases.search_urls (should be a list of tuples)

        # check that the number of book summaries is correct (10)

            # check that each item in the list is a tuple

            # check that each tuple has 3 elements

            # check that the first two elements in the tuple are string

            # check that the third element in the tuple, i.e. pages is an int

            # check that the first book in the search has 337 pages


    def test_summarize_best_books(self):
        # call summarize_best_books and save it to a variable

        # check that we have the right number of best books (20)

            # assert each item in the list of best books is a tuple

            # check that each tuple has a length of 3

        # check that the first tuple is made up of the following 3 strings:'Fiction', "The Midnight Library", 'https://www.goodreads.com/choiceawards/best-fiction-books-2020'

        # check that the last tuple is made up of the following 3 strings: 'Picture Books', 'A Beautiful Day in the Neighborhood: The Poetry of Mister Rogers', 'https://www.goodreads.com/choiceawards/best-picture-books-2020'


    def test_write_csv(self):
        # call get_titles_from_search_results on search_results.htm and save the result to a variable

        # call write csv on the variable you saved and 'test.csv'

        # read in the csv that you wrote (create a variable csv_lines - a list containing all the lines in the csv you just wrote to above)


        # check that there are 21 lines in the csv

        # check that the header row is correct

        # check that the next row is 'Harry Potter and the Deathly Hallows (Harry Potter, #7)', 'J.K. Rowling'

        # check that the last row is 'Harry Potter: The Prequel (Harry Potter, #0.5)', 'Julian Harrison (Introduction)'



if __name__ == '__main__':
    print(extra_credit("extra_credit.htm"))
    unittest.main(verbosity=2)



