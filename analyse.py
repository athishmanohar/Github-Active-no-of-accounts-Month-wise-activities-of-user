import pandas as pd
def Run_Filter():	
	train=pd.read_csv("data.csv")
	#print(train.describe())
	active=train[(train.First_Month>0) | (train.Second_Month>0)|(train.Third_Month>0 )|(train.Fourth_Month>0 )|(train.Fifth_Month>0 )|(train.Sixth_Month>0 )|(train.Seventh_Month>0 )|(train.Eighth_Month>0 )|(train.Ninth_Month>0 )|(train.Tenth_Month>0) |(train.Eleventh_Month>0) |(train.Twelveth_Month>0) ]
	selected=active[['User_ID','User_Name','Followers','First_Month','Second_Month','Third_Month','Fourth_Month','Fifth_Month','Sixth_Month','Seventh_Month','Eighth_Month','Ninth_Month','Tenth_Month','Eleventh_Month','Twelveth_Month']]
	count=selected.groupby('User_ID')['User_Name'].count()
	lis=list(count)
	selected=selected.groupby(['User_ID','User_Name'],as_index=False)[['Followers','First_Month','Second_Month','Third_Month','Fourth_Month','Fifth_Month','Sixth_Month','Seventh_Month','Eighth_Month','Ninth_Month','Tenth_Month','Eleventh_Month','Twelveth_Month']].sum()
	selected['Repo_count']=lis
	col_list=list(selected)
	col_list.remove('User_ID')
	col_list.remove('User_Name')
	col_list.remove('Followers')
	col_list.remove('Repo_count')
	selected['Total_Commits']=selected[col_list].sum(axis=1)
	#print(selected)
	#print(list(selected.iloc[193]))
	return selected

