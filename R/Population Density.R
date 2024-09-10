library(readxl)
library(dplyr)
excel_file <-"E:\\Data_analysis_projects\\Population Density\\dataset\\cities_population.xlsx"
df <-read_excel(excel_file )
df1 <- df %>%
  group_by(city, country) %>%
  summarise(density = round(sum(population) / sum(area)))

print(df1,n=5000)

df_min <- df1 %>%
  filter(density == min(density))

print("City with Minimum Density:")
print(df_min)

df_max <- df1 %>%
  filter(density == max(density))

print("City with max Density:")

print(df_max)
