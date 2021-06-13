lg="y"
while lg=="y":

    print ("          ")
    print ("cek nilai ")
    n = input("masukan nilai: ")
    if int(n) >= 60:
        sts="lulus"
    else:
        sts="tidak lulus"
    print(sts)
    
    lg=input("cek nilai lagi? y/t.  ")
    if lg=="t":
        break