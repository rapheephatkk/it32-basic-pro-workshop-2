a = input("Enter name : ")
b = int(input("Enter age : "))
c = int(input("Enter height : "))
d = int(input("Enter power : "))
e = int(input("Enter money : "))
if a == a and b <= 15 and c <= 160 and d <= 5 and e <= 5:
    print("---- ผลพิจารณา ----")
    print(f"ยินดีต้อนรับ {a} ตำแหน่งของแกคือ : ภารโรงล้างจาน")
elif a == a and b <= 18 and c <= 170 and d <= 7 and e <= 7:
    print("---- ผลพิจารณา ----")
    print(f"ยินดีต้อนรับ {a} ตำแหน่งของแกคือ : ลูกกะจ๊อก")
else :
    print("---- ผลพิจารณา ----")
    print(f"ยินดีต้อนรับ {a} ตำแหน่งของแกคือ : ลูกน้องมาเฟีย")