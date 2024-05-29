#  SunShop☀️ Project

This is a simple e-commerce web application built with Django. The project allows users to view products, search for products, view product details, and complete a checkout process.

## Features

- View all products with pagination
- Search for products by name
- View detailed information about a specific product
- Checkout process with order saving

## Models

### Product
Represents a product available in the shop.

- `item_name` (CharField): The name of the product.
- `price` (FloatField): The price of the product.
- `discount` (FloatField): The discount on the product.
- `category` (CharField): The category of the product.
- `description` (TextField): A detailed description of the product.
- `image` (CharField): The URL of the product's image.

### Order
Represents an order made by a user.

- `items` (CharField): The items in the order.
- `name` (CharField): The name of the customer.
- `email` (CharField): The email of the customer.
- `address` (CharField): The address of the customer.
- `city` (CharField): The city of the customer.
- `state` (CharField): The state of the customer.
- `zip` (CharField): The zip code of the customer.
- `total` (CharField): The total cost of the order.

## Views

### index
Displays all products with pagination and search functionality.

### details
Displays detailed information about a specific product.

### checkout
Handles the checkout process and saves the order information.

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/django-shop.git
    cd django-shop
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
    
3. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

4. **Create a superuser (optional, for accessing the admin site):**
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Open your browser and go to:**
    ```
    http://127.0.0.1:8000/
    ```

## Usage

- **Home Page:** View all products with pagination.
- **Search:** Use the search bar to find products by name.
- **Product Details:** Click on a product to view its details.
- **Checkout:** Add items to your cart and proceed to checkout.
