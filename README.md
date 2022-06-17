# Django Tutorial
> <span style="color:yellow">New instructions and hints will be added frequently so visit this README on regular basis. <br> Some details are left vague on purpose, it's your task to understand it and get the work done.</span>


# Fruit Basket
This is a simple web application where users can buy fruits.
## Technology to be used - 
- Frontend
    - HTML
    - CSS
    - JavaScript
- Backend
    - Python
    - Django

## Functionality 
- This will have 2 type of users
    - Authenticated Users (Will need username and password to login)
    - Normal Users
- Authenticated users can add, update, view and delete the fruits
- Normal (unauthenticated) users can only view the fruits list and buy them
- Fruits will have these attribute
    1. Name of the fruit
    2. Price of the fruit (in rupees)
    3. Picture of the fruit
    4. Total Quantity Available of the fruit

## URL Endpoints

| Endpoint | Description | Remark|
| :----: | --- | ----|
| `/login/` | This will allow users to login using their userid and password | |
| `/home/` | This will show the list of all fruits | Autheticated users will also have the update the delete button on fruit|
| `/add/` | add new fruits | authenticated users can add new fruits by filling required details |
| `/fruits/list/` | a table containing all fruits with their details along with update and delete button | Accessible to authenticated users only |
| `/buy/` | a dummy page with all payment options | |
  
    
> You are free to add extra endopints as per your requirements, this is only for your minimum reference

## How to contribute 

- Create a django project in this directory.
- Your fruit_basket_`Aktu roll No.` should be the name of your django project. (dummy project is provided for reference)
- You are advised to create seperate app in your django project
- If you have used virtual enviornment in your django app then name it `env` or `venv`.
- Create a README.md in your project folder with the instructions how to use it or how to install it.
- Create a `requirements.txt` file. (compulsory).
- When you are done with this task then create a pull request.
- Use proper screenshots of running site and description in your pull request.


> You are free to use Google, Youtube, Stackoverflow or anything else but focus on understanding rather than just copy-pasting.
