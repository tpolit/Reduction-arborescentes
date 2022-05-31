import math

class DecisionTree:

    def __init__(self, value, left_child, right_child, dyck):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.dyck = dyck

    def treeToTab(self, tree):
        if tree.left_child == None:
            return str(tree.value)
        else:
            return [id(tree)] + [self.treeToTab(tree.left_child)] + [self.treeToTab(tree.right_child)]


    def __str__(self):
        all_values = self.treeToTab(self)
        return str(all_values)



def cons_arbre(table_verite):
    length = len(table_verite)
    if length == 1:
        return DecisionTree(table_verite[0], None, None,"")
    elif length > 0:
        return DecisionTree(int(math.log(length, 2)), cons_arbre(table_verite[0:(length//2)]), cons_arbre(table_verite[length//2:length]), "")
    else:
        return DecisionTree(None, None, None,"")


"""fonction prise sur https://webdevdesigner.com/q/how-to-check-if-a-number-is-a-power-of-2-8538/"""
def isPowerOfTwo(x):
    return (x != 0) and ((x & (x - 1)) == 0)


def luka(t):
    if t.left_child != None or t.right_child != None:
        t.dyck =  str(t.value) + "(" + luka(t.left_child) + ")" + "(" + luka(t.right_child) + ")"
        return t.dyck
    elif t.value != None:
        t.dyck =  str(t.value)
        return t.dyck
    else:
        t.dyck = ""
        return t.dyck

def compression(t, dico):
    if t.left_child != None or t.right_child != None:
        if t.dyck in dico:
            return dico[t.dyck]
        else:
            temp = DecisionTree(t.value, compression(t.left_child, dico), compression(t.right_child, dico), t.dyck)
            dico[t.dyck] = temp
            return temp
    elif t.value != None:
        if t.dyck in dico:
            return dico[t.dyck]
        else:
            temp = DecisionTree(t.value, None, None, t.dyck)
            dico[t.dyck] = temp
            return temp
    else: 
        return DecisionTree(None, None, None,"")

# creer et remplit le fichier .dot
def createDotFile(t, file):
    res = compressedTreeToDot(t)
    res_splitted = res.split('\n')

    lines_seen = {}
    with open(file, "w") as graph:
        graph.write("graph { \n")
        for line in res_splitted:
            if line in lines_seen:
                if lines_seen[line] >= 1:
                    continue
                else:
                    graph.write(line + "\n")
                    lines_seen[line] += 1
            else:
                graph.write(line + "\n")
                lines_seen[line] = 1
        graph.write("}")
        graph.seek(0, 0)


    
# construit une string pour afficher l'arbre au format .dot
def compressedTreeToDot(t):
    if t.left_child != None and t.right_child != None:
        temp = '\t"' + str(t.value) + '[@'+str(id(t))+']"' + " -- " + '"' + str(t.left_child.value) + '[@'+str(id(t.left_child))+']"' + "[color=red, pendwidth=4.0];\n"
        temp += '\t"' + str(t.value) + '[@'+str(id(t))+']"' + " -- " + '"' + str(t.right_child.value) + '[@'+str(id(t.right_child))+']"'  + "[color=green, pendwidth=4.0];\n"
        temp += compressedTreeToDot(t.left_child)
        temp += compressedTreeToDot(t.right_child)
        return temp
    return ""


def compression_bdd(t):
    temp = t
    if not(temp.left_child is None) or not(temp.right_child is None):
        if temp.left_child is temp.right_child:
            return compression_bdd(temp.left_child)
        temp.left_child = compression_bdd(temp.left_child)
        temp.right_child = compression_bdd(temp.right_child)
        return temp
        
    else:
        return temp
