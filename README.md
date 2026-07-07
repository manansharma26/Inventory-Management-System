# Inventory Management System 📦

This is a Python + SQLite project I made to practice database handling along with regular Python programming. It's a command-line Inventory Management System where you can add, view, search, update, delete, and sell products, plus check low stock items and total inventory value.

I built this to get comfortable with SQL inside Python (using the `sqlite3` module) since my earlier projects only used JSON files for storage. This one actually uses a real database.

## What it does

- Add a new product (ID, Name, Category, Price, Quantity)
- View all products in a formatted table
- Search for a product by ID
- Update a product's details
- Delete a product
- Sell a product (automatically reduces stock, checks for insufficient quantity)
- View low stock products (default threshold: 5 or below)
- View total inventory value (price × quantity for all products)

## How to run it

1. Make sure you have Python installed (Python 3). `sqlite3` comes built-in, so no extra installation needed.
2. Download or clone this repo. Make sure `main.py` and `database.py` are in the same folder.
3. Open terminal in the project folder and run:

```
python main.py
```

4. You'll see a menu like this:

```
==================================================
      INVENTORY MANAGEMENT SYSTEM
==================================================
1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Sell Product
7. Low Stock Products
8. Total Inventory Value
9. Exit
==================================================
```

5. Enter the number for whatever you want to do and follow the prompts.

## Example

```
Enter your choice: 1
Enter Product ID: 101
Enter Product Name: Notebook
Enter Category: Stationery
Enter Price: 45.50
Enter Quantity: 100

Product Added Successfully.
```

## Files in this project

- `main.py` – handles the menu, user input, and calls the database functions
- `database.py` – all the SQLite logic (connecting to the database, creating the table, and all CRUD + sell/low-stock/value functions)
- `inventory.db` – this file gets created automatically the first time you run the program; it's where all product data is actually stored

## Things I learned making this

- Using the `sqlite3` module to connect, create tables, and run queries from Python
- Separating logic into two files (`main.py` for UI, `database.py` for database operations) instead of writing everything in one file
- Using `try/except` blocks to catch `ValueError` for invalid inputs and `sqlite3.IntegrityError` for duplicate Product IDs
- Writing SQL queries with parameterized `?` placeholders to avoid SQL injection
- Using `cursor.rowcount` to check whether an update/delete actually affected a row
- Formatting table-style output in the console using f-strings and `:<width` alignment

## Things I want to improve later

- Add proper validation so negative price/quantity can't be entered
- Add a confirmation step before deleting a product
- Maybe add a search-by-name or search-by-category option
- Try connecting this to a simple GUI (Tkinter) or a web frontend someday

## Note

This is a learning project, not a production-grade inventory system, so some parts (like input validation) are still basic. Feel free to explore the code or suggest improvements!
