
# Fruit Basket

Its a django based web app for the simulation of fruit shop.


## Run locally

To run this project change directory to the project folder and run the command

```bash
  python manage.py runserver
```


## Features

- Two user modes
- Authenticated users can update and delete from  fruit list.
- Normal users can buy the fruits



## Tech Stack

**Client:** HTML, CSS, Javascript

**Server:** Python, Django


## End points

| Endpoints | Function | Users 
|----------:|:--------:|:---------------------------------|
|`/` | Here the list of fruits and their qty with price is present | `Normal` user can buy it and `Authenticated` users can change it.|
|`/add` | `Authenticated` users can add items. | not applicable for `Normal` users |
|`/login` | To `Authenticate` users | not applicable for `Normal` users |
|`/register` | To register users | `Normal` users can register themselves in order to become a privillaged user |
|`/buy` | To Purchase the fruits | `Normal` users can purchase|
|`/update` | To update the fruit details | `Authenticated` users can only update|
|`/delete` | To delete the fruits | `Authenticated` users can only delete|



## Screenshots

`/` (home)

![App Screenshot](https://github.com/hackman01/iert-django-workshop/assets/84094140/fe7c977e-4717-4f8b-826c-ddc514eb94bb)

`/login`

![App Screenshot](https://github.com/hackman01/iert-django-workshop/assets/84094140/23c58530-f757-4f42-ba6a-641282acc884)


`/register`


![register](https://github.com/hackman01/iert-django-workshop/assets/84094140/568620db-97cc-4a76-b3a9-a054a4a94758)


`/` (Authenticated user)


![loginA](https://github.com/hackman01/iert-django-workshop/assets/84094140/0202cbc5-7f58-4ac3-a4aa-45f4aba65c0e)