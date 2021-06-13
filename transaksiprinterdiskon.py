lg="y"
while lg=="y":
    harga=660000
    print("            ")
    print("jual printer")
    jumlah=int(input("beli berapa printer? "))
    total=harga*jumlah
    print("total yang harus dibayarkan Rp.",total)
    if total>=1500000:
        diskon=total*0.15
        distot=total-diskon
        print("selamat karena pembelian mencapai Rp1500000 anda dapat diskon Rp.",diskon)
        print("total yang harus dibayarkan Rp.",distot)
    lg=input("beli lagi? y/t. ")
    if lg=="t":
        break