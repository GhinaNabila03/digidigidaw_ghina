def garis () :
    print ("---------------------------------------")

#fungsi bubble sort ascreding (dari kecil ke besar)
def sort_asc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range (n-i-1):
            #membandingkan masing" elemen ke kanan
            if array [j] > array[j+i]:
                #jika lebih besar tuker ke kiri
                array[j], array[j+1] =  array[j+1], array[j]
    return array

#fungsi bubble sort descending (dari besar kecil)

def sort_desc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range (n-i-1):
            #membandingkan masing" elemen ke kanan
            if array [j] < array[j+i]:
                #jika lebih besar tuker ke kiri
                array[j], array[j+1] =  array[j+1], array[j]
    return array

#fungsi rata rata
def rata_rata(angka):
    return sum(angka)/len(angka)

#input nilai
garis()
print("masukan tiga buah nilai")
nama = (input("Masukan Nama Anda : "))
nilai_a = int(input("Nilai A : "))
nilai_b = int(input("Nilai B : "))
nilai_c = int(input("Nilai C : "))
nilai_d = int(input("Nilai D : "))
nilai_e = int(input("Nilai E : "))
nilai_f = int(input("Nilai F : "))
nilai_g = int(input("Nilai G : "))
nilai_h = int(input("Nilai H : "))
nilai_i = int(input("Nilai I : "))
nilai_j = int(input("Nilai J : "))
angka = [nilai_a, nilai_b, nilai_c, nilai_d, nilai_e, nilai_f,nilai_g, nilai_h, nilai_i, nilai_j]
garis()
print()

#nilai akhir
print("HASIL AKHIR----")
#nama
print("Nama Anda : ",(nama))
print("Urutan Angka ascending : ",(sort_asc(angka)))
print ("Urutan Angka descending : ",(sort_desc(angka)))

#angka terbesar
print("Angka Terbesar : ", max(angka))

#angka terkecil
print("Angka Terkecil : ", min(angka))

#rata rata
print("Rata Rata : ",round(rata_rata(angka)))



















