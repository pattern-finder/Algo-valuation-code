# Tokenisation:  déoupe les block de code: Fait

# Supresion des infos superflue:
#   - rename var  (fait)
#   - stemming
#   - supression commentaire/saut de ligne  (fait)

# retirer le code concerné ar le plagiat afin de ne tester que le code plagié (si sela représente une fonction complete)


dico_stemming = {
    "def": "d",
    "while": "w",
    "for": "f",
    "if": "i",
    "elif": "ei",
    "else": "e",
    "<=": "c",
    ">=": "c",
    "<": "c",
    ">": "c",
    "def": "d",

    "!=": "!",
    "==": "-",
    "and": "&",
    "or": "|",
    "var": "v"
}

dico_supression = {
    " ": "",
    "{": "",
    "}": "",
    "(": "",
    ")": "",
    ";": "",
    ":": ""
}


def delete_string(ligne):
    delete = False
    list_chain_to_remove = []

    if ligne.count("\"") > 0:

        i = 0
        chain_to_remove = ""

        while i < len(ligne):

            if ligne[i] == '\"':
                list_chain_to_remove.append(chain_to_remove)
                chain_to_remove = ""
                delete = not delete

            if delete and ligne[i] != '"':
                chain_to_remove = chain_to_remove + ligne[i]

            i += 1

    for chain in list_chain_to_remove:
        ligne = ligne.replace(chain, "")

    ligne = ligne.replace("\"\"", "\"")

    return ligne


def replace_by_new_content(ligne):
    for key in dico_stemming:
        ligne = ligne.replace(key, dico_stemming[key])

    return ligne


def delete_unuse_content(ligne):
    for key in dico_supression:
        ligne = ligne.replace(key, dico_supression[key])

    return ligne


def sanitize_content(lignes):
    filtered_content = ""

    for ligne in lignes:
        ligne = delete_string(ligne)

        filtered_content = filtered_content + (replace_by_new_content(ligne))

    filtered_content = delete_unuse_content(filtered_content)

    return filtered_content



#   hash_value = calculate_hash(token)

#  print(hash_value)
#
#     print(checker("abcdefgh", "a"))
