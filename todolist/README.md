# Link Heroku App Tugas 3 PBP
```shell
https://pbp-tugas-2-dito.herokuapp.com/todolist
```

## Why Do We Need {% csrf_token %}

csrf_token merupakan serangkaian string yang memiliki value acak dan bersifat rahasia yang tersimpan ke dalam setiap client yang mengakses. Hal ini ditujukan untuk
mengurangi resiko peretasan oleh pihak tidak bertanggung jawab yang dapat menyamarkan dirinya sebagai client tertentu lalu mengambil seluruh data pribadi
yang dapat menguntungkan dirinya.

Jika tidak ada token ini, maka suatu website akan sangat rentan mengalami peretasan karena tidak dapat mengidentifikasi apakah client yang mengakses suatu data
benar-benar berasal dari pemilik data tersebut.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Bisa, dengan membuat file forms.py pada folder todolist yang dimana file tersebut akan berisikan field field dari data yang ingin diambil dari user.

## Proses Alur Data

Ketika user ingin menambahkan task, maka user akan menekah button add new task. Kemudian akan muncul halaman forms yang meminta judul dan deskripsi untuk task baru tersebut. JIka input sudah valid, maka data baru akan disimpan kedalam database dan ditampilkan kembali oleh method show_todolist yang akan merender ke dalan HTML.
Nantinya HTML tersebutlah yang dapat dilihat perubahannya oleh User.


## Step by Step Explanation

Membuat sebuah app baru dengan nama mywatchlist dengan menjalankan perintah

```shell
python manage.py startapp todolist
```

Menambahkan path mywatchlist pada urls.py project_django dengan kode berikut agar mywatchlist dapat di akses pathnya.

```shell
path('todolist/', include('todolist.urls'))
```

Membuat sebuah model pada app mywatchlist dengan nama class Movie beserta attributnya seperti berikut

```shell
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    title = models.TextField()
    description = models.TextField()
    is_finished = models.TextField()
    
```
Kemudian membuat halaman utama todolist yang akan menampilkan data dari task yang sudah dan akan dibuat.

todolist.html
```shell
{% extends 'base.html' %}

{% block content %}
<style>
    body{
        font-family: Helvetica;
    }

    table{
        box-shadow: 0px 3px 2px rgb(0 0 0/ 0.2);
        width: 1200px;
        margin-left: auto;
        margin-right: auto;
    }

    button{
        border-radius: 5px;
        border: none;
        text-decoration: none;
        min-height: 20px;
        min-width: 50px;
        font-size: 10px;
        box-shadow: 0px 3px 2px rgb(0 0 0/ 0.2);
    }
    a{
        text-decoration: none;
        color: white;
    }

    .greenbutton{
        background-color: #53d769
    }

    .greenbutton:hover{
        background-color: #46c263;
    }

    .bluebutton{
        background-color: #5BA4FC
    }

    .bluebutton:hover{
        background-color: #5897EE;
    }

    .redbutton{
        background-color:#FC3D39 ;
    }

    .redbutton:hover{
        background-color: #E33437;
    }

    #userprofile{
        font-size: 25px;
        font-weight: 400;
        height: 15px;
    }

</style>

<div style="text-align: right;">
    <p id="userprofile">Welcome, {{username}}! </p>
    <button class = "redbutton" style="font-size:15px; height:30px; width:100px"><a href="{% url 'todolist:logout' %}">Logout</a></button>
    
</div>
<p id="header_utama" style="padding-left: 20px;">📃Tasks Management</p>

<div style="padding-top:20px;">
    <table>
        <tr>
        <th class = "judul">Title</th>
        <th class = "judul">Description</th>
        <th class = "judul">Date Added</th>
        <th class = "judul">Status</th>
        <th class = "judul">Change</th>
        <th class = "judul">Delete</th>
    
        </tr>
        {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
        {% for todo in data_tasks %}
            <tr>
                <th class = "data" style="width: 20%;">{{todo.title}}</th>
                <th class = "data" style="width: 25%;">{{todo.description}}</th>
                <th class = "data" style="width: 15%;">{{todo.date}}</th>
                <th class = "data" style="width: 15%;">{{todo.is_finished}}</th>
                <th class = "data" style="width: 15%;"><button class="greenbutton"><a href="{% url 'todolist:change_status' todo.id %}">Switch</a></button></th>
                <th class = "data" style="width: 10%;"><button class = "redbutton" style="min-width: 25px"><a href="{% url 'todolist:delete_task' todo.id %}">X</a></button></th>
    
            </tr>
        {% endfor %}
    </table>
    
</div>

<div style="padding-top: 10px; text-align: center;">
    <button class="bluebutton" style="width: 100px;"><a href="{% url 'todolist:add_task' %}">Add New Task</a></button>

</div>
<h5 id="identity">Sesi terakhir login: {{ last_login }}</h5>

{% endblock content %}
```

