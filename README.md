# Ecommerce with Django

This ecommerce es a basic app in Django and Bootstrap

## Structure of project
This project is structured by apps (directories)

```
.
├── accounts            # Account for user apps
│   ├── ...
├── category            # Categories for products app
│   ├── ...
├── core                # Main app for settings
│   ├── ...
├── ecommerce           # Primary interface and views (frontend)
│   ├── ...
├── templates           # Static files and html files for apps
│   ├── ...
├── LICENSE
├── manage.py           # Main script
├── README.md           # README file and documentations
└── requirements.txt    # Requirements for pip
```

## Run app
If you wish run this app you need create a virtualenv, and activate the virtualenv
```
python -m venv venv
source venv/bin/activate
```

Next you need create the static files
```
python manage.py collectstatic
```

Last, run the app
```
python manage.py runserver 0.0.0.0:5000
```

If you change the database you need make migrations again
```
python manage.py makemigrations
python manage.py migrate
```