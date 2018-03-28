# -----------------------------------------------------------------------------
# Name:   word statistics

# Author: Christine Pham

# -----------------------------------------------------------------------------
"""
A program that scans a user-selected file and returns statistics on the words
in the document.

The methods used were count_word() and report(). count_words() builds a
dictionary of the words used in the file and returns the dictionary. report()
takes and sorts the dictionary and displays statistics on the words. It then
writes the sorted list of words onto a new file.

returns nothing.
"""
import string

def count_words(filename):
    """
    Builds and returns a dictionary based on word count in text

    Parameter: filename - a file the user has inputted to build a dictionary
    Returns: dictionary with number of occurrences of a word in file
    """
    word_count = {}

    with open(filename,'r',encoding='utf-8') as my_file:
        for line in my_file:
            lower_line = line.lower()
            for word in lower_line.split(' '):
                word = word.strip(string.punctuation + '\n')
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return word_count

def report(word_count):
    """
    Reports on various statistics based on the given word count dictionary and
    writes a sorted list of the file contents into a new file.

    Parameter: word_count - a dictionary with number of occurrences of a word
        in a file.
    Returns: None
    """

    print('The longest word is:', max(word_count, key=len))
    print('The 5 most common words are:')
    sorted_file = sorted(word_count, key = word_count.get, reverse=True)
    for word in sorted_file[0:5]:
        print(word + ':', word_count[word])

    with open('out.txt','a',encoding='utf-8') as my_file:
        for word in sorted_file:
            sorted_list = word + ': ' + str(word_count[word]) + '\n'
            my_file.write(sorted_list)

def main():
    filename = input('Please enter file name to scan:')
    word_count = count_words(filename)
    report(word_count)



if __name__ == '__main__':
    main()