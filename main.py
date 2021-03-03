from myMath import myStatistics

X = []

for i in range(5):
  X.append(int(input("請輸第"+str(i+1)+"個數字：")))

print("5數平均為：",myStatistics.myMean(X))
