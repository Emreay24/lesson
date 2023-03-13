students=["Emre AY","Ayse KUM","Ahmet AKSU"]


students.append(input("lutfen eklemek istediğiniz isim giriniz:"))
print(students)

students.remove(input("lütfen çikarmak istediğini kişiyi yaziniz:"))
print(students)

students.extend(["Veli BOŞ","Esra KÜS"])
print(students)

for i in range(len(students)):
    print(students[i])

print("öğrenci Numarasi: ",students.index("Emre AY")," = ","Öğrencinin adi:",students[0])
print("öğrenci Numarasi: ",students.index("Ayse KUM")," = ","Öğrencinin adi:",students[1])
print("öğrenci Numarasi: ",students.index("Ahmet AKSU")," = ","Öğrencinin ad:",students[2])

students.remove("Emre AY")
print(students)