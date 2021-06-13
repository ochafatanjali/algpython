lg="y"
while lg=="y":
    print("                ")
    print("cek tingkat usia")
    u = input("masukan usia: ")
    if int(u)>=60: sts ="Lansia"
    elif int(u)>=35: sts ="Dewasa"
    elif int(u)>=18: sts ="Pemuda"
    elif int(u)>=15: sts ="Remaja"
    else:
        sts = "anak"
    print(sts) 

    lg=input("coba lagi ? y/t.  ")
    if lg=="t":
        break