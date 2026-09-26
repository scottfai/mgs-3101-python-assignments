coffee_shop_name= "Eliza Coffee Shop"

drinks_purchased = 100
price_per_drink = 5

pasties_purchased = 50
price_per_pastry = 3

drink_revenue= drinks_purchased * price_per_drink
pastry_revenue= pastries_puchased* price_per_pastry

total_revenue = drink_revenue + pastry_revenue

print("Shop Name:", coffee_shop_name)
print("drink Revenue:", drink_revenue)
print("pastry Revenue:", pastry_revenue)
print("total Revenue:", total_revenue)

file = open("analysis_report.txt", "r")
print(file.read())
file.close()

if total_revenue >= 500:
    print("Revenue is at least $500")
else:
     print("Revenue is less than $500")

print("Drinks Purchased:", drinks_purchased)
print("Pastries Purchased:", pastries_purchased)

if drinks_purchased > pastries_purchased:

print("Recommendation: Sell more drinks.")

else:
     print("Recommendation: Sell more pastries.")
