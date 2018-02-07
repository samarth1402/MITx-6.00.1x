import pylab as plt

#codse to fill the lists
mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []
for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i ** 2)
    myCubic.append(i ** 3)
    myExponential.append(1.5 ** i)



plt.figure('linear')    #each fig is a different graph
plt.clf()               #clears prev graph before execution
plt.title('lin')        #title to the grpah
plt.xlabel('sample points') #x axis
plt.ylabel('linear function') #y axis 
plt.ylim(0, 50)         #setting limit for y axis
plt.plot(mySamples,myLinear)    #plotting graph

plt.figure('quad')
plt.clf()
plt.ylabel('quadratic function')
plt.ylim(0,1000)
plt.plot(mySamples,myQuadratic)

plt.figure('cube')
plt.clf()
plt.plot(mySamples,myCubic)

plt.figure('expo')
plt.clf()
plt.plot(mySamples,myExponential)

plt.figure('quad')  #can be reaccessed by mentioning figure name
plt.title('Quadratic')

plt.figure('lin quad')
plt.clf()
plt.title('Linear vs Quadratic')
plt.subplot(211)    #creating subplots
plt.ylim(0, 900)
plt.plot(mySamples, myLinear, 'b-', label = 'Linear', linewidth = 2.0)  #'b-' line type, label for graph, linewidth
plt.subplot(212)
plt.ylim(0,900)
plt.plot(mySamples, myQuadratic, 'ro', label = 'quadratic', linewidth = 3.0)
plt.legend(loc = 'upper left')  #legend location for labels

plt.figure('cube exp')
plt.clf()
plt.title('Cubic vs Exponential')
plt.subplot(121)
plt.ylim(0, 140000)
plt.plot(mySamples, myCubic,'g^', label = 'cubic', linewidth = 4.0)
plt.subplot(122)
plt.ylim(0, 140000)
plt.plot(mySamples, myExponential,'r--', label = 'exponential', linewidth = 5.0)
plt.legend()    # will let comp decide location

plt.figure('cube exp log')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 2.0)
plt.plot(mySamples, myExponential, 'r', label = 'exponential', linewidth = 4.0)
plt.yscale('log')   #changing scale of y axis
plt.legend()
plt.title('Cubic vs Exponential in log scale')