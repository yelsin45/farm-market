from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String(100), nullable=False)
    role = Column(String, nullable=False)
    location = Column(String, nullable=True)
    products = relationship("Product", back_populates="farmer", cascade="all, delete")
    orders = relationship("Order", back_populates="customer", cascade="all, delete")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    farmer_id = Column(Integer, ForeignKey("users.id"))
    farmer = relationship("User", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product", cascade="all, delete")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("users.id"))
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    customer = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete")

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")

engine = create_engine("sqlite:///market.db")
Session = sessionmaker(bind=engine)