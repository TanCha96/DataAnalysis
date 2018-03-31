import scipy as sc
import matplotlib.pyplot as plt

data = sc.genfromtxt("web_traffic.tsv", delimiter="\t")
x = data[:,0]
y = data[:,1]

x=x[~sc.isnan(y)]
y=y[~sc.isnan(y)]

plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i'%w for w in range(10)] )
plt.autoscale(tight=True)
plt.grid()
#plt.show()

def error(f,x,y):
    return sc.sum((f(x)-y)**2)



fp1, residuals, rank,sv, rcond = sc.polyfit(x,y,1,full = True)

f1 = sc.poly1d(fp1)
fx = sc.linspace(0,x[-1],1000)
plt.plot(fx,f1(fx), linewidth = 4,color = 'green')
plt.legend(["d=%i"%f1.order], loc = "upper left")
#plt.show()

f2p = sc.polyfit(x,y,2)
f3 = sc.poly1d(f2p)
fx= sc.linspace(0,x[-1],1000)
plt.plot(fx, f1(fx), linewidth = 4, color= 'red')
plt.legend(["d=%i"%f3.order],loc = "upper left" )
plt.show()
