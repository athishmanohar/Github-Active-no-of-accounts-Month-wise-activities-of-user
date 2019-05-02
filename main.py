import gityrwise
import jsontocsv
import analyse
import piechart
import plot_user
import pandas as pd
import collections
if __name__ == '__main__':
	data=analyse.Run_Filter()
	print("1:Fechting data and store as json file")
	print("2:convert json to csv")
	print("3:Filter csv")
	print("4:Stats on repository")
	print("5:List top 50 Users")
	print("6:To see particular user activity")
	print("7:Exit")
	x=int(raw_input("Choose your Option:->"))

	def top_users(data):
		temp=data
		temp.sort_values('Total_Commits',inplace=True,ascending=False)
		return temp.head(50)

	def Fetch_Detail(data,y):
		col_list=list(data)
		col_list.remove('Followers')
		col_list.remove('Repo_count')
		col_list.remove('Total_Commits')

		temp=data[col_list]
		#print(temp)
		#index=int(temp[temp['User_ID']==y].index[0])
		#lis=list(temp.iloc[index])
		lis=temp.loc[temp['User_ID'] == y].values
		lis=lis[0]
		#lis=lis.loc[0, :].values.tolist()
		#lis=[lis['User_ID'],lis['User_Name'],lis['First_Month'],lis['Second_Month'],lis['Third_Month'],lis['Fourth_Month'],lis['Fifth_Month'],lis['Sixth_Month'],lis['Seventh_Month'],lis['Eighth_Month'],lis['Ninth_Month'],lis['Tenth_Month'],lis['Eleventh_Month'],lis['Twelveth_Month']]
		
		return lis

	while (x!=7):
		if x==1:
			try:
				gityrwise.Run_Fetch()
			except:
				x=int(raw_input("Choose your Option:->"))
		elif x==2:
			jsontocsv.Run_Convert()
			x=int(raw_input("Choose your Option:->"))
		elif x==3:
			data=analyse.Run_Filter()
			x=int(raw_input("Choose your Option:->"))
		elif x==4:
			piechart.plot_pie()
			x=int(raw_input("Choose your Option:->"))
		elif x==5:
			top_50=top_users(data)
			print(top_50)
			x=int(raw_input("Choose your Option:->"))

		elif x==6:
			y=int(raw_input("Enter user ID:->"))
			lis=Fetch_Detail(data,y)
			#print(lis)
			plot_user.user_activity(lis)
			x=int(raw_input("Choose your Option:->"))
		else:
			x=int(raw_input("Choose your Option:->"))