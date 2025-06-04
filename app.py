import crud

def main():
    while True:
        print("\nSimple Market CLI\n"
              "1. Add User\n2. List Users\n3. Delete User\n4. Update User\n"
              "5. Add Product\n6. List Products\n7. Delete Product\n8. Update Product\n"
              "9. Add Order\n10. List Orders\n11. Delete Order\n"
              "12. Add Order Item\n13. List Order Items\n14. Delete Order Item\n"
              "15. Search Products by Name\n16. Search Products by Farmer Location\n"
              "0. Exit")
        choice = input("Your choice: ")
        if choice == "1":
            username = input("Username: ")
            email = input("Email: ")
            role = input("Role (farmer/customer): ")
            location = input("Location: ")
            crud.add_user(username, email, role, location)
        elif choice == "2":
            crud.list_users()
        elif choice == "3":
            user_id = int(input("User ID to delete: "))
            crud.delete_user(user_id)
        elif choice == "4":
            user_id = int(input("User ID to update: "))
            username = input("New username (enter to skip): ")
            email = input("New email (enter to skip): ")
            role = input("New role (enter to skip): ")
            location = input("New location (enter to skip): ")
            crud.update_user(user_id,
                             new_username=username or None,
                             new_email=email or None,
                             new_role=role or None,
                             new_location=location or None)
        elif choice == "5":
            name = input("Name: ")
            price = int(input("Price: "))
            stock = int(input("Stock: "))
            farmer_id = int(input("Farmer User ID: "))
            crud.add_product(name, price, stock, farmer_id)
        elif choice == "6":
            crud.list_products()
        elif choice == "7":
            product_id = int(input("Product ID to delete: "))
            crud.delete_product(product_id)
        elif choice == "8":
            product_id = int(input("Product ID to update: "))
            name = input("New name (enter to skip): ")
            price = input("New price (enter to skip): ")
            stock = input("New stock (enter to skip): ")
            crud.update_product(
                product_id,
                new_name=name or None,
                new_price=int(price) if price else None,
                new_stock=int(stock) if stock else None
            )
        elif choice == "9":
            customer_id = int(input("Customer User ID: "))
            crud.add_order(customer_id)
        elif choice == "10":
            crud.list_orders()
        elif choice == "11":
            order_id = int(input("Order ID to delete: "))
            crud.delete_order(order_id)
        elif choice == "12":
            order_id = int(input("Order ID: "))
            product_id = int(input("Product ID: "))
            quantity = int(input("Quantity: "))
            crud.add_order_item(order_id, product_id, quantity)
        elif choice == "13":
            crud.list_order_items()
        elif choice == "14":
            order_item_id = int(input("Order Item ID to delete: "))
            crud.delete_order_item(order_item_id)
        elif choice == "15":
            name = input("Enter product name to search: ")
            crud.search_products_by_name(name)
        elif choice == "16":
            location = input("Enter location to search for products: ")
            crud.search_products_by_location(location)
        elif choice == "0":
            print("Bye!")
            break

if __name__ == "__main__":
    main()