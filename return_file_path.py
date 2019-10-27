import glob

numfour = glob.glob('/Users/yota/kishimoto_1027/result/result4/*')
numfive = glob.glob('/Users/yota/kishimoto_1027/result/result5/*')

numfour = sorted(numfour)
numfive = sorted(numfive)

for i in range(0,len(numfour)):
    print(numfour[i])

for i in range(0,len(numfive)):
    print(numfive[i])

