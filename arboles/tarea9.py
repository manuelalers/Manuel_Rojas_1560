from arboles_binarios import NodoArbol

def main():
    root=NodoArbol(10,NodoArbol(20,NodoArbol(30,None,NodoArbol(40,NodoArbol(50),NodoArbol(60,None,NodoArbol(70,NodoArbol(80)))))))
    print("\t\t\t",root.data)
    print("")
    print("")
    print("\t\t",root.left.data)
    print("")
    print("")
    print("\t",root.left.left.data)
    print("")
    print("")
    print("\t\t",root.left.left.right.data)
    print("")
    print("")
    print("\t",root.left.left.right.left.data,end="")
    print("\t\t",root.left.left.right.right.data)
    print("")
    print("")
    print("\t\t\t\t",root.left.left.right.right.right.data)
    print("")
    print("")
    print("\t\t\t",root.left.left.right.right.right.left.data)
  

main()
    
   
