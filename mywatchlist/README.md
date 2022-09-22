# Link Heroku App Tugas 3 PBP
```shell
https://pbp-tugas-2-dito.herokuapp.com/mywatchlist/html
https://pbp-tugas-2-dito.herokuapp.com/mywatchlist/xml
https://pbp-tugas-2-dito.herokuapp.com/mywatchlist/json
```

## The Difference Between JSON, XML, and HTML

JSON dan XML merupakan format yang digunakan untuk menyimpan dan membaca sebuah data. Namun perbedaan mencolok di antara keduanya ialah tentang bagaimana mereka menyimpan sebuah data. JSON memiliki teknik penyimpanan yang efisien dibanding XML. Namun, format data dalam bentuk JSON cenderung sulit dipahami oleh manusia. Sebaliknya, XML tidak memiliki teknik penyimpanan seefisien JSON. Namun, XML justru lebih mudah dipahami oleh manusia karena menyimpan data secara terstruktur

## Why We Need Data Delivery?

Data delivery sangat diperlukan dan berguna dalam pengembangan suatu platform terlebih jika platform tersebut berskala besar. Karena data delivery merupakan sebuah alur birokrasi penyimpanan dan pembacaan suatu data dengan format tertentu yang ditujukan untuk dapat mengakses data tersebut sewaktu-waktu. Jika data tidak diformat dan distruktur dengan birokrasi data delivery, maka nantinya hal tersebut akan menimbulkan sebuah kesulitan untuk mengakses sebuah data pada platform

## Step by Step Explanation

Membuat sebuah app baru dengan nama mywatchlist dengan menjalankan perintah

```shell
python manage.py startapp mywatchlist
```

Menambahkan path mywatchlist pada urls.py project_django dengan kode berikut agar mywatchlist dapat di akses pathnya.

```shell
path('mywatchlist/', include('mywatchlist.urls'))
```

Membuat sebuah model pada app mywatchlist dengan nama class Movie beserta attributnya seperti berikut

```shell
class Movie(models.Model):
    is_watched = models.BooleanField()
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.TextField()
    
```

Menambahkan 10 buah data dengan nama file initial_mywatchlist_data.json yang berisikan:

```shell
[
    {
        "model": "mywatchlist.movie",
        "pk": 1,
        "fields": {
            "is_watched": true,
            "title": "Interstellar",
            "rating": 10,
            "release_date": "2014-11-06",
            "review": "Interstellar is not only a grand space adventure worthy of the big screen, it's also a powerfully emotional story about the bond between a father and daughter, and how that love can drive one to attempt the impossible."
        }
    },
    {
        "model": "mywatchlist.movie",
        "pk": 2,
        "fields": {
            "is_watched": true,
            "title": "The Prestige",
            "rating": 10,
            "release_date": "2006-11-08",
            "review": "Just when viewers think they've figured things out, that's when the exquisite diversionary tactics really kick in."
        }
    },
    {
        "model": "mywatchlist.movie",
        "pk": 3,
        "fields": {
            "is_watched": true,
            "title": "Batman: The Dark Knight",
            "rating": 10,
            "release_date": "2008-07-18",
            "review": "A masterpiece within or outside the superhero & comic book genre it explores. Heath Ledger delivers one of the most iconic performances in film history."
        }
    },
    {
        "model": "mywatchlist.movie",
        "pk": 4,
        "fields": {
            "is_watched": true,
            "title": "The Devil All The Time",
            "rating": 8.31,
            "release_date": "2020-09-16",
            "review": "The Devil All the Time is soaked in blood and dirt, holy water and tears, and there's not a lot of it that will wash away."
        }
    },
    {
        "model": "mywatchlist.movie",
        "pk": 5,
        "fields": {
            "is_watched": false,
            "title": "Memento",
            "rating": 8.52,
            "release_date": "2000-09-05",
            "review": "Memento takes us on a mental trip of recovery, revenge, and remembering."
        }
    },
    {
        "model": "mywatchlist.movie",
        "pk": 6,
        "fields": {
            "is_watched": false,
            "title": "The Godfather",
            "rating": 10,
            "release_date": "1972-03-15",
            "review": "An engrossing metaphor for American capitalism, watching the film on the big screen emphasises the majesty of Coppolas work."
        }
    },
    {
        "model": "mywatchlist.movie",
        "pk": 7,
        "fields": {
            "is_watched": true,
            "title": "Avengers: Infinity War",
            "rating": 9.25,
            "release_date": "2018-04-27",
            "review": "Infinity War is all about balance, in many different respects. Balance and tone, both of which, for a film with such ambition and size, are remarkable in how well they are executed. It is worth 10 years of waiting."
        }
    },
    {
        "model": "mywatchlist.movie",
        "pk": 8,
        "fields": {
            "is_watched": true,
            "title": "Moonknight",
            "rating": 9.11,
            "release_date": "2022-03-30",
            "review": "After such a fun season that deftly mixed superhero heroics with genuine psychological depth, we cant wait to see whatever the characters do next. Its hard not to be over the moon."
        }
    },
    {
        "model": "mywatchlist.movie",
        "pk": 9,
        "fields": {
            "is_watched": false,
            "title": "Forrest Gump",
            "rating": 8.56,
            "release_date": "1994-07-06",
            "review": "Contrasting Forrest's unassuming innocence with the upheavals and rancor of the times, the film is a wisely goofy commentary on the stupidity of smartness."
        }
    },
    {
        "model": "mywatchlist.movie",
        "pk": 10,
        "fields": {
            "is_watched": true,
            "title": "Arrival",
            "rating": 9.23,
            "release_date": "2016-11-11",
            "review": "Both cerebral and achingly emotional, Arrival sustains a message about hope and understanding for a better humanity that audiences may need right now."
         }
    }
]
```

Melakukan routing dengan menambahkan potongan kode berikut pada urls.py yang ada di mywatchlist.

```shell
path('html/',show_watchlist, name='show_watchlist'),
path('xml/',show_xml, name='show_xml'),
path('json/',show_json, name='show_json'),
```


## Heroku Deployment

Untuk melakukan deployment ke Heroku App, kita membuat app baru pada akun heroku lalu menambahkan Secrets ke dalam repository yang akan dideploy.

Adapun Secrets yang ditambahkan adalah sebagai berikut.

```shell
HEROKU_API_KEY: ee9f6454-d896-4b62-a35a-bec40ac1562a
HEROKU_APP_NAME: pbp-tugas-2-dito
```

Setelah semua Secrets berhasil ditambahkan, kita dapat melakukan deployment melalui menu Actions pada repository yang akan dideploy

## Postman Accessing

```shell
https://pbp-tugas-2-dito.herokuapp.com/mywatchlist/html
```
![image](https://user-images.githubusercontent.com/112608897/191656282-68974e1c-73cd-4cf9-8713-74d1a38fdcea.png)

```shell
https://pbp-tugas-2-dito.herokuapp.com/mywatchlist/json
```
![image](https://user-images.githubusercontent.com/112608897/191656310-0c9f571c-a715-46b9-b2c9-3d046e364ebb.png)

```shell
https://pbp-tugas-2-dito.herokuapp.com/mywatchlist/xml
```
<img width="665" alt="image" src="https://user-images.githubusercontent.com/112608897/191656396-2aab0133-b1e5-4ca9-9f8e-16d1d5f5ea3d.png">




