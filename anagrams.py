def construct_data_structure(str):
    letter_frequencies = {}
    for each_letter in str:
        if each_letter in letter_frequencies.keys():
            letter_frequencies[each_letter] += 1
        else:
            letter_frequencies[each_letter] = 1
    return letter_frequencies

def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """

    # TODO: Write your solution here
    str1 = re.sub(' ','',str1).lower()
    str2 = re.sub(' ','',str2).lower()
    letters_in_one = construct_data_structure(str1)
    letters_in_two = construct_data_structure(str2)
    shared_items = {each_letter: letters_in_one[each_letter] for each_letter in letters_in_one if each_letter in letters_in_two and letters_in_one[each_letter] == letters_in_two[each_letter]}
    if (len(shared_items) == len(letters_in_two.keys()) and len(shared_items) == len(letters_in_one.keys())):
        return True
    else:
        return False

print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")
