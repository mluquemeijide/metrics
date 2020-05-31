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



if __name__ == "__main__":
    print("Starts Here.")

    df = pd.read_excel('./data_sets/event_data.xlsx')

    print("Here it goes.")

    # Select for COUNTRY analysis
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
    print('********** Empresas **************')
    print(df['Empresa'].value_counts())
