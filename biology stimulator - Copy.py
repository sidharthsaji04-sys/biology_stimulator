import matplotlib.pyplot as plt
n=int(input('enter the sperm count: '))
p=float(input('enter the probability of success chance of each sperm(0-1): '))
time=[]
probability=[]
max_probability=0
best_time=0
for t in range(13):
    egg_probability=(1-t/12)**3
    n = n * 0.9
    p_effective = p * egg_probability
    t_p = 1 - (1 - p_effective) ** n
    time.append(t)
    probability.append(t_p)
    if max_probability<t_p:
        max_probability=t_p
        best_time=t

print(f'best time: Hour {best_time}. Max probability: {max_probability}%')

plt.plot(time, probability)
plt.xlabel("Time (hours)")
plt.ylabel("Fertilization Probability")
plt.title("Fertilization Probability vs Time")
plt.show()




