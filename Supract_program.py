def calculate_total_cost(price_per_item,quantity,tax_rate):
    result = price_per_item*quantity
    rate=result-60
    return rate
    
    
per=int(input ("how much price : "))
qun=int(input ("how many quantity : "))
tax=int(input("how much tax : "))
print("it is total cast",calculate_total_cost(price_per_item=per,quantity=qun,tax_rate=tax))
