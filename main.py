from database import *
create_table()
while True:
    print("\n" + "=" * 50)
    print("      INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Sell Product")
    print("7. Low Stock Products")
    print("8. Total Inventory Value")
    print("9. Exit")
    print("=" * 50)
    choice = input("Enter your choice: ")
    if choice == "1":
        try:
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            category = input("Enter Category: ")
            price = float(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))
            result = add_product(
                product_id,
                name,
                category,
                price,
                quantity
            )
            if result:
                print("\nProduct Added Successfully.")
            else:
                print("\nProduct ID already exists.")
        except ValueError:
            print("\nInvalid Input.")    
    elif choice == "2":
        products = view_products()
        if len(products) == 0:
            print("\nNo Products Found.")
        else:
            print("\n")
            print("-" * 80)
            print(
                f"{'ID':<10}"
                f"{'NAME':<20}"
                f"{'CATEGORY':<15}"
                f"{'PRICE':<15}"
                f"{'QUANTITY':<10}"
            )
            print("-" * 80)
            for p in products:
                print(
                    f"{p[0]:<10}"
                    f"{p[1]:<20}"
                    f"{p[2]:<15}"
                    f"{p[3]:<15}"
                    f"{p[4]:<10}"
                )
    elif choice == "3":
        try:
            pid = int(input("Enter Product ID: "))
            product = search_product(pid)
            if product:
                print("\nProduct Found")
                print("-" * 40)
                print("Product ID :", product[0])
                print("Name       :", product[1])
                print("Category   :", product[2])
                print("Price      :", product[3])
                print("Quantity   :", product[4])
            else:
                print("\nProduct Not Found.")
        except ValueError:
            print("\nInvalid Input.")
    elif choice == "4":
        try:
            pid = int(input("Enter Product ID: "))
            product = search_product(pid)
            if product is None:
                print("\nProduct Not Found.")
            else:
                print("\nCurrent Details")
                print("Name :", product[1])
                print("Category :", product[2])
                print("Price :", product[3])
                print("Quantity :", product[4])
                print()
                name = input("Enter New Name: ")
                category = input("Enter New Category: ")
                price = float(input("Enter New Price: "))
                quantity = int(input("Enter New Quantity: "))
                result = update_product(
                    pid,
                    name,
                    category,
                    price,
                    quantity
                )
                if result:
                    print("\nProduct Updated Successfully.")
                else:
                    print("\nUpdate Failed.")
        except ValueError:
            print("\nInvalid Input.")
    elif choice == "5":
        try:
            pid = int(input("Enter Product ID to Delete: "))
            result = delete_product(pid)
            if result:
                print("\nProduct Deleted Successfully.")
            else:
                print("\nProduct Not Found.")
        except ValueError:
            print("\nInvalid Input.")
    elif choice == "6":
        try:
            pid = int(input("Enter Product ID: "))
            qty = int(input("Enter Quantity Sold: "))
            result = sell_product(pid, qty)
            if result == "SUCCESS":
                print("\nSale Completed Successfully.")
            elif result == "INSUFFICIENT":
                print("\nInsufficient Stock.")
            else:
                print("\nProduct Not Found.")
        except ValueError:
            print("\nInvalid Input.")
    elif choice == "7":
        products = low_stock()
        if len(products) == 0:
            print("\nNo Low Stock Products.")
        else:
            print("\nLow Stock Products")
            print("-" * 80)
            print(
                f"{'ID':<10}"
                f"{'NAME':<20}"
                f"{'CATEGORY':<15}"
                f"{'PRICE':<15}"
                f"{'QUANTITY':<10}"
            )
            print("-" * 80)
            for p in products:
                print(
                    f"{p[0]:<10}"
                    f"{p[1]:<20}"
                    f"{p[2]:<15}"
                    f"{p[3]:<15}"
                    f"{p[4]:<10}"
                )
    elif choice == "8":
        value = inventory_value()
        print(f"\nTotal Inventory Value : ₹{value:.2f}")
    elif choice == "9":
        print("\nThank You for using Inventory Management System.")
        print("Program Closed Successfully.")
        break
    else:
        print("\nInvalid Choice. Please Try Again.")
