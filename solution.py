hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#calc average
total_price = 0
for price in prices:
  total_price += price
average_price = total_price/len(prices)

#output meth
def message (m1, average):
  return m1 + str(average)

print(message("Average Haircut Price: $", average_price))

#adjust price
new_prices = [price - 5 for price in prices]
print(message("New Prices: ", new_prices))

#calc revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print(message("Total Revenue: $", total_revenue))

#calc avg rev
average_daily_revenue = total_revenue/7

#marketing
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)-1) if new_prices[i] < 30]
print(message("Cuts Under 30 to Advertize: ", cuts_under_30))
