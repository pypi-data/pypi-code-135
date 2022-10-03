import re 

def sans_commentaire_entete(s : str) -> str:
    '''Renvoie une chaîne identique à `s` mais sans les premiers
    commentaires et autres lignes blanches.

    Au cas où l'éditeur soit vide
    >>> sans_commentaire_entete('')
    ''
    
    Uniquement un en-tête
    >>> s = "\\n#sdf\\n#qsdfgt\\n#sdfghjk\\n\\t#qsdfgh\\n"
    >>> sans_commentaire_entete(s)
    ''

    Pas d'en-tête
    >>> s = "def toto():\\n\\treturn"
    >>> sans_commentaire_entete(s)
    'def toto():\\n\\treturn'
    

    Des commentaires et espacement avant un début de programme
    >>> s = "# nom prenom\\n\\n  # nom prenom\\n\\t  \\n# pouet pouet\\ndef toto():\\n\\treturn"
    >>> sans_commentaire_entete(s)
    'def toto():\\n\\treturn'
    '''
    liste_lignes = re.split('\n', s)
    i = 0
    while i < len(liste_lignes) and (liste_lignes[i].strip() == '' or liste_lignes[i].strip()[0] == '#'):
        i = i + 1
    return '\n'.join(liste_lignes[i:])    

def cut_topfile_comments(s : str) -> str:
    """
    cut the header of the file where the program begins
    """
    if not isinstance(s,str):
        return s
    return sans_commentaire_entete(s)

# n'est plus utilisé au profit de hash_filename
def cut_filename(s : str) -> str:
        """
        Cut the filename to keep only the last part, that is the name
        without the access path.

        Args : 
            s (str) the filename

        Return :
            (str) the filename cutted

        """
        try :
            return re.search("\/[^\/]*$",s).group()
        except Exception as e :
            return s

def hash_filename(s : str) -> str:
    """
    Returns a hashed name for s : its hash value.
    """
    return "file_" + str(s.__hash__()) 

def remplace_nom_repertoire_ds_commande_cd(s : str) -> str:
    '''
    Remplace le nom du répertoire par une valeur hachée.

    Args :
    - s (str) : de la forme "%cd <chemin_acces_dir_travail>"

    Return : 
        (str) la même chaîne commençant par "%cd" sauf que 
    <chemin_acces_dir_travail> est remplacé par une valeur hachée.
    
    '''
    nom_repertoire = s[4:].strip()
    return "%cd " + hash_filename(nom_repertoire) + "\n"

def remplace_nom_fichier_ds_commande_Run_program(s : str) -> str:
    '''
    Remplace le nom du fichier par une valeur hachée.

    Args :
    - s (str) : de la forme "%Run <nom_fichier>"

    Return : 
        (str) la même chaîne commençant par "%Run" sauf que 
    <nom_fichier> est remplacé par une valeur hachée.
    
    '''
    nom_fichier = s[5:].strip()
    return "%Run " + hash_filename(nom_fichier) + "\n"

def remplace_nom_fichier_ds_commande_Debug(s : str) -> str:
    '''
    Remplace le nom du fichier par une valeur hachée.

    Args :
    - s (str) : de la forme "%Debug <nom_fichier>"

    Return : 
        (str) la même chaîne commençant par "%Debug" sauf que 
    <nom_fichier> est remplacé par une valeur hachée.
    
    '''
    nom_fichier = s[7:].strip()
    return "%Debug " + hash_filename(nom_fichier) + "\n"


import doctest
if __name__ == '__main__':
    doctest.testmod(verbose=True)
