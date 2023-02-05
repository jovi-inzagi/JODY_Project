from flask import Flask, render_template, request, url_for
import requests
import json
import urllib.request

aplikasi = Flask(__name__, template_folder='Views')

# Memanggil data json

with open('data.json') as f:
    data = json.load(f)

# print(data)

asu = []
for sekolah in data['dataSekolah']:
    list_data = {}

    list_data['propinsi'] = sekolah['propinsi']
    list_data['kode_kab_kota'] = sekolah['kode_kab_kota']
    list_data['kabupaten_kota'] = sekolah['kabupaten_kota']
    list_data['kecamatan'] = sekolah['kecamatan']
    list_data['npsn'] = sekolah['npsn']
    list_data['sekolah'] = sekolah['sekolah']
    list_data['bentuk'] = sekolah['bentuk']
    list_data['alamat_jalan'] = sekolah['alamat_jalan']
    list_data['lintang'] = sekolah['lintang']
    list_data['bujur'] = sekolah['bujur']
    list_data['image'] = sekolah['image']
    # print(sekolah['image'])
    # print("image")
    asu.append(list_data)


# f = urllib.request.urlopen(data).read().decode()
# # Reading from file 
# data = json.loads(f)
# datasekolah = []
# # print(data)
# dataSekolah = data['dataSekolah']

# Menambahkan data kedalam dictionary kemudian input kedalam list
# kode_prop = list (map(lambda x: x['kode_prop'], dataSekolah))
# propinsi = list (map(lambda x: x['propinsi'], dataSekolah))
# kode_kab_kota = list (map(lambda x: x['kode_kab_kota'], dataSekolah))
# kabupaten_kota = list (map(lambda x: x['kabupaten_kota'], dataSekolah))
# kode_kec = list (map(lambda x: x['kode_kec'], dataSekolah))
# kecamatan = list (map(lambda x: x['kecamatan'], dataSekolah))
# id = list (map(lambda x: x['id'], dataSekolah))
# npsn = list (map(lambda x: x['npsn'], dataSekolah))
# sekolah_indonesia = list (map(lambda x: x['sekolah'], dataSekolah))
# bentuk = list (map(lambda x: x['bentuk'], dataSekolah))
# status = list (map(lambda x: x['status'], dataSekolah))
# alamat_jalan = list (map(lambda x: x['alamat_jalan'], dataSekolah))
# lintang = list (map(lambda x: x['lintang'], dataSekolah))
# bujur = list (map(lambda x: x['bujur'], dataSekolah))


# for i in range(10):
#    if i < len(data['dataSekolah']):
#     sekolah = dict()
#     sekolah['kode_prop'] = kode_prop[i]
#     sekolah['propinsi'] = propinsi[i]
#     sekolah['kode_kab_kota'] = kode_kab_kota[i]
#     sekolah['kabupaten_kota'] = kabupaten_kota[i]
#     sekolah['kode_kec'] = kode_kec[i]
#     sekolah['kecamatan'] = kecamatan[i]
#     sekolah['id'] = id[i]
#     sekolah['npsn'] = npsn[i]
#     sekolah['sekolah_indonesia'] = sekolah_indonesia[i]
#     sekolah['bentuk'] = bentuk[i]
#     sekolah['status'] = status[i]
#     sekolah['alamat_jalan'] = alamat_jalan[i]
#     sekolah['lintang'] = lintang[i]
#     sekolah['bujur'] = bujur[i]
#     datasekolah.append(sekolah)

# print(dataSekolah)

@aplikasi.route('/')
def home():
    return render_template('index.html', sekolah = asu, judul = 'home')
# print(asu)


# @aplikasi.route('/cari_sekolah', methods = ['POST', 'GET'])
# def cari_sekolah():
#     if request.method == 'POST' :
#         cari = request.form['cari']
#         new_list = list(filter(lambda x: (x['sekolah_indonesia'] == cari), data[dataSekolah]))
#         return render_template('cari.html', rs = new_list, judul='Cari Data')
#     else:
#         cari = request.args.get['cari']

# SI=[]
# for i in data['dataSekolah'] :
#     SI.append(i['sekolah'])
#     # print(i)

# @aplikasi.route('/cari-data/')
# def caridata():
#     q = set(SI)
#     p = list(map(lambda x: 'sekolah_indonesia' + x, sorted(q)))
#     return render_template('cariutama.html', x = p, judul='Cari Data')

if __name__ == '__main__':
    aplikasi.run(debug=True)  