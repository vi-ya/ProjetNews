
# News project - Django Website

A website built with Django that centralizes news articles and offers a user experience including registration, login, content interaction (with permission handling), and access to a contact form.

**Target Audience:** Developers, content managers, and anyone looking for a customizable news portal starter.

## Table of Contents


- [News project - Django Website](#news-project---django-website)
  - [Table of Contents](#table-of-contents)
    - [General Info](#general-info)
  - [Requirements](#requirements)
  - [Installation guide](#installation-guide)
  - [Environment Variables](#environment-variables)
  - [Collaboration](#collaboration)
  - [License](#license)
  - [Screenshot](#screenshot)
      - [Home page](#home-page)
      - [Login page](#login-page)
      - [Register page](#register-page)
      - [Contact page](#contact-page)
      - [News page](#news-page)
      - [News list modification pages](#news-list-modification-pages)

### General Info

**Project Status:** Work in Progress 🚧

The site is functional but still under development.

Planned improvements include:

- Adding a newsletter feature (subscription)
- Reinforcing security (axes)
- Upgrading the database system from SQLite to a more robust solution (e.g., PostgreSQL).
- Completing the multilingual system by adding a language switch button (currently only error messages switch between English and French).

The News project is designed to provide a modular, scalable, and multilingual platform for managing and displaying articles.

It includes custom static pages (Contact, About, custom 404), a secure user area for authentication and content management, and a responsive frontend.

## Requirements


- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Sass (SCSS)](https://sass-lang.com/)
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [SQLite 3](https://sqlite.org/)

## Installation guide

Clone the repository:

```html
git clone https://github.com/vi-ya/ProjetNews.git
cd ProjetNews
```

Install the dependencies:

**Set up virtual environment**

```
python -m venv env
env\scripts\activate.bat
```

**Install Dependencies**

```
pip install -r requirements.txt
```

**Migrate Database**

```
python manage.py makemigrations
python manage.py migrate
```
**Reload data to a new database**

```
python manage.py loaddata news/fixtures/news.json
```

**Create admin**

```html
python manage.py createsuperuser
```

**Run Django Server**

```html
python manage.py runserver
```

Now you can access the website

## Environment Variables

To run this project, you will need to set up the following environment variables:

| Variable | Description |
| --- | --- |
| DEBUG | Set to True in development, False in production |
| SECRET_KEY | Your Django secret key for cryptographic signing |
| ALLOWED_HOSTS | List of allowed hosts/domains for your app |
| DATABASE_NAME | Database name (SQLite by default) |
| EMAIL_BACKEND | Email backend (e.g., django.core.mail.backends.smtp.EmailBackend) |
| EMAIL_HOST | SMTP email server (e.g., smtp.gmail.com) |
| EMAIL_PORT | SMTP port (e.g., 587) |
| EMAIL_HOST_USER | Your email address used for sending |
| EMAIL_HOST_PASSWORD | Email password or app-specific password |
| EMAIL_USE_TLS | Set to True to use TLS for email sending |

You can manage these variables securely using a **.envfile** you will need to rename it **.env.** Inside there, you can fill in the values of the environment variables.

## Collaboration

All contributions are welcome, big or small ! Your contributions make the project better !
You can help by (e.g., improving features, fixing bugs, and writing tests).

## License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute it as long as you include the original license file.

## Screenshot

<div align="center">
<h4>Home page</h4>
<img  src="https://github.com/vi-ya/ProjetNews/blob/dc8d2f7365de267b8f09b8384431c3170294cdf2/resources/images/news_home.jpg" alt="news_home" >
</div>

<div align="center">
<h4>Login page</h4>
<img  src="https://github.com/vi-ya/ProjetNews/blob/dc8d2f7365de267b8f09b8384431c3170294cdf2/resources/images/news_login.png" alt="news_login" >
</div>

<div align="center">
<h4>Register page</h4>
<img  src="https://github.com/vi-ya/ProjetNews/blob/dc8d2f7365de267b8f09b8384431c3170294cdf2/resources/images/news_register.png" alt="news_register" >
</div>

<div align="center">
<h4>Contact page</h4>
<img  src="https://github.com/vi-ya/ProjetNews/blob/dc8d2f7365de267b8f09b8384431c3170294cdf2/resources/images/news_contact.jpg" alt="news_contact">
</div>

<div align="center">
<h4>News page</h4>
<img  src="https://github.com/vi-ya/ProjetNews/blob/dc8d2f7365de267b8f09b8384431c3170294cdf2/resources/images/news_list.png" alt="news_list" >
</div>
<div align="center">
<img  src="https://github.com/vi-ya/ProjetNews/blob/dc8d2f7365de267b8f09b8384431c3170294cdf2/resources/images/news_list_mobile.png" alt="news_list_mobile" >
</div>

<div align="center">
<h4>News list modification pages</h4>
<img  src="https://github.com/vi-ya/ProjetNews/blob/dc8d2f7365de267b8f09b8384431c3170294cdf2/resources/images/news_list_modify.png" alt="news_list_modify" >
</div>
<div align="center">
<img  src="https://github.com/vi-ya/ProjetNews/blob/dc8d2f7365de267b8f09b8384431c3170294cdf2/resources/images/news_detail.png" alt="news_detail" >
</div>
<div align="center">
<img  src="https://github.com/vi-ya/ProjetNews/blob/dc8d2f7365de267b8f09b8384431c3170294cdf2/resources/images/news_delete.png" alt="news_delete" >
</div>
<div align="center">
<img  src="https://github.com/vi-ya/ProjetNews/blob/dc8d2f7365de267b8f09b8384431c3170294cdf2/resources/images/news_create.png" alt="news_create" >
</div>
<div align="center">
<img  src="https://github.com/vi-ya/ProjetNews/blob/dc8d2f7365de267b8f09b8384431c3170294cdf2/resources/images/news_update.jpg" alt="news_update" >
</div>

