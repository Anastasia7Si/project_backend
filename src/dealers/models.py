from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from sqlalchemy.orm import relationship

from ..database import Base


class Dealer(Base):
    """Модель дилеров."""

    __tablename__ = 'marketing_dealer'

    id = Column(
        Integer,
        primary_key=True
    )
    name = Column(
        String(50)
    )

    dealer_product = relationship(
        'DealerPrice',
        lazy='selectin'
    )


class DealerPrice(Base):
    """Модель продуктов дилеров."""

    __tablename__ = 'marketing_dealerprice'

    id = Column(
        Integer,
        primary_key=True
    )
    product_key = Column(
        String,
        unique=False
    )
    price = Column(
        Float,
        nullable=True
    )
    product_url = Column(
        String,
        nullable=True
    )
    product_name = Column(
        String(150),
        nullable=True
    )
    date = Column(
        String,
        nullable=False
    )
    dealer_id = Column(
        ForeignKey('marketing_dealer.id'),
        nullable=False
    )
    status = Column(
        pgEnum(
            'markup',
            'unclaimed',
            'postponed',
            'waiting',
            name='status_type'
        ),
        default='waiting',
        nullable=True
    )
    product_id = Column(
        Integer,
        ForeignKey('marketing_product.id')
    )
    serial_number = Column(
        Integer,
        nullable=True,
        default=None
    )
    date_status = Column(
        TIMESTAMP,
        nullable=True,
        default=None
    )

    product = relationship(
        'Product',
        lazy='selectin'
    )
    dealer = relationship(
        'Dealer',
        lazy='selectin'
    )
