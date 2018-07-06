if __name__ == "__main__":
    import pandas as pd
    import numpy as np
    data = pd.read_csv('CRDC2013_14.csv',encoding = "Latin-1")
    data['total_enrollment'] = data['TOT_ENR_M']+data['TOT_ENR_F']
    sums=[]
    cols=['SCH_ENR_HI_M','SCH_ENR_HI_F','SCH_ENR_AM_M', 'SCH_ENR_AM_F','SCH_ENR_AS_M', 'SCH_ENR_AS_F', 'SCH_ENR_HP_M', 'SCH_ENR_HP_F', 'SCH_ENR_BL_M', 'SCH_ENR_BL_F', 'SCH_ENR_WH_M', 'SCH_ENR_WH_F', 'SCH_ENR_TR_M', 'SCH_ENR_TR_F']
    for col in cols:
        sums.append(sum(data[col]))
    
    np.asarray(sums)
                    
    all_enrollment = sum(data['total_enrollment'])
                    
    percentages = np.divide(sums,all_enrollment)
    per_race_gender=pd.DataFrame({'column':cols,'percentages': percentages*100})    
    print(per_race_gender)