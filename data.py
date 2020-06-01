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
    plt.style.use("ggplot")
    plt.suptitle('Cantidad de asistentes por país')
    plt.subplots_adjust(left=0.1, bottom=0.2, right=0.8, top=0.9)
    plt.xticks(size = 'small', color = 'b', rotation = 45)
    numeric_index = 0
    for index in df_country.index.tolist():
        plt.text(numeric_index, df_country.at[index]+1, df_country.at[index], horizontalalignment="center")
        numeric_index += 1

    print()
    print("Guardar archivo?")
    print("     1) Si")
    print("     2) No")
    print()
    print("Opcion elegida: ", end = '')
    choice = input()
    if choice == '1' or 's' in choice:
        print("Ingrese nombre del archivo para guardar (se guardara en formato png): ", end = '')
        rename = input()
        plt.savefig(rename, transparent=False)
        print()
        print("Archivo guardado con exito.")
        print()
    else:
        pass

    plt.show()


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
    plt.suptitle('Cantidad de asistentes por rol')
    plt.subplots_adjust(left=0.1, bottom=0.2, right=0.8, top=0.9)
    plt.xticks(size = 'small', color = 'b', rotation = 45)
    numeric_index = 0
    for index in job.index.tolist():
        plt.text(numeric_index, job.at[index]+1, job.at[index], horizontalalignment="center")
        numeric_index += 1

    print()
    print("Guardar archivo?")
    print("     1) Si")
    print("     2) No")
    print()
    print("Opcion elegida: ", end = '')
    choice = input()
    if choice == '1' or 's' in choice:
        print("Ingrese nombre del archivo para guardar (se guardara en formato png): ", end = '')
        rename = input()
        plt.savefig(rename, transparent=False)
        print()
        print("Archivo guardado con exito.")
        print()
    else:
        pass

    plt.show()

    print()

def list_by_enterprise(df):
    print('********** Empresas **************')
    print(df['Empresa'].value_counts())
    print()

def list_webex_only(df):
    webex_list = ((df[df['webex'].notnull()])['webex']).tolist()
    webex_assistants = pd.DataFrame()

    for index, row in df.iterrows():
        if row['Correo electrónico'] in webex_list:
            webex_assistants = webex_assistants.append(row)


    print(webex_assistants[['Nombre', 'Correo electrónico']])
    print()

    return webex_assistants


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
    #print("                              Hecho por Manu Luque")
    print()

    print("Bienvenido/a")
    print("Ingrese el nombre del archivo a analizar: ", end = "")

    #file_name = input()
    file_name = 'event_data'
    df = pd.read_excel('./data_sets/' + file_name + '.xlsx')
    get_out = False

    print()
    print("Datos cargados y listos.......")
    print()

    while(not get_out):

        print()
        print("-------------------------------------------------------")
        print("| Elija una opcion:                                    |")
        print("|     1) Listar y graficar por pais.                   |")
        print("|     2) Listar y graficar por rol.                    |")
        print("|     3) Listar por empresa.                           |")
        print("|     4) Listar solo asistentes al evento              |")
        print("|     5) Salir                                         |")
        print("-------------------------------------------------------")

        print("Opcion elegida: ", end = '')
        chosen_option = input()
        #chosen_option = '2'
        print()

        if chosen_option == '1':
            graph_by_country(df)
        elif chosen_option == '2':
            graph_by_job(df)
        elif chosen_option == '3':
            list_by_enterprise(df)
        elif chosen_option == '4':
            webex_assistants = list_webex_only(df)
        else:
            print("Hasta luego!")
            print()
            get_out = True
            exit()

    #graph_by_country(df)
