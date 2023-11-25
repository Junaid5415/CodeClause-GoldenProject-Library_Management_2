import datetime  # Used to get time details of issue of books


class LMS:  # Using OOPS concept here by making a class
    def __init__(self, list_books, library_name):  # Initializing some instances
        self.list_books = list_books
        self.library_name = library_name
        self.book_dic = {}  # This is to store the values
        self.ID = 0  # ID of book
        with open(self.list_books) as bk:  # With statement automatically closes the file
            content = bk.readlines()  # This will read all data line by line
            for line in content:  # A for loop will get each line
                self.book_dic.update({str(self.ID): {'Books Title': line.replace('\n', ''),  # Updates the Values
                                                     'Lender Name': "", 'Issue Date': "", 'Status': "Available"}})
                self.ID += 1  # It will add 1 everytime when a line in updated in {}

    def display_books(self):  # A method for displaying books
        print('---------------------------Lists Of Books----------------------------')
        print('|', 'Book ID', '\t|\t', 'Book Title', '\t|\t', 'Status', '\t|\t', 'Lender Name \t|')
        print('---------------------------------------------------------------------')
        for key, value in self.book_dic.items():  # At the same time for loop is retrieving key and values from {}
            print(key, '\t-\t', value.get('Books Title'), '- [', value.get('Status'), '] -', value.get('Lender Name'))

    def issue_books(self):  # Method for issuing books
        while True:  # This is an infinite loop
            current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Captures the exact time of issuing
            book_id = input('Enter Book ID: ')  # Asks for book id
            if book_id in self.book_dic:  # Checks if the book ID is in {}
                if self.book_dic[book_id]['Status'] == 'Available':  # If book status is 'available'
                    # it will execute next line
                    lender = input('Enter your name please:\n')  # Asks for issuer name
                    self.book_dic[book_id]['Lender Name'] = lender  # Changes the 'lender' name to given name
                    self.book_dic[book_id]['Issue Date'] = current_date  # Changes the 'issue date' to current_date
                    self.book_dic[book_id]['Status'] = 'Already Issued'  # And 'status' to already issued
                    print(f'Book Successfully Issued To {self.book_dic[book_id]["Lender Name"]} On {current_date} \n')
                    break  # Breaks the infinite loop
                else:  # If book status is other than available
                    print(f'Sorry, This Book Is Already Issued To\
 {self.book_dic[book_id]["Lender Name"]} on {self.book_dic[book_id]["Issue Date"]}!')
                    break
            else:  # if book_id not in {}, this code executes
                print('Book ID Not Found. Please Try Again!')

    def add_books(self):  # Method for adding books to {}
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_book = input('Enter Book Title: ').strip()
        if new_book == '':  # If no name given it will return to method add_books
            print('Please Enter A Name Of The Book')
            return self.add_books
        elif len(new_book) > 30:  # The length of book name should be under 30 characters
            print('Book Title Is Too Long, Title Length Should Be 30 Characters')
            return self.add_books
        else:  # If book name given, this code will execute
            with open('books.txt', 'a') as o:
                o.writelines(f'\n"{new_book}"')
                lender = input('Enter Your Name Please: ')
                self.book_dic.update({
                    str(int(max(self.book_dic)) + 1): {'Books Title': new_book, 'Lender Name': "", 'Issue Date': "",
                                                       'Status': "Available"}
                })  # First we need to find the max of {ID} and then type cast it to integer, so we can +1 the {ID}
                # and lastly converting the new number to string, so we can access it, and updating others
                print(f'New Book "{new_book}" Has Been Added To The Library On {current_date} By {lender}')

    def return_book(self):  # Method for returning books
        book_id = input('Enter book ID: ')
        if book_id in self.book_dic.keys():  # Checks If book_id exist in {}.keys() or not
            if self.book_dic[book_id]['Status'] == 'Available':  # Check the status of that book_id
                print(f'This Book {book_id} Is Already In The Library, Please Check The ID Of The Book')
                # If book_id is already in {} it show above message and return to main task
            elif not self.book_dic[book_id]['Status'] == 'Available':  # if status of that book_id is not available
                # it executes below codes
                self.book_dic[book_id]['Lender Name'] = ''
                self.book_dic[book_id]['Issue Date'] = ''
                self.book_dic[book_id]['Status'] = 'Available'
                print(f'Book Returned Successfully, Record Will Be Updated Soon!!:\n')
        else:  # If book_id is not found in {}
            print(f'Book ID {book_id} Not Found\nPlease Try Again')


try:  # try and exception for better handling of error
    myLMS = LMS('books.txt', "Junaid's Library")  # Creates an object of class
    Key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books",
                "Q or QUIT or EXIT": "Quit"}
    key_press = False
    while not (key_press == 'Q'):  # If the key pressed in other than q it will execute below code
        print(f'\n------------Welcome To {myLMS.library_name}------------\n')
        for key, value in Key_list.items():  # a for loop to get key and value from key_list
            print(f'Press {key} To {value}')
        key_press = input('Enter Key: ').lower()  # Converts alphabet input to small letters
        if key_press == "d":
            print('\nCurrent Selection : Display Books')
            myLMS.display_books()
        elif key_press == "i":
            print('\nCurrent Selection : Issue Books')
            myLMS.issue_books()
        elif key_press == 'a':
            print('\nCurrent Selection : Add Books')
            myLMS.add_books()
        elif key_press == 'r':
            print('\nCurrent Selection : Return Books')
            myLMS.return_book()
        elif key_press in ['q', 'quit', 'exit']:  # If any letter from [] is pressed the loop will break
            break
        else:  # if other characters
            continue

except Exception:
    print('There Is Something Wrong\nPlease Try Again')
