import sqlite3
import os

APP_PATH= os.getcwd()
DB_PATH= APP_PATH+'/my.database.db'

##Creacion de la DB
con = sqlite3.connect(DB_PATH)
cursor=con.cursor()
try:
    cursor.execute('''
        CREATE TABLE DICTIONARY(
        ID        INT PRIMARY KEY NOT NULL,
        WORD      TEXT             NOT NULL,
        TRANSLATE TEXT             NOT NULL    
         )
    ''')
except Exception as exc:
    print(exc)

##Coloque 5 palabras de inicio
try:
        cursor.execute('''
            INSERT INTO DICTIONARY(ID,WORD,TRANSLATE)
            VALUES('1','XOPA','HOLA')
    
          ''')

        cursor.execute('''
              INSERT INTO DICTIONARY(ID,WORD,TRANSLATE)
              VALUES('34','Buco','Mucho')
          ''')

        cursor.execute('''
              INSERT INTO DICTIONARY(ID,WORD,TRANSLATE)
              VALUES('55','Borrador','Autobus')
          ''')
        cursor.execute('''
                     INSERT INTO DICTIONARY(ID,WORD,TRANSLATE)
                     VALUES('25','Cha','Para enfatizar algo')
                 ''')
        cursor.execute('''
                     INSERT INTO DICTIONARY(ID,WORD,TRANSLATE)
                     VALUES('99','Chantin','Casa')
                 ''')


        con.commit()
except Exception as ex:
    print(ex)
##Funciones de CRUD para el menu de opciones
def translation(word):
    cursor.execute(" SELECT TRANSLATE  FROM DICTIONARY WHERE WORD ='"+word+"'")
    for i in cursor:
        print("Definicion: ",i)
def search_all():
    cursor.execute('''
        SELECT ID,WORD  FROM DICTIONARY
    
    ''')
    for i in cursor:
        print("ID:", i[0]," Palabra: ",i[1])

def add_word(id,word,translate):

    try:
     cursor.execute("INSERT INTO DICTIONARY(ID,WORD,TRANSLATE)""  VALUES('"+str(id)+"','"+word+"','"+translate+"')  ")
     con.commit()
    except Exception as ex:
        print(ex)
    print("................................................................................")
    print(".                    Palabra agregada correctamente                            .")
    print("................................................................................")
def del_word(id):

    try:
        cursor.execute("DELETE FROM DICTIONARY WHERE ID='"+str(id)+"'")
        con.commit()
    except Exception as ex:
        print(ex)
    print("................................................................................")
    print(".                 Palabra eliminada correctamente                              .")
    print("................................................................................")

def edit_word(change,translate):

    try:
        cursor.execute("UPDATE DICTIONARY SET WORD='"+change+"' WHERE TRANSLATE='"+translate+"'")
        con.commit()
    except Exception as ex:
        print(ex)
    print("................................................................................")
    print(".                 Palabra actualizada correctamente                            .")
    print("................................................................................")
def edit_translate(change,word):

    try:
        cursor.execute("UPDATE DICTIONARY SET TRANSLATE='"+change+"' WHERE WORD='"+word+"'")
        con.commit()
    except Exception as ex:
        print(ex)
    print("................................................................................")
    print(".                 Concepto actualizada correctamente                           .")
    print("................................................................................")


##Menu normal en bucle while
print("................................................................................")
print(".          Bienvenido al sistema CRUD del Dicionario Panameno                  .")
print("................................................................................")
print("""Favor elija una opcion:
    1.Ver listado de palabras
    2.Agregar una palabra
    3.Borrar una palabra
    4.Consultar Definicion
    5.Editar palabra panamena
    6.Editar concepto de palabra
    7.Salir
""")
print("................................................................................")
opc = int(input("Ingrese el numero de opcion que desea:"))
while (opc!=-1):


    if opc==1:
        print("................................................................................")
        print(".                           Listado de palabras                                .")
        print("................................................................................")
        search_all()
    elif opc==2:
        id = int(input("Ingresa el numero de ID que quieres asignarle a la palabra:"))
        word = input("Ingresa la palabra panamena que quieres agregar:")
        translate = input("Ingresa la traduccion de la palabra panamena:")
        add_word(id,word,translate)
    elif opc==3:
        id = int(input("Ingresa el numero de ID de la palabra a borrar:"))
        del_word(id)
    elif opc == 4:
        word = input("Ingresa la palabra que quieres conocer el concepto:")
        translation(word)
    elif opc == 5:
        translate = input("Ingresa el concepto de la palabra que quieres cambiar:")
        change=input("Ingresa la nueva palabra:")
        edit_word(change,translate)
    elif opc == 6:
        word = input("Ingresa la palabra panamena que le quieras cambiar el concepto:")
        change = input("Ingresa el nuevo concepto:")
        edit_translate(change,word)
    elif opc==7:
        print("................................................................................")
        print(".                     Gracias por utilizar el programa!                        .")
        print("................................................................................")
        break
    else:
        print("Opcion invalida por favor volver a ingresar.")
    print("................................................................................")
    print(".          Bienvenido al sistema CRUD del Dicionario Panameno                  .")
    print("................................................................................")
    print("""Favor elija una opcion:
        1.Ver listado de palabras
        2.Agregar una palabra
        3.Borrar una palabra
        4.Consultar Definicion
        5.Editar palabra panamena
        6.Editar concepto de palabra
        7.Salir
    """)
    print("................................................................................")
    opc = int(input("Ingrese el numero de opcion que desea:"))

con.close()

