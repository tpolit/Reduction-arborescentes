# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import echauffement
import decisionTree
import samples

def main():

    table_verite = echauffement.table(5, 4)
    print(table_verite)
    arbre = decisionTree.cons_arbre(table_verite)
    print(arbre)
    decisionTree.luka(arbre)
    compressedArbre = decisionTree.compression(arbre, {})
    decisionTree.createDotFile(compressedArbre, "graph5.dot")
    robddTree = decisionTree.compression_bdd(compressedArbre)
    decisionTree.createDotFile(robddTree, "robdd5.dot")
    #print(samples.allBooleanFunction(3))
    #print(samples.nofbn(4))
    #print(samples.numberOfNode(robddTree))
    i = 1
    while i < 6:
        with open("nbnodes" + str(i) + ".txt", "w") as file:
            nb_nodes_occ = samples.nofbn(i)
            nb_nodes = 0
            for occ in nb_nodes_occ:
                file.write(str(nb_nodes) + " = " + str(occ) + "\n")
                nb_nodes+=1
        i+=1
        print(i)
        

if __name__ == "__main__":
    main()
