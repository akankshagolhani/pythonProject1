import _collections

user={'L34':'Andrea Selleck', 'L22':'Lucas Hyatt', 'L19':'Carol Leonard', 'L84':'Ayesha Ford', 'L77':'Kenneth Trout'}
book={'A234':'The 101 Dalmations', 'A675':'The Adventures of Huckleberry Finn', 'A212':'Bag of Bones', 'B671':'Charlie and the Chocolate Factory', 'B534':'Charlottes Web', 'B777':'A Christmas Carol', 'B778':'Dracula', 'B812':'A Farewell to Arms', 'C101':'The Firm', 'C102':'War and Peace'}
issued ={}
book_name={}

def checkout_book():
    user_id=input("Please enter borrower id").upper()
    for key in user.keys():
         if(key != user_id):
             pass
         elif(key == user_id):
             #print('{}:{}'.format(key,value))
             book_id= input("Please enter the book_id").upper()
             for key,value in book.copy().items():
                    if (key == book_id):
                           print("checkout successful")
                           issued.update({user_id:book_id})
                           book_name.update({book_id:value})
                           print(book_name)
                           del book[book_id]
                           main()
                    else:
                         for value in issued.values():
                            if(value==book_id):
                                print("VYZ already checked out")
                                main()
                         else:
                             print("there is no such book XYZ")
                             main()
         #else:
         #   print("XYZ is not a valid borrower")

def return_book():
    user_id = input("Please enter borrower id").upper()
    for key in user.keys():
        if (key != user_id):
            pass
        elif (key == user_id):
            # print('{}:{}'.format(key,value))
            book_id = input("Please enter the book_id").upper()
            for key,value in issued.copy().items():
                print(key,value)
                if ((key == str(user_id)) and (value == str(book_id))):
                    print("return successful")
                    del issued[user_id]
                    for key,value in book_name.items():
                        if key == book_id:
                           book.update({key: value})
                        else:
                            continue
                    main()
                else:
                    print("XYZ not currently checked out")
                    main()



def main():
    print("Please select one of the following:")
    print("Please enter 'checkout' if you want to issue a book")
    print("Please enter 'return' if you want to return a book")
    print("Please enter 'exit' if you want to exit from the system")
    user_input = input("").lower()
    if user_input=='checkout':
        checkout_book()
    elif user_input=='return':
        return_book()
    elif user_input=='exit':
        exit()
    else:
        print("Invalid Command")
        main()

main()