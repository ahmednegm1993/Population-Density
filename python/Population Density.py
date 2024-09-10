import pandas as pd

df=pd.read_excel(r'E:\\Data_analysis_projects\\Population Density\\dataset\\cities_population.xlsx')
df1 = df.groupby(['city', 'country']).apply(
    lambda x: pd.Series({
        'density': (x['population'].sum() / x['area'].sum()).round().astype(int)
    })
).reset_index()

df1_min = df1.loc[df1['density'].idxmin(), ['city', 'country', 'density']]
df1_max = df1.loc[df1['density'].idxmax(), ['city', 'country', 'density']]
df2=df.pivot_table(
    index=['city', 'country'],
    values=['population', 'area'],
    aggfunc={'population': 'sum', 'area': 'sum'}
)
df2['density'] = (df2['population'] / df2['area']).round().astype(int)
df2 = df2.reset_index()

df2_min = df2.loc[df2['density'].idxmin(), ['city', 'country', 'density']]
df2_max = df2.loc[df2['density'].idxmax(), ['city', 'country', 'density']]


print(df1)

print(df1_min)

print(df1_max)


print(df2)

print(df2_min)

print(df2_max)
