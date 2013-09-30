
#lower all characters
#for loop to run through text
#split into a list with
#strip the list items to get rid of non-word characters
#set default to 1 (dict.setdefault)
#iterate through list of words (dict.iteritems)
    #if not in list, set it to default
    #if in list +=1


def main():
    f = open("twain.txt")
    filetext = f.read()
    f.close()

    # lowercase all text
    filetext = filetext.lower()

    # removes all spaces and creates a list of words
    words = filetext.split()
    word_count = {}
    
    for i in range(len(words)):
        words[i:i + 1] = words[i].split("--")

        # removes periods and commas
        words[i] = words[i].strip("\"\'.,?():;!_")

        # check if word exists in key-value word_count 
        word_count.setdefault(words[i], 0)
        word_count[words[i]] += 1

    # create new dict and list to sort words alphabetically by frequency
    frequency_of_words = {}


    for key, value in word_count.iteritems():
        # originally print key, value
        # sets frequency as key in dict and value is list of 
        # words that has that frequency
        frequency_of_words.setdefault(value, [])
        frequency_of_words[value].append(key)
        frequency_of_words[value].sort()

    # creates list that we can sort frequencies
    for frequency in sorted(frequency_of_words.keys())[::-1]:
        for word in frequency_of_words[frequency]:
            print word, frequency


    # printing sorted frequencies on the list of words for that frequency
    # for frequency in frequency_count:
    #     for word in frequency_of_words[frequency]:
    #         print word, frequency


main()