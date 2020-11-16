from matplotlib import pyplot as plt
Capacity_K = 10000
population_a = [9900]
population_b = [99]
rate_a = 0.7
rate_b = 1.5
proportion = [0.99]
for i in range(1, 151):
    new_a = rate_a * population_a[-1] * (1 - ((population_a[-1] + 1.06*population_b[-1]) / Capacity_K))
    new_b = rate_b * population_b[-1] * (1 - ((population_b[-1] + 0.94*population_a[-1]) / Capacity_K))
    population_a.append(int(population_a[-1] + new_a))
    population_b.append(int(population_b[-1] + new_b))
    proportion.append(population_a[-1] / (population_b[-1] + population_a[-1]))
    plt.cla()
    plt.title("Competition Between A and B")
    plt.grid(True)
    plt.xlabel("year(s)")
    plt.ylabel("population")
    plt.xlim(0,i+5)
    plt.ylim(0,10000)
    plt.plot(range(0,i+1), population_a, "b-", linewidth=2.0, label="species A")
    plt.plot(range(0,i+1), population_b, "g-", linewidth=2.0, label="species B")
    #plt.plot(range(0,i+1), [j * 10000 for j in proportion], "r-", linewidth=2.0, label="proportion")
    plt.legend(loc="center left", shadow=True)
    plt.pause(0.001)
plt.ioff()
plt.show()
print("year | population of A | population of B | propotion of A")
print(":------------: | :------------: | :-------------: | :------------:")
for index, each in enumerate(population_a):
    print(index+1,'|',each,'|',population_b[index],"|",round(proportion[index],4))