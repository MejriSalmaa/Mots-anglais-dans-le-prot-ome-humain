def read_words(chemin):

    liste_mot = []
    with open(chemin, "r") as f_in:
        for line in f_in:
            mot = line.strip()
            if len(mot) >= 3:
                liste_mot.append(mot.upper())
    return liste_mot


def read_sequences(chemin):

    prot_dict = {}
    with open(chemin, "r") as f_in:
        prot_id = ""
        for line in f_in:
            if line.startswith(">"):
                prot_id = line.split("|")[1]
                prot_dict[prot_id] = ""
            else:
                prot_dict[prot_id] += line.strip()
    return prot_dict

def search_words_in_proteome(liste_mot, prot_dict):

    mot_trouve = {}
    for word in liste_mot:
        res = 0
        for prot_id in prot_dict:
            if word in prot_dict[prot_id]:
                res += 1
        if res != 0:
            mot_trouve[word] = res
            print(f"{word} found {res} in sequences")
    return mot_trouve

def find_most_frequent_word(freq_dict):

    maxi = max(freq_dict.values())
    for word in freq_dict:
        if freq_dict[word] == maxi:
            print(f"=> {word} found in {maxi} sequences")



