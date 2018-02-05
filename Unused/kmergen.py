def all_possible_kmers(k):
    built_kmers = []

    # def add_letter(kmer, j=0):
    #     # # If we have a sequence of 3, return it
    #     # if j == k:
    #     #     return "".join(kmer)
    #     # # If shorter than 3, add a letter
    #     # # Define what we're shuffling
    single_letter_codes = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N",
                               "P", "Q", "R", "S", "T", "V", "W", "Y"]


    for letter in single_letter_codes:
        start_letter = letter
        letter = [letter]
        for another_letter in single_letter_codes:
            letter.append(another_letter)
            built_kmers.append(letter)
            letter = []

    for i in built_kmers:
        i = "".join(i)

    return built_kmers


combos = all_possible_kmers(3)
print(combos)

#I want to:
# Take a letter. Recurse through the list of letters and make a two-mer between that letter and the others.
# Repeat this with each two-mer and add a third letter.