# One Health Laboratory Network website project

Website yang di pakai untuk laboratorium membuat sejumlah laporan mengenai laboratorium mereka

## Getting Started

Instruksi dibawah ini akan menjelaskan bagaimana cara menjalankan website ini dalam lokal komputer


### Installing

Bagaimana cara menjalankan di local komputer masing-masing

Membuat Virtual Environment di dalam laptop kita (pastikan di dalam direktori dimana project kita berada)

```
python3 -m venv env
source ./env/bin/activate 
```

Setelah itu, kita menginstall segala dependency yang kita butuhkan (yang tertulis dalam `setting.py`)

```
pip3 install -r requirements.txt
```

Kita bisa run website ini dalam local komputer dengan alamat port http://127.0.0.1:8000/ atau localhost/8000

```
python3 manage.py runserver
```

Jangan lupa, jika ada perubahan di dalam file `models.py` untuk selalu melakukan migration setiap kalinya

```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc