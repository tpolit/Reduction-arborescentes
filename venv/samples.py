import echauffement
import decisionTree

def allBooleanFunction(x):
    rtn = []
    for i in range(0, pow(2, pow(2, x))):
        rtn.append(echauffement.table(i, pow(2, x)))
    return rtn


def numberOfNode(t):
    dico = {}

    def temp(a):
        dico[id(a)] = 1
        if a.left_child is None and a.right_child is None:
            return 0
        else:
            temp(a.left_child)
            temp(a.right_child)
            return 0
    temp(t)
    return len(dico.keys())


def nofbn(n):
    liste = [0] * 20
    print(liste)
    abf = allBooleanFunction(n)
    cpt = 0

    while cpt < len(abf):
        arbre = decisionTree.cons_arbre(abf[cpt])
        decisionTree.luka(arbre)
        first_compr = decisionTree.compression(arbre, {})
        snd_compr = decisionTree.compression_bdd(first_compr)
        nbnode = numberOfNode(snd_compr)
        liste[nbnode] += 1
        cpt+=1

    return liste
