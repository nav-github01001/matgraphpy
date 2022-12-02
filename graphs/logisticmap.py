# For an example of how this look like in specific settings, go to Images directory
import matplotlib.pyplot as plt
# You may adjust the setting below
init_percentage= .7
rate = 3.8
iterations = 50
# You should not adjust these settings
x = []
y = []
for year in range(iterations):
    x.append(year)
    if year==0:
        percentage = init_percentage
    elif year==1:
        percentage = rate*init_percentage*(1-init_percentage)
    else:
        percentage = rate*y[-1]*(1-y[-1])

    y.append(percentage)
    print(f"{year} - {percentage*100}%")

  

plt.plot(x,y)
plt.ylabel('theoretical population %')
plt.xlabel('Year')
plt.show()
