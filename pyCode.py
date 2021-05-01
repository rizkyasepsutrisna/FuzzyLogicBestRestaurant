import os
import pandas as pd
import csv

pRendah = 0
pStandar = 0
pTinggi = 0
mKecil = 0
mSedang = 0
mBesar = 0
N1 = 0
N2 = 0


def fuzzifikasiPelayanan(nPelayanann):
    global pRendah, pStandar, pTinggi

    if (nPelayanann > 0 and nPelayanann <= 15):
        pRendah = 1
        pStandar = 0
        pTinggi = 0
    elif (nPelayanann > 15 and nPelayanann <= 30):
        pRendah = (30 - nPelayanann) / (30 - 15)
        pStandar = 0
        pTinggi = 0
    elif (nPelayanann > 30 and nPelayanann <= 45):
        pRendah = 0
        pStandar = (nPelayanann - 30) / (45 - 30)
        pTinggi = 0
    elif (nPelayanann > 45 and nPelayanann <= 60):
        pRendah = 0
        pStandar = 1
        pTinggi = 0
    elif (nPelayanann > 60 and nPelayanann <= 75):
        pRendah = 0
        pStandar = (75 - nPelayanann) / (75 - 60)
        pTinggi = 0
    elif (nPelayanann > 75 and nPelayanann <= 90):
        pRendah = 0
        pStandar = 0
        pTinggi = (nPelayanann - 75) / (90 - 75)
    elif (nPelayanann > 90 and nPelayanann <= 100):
        pRendah = 0
        pStandar = 0
        pTinggi = 1

    return [pRendah, pStandar, pTinggi]


def fuzzifikasiMakanan(nMakanann):
    global mKecil, mSedang, mBesar

    if (nMakanann <= 1.5):
        mKecil = 1
        mSedang = 0
        mBesar = 0
    elif (nMakanann <= 3):
        mKecil = (3 - nMakanann) / (3 - 1.5)
        mSedang = 0
        mBesar = 0
    elif (nMakanann <= 4.5):
        mKecil = 0
        mSedang = (nMakanann - 3) / (4.5 - 3)
        mBesar = 0
    elif nMakanann > 4.5 and nMakanann <= 6:
        mKecil = 0
        mSedang = 1
        mBesar = 0
    elif nMakanann > 6 and nMakanann <= 7.5:
        mKecil = 0
        mSedang = (7.5 - nMakanann) / (7.5 - 6)
        mBesar = 0
    elif nMakanann > 7.5 and nMakanann <= 9:
        mKecil = 0
        mSedang = 0
        mBesar = (nMakanann - 7.5) / (9 - 7.5)
    elif nMakanann > 9 and nMakanann <= 10:
        mkecil = 0
        mSedang = 0
        mBesar = 1
    return [mKecil, mSedang, mBesar]


def ruleInferensi(pRendah, pStandar, pTinggi, mKecil, mSedang, mBesar):
    global nilaiX, nilaiY

    x1 = min(pTinggi, mBesar)
    x2 = min(pTinggi, mSedang)
    y1 = min(pTinggi, mKecil)
    x3 = min(pStandar, mBesar)
    x4 = min(pStandar, mSedang)
    y2 = min(pStandar, mKecil)
    x5 = min(pRendah, mBesar)
    x6 = min(pRendah, mSedang)
    y3 = min(pRendah, mKecil)
    nilaiX = max(x1, x2, x3, x4, x5, x6)
    nilaiY = max(y1, y2, y3)

    return [nilaiX, nilaiY]


def sugenoDefuzzyfikasi(N1, N2, i):
    global listHasil
    Nx = float((N1 * 50) + (N2 * 100))
    Ny = float((N1 + N2))
    if (Nx == 0 and Ny == 0):
        a = 0
    else:
        a = Nx/Ny

    if a >= 70 and a < 100:
        listHasil.append(i)
    elif a == 100:
        listHasil.append(i)
    return listHasil


def Output():
    for i in range(0, len(listHasil)):
        fuzzifikasiPelayanan(nPelayanann=listHasil[i][1])
        fuzzifikasiMakanan(nMakanann=listHasil[i][2])
        ruleInferensi(pRendah, pStandar, pTinggi, mKecil, mSedang, mBesar)
        sugenoDefuzzyfikasi(N1, N2, i)
    return sugenoDefuzzyfikasi(N1, N2, i)


pRendah = 0
pStandar = 0
pTinggi = 0
mKecil = 0
mSedang = 0
mBesar = 0
N1 = 0
N2 = 0
bantuan = []
listBantuan = []

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

listHasil = []
for i in range(0, len(pelayanan)):
    listHasil.append([x[i], pelayanan[i], makanan[i]])


with open('testing.csv', 'w') as newFile:
    tulisFile = csv.writer(newFile, delimiter=',')
    for i in range(0, 10):
        tulisFile.writerow([Output()[i][0]])
        tulisFile.writerow([Output()[i][1]])

print("Testing.csv is ready!")
