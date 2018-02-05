aas = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N",
       "P", "Q", "R", "S", "T", "V", "W", "Y"]


def all_possible_kmers(k, monomers):
    # Define a function that takes a list and spawns that list with
    # each element of monomers appended; call recursively
    def add_one(perm_list):
        out = []
        # Base case: maximum k-mer length will be reached when
        if len(perm_list) >= len(monomers)**k:
            return perm_list
        # Loop through the things to add to the list
        for i in monomers:
            # Loop through the existing input list and construct many new list items
            # with a monomer appended to each one
            for perm in perm_list:
                if type(perm) is not list: # Elements of the input list may be strings; handle this
                    perm = list(perm)
                out.append([i] + perm)
        # Repeat on the newly generated items
        return add_one(out)
    # output = ["".join(permutation) for permutation in add_one(monomers)]
    # return add_one(monomers)
    return ["".join(permutation) for permutation in add_one(monomers)]


combos = all_possible_kmers(5, aas)
print(len(combos))
# print(combos)