# JuJu Collective

## Overview

Welcome to the Juju Collective project, a Django-based web application that powers the Juju Collective brand. This project includes three Django apps for managing products, storefronts, and collective user interaction. The project is containerized using Docker for seamless development and deployment.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Setup](#docker-setup)
- [Sphinx Documentation](#sphinx-documentation)
- [Contributing](#contributing)
- [License](#license)

---

## Project Structure


```plaintext
juju_collective/
├── juju_warehouse/       # Handles product inventory and warehouse management
├── juju_storefront/      # Manages storefront, product display, and customer-facing features
├── templates/            # Django templates (e.g., dashboard.html)
├── manage.py             # Django project management script
├── Dockerfile            # Docker configuration
└── README.md             # Project documentation
```
---

## Features

- **Product Management**: The `juju_warehouse` app allows for product uploads, inventory management, and warehousing.
- **Storefront**: The `juju_storefront`  app provides the public-facing storefront for product display and user interaction.
- **Sphinx Documentation**: Comprehensive project documentation is generated using Sphinx.

---

## Installation
### Prerequisites

- Python 3.10+
- Django 4.x
- Docker (optional but recommended for deployment)
- Node.js and npm (for managing front-end assets, if applicable)
- SQLite (for local development)

### Steps

1. **Clone the repository:**
`git clone https://github.com/JudeKing/juju_collective.git`

2. **cd into juju_collective directory:**
`cd juju_collective`

4. **Set up a virtual environment:**
```
python -m venv venv
venv\Scripts\activate # On Mac: source venv/bin/activate
```

4. **Install dependencies:**
`pip install -r requirements.txt`

5. **Run migrations:**
`python manage.py migrate`

6. **Run the development server:**
`python manage.py runserver`

---

## Usage

- Navigate `http://localhost:8080` to access the application.
- Use the Django Admin at `http://localhost:8000/admin` for administrative tasks (e.g., managing users and products).

---

## Docker Setup

1. **Build and run the Docker container:**
```
docker build -t juju_collective .
docker run -d -p 8000:8000 juju_collective
```
2. **Access the application:** The app will be accessible at `http://localhost:8000` inside your browser.

---

## Sphinx Documentation

The project uses **Sphinx** to generate documentation. To build the HTML documentation:

1. Install Sphinx:

`pip install sphinx`

2. Navigate to the documentation directory (if available) and build the documentation:
```
cd docs
.\make.bat html # On Mac: make html
```

The generated documentation will be located in the `_build/html/` folder.

## Contact

For inquiries, collaborations, or contributions, feel free to contact me at judecoding@gmail.com
