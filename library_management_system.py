class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        
    def adding_book(self,title,author,copies):
        book = {"title":title,"author":author,"avaiable_copies":copies,"copies":copies}
        self.books.append(book)
        print(f"{title} book has been added to library successfully!!")
        
    def display_book(self):
        if self.books:
            print("Book Details")
            for book in self.books:
                print(f"The Book Title: {book['title']} | Author: {book['author']} | Available Copies: {book['avaiable_copies']}")
        else:
            print("No book Available!!")
            
    #helper function
    def find_book(self,title):
        if self.books:
            for book in self.books:
                if book['title'].lower() == title.lower():
                    return book
        return None
    def barrow_book(self,title):
        book = self.find_book(title)
        
        if book is not None:
            if book['avaiable_copies'] != 0:
                book['avaiable_copies']-=1
                print(f"{title} book has been barrrowed succesfully!!")
            else:
                print("Book out of stock!!")
        else:
            print(f"{title} book is not avaialble in library!!")
            
    def returning_book(self,title):
        book = self.find_book(title)
        if book is not None:
            if book['avaiable_copies'] != book['copies']:
                book['avaiable_copies'] += 1
                print(f"{title} book has been return successfully!!")
            else:
                print(f"{title} book not belongs to the library")
        else:
            print("The book is not available")            
        
l = LibraryManagementSystem()
l.adding_book("Algorithm","Alen",2)
# l.display_book()
# l.barrow_book('Algorithm')
# l.display_book()
# l.barrow_book('Algorithm')
# l.display_book()

# l.returning_book('Algorithm')
# l.display_book()
# l.returning_book('Algorithm')
# # l.display_book()


# l.barrow_book('ML_learning')
l.adding_book('ML_Learning','CoderAlen',5)
l.display_book()

l.barrow_book('ml_learning')
l.display_book()
l.barrow_book('ml_learning')
l.display_book()
l.barrow_book('ml_learning')
l.display_book()

l.barrow_book('ml_learning')
l.display_book()

l.barrow_book('ml_learning')
l.display_book()

l.barrow_book('ml_learning')
l.display_book()



