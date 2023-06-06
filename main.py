import random

yazi = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre_uzunlugu = int(input("Şifre uzunluğu ne kadar olsun: "))


for _ in range(sifre_uzunlugu):
    print(random.choice(yazi), end="")

