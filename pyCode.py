import csv

# Untuk memberikan nilai pada pelayanan suatu restoran
nilaiRendah = 0
nilaiStandar = 0
nilaiTinggi = 0
# ----------------------------------------------------

# Untuk memberikan nilai pada makanan suatu restoran
nilaiKecil = 0
nilaiSedang = 0
nilaiBesar = 0
# ----------------------------------------------------

# Untuk perhitungan dari hasil nilai
nilaiSatu = 0
nilaiDua = 0
# ----------------------------------------------------

# Untuk memberikan nilai kepada sebuah pelayanan dalam range 1-100


def fuzzifikasiPelayanan(nLayanan):
    global nilaiRendah, nilaiStandar, nilaiTinggi

    if (nLayanan > 0 and nLayanan <= 15):
        nilaiRendah = 1
        nilaiStandar = 0
        nilaiTinggi = 0
    elif (nLayanan > 15 and nLayanan <= 30):
        nilaiRendah = (30 - nLayanan) / (30 - 15)
        nilaiStandar = 0
        nilaiTinggi = 0
    elif (nLayanan > 30 and nLayanan <= 45):
        nilaiRendah = 0
        nilaiStandar = (nLayanan - 30) / (45 - 30)
        nilaiTinggi = 0
    elif (nLayanan > 45 and nLayanan <= 60):
        nilaiRendah = 0
        nilaiStandar = 1
        nilaiTinggi = 0
    elif (nLayanan > 60 and nLayanan <= 75):
        nilaiRendah = 0
        nilaiStandar = (75 - nLayanan) / (75 - 60)
        nilaiTinggi = 0
    elif (nLayanan > 75 and nLayanan <= 90):
        nilaiRendah = 0
        nilaiStandar = 0
        nilaiTinggi = (nLayanan - 75) / (90 - 75)
    elif (nLayanan > 90 and nLayanan <= 100):
        nilaiRendah = 0
        nilaiStandar = 0
        nilaiTinggi = 1

    return [nilaiRendah, nilaiStandar, nilaiTinggi]


def fuzzifikasiMakanan(nMakan):
    global nilaiKecil, nilaiSedang, nilaiBesar

    if (nMakan <= 1.5):
        nilaiKecil = 1
        nilaiSedang = 0
        nilaiBesar = 0
    elif (nMakan <= 3):
        nilaiKecil = (3 - nMakan) / (3 - 1.5)
        nilaiSedang = 0
        nilaiBesar = 0
    elif (nMakan <= 4.5):
        nilaiKecil = 0
        nilaiSedang = (nMakan - 3) / (4.5 - 3)
        nilaiBesar = 0
    elif nMakan > 4.5 and nMakan <= 6:
        nilaiKecil = 0
        nilaiSedang = 1
        nilaiBesar = 0
    elif nMakan > 6 and nMakan <= 7.5:
        nilaiKecil = 0
        nilaiSedang = (7.5 - nMakan) / (7.5 - 6)
        nilaiBesar = 0
    elif nMakan > 7.5 and nMakan <= 9:
        nilaiKecil = 0
        nilaiSedang = 0
        nilaiBesar = (nMakan - 7.5) / (9 - 7.5)
    elif nMakan > 9 and nMakan <= 10:
        nilaiKecil = 0
        nilaiSedang = 0
        nilaiBesar = 1
    return [nilaiKecil, nilaiSedang, nilaiBesar]


def ruleInferensi(nilaiRendah, nilaiStandar, nilaiTinggi, nilaiKecil, nilaiSedang, nilaiBesar):
    global hasilSatu, hasilDua

    x1 = min(nilaiTinggi, nilaiBesar)
    x2 = min(nilaiTinggi, nilaiSedang)
    y1 = min(nilaiTinggi, nilaiKecil)
    x3 = min(nilaiStandar, nilaiBesar)
    x4 = min(nilaiStandar, nilaiSedang)
    y2 = min(nilaiStandar, nilaiKecil)
    x5 = min(nilaiRendah, nilaiBesar)
    x6 = min(nilaiRendah, nilaiSedang)
    y3 = min(nilaiRendah, nilaiKecil)
    hasilSatu = max(x1, x2, x3, x4, x5, x6)
    hasilDua = max(y1, y2, y3)

    return [hasilSatu, hasilDua]


def SugenoDefuzzyfikasi(nilaiSatu, nilaiDua, batas):
    global hasilNilai
    hasilNilaiSatu = float((nilaiSatu * 50) + (nilaiDua * 100))
    hasilNilaiDua = float((nilaiSatu + nilaiDua))
    if (hasilNilaiSatu == 0 and hasilNilaiDua == 0):
        a = 0
    else:
        a = hasilNilaiSatu/hasilNilaiDua

    if a >= 70 and a < 100:
        hasilNilai.append(i)
    elif a == 100:
        hasilNilai.append(i)
    return hasilNilai


def Output():
    for i in range(0, len(hasilNilai)):
        fuzzifikasiPelayanan(nLayanan=hasilNilai[i][1])
        fuzzifikasiMakanan(nMakan=hasilNilai[i][2])
        ruleInferensi(nilaiRendah, nilaiStandar, nilaiTinggi, nilaiKecil, nilaiSedang, nilaiBesar)
        SugenoDefuzzyfikasi(nilaiSatu, nilaiDua, i)
    return SugenoDefuzzyfikasi(nilaiSatu, nilaiDua, i)


# Nilai untuk pelayanan
nilaiRendah = 0
nilaiStandar = 0
nilaiTinggi = 0
# ----------------------------------------------------

# Nilai untuk makanan
nilaiKecil = 0
nilaiSedang = 0
nilaiBesar = 0
# ----------------------------------------------------

# Nilai akhir
nilaiSatu = 0
nilaiDua = 0
bantuan = []
listBantuan = []
# ----------------------------------------------------

labelKolom = ['id', 'pelayanan', 'makanan']
with open('restoran.csv') as rdFile:
    rdFile = csv.reader(rdFile, delimiter=',')
    count = 0
    x = []
    pelayanan = []
    makanan = []
    for row in rdFile:
        if count == 0:
            count += 1
        else:
            x.append(int(row[0]))
            pelayanan.append(float(row[1]))
            count = 0
            x = []
            pelayanan = []
            makanan = []
            for row in rdFile:
                if count == 0:
                    count += 1
                else:
                    x.append(int(row[0]))
                    pelayanan.append(float(row[1]))
                    makanan.append(float(row[2]))

hasilNilai = []
for i in range(0, len(pelayanan)):
    hasilNilai.append([x[i], pelayanan[i], makanan[i]])


with open('BestRestoran.csv', 'w') as newFile:
    tulisFile = csv.writer(newFile, delimiter=',')
    for i in range(0, 5):
        tulisFile.writerow([Output()[i][0]])
        tulisFile.writerow([Output()[i][1]])

print("BestRestoran.csv is ready!")
