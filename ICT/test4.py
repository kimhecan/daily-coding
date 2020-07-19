def stockPairs(stocksProfit, target):
    stocksProfit.sort()
    result = []
    a, b = 0, len(stocksProfit) - 1

    while a < b:
        sums = stocksProfit[a] + stocksProfit[b]
        if sums == target:
            result.append((stocksProfit[a], stocksProfit[b]))
            a += 1
            b -= 1
        elif sums > target:
            b -= 1
        else:
            a += 1
    return len(set(result))
