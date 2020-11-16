from matplotlib import pyplot as plt
import random
Capacity_K = 10000
population_a = [9900]
population_b = [99]
population_c = [9900]

rate_a = 0.7
rate_b = 1.5
rate_c = 0.04

x, y, new_c = 0.4, 0.4, 0
x_list=[0.4]
proportion = [0.99]
for i in range(1, 151):
    new_a = rate_a * population_a[-1] * (1 - ((population_a[-1] + 1.06*population_b[-1]) / Capacity_K))
    new_b = rate_b * population_b[-1] * (1 - ((population_b[-1] + 0.94*population_a[-1]) / Capacity_K))
    population_a.append(int(population_a[-1] + new_a))
    population_b.append(int(population_b[-1] + new_b))
    proportion.append(population_a[-1] / (population_b[-1] + population_a[-1]))

    temp_c = population_c[-1]+new_c
    short = int((4*x*(1-x)*y*(1-y)+2*(1-x)*(1-x)*y*(1-y)+2*(1-y)*(1-y)*x*(1-x)+2*x*(1-x)*y*y+2*y*(1-y)*x*x+x*x*(1-y)*(1-y)+y*y*(1-y)*(1-y)+(1-x)*(1-x)*(1-y)*(1-y))*temp_c)
    long = int(x*x*y*y*temp_c)
    population_c.append(int(temp_c-short*(1-proportion[-1])))
    # if population_c[-1]<1000:
    #     population_c[-1] = population_c[-1] + random.randint(-500,500)
    x = pow((long/population_c[-1]),0.25)
    y = x
    x_list.append(x)
    new_c = rate_c * population_c[-1] * (1 - (population_c[-1] / Capacity_K))

    plt.cla()
    fig,ax = plt.subplots()
    plt.title("changes in 150 years")
    plt.grid(True)
    plt.xlabel("year(s)")
    plt.ylabel("population")
    plt.xlim(0,i+5)
    plt.ylim(0,10000)
    plt.plot(range(0,i+1), population_a, "b-", linewidth=2.0, label="species A")
    plt.plot(range(0,i+1), population_b, "g-", linewidth=2.0, label="species B")
    plt.plot(range(0,i+1), population_c, "r-", linewidth=2.0, label="species C")
    plt.plot(range(0,i+1), [j * 10000 for j in x_list], "m-", linewidth=2.0, label="proportion")
    legend = plt.legend(loc = 2,bbox_to_anchor=(1.05,0.5),borderaxespad = 0., shadow=True)
    legend.legendHandles[0]._legmarker.set_markersize(10)
    legend.legendHandles[1]._legmarker.set_markersize(16)
    fig.subplots_adjust(right=0.75)
    plt.pause(0.001)
    plt.ioff()
    fig.savefig(r"C:\Users\glen_\Desktop\生物进化论期中作业\动图合成\\"+str(i)+".png",dpi=600)
print("a:",population_a,"\nb:",population_b,"\nc:",population_c,"\np:",proportion)
print(x)