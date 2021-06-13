lg="y"
while lg=="y":
    harga=660000
    print("            ")
    print("jual printer")
    jumlah=int(input("beli berapa printer? "))
    total=harga*jumlah
    print("total yang harus dibayarkan Rp.",total)

    lg=input("beli lagi? y/t. ")
    if lg=="t":
        break