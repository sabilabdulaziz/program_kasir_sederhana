option = []
harga = []
total = []
def menu():
    e = ['food','drink','packet','order','exit']
    print('menu :')
    for i in range(len(e)):
        print(f"({i+1}) {e[i]}")
def food():
    f = ['bakmi jowo WUP ','mie pedas WUP','mie ayam WUP ','mie dok-dok WUP','indomie scotel', 'mie tek tek WUP','ayam kremes','nasi goreng telur WUP','nasi goreng bakso WUP ',' nasi goreng ayam WUP ', ' nasi goreng teri WUP ',' Tongseng sapi WUP ',' nasi telur kornet WUP',' nasi telur kecap / balado WUP ',' ayam bakar maranggi',' spageti', ' lasagna',' makaroni skotel',' nasi kuning WUP ',' kwetiaw goreng WUP']
    b = [18000,12000,17000,17000,16000,17000,18000,18000,19000,20000,23500,30000,18000,13000,18000,20000,40000,30000,12000,17000]
    print('makanan :')
    for i in range(len(f)):
        print(f"({i+1}) {f[i]} - Rp.{b[i]}")

def drink():
    f = ['Robusta COCO WUP','kopi susu aren WUP','capuchino WUP','americano WUP','kopi toraja WUP ','mochachino WUP ','kopi gayo WUP ','mojito','nutrisari ice amrican sweet orange',' ice tea tarik',' ice chocho cadbury WUP',' jahe hangat WUP',' ice thai tea',' melon lemonade',' fresh milk chocho WUP',' green tea latte WUP',' sekoteng anggur WUP']
    b = [18000,17000,16000,14000,20000,14000,14000,9000,6000,9000,13000,7000,8000,8000,15000,15000,11000]
    for i in range(len(f)):
        print(f"({i+1}) {f[i]} - Rp.{b[i]}")

def snack():
    f = ['kebab WUP','sosis jumbo WUP','kentang goreng WUP','omelet keju WUP','bakso kecil halus WUP','nasi 1 porsi WUP','telur ceplok or dadar WUP']
    b = [10000,12000,12000,12000,2500,5000,5000]
    for i in range(len(f)):
        print(f"({i+1}) {f[i]} - Rp.{b[i]}")

def self():
    f=[ 'bento 1 WUP','bento 2 WUP','bento 3 WUP','bento 4 WUP','bento 5 WUP','bento 6 WUP','bento 7 WUP','bento 8 WUP','bento 9 WUP','bento 10 WUP']
    b = [20000,20000,21000,22000,22000,24000,24000,24000,24000,26500]
    for i in range(len(f)):
        print(f"({i+1}) {f[i]} - Rp.{b[i]}")
    
while True:
    menu()
    pilihan = input('masukan pilihan anda : ')

    #makanan menu 
    if pilihan == '1':
        food()
        pilihan2 = input('masukan pilihan makanan anda : ')
        if pilihan2 == '1':
            pilihan3 = input('apakah anda akan membeli makanan bakmi jowo WUP dengan harga 18.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'bakmi jowo WUP'
                b = 18000
                option.append(a)
                harga.append(b)
            else :
                continue
        
        elif pilihan2 == '2':
            pilihan3 = input('apakah anda akan membeli mie pedas WUP dengan harga 12.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'mie pedas WUP'
                b = 12000
                option.append(a)
                harga.append(b)
            else:
                continue
        
        elif pilihan2 == '3':
             
            pilihan3 = input('apakah anda akan membeli mie ayam WUP dengan harga 17.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'mie ayam WUP'
                b = 17000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '4':
             
            pilihan3 = input('apakah anda akan membeli mie dok - dok WUP dengan harga 17.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'mie dok-dok WUP'
                b = 17000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '5':
             
            pilihan3 = input('apakah anda akan membeli indomie scotel dengan harga 16.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'indomie scotel'
                b = 16000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '6':
             
            pilihan3 = input('apakah anda akan membeli mie tek-tek WUP  dengan harga 17.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'mie tek-tek WUP'
                b = 17000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '7':
             
            pilihan3 = input('apakah anda akan membeli ayam kremes WUP  dengan harga 18.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'ayam kremes WUP'
                b = 18000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '8':
             
            pilihan3 = input('apakah anda akan membeli nasi goreng telur WUP  dengan harga 18.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'nasi goreng telur WUP'
                b = 18000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '9':
             
            pilihan3 = input('apakah anda akan membeli nasi goreng bakso WUP  dengan harga 19.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'nasi goreng bakso WUP'
                b = 19000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '10':
             
            pilihan3 = input('apakah anda akan membeli nasi goreng ayam WUP  dengan harga 20.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'nasi goreng ayam WUP'
                b = 20000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '11':
             
            pilihan3 = input('apakah anda akan membeli nasi goreng teri WUP  dengan harga 23.500 ? y/n ')
            if pilihan3 == 'y':
                a = 'nasi goreng teri WUP'
                b = 23500
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '12':
             
            pilihan3 = input('apakah anda akan membeli tongseng sapi dengan harga 30.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'tongseng sapi'
                b = 30000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '13':
             
            pilihan3 = input('apakah anda akan membeli nasi telur kornet WUP dengan harga 18.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'nasi kornet WUP'
                b = 18000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '14':
             
            pilihan3 = input('apakah anda akan membeli nasi telur kecap atau balado dengan harga 13.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'nasi goreng telur kecap atau balado'
                b = 13000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '15':
             
            pilihan3 = input('apakah anda akan membeli ayam bakar maranggi WUP dengan harga 18.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'ayam bakar maranggi WUP'
                b = 18000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '16':
             
            pilihan3 = input('apakah anda akan membeli spageti dengan harga 20.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'spageti'
                b = 20000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '17':
             
            pilihan3 = input('apakah anda akan membeli lasagna dengan harga 40.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'lasagna'
                b = 40000
                option.append(a)
                harga.append(b)
            else:
                continue
        
        elif pilihan2 == '18':
             
            pilihan3 = input('apakah anda akan membeli makaroni skotel dengan harga 30.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'makaroni skotel'
                b = 30000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '19':
             
            pilihan3 = input('apakah anda akan membeli nasi kuning WUP dengan harga 12.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'nasi kuning'
                b = 12000
                option.append(a)
                harga.append(b)
            else:
                continue

        elif pilihan2 == '20':
             
            pilihan3 = input('apakah anda akan membeli kwetiaw goreng WUP dengan harga 17.000 ? y/n ')
            if pilihan3 == 'y':
                a = 'kwetiaw goreng'
                b = 17000
                option.append(a)
                harga.append(b)
            else:
                continue
    elif pilihan == '2':
        drink()
        pilihan2 = input('masukan pilihan anda : ')

        if pilihan2 == '1':
            
            pilihan3 = input('apakah anda akan')

    elif pilihan == '5':
       
        break


print(harga)