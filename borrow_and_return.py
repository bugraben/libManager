# Digital library management system by Bugra, Ozgur, Talip, Yakup and Samet
# Project for Computer Programming Lab Lecture
# Borrow dictionary, give borrow, take borrow


# Dictionary to store book isbn id's and their availability
# True means that the book is available, False means it's borrowed already
table_library = {
    0: [None, True],
    1: [None, True]
    # This is a test library
}


def borrow_book(book_id):
    """Function to borrow a book from the library using its ISBN id.
    Args:
        book_id(int): Book's ISBN id.
    Returns: Strings with information about book's borrow status.
    """

    if book_id in table_library.keys() and table_library[book_id][1]:
        table_library[book_id][1] = False
        return f" {book_id} ISBN'li kitap iade edilmistir."
    else:
        return "Bu kitap mevcut değil veya ödünç alinmistir."


def return_book(book_id):
    """Function to return a borrowed book to the library by using ISBN id.
    Args:
        book_id(int): Book's ISBN id.
    Returns: Strings with information about book's borrow and return status.
    """
    if book_id in table_library.keys() and not table_library[book_id][1]:
        table_library[book_id][1] = True
        return f"{book_id} ISBN'li kitap iade edilmistir."
    else:
        return "Bu kitap kütüphanemizde değil ya da ödünç alınmadı."

# Example
# print(table_library)
# borrow_book(0)
# print(table_library)
# return_book(0)
# print(table_library)
# borrow_book(1)
# print(table_library)