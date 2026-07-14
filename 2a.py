quantity = int(input("จำนวนปืนที่รับมาขาย : "))
cost_price = int(input("ต้นทุนของปืนที่รับมา : "))
sell_price = int(input("ราคาที่จะนำไปขายต่อ : "))
team_members = int(input("จำนวนลูกน้องที่ในที่มีไปทำงาน : "))

a = quantity * cost_price
b = sell_price * quantity
c = b - a
d = c // team_members
e = (c - d) // team_members

print(f"ต้นทุนทั้งหมด {a}: บาท")
print(f"รายรับทั้งหมด {b}: บาท")
print(f"กำไรสุทธิ : {c} บาท")
print(f"จำนวนเงินที่หักไปให้บอส  : {d} บาท")
print(f"จำนวนเงินที่ลูกน้องแต่ละคนได้  : {e} บาท")