# Link Heroku App Tugas 2 PBP
```shell
https://pbp-tugas-2-dito.herokuapp.com/katalog/
```

## Bagan Request Client

![Bagan](https://user-images.githubusercontent.com/112608897/190315700-375282c1-ce6c-4505-ab9e-6574a991b498.jpg)


## Why We Should use Virtuel Environment?

Kita menggunakan Virtual Environment pada setiap project agar masing-masing dari project tersebut bersifat independen. Independen pada hal ini artinya ketika kita
melakukan atau menginstall sesuatu pada satu project, perubahan ini tidak akan mengganggu project lainnya. Tentu jika tidak menggunakan Virtual Environment, maka
bisa saja terjadi perubahan pada project yang lain tanpa kita inginkan

## Step by Step Explanation

Menambahkan potongan kode berikut ke file views.py yang ada di folder katalog. Hal ini bertujuan untuk mengambil semua data yang telah di load dari fixtures ke
models serta menambahkan beberapa field data tambahan yang kemudian akan di render ke dalam sebuah HTML

```shell
from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_barang_katalog,
    'nama': 'Dito Syahputra',
    'npm' : '2106638053',
    }
    return render(request, "katalog.html",context)
```

Menambahkan potongan kode berikut ini ke dalam urls.py yang ada pada folder project_django agar path baru dari katalog yang kita buat dapat di akses oleh browser

```shell
path('katalog/', include('katalog.urls'))
```

Kemudian menambahkan potongan kode berikut ini pada urls.py yang ada di folder katalog. Hal ini ditujukan untuk menampilkan halaman yang kita buat ketika membuka
path /katalog di browser


```shell
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```

Selanjutnya membuat file katalog.html pada folder katalog.templates untuk menampilkan data yang kita punya dalam sajian HTML yang dapat dilihat oleh web browser
masing-masing. File tersebut akan berisi kode sebagai berikut.


```shell
{% extends 'base.html' %}

 {% block content %}

  <h1>Lab 1 Assignment PBP/PBD</h1>

  <h5>Name: </h5>
  <p>{{nama}}</p>

  <h5>Student ID: </h5>
  <p>{{npm}}</p>

  <table>
    <tr>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Item Stock</th>
      <th>Rating</th>
      <th>Description</th>
      <th>Item URL</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for barang in list_barang %}
    <tr>
        <th>{{barang.item_name}}</th>
        <th>{{barang.item_price}}</th>
        <th>{{barang.item_stock}}</th>
        <th>{{barang.rating}}</th>
        <th>{{barang.description}}</th>
        <th>{{barang.item_url}}</th>
    </tr>
{% endfor %}
  </table>

 {% endblock content %}
```

Potongan kode ini menampilkan field nama, npm, dan iterasi dari seluruh object barang yang menampilkan attribut masing-masing.

## Heroku Deployment

Untuk melakukan deployment ke Heroku App, kita membuat app baru pada akun heroku lalu menambahkan Secrets ke dalam repository yang akan dideploy.

Adapun Secrets yang ditambahkan adalah sebagai berikut.

```shell
HEROKU_API_KEY: ee9f6454-d896-4b62-a35a-bec40ac1562a
HEROKU_APP_NAME: pbp-tugas-2-dito
```

Setelah semua Secrets berhasil ditambahkan, kita dapat melakukan deployment melalui menu Actions pada repository yang akan dideploy



