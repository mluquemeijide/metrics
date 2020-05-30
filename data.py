import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

dev = ['ux designer', 'testing', 'tecnico', 'sysadmin', 'system admin', 'software developer', 'developer', 'soporte',
        'soporte tecnico', 'tecnico', 'it', 'informatica', 'programador web', 'web designer', 'it', 'ingeniero', 'dev',
        'desarrollador', 'cientifico', 'analista']



if __name__ == "__main__":
    print("Starts Here.")

    df = pd.read_excel('./event_data.xlsx')

    print("Here it goes.")

    print("******** Divided by Country *********")

    df_country = df['País'].value_counts()
    df_country.columns = ['País', 'Cantidad']
    cols = df_country.columns

    for column in cols:
        print(column, end = '\t')
    print()

    print(df_country)
    #df_country.set_index("País")

    df_country.plot.bar()
    plt.show()


    print("********* Divided by job *************")

    job = df['Cargo']

    for index, row in df.iterrows():
        if isinstance(row['Cargo'], str):
            print(str(row['Cargo']).lower())
            if str(row['Cargo']).lower() in dev:
                row['Cargo'] = dev

    print(df[df['Cargo'] == 'dev'])

    df_job = df['Cargo'].value_counts()
    df_job.columns = ['Cargo', 'Cantidad']
    cols = df_job.columns

    for column in cols:
        print(column, end = '\t')
    print()

    #print(df_job)

    df_job.plot.bar()
    #plt.show()
