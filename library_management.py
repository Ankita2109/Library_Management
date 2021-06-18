import sys
class Library:
	''' CLass for managing the library'''
      def __init__(self,listofbooks):
      	'''  method containing the list of all books'''
            self.availablebooks=listofbooks

      def addNewBook(self):
      	'''add new book in the library '''
      	newBook = input("Enter the name of the new book you want to add: ")
      	self.availablebooks.append(newBook)
      	print("The following new book has been added in the library : "+newBook)

      def displayAvailablebooks(self):
      	'''display all the available book '''
                   print("The books we have in our library are as follows:")
                   print("================================")
                   for book in self.availablebooks:
                         print(book)

      def lendBook(self,requestedBook):
      	''' it lends the book from the library'''
            if requestedBook in self.availablebooks:
                  print("The book you requested has now been borrowed")
                  self.availablebooks.remove(requestedBook)
            else:
                  print("Sorry the book you have requested is currently not in the library")
                  
      def returnTheBook(self,returnedBook):
      	''' return the book in the library '''
            self.availablebooks.append(returnedBook)
            print("Thanks for returning your borrowed book")



class Student:
'''deals with the student queries'''
      def requestBook(self):
      	''' student can request the book '''
            print("Enter the name of the book you'd like to borrow>>")
            self.book=input()
            return self.book

      def returnBook(self):
      	'''student can return the book '''
            print("Enter the name of the book you'd like to return>>")
            self.book=input()
            return self.book

def main():            
      library=Library(["The Nightangle","The Last Battle","The Screwtape letters","The Great Divorce"])
      student=Student()
      done=False
      while done==False:
            print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Add New Book
                  5. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        library.displayAvailablebooks()
            elif choice==2:
                        library.lendBook(student.requestBook())
            elif choice==3:
                        library.returnTheBook(student.returnBook())
            elif choice ==4:
            			library.addNewBook()
            elif choice==5:
                  sys.exit()
                  
main()