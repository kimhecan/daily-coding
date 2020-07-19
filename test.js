def stockPairs(stocksProfit, target):
newArr = []
count = 0
stocksProfit.sort()
for i in range(len(stocksProfit) - 1):
  if stocksProfit[i] + stocksProfit[-1] < target:
    continue
for j in range(i + 1, len(stocksProfit)):
  if stocksProfit[i] + stocksProfit[j] == target:
    if (stocksProfit[i], stocksProfit[j]) not in newArr:
newArr.append((stocksProfit[i], stocksProfit[j]))
count += 1
return count


function stockPairs(stocksProfit, target) {
  // Write your code here

}