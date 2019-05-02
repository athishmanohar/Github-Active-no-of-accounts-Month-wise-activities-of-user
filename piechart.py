import matplotlib.pyplot as plt
def plot_pie():
	labels = 'total_repositories', 'scanned_repositories', 'sample_repositories', 'active_repositores'
	titlees ='50_million','4_million','4_thousand','250'
	sizes = [90, 5, 3, 1]
	explode = (0, 0, 0, 0.2)
	colors = ['lightskyblue', 'yellowgreen', 'lightcoral', 'red']  

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=titlees,
	        shadow=True, startangle=90,colors=colors)
	ax1.axis('equal') 
	plt.legend(labels,loc="best",
	            title="Legend", fancybox=True)
	plt.show()
