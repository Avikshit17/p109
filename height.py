import pandas as pd
import statistics
df=pd.read_csv("height-weight.csv")
height=df["Height(Inches)"].tolist()
mean=statistics.mean(height)
std=statistics.stdev(height)
# sftd_sp=mean-std
# sftd_ep=mean+std
# sftd_count=0
# for eachdata in height:
#     if(eachdata>=sftd_sp and eachdata<sftd_ep):
#         sftd_count=sftd_count+1
# percentage=(sftd_count/len(height))*100
# print(percentage)



# sstd_sp=mean-(2*std)
# sstd_ep=mean+(2*std)
# sstd_count=0
# for eachdata in height:
#     if(eachdata>=sstd_sp and eachdata<sstd_ep):
#         sstd_count=sstd_count+1
# percentage=(sstd_count/len(height))*100
# print(percentage)



tftd_sp=mean-(3*std)
tftd_ep=mean+(3*std)
tftd_count=0
for eachdata in height:
    if(eachdata>=tftd_sp and eachdata<tftd_ep):
        tftd_count=tftd_count+1
percentage=(tftd_count/len(height))*100
print(percentage)