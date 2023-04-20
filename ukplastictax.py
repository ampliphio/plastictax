# %% [markdown]
# # Import Packages
# 
# 

# %%
#import packages 

import pandas as pd
from statistics import mean
import numpy as np


# %% [markdown]
# # Step 1: Import Source File

# %%
#import input_file
df_ClientName_Survey = pd.read_csv('/2021_InputFile_ClientName_SKUReport.csv', sep=',')
df_ClientName_Survey.head()

# %% [markdown]
# # Step 2: Prepare File 

# %%
#Add 0 for empty cells
df_ClientName_Survey = df_ClientName_Survey.fillna(0)

#Drop irrelevant columns

df_ClientName_Survey.head()

# %% [markdown]
# # Step 3: Calculate Results/KPIs as DataFrame

# %%
#KPI1: Average Recycled Plastic

#Prepare Numbers for Material 1
df_ClientName_Survey.loc[df_ClientName_Survey['Material 1 Cat']=="Plastics",'Rec_Plastic_content_Mat1'] = df_ClientName_Survey["Material 1 Weight per Unit in Grams"] * df_ClientName_Survey['Material 1 % Recycled Content']
df_ClientName_Survey.loc[df_ClientName_Survey['Material 1 Cat']=="Plastics", 'Plastic_content_Mat1'] = df_ClientName_Survey["Material 1 Weight per Unit in Grams"]

#Prepare Numbers for Material 2
df_ClientName_Survey.loc[df_ClientName_Survey['Material 2 Cat']=="Plastics",'Rec_Plastic_content_Mat2'] = df_ClientName_Survey["Material 2 Weight per Unit in Grams"] * df_ClientName_Survey['Material 2 % Recycled Content']
df_ClientName_Survey.loc[df_ClientName_Survey['Material 2 Cat']=="Plastics", 'Plastic_content_Mat2'] = df_ClientName_Survey["Material 2 Weight per Unit in Grams"]

#Prepare Numbers for Material 3
df_ClientName_Survey.loc[df_ClientName_Survey['Material 3 Cat']=="Plastics",'Rec_Plastic_content_Mat3'] = df_ClientName_Survey["Material 3 Weight per Unit in Grams"] * df_ClientName_Survey['Material 3 % Recycled Content']
df_ClientName_Survey.loc[df_ClientName_Survey['Material 3 Cat']=="Plastics", 'Plastic_content_Mat3'] = df_ClientName_Survey["Material 3 Weight per Unit in Grams"]

#Prepare Numbers for Material n
df_ClientName_Survey.loc[df_ClientName_Survey['Material n Cat']=="Plastics",'Rec_Plastic_content_Matn'] = df_ClientName_Survey["Material n Weight per Unit in Grams"] * df_ClientName_Survey['Material n % Recycled Content']
df_ClientName_Survey.loc[df_ClientName_Survey['Material n Cat']=="Plastics", 'Plastic_content_Matn'] = df_ClientName_Survey["Material n Weight per Unit in Grams"]

#Replace new NAs with zero
df_ClientName_Survey = df_ClientName_Survey.fillna(0)

# Calculate Average Recycled Plastic Content per SKU
df_ClientName_Survey['tot_recycled_plastic'] = (df_ClientName_Survey['Rec_Plastic_content_Mat1'] + df_ClientName_Survey['Rec_Plastic_content_Mat2'] + df_ClientName_Survey['Rec_Plastic_content_Mat3'] + df_ClientName_Survey['Rec_Plastic_content_Matn']) 
df_ClientName_Survey['Plastic_content_tot'] = df_ClientName_Survey['Plastic_content_Mat1'] + df_ClientName_Survey['Plastic_content_Mat2'] +df_ClientName_Survey['Plastic_content_Mat3'] + df_ClientName_Survey['Plastic_content_Matn']
df_ClientName_Survey['tot_recycled_plastic'] = df_ClientName_Survey['tot_recycled_plastic'] / df_ClientName_Survey['Plastic_content_tot']

df_ClientName_Survey.head()

# %%
#KPI 2: Percentage of Bio-Based Plastic Content

#Prepare Numbers for Material 1
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 1 Cat']=="Other bio-based substance"),
                        'BioBased_Mat1']= df_ClientName_Survey['Material 1 Weight per Unit in Grams']

#Prepare Numbers for Material 2
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 2 Cat']=="Other bio-based substance"),
                        'BioBased_Mat2']= df_ClientName_Survey['Material 2 Weight per Unit in Grams']

#Prepare Numbers for Material 3
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 3 Cat']=="Other bio-based substance"),
                        'BioBased_Mat3']= df_ClientName_Survey['Material 3 Weight per Unit in Grams']

