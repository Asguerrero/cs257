import csv
import re
import argparse
import sys
# Authors: Valentina Guerrero, Aishwarya Varma
# Date: 1/15/2021
#Revised by Valentina Guerrero and Aishwarya Varma

class Books:

    def __init__(self, title, authors, year):
        self.title= title
        self.authors = authors
        self.year = year

def swap_list_elements(array, index1, index2):
    temp = array[index2]
    array[index2] = array[index1]
    array[index1] = temp

def fill_books_data_set():
    books_data_set = []
    with open('books.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            title = row[0]
            year = int(row[1])
            authors = row[2]
            # Regular expression to find and delete the author's lifespan in parentheses by replacing it with an
            # empty string.
            regex = "\s\((.*)\)"
            # Assuming that multiple authors will be separated by the word "and", create an additional array to
            # contain them
            if authors.find(" and ") != -1:
                authors = authors.split(" and ")
                for i in range(0, len(authors)):
                    authors[i] = re.sub(regex, "", authors[i])
            else:
                authors = [re.sub(regex, "", authors)]

            book = Books(title, authors, year)

            books_data_set.append(book)
    return books_data_set

def find_authors(author_input, books_data_set):
    books_filtered_authors = []
    for book in books_data_set:
        for i in range(len(book.authors)): 
            first_author = book.authors[0]
            current_author = book.authors[i]

            if string_contains_substring(current_author, author_input):
                if current_author != first_author:
                    swap_list_elements(book.authors, 0, i)
        books_filtered_authors.append(book)
    return books_filtered_authors

def find_titles(title_input, books_data_set):
    books_filtered_titles = []
    for book in books_data_set:
        if string_contains_substring(book.title, title_input):
            books_filtered_titles.append(book)
    return books_filtered_titles

def find_years(year1, year2, books_data_set):
    books_filtered_years = []
    year1 = convert_string_to_int(year1)
    year2 = convert_string_to_int(year2)
    # If the conversion happened succesfully:
    if year1 and year2:
        for book in books_data_set:
            if year1 <= book.year <= year2 or year2 <= book.year <= year1:
                books_filtered_years.append(book)
    return books_filtered_years

def display_find_years_results(books_filtered_years, first_input, second_input):
    # If the find_years method found any matches and returned a not empty list:
    if books_filtered_years:
        print('\n')
        print(f'Results for books published between: {first_input, second_input} \n')
        sorted_array = sorted(books_filtered_years, key=lambda books: books.year, reverse=True)
        for book in sorted_array:
            authors = change_author_list_to_string(book.authors)
            print(f'{book.year}: "{book.title}" by {authors}')
    else:
        print("No matches.")

def display_find_titles_results(books_filtered_titles, title_input):
    # If the find_titles method found any matches and returned a not empty list:
    if books_filtered_titles:
        print('\n')
        print(f'Results for titles that match the following string: "{title_input}" \n')
        
        sorted_array = sorted(books_filtered_titles, key=lambda books: books.title)
        for book in sorted_array:
            author = change_author_list_to_string(book.authors)
            print(f'"{book.title}" by {author}')
    else:
        print("No matches.")

# Given a non-empty list of books, this method displays the authors and their books
def display_find_authors_results(books_filtered_authors, author_input):
    if books_filtered_authors:
        print(f'Results for authors that match the following string: "{author_input}" \n')
        for book in books_filtered_authors:
            author = change_author_list_to_string(book.authors)
        sorted_array = sorted(books_filtered_authors, key=lambda books: books.authors)

        for i in range(len(sorted_array)):
            if i < (len(sorted_array)-1):
                current_author = change_author_list_to_string(sorted_array[i].authors)
                next_author = change_author_list_to_string(sorted_array[i+1].authors)

                print(f'"{current_author}" by {sorted_array[i].title}')
                if not(string_contains_substring(next_author, current_author)):
                    print('-------------------------------------------------')
               
            else:
                print(f'"{current_author}" by {sorted_array[i].title}')

            
    else:
        print("No matches.")

def change_author_list_to_string(author_list):
    return_string = ""
    for elementIndex in range(0, len(author_list) - 1):
        return_string += author_list[elementIndex] + ", "
    return_string += author_list[len(author_list) - 1]
    return return_string

def convert_string_to_int(year):
    if len(year) == 4:
        try:
            int_year = int(year)
            return int_year
        except:
            print("Please input two valid four-digit integers")
            sys.exit()

def string_contains_substring(main_string, sub_string):
    if main_string.lower().find(sub_string.lower()) != -1:
        return True
    return False

def get_arguments():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--author", action="store_true", help="Accepts a single search string. \n Print a list "
                                                                   "of authors whose names contain the search string  "
                                                                   "")
    group.add_argument("-t", "--title", action="store_true", help="Accepts a single search string. \n Print a list of "
                                                                  "books whose titles and their "
                                                                  "corresponding authors "
                                                                  "which contain the search string")
    group.add_argument("-y", "--year", action="store_true", help="Accepts two 4-digit integers. \n Print a list of "
                                                                 "books' titles and authors published between years A "
                                                                 "and B")
    parser.add_argument("Input", nargs="*", type=str, help="The search string")

    args = parser.parse_args()

    return args

def main():
    books_data_set = fill_books_data_set()
    args = get_arguments()
    
    # If the user writes a command (-y or --author) and does not provide a search input, print error message
    if len(args.Input) == 0:
        print("Error. Input is required. --help for more information")
        sys.exit()
    else:
        first_input = args.Input[0]

    # Checks the number of inputs provided by the user. If they correspond to the command written, execute the
    # corresponding method. Otherwise, print error message
    if len(args.Input) == 1:
        if args.author:
            books_filtered_authors = find_authors(first_input, books_data_set)
            display_find_authors_results(books_filtered_authors, first_input)
        elif args.title:
            books_filtered_titles = find_titles(first_input, books_data_set)
            display_find_authors_results(books_filtered_titles, first_input)
        else:
            print("Use either --author or --title with one argument. For --year, you must provide two arguments")
    elif len(args.Input) == 2:
        if args.year:
            second_input = args.Input[1]
            books_filtered_years = find_years(first_input, second_input, books_data_set)
            display_find_years_results(books_filtered_years, first_input, second_input)
        else:
            print("The only command that accepts two arguments is --year")
    else:
        print("Error, too many inputs --help for more information")


main()
