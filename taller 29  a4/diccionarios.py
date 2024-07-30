def diccionarioListas():
    notasPersonas={
    "Historia":[95,80,82],
    "Literatura":[85,87,90],
    "Matematicas":[90,85,92],
    "Ciencias":[88,79,85]
    }
    return notasPersonas

if __name__=="__main__":

    dicNotas=(diccionarioListas())
    print(dicNotas)