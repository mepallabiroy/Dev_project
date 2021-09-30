# **Dev_project**

Start by creating the root folder for the project. In my case it is ```trustbook```.

## **Backend**
>Steps followed in building the backend:
I used Django and Django rest framework at the backend. Django has builtin SQLite. Since this is a basic project, I used the same.
Basic Setup requires : 
- Installing Python.
- Intalling virtual environment. ```pip install virtualenv```.
- Installing Django inside virtual environment.


1. Create the root folder for backend. In my case, I named it ```backend```.
2. ```cd backend``` into the directory and create virtual environment to isolate the project to avoid messing up the dependencies. ```virtualenv venv```.
3. Activate virtual environment and install django inside it. ```venv\Scripts\activate``` (To deactivate the virtual environment, use ```venv\Scripts\deactivate.bat```). Install Django. ```pip install django```.
4. Start project. I named my project "myproject". ```django-admin startproject myproject```.
5. ```cd myproject```. Craete the app which we will be working on. I named it "app". ```django-admin startapp app```.  Install this app in settings.py (INSTALLED_APPS).
6. Create model in models.py.
7. Create superuser. ```python manage.py createsuperuser``` and fill the necessary details. Superuser is the administrator of the app.
8. Register the model in admin.py.
9. Install Django Rest Framework in the same virtual network. ```pip install djangorestframework```. Add 'rest_framework' in INSTALLED_APPS in settings.py.
10. Create view in views.py and add URL in urls.py. I used Function based API view in views.py.
11. Create serializer.py and make neccesary changes. Serializers allow complex data such as QuerySets and Model Instances to be converted to native python data types that can be easily rendered into JSON, XML etc.
12. Add all the necessary URLs in urls.py
13. Make migrates to create database. ```python manage.py makemigrations```, ```python manage.py migrate```.
14. Launch server. ```python manage.py runserver```.

![Backend](https://drive.google.com/uc?export=view&id=1pNqvUfXtbYKQQD10x6ZCbrwfw1FBUJlG)

## **Frontend**
> Steps to be followed in frontend
I used react-native as frontend.
Basic set-up requirements:
- Download [node.js](https://nodejs.org/en/download/).
- Install expo-cli and start the project. I named my project "trustbook". ```npm install -g expo-cli``` , ```expo init trustbook```.
- ```cd trustbook``` Start the project. ```npm start``` or ```expo start```.
- You may install "expo go" app in mobile to check if our app is working by scanning the QR code. Alternatively, you can run the app in web browser as well. It it doesn't work, try ```expo r --tunnel``` from cmd instead of ```npm start```. After the command runs successfully, this tab opens in our browser.

![Meta bundler](https://drive.google.com/uc?export=view&id=1HFzeLZOc2euxBYnl_TL3Lq7KanKmTX1S)

1. Make necessary changes in App.js to render the required data.

![Frontend](https://drive.google.com/uc?export=view&id=1mAqIjEpGnrn3sxSpGsS4nUwulwT7Rzn9)

### Note

- We might not get required output while rendering data. 
- On inspecting the page (our app), we find that access to our backend is blocked. Hence frontend is not able to fetch. 
- This is due to Access to fetch at 'http://127.0.0.1:8000/json' (Backend URL) from origin  has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
- To solve this issue, refer this [link](https://dzone.com/articles/how-to-fix-django-cors-error).
