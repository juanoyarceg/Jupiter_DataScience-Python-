def medidas(df):
    for index, row in df.iteritems():
        if(row.dtypes == 'object'):
            print(row.value_counts('%'))
        else:
            print(row.describe())

def lost_data(df, var, print_list = False):
    
    datos_totales = len(df[var])
    df_null = df[df[var].isnull()]
    datos_lost = len(df_null)
    print("Datos totales =" + str(datos_totales))
    print("Datos totales perdidos =" + str(datos_lost))
    print("Porcentaje de datos perdidos =" + str(round(100*datos_lost/datos_totales, 2)) + "%")
    if(print_list):
        print(df_null['ccodealp'])

def graph_df(data,var,sample_mean=False,true_mean = False):
    plt.hist(data[var],bins=10, alpha=0.65)
    if(sample_mean):
        plt.axvline(data[var].mean(), color='k', linestyle='dashed', linewidth=1)
    if(true_mean):
        plt.axvline(df[var].mean(), color='k', linestyle='dashed', linewidth=1)

def dot_plot(data,var,plot_by,global_stat=False,statistic='mean'):
    if(statistic == 'mean'):
        temp = data.groupby(plot_by).mean()[var]
    elif(statistic != 'mean'):
        temp = data.groupby(plot_by).median()[var]
    plt.plot(temp.values,temp.index,'ro')
    if(global_stat):
        plt.axvline(df[var].mean(), color='k', linestyle='dashed', linewidth=1)