from pydantic import BaseModel, Field

# ## Схемы продукта Компании


# Базовая схема продукта Компании
class ProductBase(BaseModel):
    article: str
    ean_13: str
    name: str
    cost: float = Field(gt=0)
    min_recommended_price: float | None
    recommended_price: float | None = Field(gt=0)
    category_id: float
    ozon_name: str
    name_1c: str
    wb_name: str
    ozon_article: str
    wb_article: str
    ym_article_td: str


# Схема чтения продукта Компании
class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


# Схема записи продукта компании
class ProductCreate(ProductBase):
    pass
