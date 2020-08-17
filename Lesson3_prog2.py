a_str = input("Введите слово: ")
b_str = input("Введите символ: ")
chr_list = list(b_str)
a = 0
for chr in a_str:
    if b_str == chr:
        a += 1
if a > 0:
    print("here")
else:
    print("Isnt here")