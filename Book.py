class Book :
    def __init__(self,title,author,numberOfPages):
        self.title = ""
        self.author = ""
        self.numberOfPages = 0

# TODO Step 1 - instantiate an object of class Book and assign it to a variable named myBook

myBook=Book("","",0)
# TODO Step 2 - assign a value to the title, author and numberOfPages fields of your object.
myBook.title="Harry Potter"
myBook.author="J.K.Rowling"
myBook.numberOfPages=550

# Print the values
print("The title of the book is ", myBook.title, "\nIts author is",
      myBook.author, "\nIt contains ", myBook.numberOfPages)
