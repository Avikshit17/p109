import random
import plotly.figure_factory as pf
import statistics
num=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    sum=dice1+dice2
    num.append(sum)
# graph=pf.create_distplot([num],["number"],show_hist=False)
# graph.show()
mean=statistics.mean(num)
std=statistics.stdev(num)
# fstd_sp=mean-std
# fstd_ep=mean+std
# fstd_count=0
# for eachdata in num:
#     if(eachdata>=fstd_sp and eachdata<fstd_ep):
#         fstd_count=fstd_count+1
# percentage=(fstd_count/len(num))*100
# print(percentage)


# sstd_sp=mean-(2*std)
# sstd_ep=mean+(2*std)
# sstd_count=0
# for eachdata in num:
#     if(eachdata>=sstd_sp and eachdata<sstd_ep):
#         sstd_count=sstd_count+1
# percentage=(sstd_count/len(num))*100
# print(percentage)

tstd_sp=mean-(3*std)
tstd_ep=mean+(3*std)
tstd_count=0
for eachdata in num:
    if(eachdata>=tstd_sp and eachdata<tstd_ep):
        tstd_count=tstd_count+1
percentage=(tstd_count/len(num))*100
print(percentage)
    