#Prepare Numbers for Material n
df_ClientName_Survey.loc[(df_ClientName_Survey['Material n Cat']=="Other bio-based substance"),
                        'BioBased_Matn']= df_ClientName_Survey['Material n Weight per Unit in Grams']

#Replace new NAs with zero
df_ClientName_Survey = df_ClientName_Survey.fillna(0)

#This is the column AK -> BioBased Plastic content
df_ClientName_Survey['Tot_BioBased'] = df_ClientName_Survey['BioBased_Mat1'] + df_ClientName_Survey['BioBased_Mat2'] + df_ClientName_Survey['BioBased_Mat3'] + df_ClientName_Survey['BioBased_Matn']

df_ClientName_Survey.head()

# %%
#KPI 3: Imported / Manufactured Weight

#Prepare Numbers for Material 1
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 1 Cat']=="Plastics"),
                        'Imp_Plastic_weight_Mat1']= df_ClientName_Survey['Material 1 Weight per Unit in Grams'] * df_ClientName_Survey['Imported/Manufactured']

#Prepare Numbers for Material 2
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 2 Cat']=="Plastics"),
                        'Imp_Plastic_weight_Mat2']= df_ClientName_Survey['Material 2 Weight per Unit in Grams']*df_ClientName_Survey['Imported/Manufactured']

#Prepare Numbers for Material 3
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 3 Cat']=="Plastics"),
                        'Imp_Plastic_weight_Mat3']= df_ClientName_Survey['Material 3 Weight per Unit in Grams']*df_ClientName_Survey['Imported/Manufactured']

#Prepare Numbers for Material n
df_ClientName_Survey.loc[(df_ClientName_Survey['Material n Cat']=="Plastics"),
                        'Imp_Plastic_weight_Matn']= df_ClientName_Survey['Material n Weight per Unit in Grams']*df_ClientName_Survey['Imported/Manufactured']

#Replace new NAs with zero
df_ClientName_Survey = df_ClientName_Survey.fillna(0)

#find the total amount of plastic weight imported
df_ClientName_Survey['Imp_Tot_weight'] = df_ClientName_Survey['Imp_Plastic_weight_Mat1'] + df_ClientName_Survey['Imp_Plastic_weight_Mat2'] + df_ClientName_Survey['Imp_Plastic_weight_Mat3'] + df_ClientName_Survey['Imp_Plastic_weight_Matn']
df_ClientName_Survey['Imp_Tot_weight'] = df_ClientName_Survey['Imp_Tot_weight'] / 1000

df_ClientName_Survey.head()



# %%
#KPI 4: Weight Sold

#Prepare Numbers for Material 1
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 1 Cat']=="Plastics"),
                        'Sold_Plastic_weight_Mat1']= df_ClientName_Survey['Material 1 Weight per Unit in Grams'] * df_ClientName_Survey['Units Sold']

#Prepare Numbers for Material 2
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 2 Cat']=="Plastics"),
                        'Sold_Plastic_weight_Mat2']= df_ClientName_Survey['Material 2 Weight per Unit in Grams']*df_ClientName_Survey['Units Sold']

#Prepare Numbers for Material 3
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 3 Cat']=="Plastics"),
                        'Sold_Plastic_weight_Mat3']= df_ClientName_Survey['Material 3 Weight per Unit in Grams']*df_ClientName_Survey['Units Sold']

#Prepare Numbers for Material n
df_ClientName_Survey.loc[(df_ClientName_Survey['Material n Cat']=="Plastics"),
                        'Sold_Plastic_weight_Matn']= df_ClientName_Survey['Material n Weight per Unit in Grams']*df_ClientName_Survey['Units Sold']

#Replace new NAs with zero
df_ClientName_Survey = df_ClientName_Survey.fillna(0)

#find the total amount of plastic weight manufactured
df_ClientName_Survey['Sold_Tot_weight'] = df_ClientName_Survey['Sold_Plastic_weight_Mat1'] + df_ClientName_Survey['Sold_Plastic_weight_Mat2'] + df_ClientName_Survey['Sold_Plastic_weight_Mat3'] + df_ClientName_Survey['Sold_Plastic_weight_Matn']
df_ClientName_Survey['Sold_Tot_weight'] = df_ClientName_Survey['Sold_Tot_weight'] / 1000

df_ClientName_Survey.head()

# %%
#KPI 5: Weight Distributed as Samples

#Prepare Numbers for Material 1
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 1 Cat']=="Plastics"),
                        'Plast_distributed_1']= df_ClientName_Survey['Material 1 Weight per Unit in Grams']*df_ClientName_Survey['Units Distributed as Samples']

