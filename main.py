from Math import myStatistics

X = []

for i in range(5):
  X.append(int(input("請輸第"+str(i+1)+"個數字：")))

print(myStatistics.myMean(X))
