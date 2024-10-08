# Sat Nusapersada ![Indonesia](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/36/country-4x3/id.png "Indonesia")
Full Stack Apps

> [!IMPORTANT]\
> TECHNOLOGY STACK :
<p align="left">
  <a><img src="https://img.shields.io/badge/v20.17.0-node-importantyellow?logo=nodedotjs" alt="NodeJs"></a>
  <a><img src="https://img.shields.io/badge/v3.4.29-vue-green?logo=vuedotjs" alt="VueJs"></a>
  <a><img src="https://img.shields.io/badge/v5.3.1-vite-blueviolet?logo=vite" alt="ViteJs"></a>
  <a><img src="https://img.shields.io/badge/v3.4.10-tailwind-yellow?logo=tailwindcss" alt="TailwindCss"></a>
  <a><img src="https://img.shields.io/badge/v3.14.0-restframework-red?logo=python" alt="DjangoRestFramework"></a>
  <a><img src="https://img.shields.io/badge/v5.0.3-django-teal?logo=django" alt="Django"></a>
  <a><img src="https://img.shields.io/badge/PostgreSQL v16.4.1-316192?logo=postgresql&logoColor=white" alt="Postgres"></a>
  <a><img src="https://img.shields.io/badge/v2024.1-kalilinux-purple?logo=kalilinux" alt="Kali Linux OS"></a>
</p>

> Installation

Backend
```bash
# Create a virtual environment to isolate our package dependencies locally
> python3 -m venv venv
> source venv/bin/activate  # On Windows use `venv\Scripts\activate`
> (venv) pip install -r requirements.txt
# Sync Database, before migration set up the database connection in .env file
> (venv) python3 manage.py migrate v1
# Seeding data
> (venv) python3 manage.py loaddata fixtures/*.json
# Import PostgreSQL DB (file in dir /api_service)
> psql -h 127.0.0.1 -U postgres -d nusapersada -f nusapersada.sql
```

Frontend
```bash
> npm install OR yarn add
```

> Running Local Development

Backend
```bash
> (venv) python3 manage.py runserver
```
Frontend
```bash
> npm run dev OR yarn run dev
```

Open a browser and access the web app at http://localhost:5173/

![View](/view.png)