#Prepare Numbers for Material 2
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 2 Cat']=="Plastics"),
                        'Plast_distributed_2']= df_ClientName_Survey['Material 2 Weight per Unit in Grams']*df_ClientName_Survey['Units Distributed as Samples']

#Prepare Numbers for Material 3
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 3 Cat']=="Plastics"),
                        'Plast_distributed_3']= df_ClientName_Survey['Material 3 Weight per Unit in Grams']*df_ClientName_Survey['Units Distributed as Samples']

#Prepare Numbers for Material n
df_ClientName_Survey.loc[(df_ClientName_Survey['Material n Cat']=="Plastics"),
                        'Plast_distributed_n']= df_ClientName_Survey['Material n Weight per Unit in Grams']*df_ClientName_Survey['Units Distributed as Samples']

#Replace new NAs with zero
df_ClientName_Survey = df_ClientName_Survey.fillna(0)

#This is the column AQ -> weight of plastic distributed as samples
df_ClientName_Survey['Plastic_weight_distributed'] = df_ClientName_Survey['Plast_distributed_1'] + df_ClientName_Survey['Plast_distributed_2'] + df_ClientName_Survey['Plast_distributed_3'] + df_ClientName_Survey['Plast_distributed_n']
df_ClientName_Survey['Plastic_weight_distributed'] = df_ClientName_Survey['Plastic_weight_distributed'] / 1000

df_ClientName_Survey.head()

# %%
#KPI 6: Weight Expired/Rejected Product

#Prepare Numbers for Material 1
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 1 Cat']=="Plastics"),
                        'Plast_expired_1']= df_ClientName_Survey['Material 1 Weight per Unit in Grams']*df_ClientName_Survey['Units Expired/Rejected Product']

#Prepare Numbers for Material 2
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 2 Cat']=="Plastics"),
                        'Plast_expired_2']= df_ClientName_Survey['Material 2 Weight per Unit in Grams']*df_ClientName_Survey['Units Expired/Rejected Product']

#Prepare Numbers for Material 3
df_ClientName_Survey.loc[(df_ClientName_Survey['Material 3 Cat']=="Plastics"),
                        'Plast_expired_3']= df_ClientName_Survey['Material 3 Weight per Unit in Grams']*df_ClientName_Survey['Units Expired/Rejected Product']

#Prepare Numbers for Material n
df_ClientName_Survey.loc[(df_ClientName_Survey['Material n Cat']=="Plastics"),
                        'Plast_expired_n']= df_ClientName_Survey['Material n Weight per Unit in Grams']*df_ClientName_Survey['Units Expired/Rejected Product']

#Replace new NAs with zero
df_ClientName_Survey = df_ClientName_Survey.fillna(0)

#This is the column AS -> weight of plastic expired or rejected
df_ClientName_Survey['Plastic_weight_expired'] = df_ClientName_Survey['Plast_expired_1'] + df_ClientName_Survey['Plast_expired_2'] + df_ClientName_Survey['Plast_expired_3'] + df_ClientName_Survey['Plast_expired_n']
df_ClientName_Survey['Plastic_weight_expired'] = df_ClientName_Survey['Plastic_weight_expired'] / 1000

df_ClientName_Survey.head()

# %% [markdown]
# # Step 4: Prepare UK Reporting DataFrame (Single Period)

# %%
#Total weight of chargeable plastic packaging components manufactured in the UK in the accounting period (weight in kgs)
df_ClientName_Survey.loc[~(df_ClientName_Survey['Industry Application']=="Licenced Human Medicines")
                          &(df_ClientName_Survey['Manufactured in UK']=="Yes")
                          &(df_ClientName_Survey['Sales Region(s)']=="United Kingdom")
                          &(df_ClientName_Survey['tot_recycled_plastic'] < 0.3) ,
                        'Man_Plast_Charged']= df_ClientName_Survey['Imp_Tot_weight']

Man_Plast_Charged=df_ClientName_Survey['Man_Plast_Charged'].sum()
Man_Plast_Charged


# %%
#Total weight of finished plastic packaging components imported into the UK in the accounting period (weight in kgs)
df_ClientName_Survey.loc[~(df_ClientName_Survey['Industry Application']=="Licenced Human Medicines")
                          &(df_ClientName_Survey['Imported to UK']=="Yes")
                          &(df_ClientName_Survey['Sales Region(s)']=="United Kingdom")
                          &(df_ClientName_Survey['tot_recycled_plastic'] < 0.3) ,
                        'Imp_Plast_Charged']= df_ClientName_Survey['Imp_Tot_weight']

Imp_Plast_Charged=df_ClientName_Survey['Imp_Plast_Charged'].sum()
Imp_Plast_Charged


