import sqlite3
DB_NAME = "inventory.db"
def connect():
    return sqlite3.connect(DB_NAME)
def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()
def add_product(product_id, name, category, price, quantity):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
        INSERT INTO products(product_id,name,category,price,quantity)
        VALUES(?,?,?,?,?)
        """,(product_id,name,category,price,quantity))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
def view_products():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    conn.close()
    return data
def search_product(product_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE product_id=?",(product_id,))
    data = cursor.fetchone()
    conn.close()
    return data
def update_product(product_id,name,category,price,quantity):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE products
    SET name=?,category=?,price=?,quantity=?
    WHERE product_id=?
    """,(name,category,price,quantity,product_id))
    conn.commit()
    result = cursor.rowcount
    conn.close()
    return result
def delete_product(product_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE product_id=?",(product_id,))
    conn.commit()
    result = cursor.rowcount
    conn.close()
    return result
def sell_product(product_id,qty):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT quantity FROM products WHERE product_id=?",(product_id,))
    data = cursor.fetchone()
    if data is None:
        conn.close()
        return "NOT FOUND"
    stock = data[0]
    if qty > stock:
        conn.close()
        return "INSUFFICIENT"
    new_stock = stock - qty
    cursor.execute("""
    UPDATE products
    SET quantity=?
    WHERE product_id=?
    """,(new_stock,product_id))
    conn.commit()
    conn.close()
    return "SUCCESS"
def low_stock(limit=5):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM products
    WHERE quantity<=?
    """,(limit,))
    data = cursor.fetchall()
    conn.close()
    return data
def inventory_value():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT SUM(price*quantity)
    FROM products
    """)
    value = cursor.fetchone()[0]
    conn.close()
    if value is None:
        return 0
    return value
