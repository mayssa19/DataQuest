if __name__ == "__main__":
    import pandas as pd
    data = pd.read_csv('CRDC2013_14.csv',encoding = "Latin-1")
    print("The number of schools that fall within Juvenile Justice category: ",data['JJ'].value_counts())
    print("The number of schools that fall within magnet school category: ",data['SCH_STATUS_MAGNET'].value_counts())
    
    table1 = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")
    table2 = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum")
    
    print(table1)
    print(table2)