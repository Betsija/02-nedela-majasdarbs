print(int("7") - int("5"))
print(int("34") + int("8")- int("3"))

x = 17
y = 2
print(x/y)
print(x//y)
print(x*y)
print(x**y)
print(x%y)
x1 = 200
y1 = 800
print(x1%y1)
k = 3
l = [4, 6, 8]
m = "Liene"
print(type(k))
print(type(l))
print(type(m))
a = 8
b = 3
print(type(a) == type(b))
print("Abi ir integrāļi")
c = 8
d = 3.5
print(type(c) == type(d))
print("Otrs ir decimālis - float")
f = 7
g = 2
print(f != y)
print("Skaitļi nav vienādi")
h = 2
i = 3
print(h >= i)
print("Skaitlis h nav lielāks vai vienāds ar i\n")
j = 3
print(j < 2 or j > 4)
print("Skaitlis j nav mazāks par 2 un nav lielāks par 4")  
print(j > 2 and j < 4)
print("Skaitlis j ir lielāks par 2 un mazāks par 4")
print(j < 2 or j > 4)
print("Skaitlis j nav mazāks par 2 un nav lielāks par 4\n\n")
print(bool([1, 2, 3]))

print(bool([])) # False (tukšs saraksts)

print(int("3")) # ValueError, jo 3.14 nebija vesels skaitlis

print(int(3.86)) # 3 ('norauj' beigas, nenotiek apaļošana)


print(int(float("3.14")))

print(0.1 + 0.2 == 0.3) # False, kāpēc?
# Šī problēma rodas tāpēc, ka 0.1 un 0.2 nevar precīzi attēlot binārajā formā, un rezultāts ir nedaudz mazāks par 0.3, kas izraisa salīdzinājuma kļūdu.
print(round(2.5)) # 2

print(round(3.5)) # 4
print(round(8.5)) # 8 - 8.5 tiek noapaļots uz leju, jo tas ir pāra skaitlis (8), savukārt 9.5 tiek noapaļots uz augšu, jo tas ir nepāra skaitlis (9).

print(round(9.5)) # 10 - 9.5 tiek noapaļots uz augšu, jo tas ir nepāra skaitlis (9). Šī metode samazina dažādas kļūdas.


























