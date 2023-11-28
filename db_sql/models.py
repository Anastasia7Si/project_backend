import bcrypt
from fastadmin import SqlAlchemyModelAdmin, register
from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        select, String)
from sqlalchemy.orm import Mapped, mapped_column, relationship


from .database import Base, LocalSession


class Dealer(Base):
    """Модель Дилера."""
    __tablename__ = 'marketing_dealer'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    dealer_product = relationship('DealerPrice', back_populates='dealer')


class DealerPrice(Base):
    """Модель продукта Дилера."""
    __tablename__ = 'marketing_dealerprice'

    id = Column(Integer, primary_key=True)
    product_key = Column(Integer, unique=True)
    price = Column(Float)
    product_url = Column(String, nullable=True)
    product_name = Column(String(150))
    date = Column(DateTime)
    dealer_id = Column(ForeignKey('marketing_dealer.id'))
    # Разобраться с back_populates = products: напоминалка
    dealer = relationship('Dealer')


class Product(Base):
    """Модель продукта Компании."""
    __tablename__ = 'marketing_product'

    id = Column(Integer, primary_key=True)
    article = Column(String(30))
    ean_13 = Column(String(13), nullable=True)
    name = Column(String(150), nullable=True)
    cost = Column(Float, nullable=True)
    min_recommended_price = Column(Float, nullable=True)
    recommended_price = Column(Float, nullable=True)
    category_id = Column(Float, nullable=True)
    ozon_name = Column(String(150), nullable=True)
    name_1c = Column(String(150), nullable=True)
    wb_name = Column(String(150), nullable=True)
    ozon_article = Column(String(30), nullable=True)
    wb_article = Column(String(30), nullable=True)
    ym_article_td = Column(String(30), nullable=True)


class ProductDealerKey(Base):
    """Модель соответствия продуктов."""
    __tablename__ = 'marketing_productdealerkey'

    id = Column(Integer, primary_key=True)
    key = Column(Integer, ForeignKey('marketing_dealerprice.id'))
    product_id = Column(Integer, ForeignKey('marketing_product.id'))
    dealer_id = Column(Integer, ForeignKey('marketing_dealer.id'))

    product = relationship('Product')
    dealer = relationship('Dealer')


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,
                                    nullable=False)
    username: Mapped[str] = mapped_column(String(length=255),
                                          nullable=False)
    hash_password: Mapped[str] = mapped_column(String(length=255),
                                               nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False,
                                               nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False,
                                            nullable=False)

    def __str__(self):
        return self.username


@register(User, sqlalchemy_sessionmaker=LocalSession)
class UserAdmin(SqlAlchemyModelAdmin):
    exclude = ("hash_password",)
    list_display = ("id", "username", "is_superuser", "is_active")
    list_display_links = ("id", "username")
    list_filter = ("id", "username", "is_superuser", "is_active")
    search_fields = ("username",)

    def authenticate(self, username, password):
        sessionmaker = self.get_sessionmaker()
        with sessionmaker() as session:
            query = select(User).filter_by(username=username,
                                           password=password,
                                           is_superuser=True)
            result = session.scalars(query)
            user = result.first()
            if not user:
                return None
            if not bcrypt.checkpw(password.encode(),
                                  user.hash_password.encode()):
                return None
            return user.id
