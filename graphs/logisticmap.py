# For an example of how this look like in specific settings, go to Images directory
import matplotlib.pyplot as plt
# You may adjust the setting below
init_percentage= .7
rate = 3.8
iterations = 50
# You should not adjust these settings
years = []
percentages = []
for year in range(iterations+1):
    years.append(year)
    if year==0:
        percentage = init_percentage
    elif year==1:
        percentage = rate*init_percentage*(1-init_percentage)
    else:
        percentage = rate*percentages[-1]*(1-percentages[-1])

    percentages.append(percentage)
    print(f"{year} - {percentage*100}%")

  

plt.plot(years,percentages)
plt.ylabel('Value%')
plt.xlabel('Year')
plt.title(f"Percentage graph for {iterations} years \nif initial_percentage = {init_percentage*100}% and Growth Rate = {rate}")
plt.show()
