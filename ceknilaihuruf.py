lg="y"
while lg=="y":
    print("               ")
    print("cek nilai huruf")
    n = input("masukan nilai: ")
    if int(n)>0 and int(n)<=100:
        if int(n)>80: sts ="Baik Sekali"
        elif int(n)>=65: sts ="Baik"
        elif int(n)>=55: sts ="Cukup"
        elif int(n)>=40: sts ="Kurang"
        else:
            sts = "kurang sekali"
        print(sts) 
    else:
        pesan="maaf nilai huruf hanya 0-100"
        print(pesan)

    lg=input("coba lagi ? y/t.  ")
    if lg=="t":
        break