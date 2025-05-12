# 🥂 Miguel and Patri's Wedding Invitation Website 🥂

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.7.10+-5646ED?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)](https://reflex.dev)

Welcome to the official repository of Miguel and Patri's wedding invitation website. This project was adapted from my own wedding invitation website (<https://github.com/AlexAlgarate/wedding_web>). As a good friend, I gifted them the same invitation with some modifications (adding bank account details and their personal information).

## 📌 Description

This website is designed to provide an interactive and modern experience, allowing guests to easily access relevant information about the wedding, such as the date, venue, schedule, and other important details. It also includes a section for confirming attendance and leaving messages for the newlyweds.
The website is fully responsive, providing an optimal experience on both mobile devices and desktop computers.

## 🚀 Technologies Used

- **Framework**: Reflex, CSS, and JavaScript
- **Deployment**: Vercel

## 🔧 Installation

To run this project locally, follow these steps:

### 1. Clone the repository

   ```bash
   git clone https://github.com/AlexAlgarate/wedding_miguel_patri.git

### 1. Create the project directory

```cmd
mkdir my_app_name
cd my_app_name
```

### 2. Setup virtual environment

Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```python
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Reflex package

Reflex is available as a pip package.

```python
pip install reflex
```

### 4. Initialize the project

```cmd
reflex init
```

### 5. Run the App

```cmd
reflex run
```

## 🚀 Deployment

To deploy the project, I use *[Vercel](https://vercel.com/)*, but you can also use the service provided by Reflex (*[see the documentation here](https://reflex.dev/docs/hosting/self-hosting/#exporting-a-static-build)*).
I have automated the deployment process with a GitHub Action following Reflex's instructions for exporting the frontend. If you want to add states and backend functionality, you should review this point as Vercel doesn't handle Python code well (an alternative is *[Railway](https://railway.app/)*).

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only 
unzip frontend.zip -d public
rm -f frontend.zip
deactivate
```

### 💻 [Access the project's code](./wedding_miguel_patri)

## 📦 Live Demo

This project is deployed on Vercel. You can access the live site at:

👉 <https://boda-miguel-patri.vercel.app/>

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/AlexAlgarate/wedding_miguel_patri/issues).

## 📝 License

This project is licensed under the terms of the license included in the repository.

## 🙏 Acknowledgements

Special thanks to Miguel and Patri for letting me be part of their special day!