# %%
#The total weight of finished plastic packaging components not subject to the tax (weight in kgs)

#Manufactured not charged because Human medicines
df_ClientName_Survey.loc[(df_ClientName_Survey['Industry Application']=="Licenced Human Medicines")
                          &(df_ClientName_Survey['Sales Region(s)']=="United Kingdom"),
                        'MedMan_Plast_NotCharged']= df_ClientName_Survey['Imp_Tot_weight']

MedMan_Plast_NotCharged=df_ClientName_Survey['MedMan_Plast_NotCharged'].sum()
MedMan_Plast_NotCharged

#Manufactured not charged because more than 0.3 recycled plastic
df_ClientName_Survey.loc[~(df_ClientName_Survey['Industry Application']=="Licenced Human Medicines")
                          &(df_ClientName_Survey['Sales Region(s)']=="United Kingdom")
                          &(df_ClientName_Survey['tot_recycled_plastic'] >=0.3),
                        'Man_Plast_NotCharged']= df_ClientName_Survey['Imp_Tot_weight']
Man_Plast_NotCharged=df_ClientName_Survey['Man_Plast_NotCharged'].sum()
Man_Plast_NotCharged

#Plastic not charged because abroad
df_ClientName_Survey.loc[(df_ClientName_Survey['Sales Region(s)']=="Abroad"),
                        'Abroad_NotCharged']= df_ClientName_Survey['Sold_Tot_weight']
Abroad_NotCharged=df_ClientName_Survey['Abroad_NotCharged'].sum()
Abroad_NotCharged

#Print Total Result
tot_not_charged = MedMan_Plast_NotCharged + Man_Plast_NotCharged + Abroad_NotCharged
tot_not_charged

# %%
#Total weight of finished plastic packaging components manufactured or imported for use in the immediate packaging for licenced human medicines (weight in kgs)
df_ClientName_Survey.loc[(df_ClientName_Survey['Industry Application']=="Licenced Human Medicines"),
                        'Med_Plast']= df_ClientName_Survey['Imp_Tot_weight']

Med_Plast=df_ClientName_Survey['Med_Plast'].sum()
Med_Plast

# %%
#Total weight of chargeable plastic packaging components manufactured or imported in this accounting period, which have been exported directly by you during this accounting period and are due to be exported directly by you within the next 12 months (weight in kgs)
df_ClientName_Survey.loc[(df_ClientName_Survey['Sales Region(s)']=="Abroad")
                         &(df_ClientName_Survey['Industry Application']!="Licenced Human Medicines")
                          &(df_ClientName_Survey['tot_recycled_plastic'] <0.3),
                        'Export_Plast']= df_ClientName_Survey['Sold_Tot_weight']
Export_Plast=df_ClientName_Survey['Export_Plast'].sum()
Export_Plast

# %%
#Total weight of any finished plastic packaging components that contain at least 30% recycled plastic content (weight in kgs)
df_ClientName_Survey.loc[(df_ClientName_Survey['tot_recycled_plastic'] >=0.3),
                        'Rec_Plastic_Weight']= df_ClientName_Survey['Imp_Tot_weight']

Rec_Plastic_Weight=df_ClientName_Survey['Rec_Plastic_Weight'].sum()
Rec_Plastic_Weight

# %%
#Total value of taxed plastic packaging components which a credit is being claimed for (value in £)
Credit_Rep1 = 0
Credit_Rep1

# %% [markdown]
# # Step 5: Calculate final Totals

# %%
#Total weight of plastic packaging components which are subject to the tax (weight in kg) after deducting
Total_Tax_Weight = Man_Plast_Charged + Imp_Plast_Charged
Total_Tax_Weight

# %%
#Tax due for this period (value in £) - £200 until 30.03 and £210.82 from 01.04 onwards
PriceperTon = 210.82

Tax_Due_Rep1 = Total_Tax_Weight * PriceperTon/1000 - Credit_Rep1
Tax_Due_Rep1

# %% [markdown]
# # Final Quality Check & Control

# %%
#Check 1
Test1 = Man_Plast_Charged + Imp_Plast_Charged + tot_not_charged
print(Test1)

#Check 2
df_ClientName_Survey.loc[(df_ClientName_Survey['Sales Region(s)']=="United Kingdom"),
                        'Check21']= df_ClientName_Survey['Imp_Tot_weight']

Check21 = df_ClientName_Survey['Check21'].sum()
Check21

df_ClientName_Survey.loc[(df_ClientName_Survey['Sales Region(s)']=="Abroad"),
                        'Check22']= df_ClientName_Survey['Sold_Tot_weight']

Check22=df_ClientName_Survey['Check22'].sum()
Check22

print(Check21 + Check22)


