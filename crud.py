from models import User, Product, Order, OrderItem, Session
import datetime

def add_user(username, email, role, location):
    with Session() as session:
        user = User(username=username, email=email, role=role, location=location)
        session.add(user)
        session.commit()
        print("User added.")

def list_users():
    with Session() as session:
        for u in session.query(User).all():
            print(f"{u.id}: {u.username} ({u.role}) [{u.location}]")

def delete_user(user_id):
    with Session() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            print("User deleted.")
        else:
            print("User not found.")

def update_user(user_id, new_username=None, new_email=None, new_role=None, new_location=None):
    with Session() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            print("User not found.")
            return
        if new_username: user.username = new_username
        if new_email: user.email = new_email
        if new_role: user.role = new_role
        if new_location: user.location = new_location
        session.commit()
        print("User updated.")

def add_product(name, price, stock, farmer_id):
    with Session() as session:
        product = Product(name=name, price=price, stock=stock, farmer_id=farmer_id)
        session.add(product)
        session.commit()
        print("Product added.")

def list_products():
    with Session() as session:
        for p in session.query(Product).all():
            print(f"{p.id}: {p.name} - ${p.price} ({p.stock} in stock) Farmer:{p.farmer_id}")

def delete_product(product_id):
    with Session() as session:
        product = session.query(Product).filter(Product.id == product_id).first()
        if product:
            session.delete(product)
            session.commit()
            print("Product deleted.")
        else:
            print("Product not found.")

def update_product(product_id, new_name=None, new_price=None, new_stock=None):
    with Session() as session:
        product = session.query(Product).filter(Product.id == product_id).first()
        if not product:
            print("Product not found.")
            return
        if new_name: product.name = new_name
        if new_price is not None: product.price = new_price
        if new_stock is not None: product.stock = new_stock
        session.commit()
        print("Product updated.")

def add_order(customer_id):
    with Session() as session:
        order = Order(customer_id=customer_id, order_date=datetime.datetime.utcnow())
        session.add(order)
        session.commit()
        print("Order added. ID:", order.id)

def list_orders():
    with Session() as session:
        for o in session.query(Order).all():
            print(f"{o.id}: Customer {o.customer_id} on {o.order_date}")

def delete_order(order_id):
    with Session() as session:
        order = session.query(Order).filter(Order.id == order_id).first()
        if order:
            session.delete(order)
            session.commit()
            print("Order deleted.")
        else:
            print("Order not found.")

def add_order_item(order_id, product_id, quantity):
    with Session() as session:
        product = session.query(Product).filter(Product.id == product_id).first()
        if not product:
            print("Product not found.")
            return
        if product.stock < quantity:
            print("Not enough stock!")
            return
        item = OrderItem(order_id=order_id, product_id=product_id, quantity=quantity)
        product.stock -= quantity  
        session.add(item)
        session.commit()
        print("Order item added and stock updated.")

def list_order_items():
    with Session() as session:
        for oi in session.query(OrderItem).all():
            print(f"{oi.id}: Order {oi.order_id} Product {oi.product_id} Qty {oi.quantity}")

def delete_order_item(order_item_id):
    with Session() as session:
        order_item = session.query(OrderItem).filter(OrderItem.id == order_item_id).first()
        if order_item:
            session.delete(order_item)
            session.commit()
            print("Order item deleted.")
        else:
            print("Order item not found.")

def search_products_by_name(name):
    with Session() as session:
        results = session.query(Product).filter(Product.name.ilike(f"%{name}%")).all()
        if results:
            for p in results:
                print(f"{p.id}: {p.name} - ${p.price} ({p.stock} in stock) Farmer:{p.farmer_id}")
        else:
            print("No products found with that name.")

def search_products_by_location(location):
    with Session() as session:
        results = session.query(Product).join(User).filter(User.location.ilike(f"%{location}%")).all()
        if results:
            for p in results:
                print(f"{p.id}: {p.name} - ${p.price} ({p.stock} in stock) Farmer:{p.farmer_id} [{p.farmer.location}]")
        else:
            print("No products found for that location.")