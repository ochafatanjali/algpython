lg="y"
while lg=="y":
    print("                   ")
    print("Penilaian Mahasiswa")
    n = input("masukan nilai: ")
    if int(n)>0 and int(n)<=100:
        if int(n)>=90 and int(n)<=100: sts ="A"
        elif int(n)>=80 and int(n)<=89: sts ="B"
        elif int(n)>=70 and int(n)<=79: sts ="C"
        else:
            sts = "D"
        print(sts) 
    else:
        pesan="maaf nilai mahasiswa hanya 0-100"
        print(pesan)

    lg=input("coba lagi ? y/t.  ")
    if lg=="t":
        break