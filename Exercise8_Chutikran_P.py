usernameInput = input("username :")
passwordInput = input("password :")
if usernameInput == "admin" and passwordInput == "1234" :
    print("ยินดีต้อนรับเข้าสู่ร้านค้าของเรา")
    print("--------------------")
    print("รายการสินค้า")
    print("1.ปลากระป๋อง 30 บาท")
    print("2.น้ำอัดลม 15 บาท")
    print("3.ไอศกรีม  10 บาท")
    userSelected = int(input("กรุณาใส่รหัสเมนูสินค้า :"))
    if userSelected == 1:
        x = int(input("ต้องการซื้อกี่จำนวน :"))
        print("รวมราคา",30*x,"บาท")
    elif userSelected == 2:
        y = int(input("ต้องการซื้อกี่จำนวน :"))
        print("รวมราคา",15 * y,"บาท")
    elif userSelected == 3:
        z = int(input("ต้องการซื้อกี่จำนวน :"))
        print("ทั้งหมดราคา",10 * z,"บาท")