totalPrice = int(input("ราคาสินค้าทั้งหมด :"))
def vatCalculate(totalPrice):
    result =totalPrice+(totalPrice*7/100)
    return result
print(vatCalculate(totalPrice))