Membuat fungsi show_todolist pada views.py
```shell
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
    'data_tasks': data_todolist,
    'username' : request.user,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html",context)
```


Membuat halaman form dengan HTML add_task.html serta fungsi untuk menjalankannya pada views.py

add_task.html

```shell
{% extends 'base.html' %}

{% block meta %}
<title>Todolist</title>
{% endblock meta %}

{% block content %}

<div class = "create_new_task">

    <h1>Tambah Task Baru</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Judul: </td>
                <td><input style="width: 500px;" type="text" name="title" placeholder="Masukkan judul disini..."></td>
            </tr>
                    
            <tr>
                <td>Deskripsi: </td>
                <td ><input style="width: 500px;" type="text" name="description" placeholder="Masukkan deskripsi disini.."></td>
            </tr>

            <tr>
                <td></td>
                <td><input type="submit" value="Tambahkan"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}

{% endblock content %}

```

fungsi add_task pada views.py
```shell
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title != "" and description != "":
            Task.objects.create(title=title, description=description, date=datetime.date.today(), user=request.user, is_finished="Belum Selesai")
            return HttpResponseRedirect(reverse("todolist:show_todolist")) 
        
        if title == "" and description == "":
            messages.info(request, 'Judul dan Deskripsi tidak boleh kosong!')
        elif title == "":
            messages.info(request, 'Judul tidak boleh kosong!')
        else:
            messages.info(request, 'Deskripsi tidak boleh kosong!')

            
    return render(request, "add_task.html")
```

Melakukan routing dengan menambahkan potongan kode berikut pada urls.py yang ada di todolist.py.

```shell
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-task/', add_task, name='add_task'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('change-status/<int:id>', change_status, name='change_status'),
```

# Tugas 5

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Inline CSS merupakan potongan kode CSS yang langsung ditambahkan pada tag/element terkait>. Internal CSS merupakan potongan kode CSS yang ditambahkan pada awal file HTML yang ditandai dengan <style></style>. Sedangan Eksternal CSS merupakan potongan kode CSS yang terpisah dari file html dalam berupa file .css.

Inline CSS
Kelebihan : Dapat melakukan directly styling ke element yang di tuju tanpa mempengaruhi element lain
Kekurangan : Penulisan kode yang kurang rapih

Internal CSS
Kelebihan : Memudahkan suatu file untuk mendefine class-class yang sama style nya
Kekurangan : Tidak bisa digunakan secara umum oleh file html lain

Eksternal CSS
Kelebihan : Dapat digunakan secara umum oleh semua file yang ada
Kekurangan : Tidak praktis karena harus berganti file jika ingin mengedit css

## Jelaskan tag HTML5 yang kamu ketahui.

<head> Untuk membuat bagian header dari tampilan dokumen yang kita buat. <body> untuk mendefinisikan isi konten utama dari sebuah halaman. <div> membuat section baru untuk menaruh beberapa konten yang diinginkan. <h1>,<h2>,dst, untuk membuat header text dari yang paling besar ke kecil. <button> membuat sebuah button yang dapat merefer hal tertentu. dll

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

Secara umum, selector pada CSS dibagi menjadi 3 yaitu:

Element selector
Selector ini digunakan untuk merubah element yang sudah menjadi bawaan html secara umum yang dapat dilakukan hanya dengan elemen{}

Id selector
Selector ini digunakan untuk merubah style single element yang telah diberi id oleh kita sebagai developer yang dapat dilakukan dengan #id{}

Class selector
Tak berbeda jauh dengan Id selector, Class selector juga digunakan untuk merubah banyak element yang telah diberi class oleh developer yang dapat diedit dengan .nama_class{}

## Step by Step Explanation

Menambahkan potongan kode berikut pada base.html untuk menginstal bootstrap pada file html kita.

```shell
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
```
```shell
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
```

Mengedit dan menghias CSS sesuai keinginan kita dan menggunakan Media Query agar web menjadi responsive



## Heroku Deployment

Untuk melakukan deployment ke Heroku App, kita membuat app baru pada akun heroku lalu menambahkan Secrets ke dalam repository yang akan dideploy.

Adapun Secrets yang ditambahkan adalah sebagai berikut.

```shell
HEROKU_API_KEY: ee9f6454-d896-4b62-a35a-bec40ac1562a
HEROKU_APP_NAME: pbp-tugas-2-dito
```

Setelah semua Secrets berhasil ditambahkan, kita dapat melakukan deployment melalui menu Actions pada repository yang akan dideploy


