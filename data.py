import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

dev = ['ux', 'testing', 'tecnico', 'sysadmin', 'system', 'admin', 'software', 'developer', 'soporte',
        'it', 'informatic', 'programador', 'ingeniero', 'dev',
        'desarrollador', 'cientifico', 'analista', 'sistema', 'consultor', 'technical',
        'backend', 'ingeniero', 'desarrollo', 'innova', 'data', 'web', 'cto', 'app']

teacher = ['prof', 'docente']

student = ['estudiante', 'alum', 'student']

def lowercase_country(nombre_pais):
    return nombre_pais.lower()

def job_category(cargo):
    for dev_category in dev:
        if dev_category in str(cargo).lower():
            return 'Tecnico'
    for prof_category in teacher:
        if prof_category in str(cargo).lower():
            return 'Docente'
    for student_category in student:
        if student_category in str(cargo).lower():
            return 'Estudiante'
    return 'Otro'

def graph_by_country(df):
    print()
    print("******** Divided by Country *********")
    #
    df_country = (df['País'].apply(lowercase_country)).value_counts()
    #
    #print(df_country)
    #
    df_country.columns = ['País', 'Cantidad']
    cols = df_country.columns

    for column in cols:
        print(column, end = '\t')
    print()

    print(df_country)

    df_country.plot.bar()
    plt.show()

    print()

def graph_by_job(df):
    print("********* Divided by job *************")

    job = (df['Cargo'].apply(job_category)).value_counts()

    job.columns = ['Rol', 'Cantidad']
    cols = job.columns

    for column in cols:
        print(column, end = '\t')
    print()

    print(job)

    job.plot.bar()
    plt.show()

    print()

def list_by_enterprise(df):
        print('********** Empresas **************')
        print(df['Empresa'].value_counts())
        print()

if __name__ == "__main__":
    print()
    print()
    print("#####################################################################################")
    print("##                                                                                 ##")
    print("##     $       $    $$$$$$$    $$$$$$$$$$$     $$$$$$    $    $$$$$$$   $$$$$$$    ##      ")
    print("##     $ $   $ $    $               $          $    $    $    $         $          ##      ")
    print("##     $   $   $    $$$$$$$         $          $$$$$$    $    $         $$$$$$$    ##      ")
    print("##     $       $    $               $          $ $$      $    $               $    ##      ")
    print("##     $       $    $$$$$$$         $          $   $$    $    $$$$$$$   $$$$$$$    ##      ")
    print("##                                                                                 ##")
    print("#####################################################################################")
    print("                              Hecho por Manu Luque")
    print()

    print("Bienvenido/a")
    print("Ingrese el nombre del archivo a analizar: ", end = "")
    file_name = input()
    df = pd.read_excel('./data_sets/' + file_name + '.xlsx')

    print("Elija una opcion:")
    print("     1) Listar y graficar por pais.")
    print("     2) Listar y graficar por rol.")
    print("     3) Listar por empresa.")
    print("     4) Salir")

    chosen_option = input()

    if chosen_option == '1':
        graph_by_country(df)
    elif chosen_option == '2':
        graph_by_job(df)
    elif chosen_option == '3':
        list_by_enterprise(df)
    else:
        print("Hasta luego!")
        exit()

    #graph_by_country(df)
