import pytest
from httpx import AsyncClient

from src.main import app


@pytest.mark.asyncio
async def test_create_dealer():
    async with AsyncClient(app=app, base_url="http://test") as session:
        response = await session.post("/dealers/",
                                      json={"name": "string",
                                            "dealer_product": []})

    assert response.raise_for_status()
    assert response.json() == {"name": "string",
                               "dealer_product": []}


@pytest.mark.asyncio
async def test_create_company_product():
    async with AsyncClient(app=app, base_url="http://test") as session:
        response = await session.post("/company/products/",
                                      json={"article": "string",
                                            "ean_13": "string",
                                            "name": "string",
                                            "cost": 1.0,
                                            "min_recommended_price": 0.0,
                                            "recommended_price": 1.0,
                                            "category_id": 0.0,
                                            "ozon_name": "string",
                                            "name_1c": "string",
                                            "wb_name": "string",
                                            "ym_article": "string",
                                            "ozon_article": "string",
                                            "wb_article_td": "string",
                                            "ym_article_td": "string",
                                            "id": 1})

    assert response.raise_for_status()
    assert response.json() == {"article": "string",
                               "ean_13": "string",
                               "name": "string",
                               "cost": 1.0,
                               "min_recommended_price": 0.0,
                               "recommended_price": 1.0,
                               "category_id": 0.0,
                               "ozon_name": "string",
                               "name_1c": "string",
                               "wb_name": "string",
                               "ym_article": "string",
                               "ozon_article": "string",
                               "wb_article_td": "string",
                               "ym_article_td": "string",
                               "id": 1}


@pytest.mark.asyncio
async def test_create_dealer_product():
    async with AsyncClient(app=app, base_url="http://test") as session:
        response = await session.post("/dealers/products/",
                                      json={"product_key": 1,
                                            "price": 1,
                                            "product_url": "string",
                                            "product_name": "string",
                                            "date": "string",
                                            "dealer_id": 1})

    assert response.raise_for_status()
    assert response.json() == {"product_key": 1,
                               "price": 1,
                               "product_url": "string",
                               "product_name": "string",
                               "date": "string", 'status': 'waiting'}


@pytest.mark.asyncio
async def test_get_dealers_products():
    async with AsyncClient(app=app, base_url="http://test") as session:
        response = await session.get("/dealers/products/")

    assert response.raise_for_status()
    assert response.json() == [{"product_key": 1,
                                "price": 1.0,
                                "product_url": "string",
                                "product_name": "string",
                                "date": "string",
                                "dealer_id": 1,
                                "status": "waiting",
                                "id": 1}]


@pytest.mark.asyncio
async def test_get_dealer_product():
    async with AsyncClient(app=app, base_url="http://test") as session:
        response = await session.get("/dealers/products/1/")

    assert response.raise_for_status()
    assert response.json() == {"product_key": 1,
                               "price": 1.0,
                               "product_url": "string",
                               "product_name": "string",
                               "date": "string",
                               "dealer_id": 1,
                               "status": "waiting",
                               "id": 1}


@pytest.mark.asyncio
async def test_status_dealer_product():
    async with AsyncClient(app=app, base_url="http://test") as session:
        response = await session.put(
            "/dealers/products/1/waiting/")

    assert response.raise_for_status()
    assert response.json() == {"product_key": 1,
                               "price": 1.0,
                               "product_url": "string",
                               "product_name": "string",
                               "date": "string",
                               "dealer_id": 1,
                               "status": "waiting",
                               "id": 1}


@pytest.mark.asyncio
async def test_get_dealers():
    async with AsyncClient(app=app, base_url="http://test") as session:
        response = await session.get("/dealers/")

    assert response.raise_for_status()
    assert response.json() == [{"name": "string",
                                "dealer_product": [{"product_key": 1,
                                                    "price": 1.0,
                                                    "product_url": "string",
                                                    "product_name": "string",
                                                    "date": "string",
                                                    "dealer_id": 1,
                                                    "status": "waiting",
                                                    "id": 1}],
                                "id": 1}]


@pytest.mark.asyncio
async def test_get_relation_products():
    async with AsyncClient(app=app, base_url="http://test") as session:
        response = await session.get("/dealers/dealerprice/")

    assert response.raise_for_status()
    assert response.json() == [{"product_id": 1,
                                "dealer_id": 1,
                                "key": 1,
                                "date_markup": "2023-12-05T09:16:49.500Z",
                                "id": 1,
                                "product": {"article": "string",
                                            "ean_13": "string",
                                            "name": "string",
                                            "cost": 1.0,
                                            "min_recommended_price": 0.0,
                                            "recommended_price": 1.0,
                                            "category_id": 0.0,
                                            "ozon_name": "string",
                                            "name_1c": "string",
                                            "wb_name": "string",
                                            "ym_article": "string",
                                            "ozon_article": "string",
                                            "wb_article_td": "string",
                                            "ym_article_td": "string",
                                            "id": 1},
                                "dealer": {"name": "string",
                                           "dealer_product": [{"product_key": 1,
                                                               "price": 1.0,
                                                               "product_url": "string",
                                                               "product_name": "string",
                                                               "date": "string",
                                                               "dealer_id": 1,
                                                               "status": "waiting",
                                                               "id": 1}],
                                           "id": 1}}]


@pytest.mark.asyncio
async def test_get_dealer():
    async with AsyncClient(app=app, base_url="http://test") as session:
        response = await session.get("/dealers/1/")

    assert response.raise_for_status()
    assert response.json() == {"name": "string",
                               "dealer_product": [{"product_key": 1,
                                                   "price": 1.0,
                                                   "product_url": "string",
                                                   "product_name": "string",
                                                   "date": "string",
                                                   "dealer_id": 1,
                                                   "status": "waiting",
                                                   "id": 1}],
                                       "id": 1}


@pytest.mark.asyncio
async def test_get_company_products():
    async with AsyncClient(app=app, base_url="http://test") as session:
        response = await session.get("/company/products/")

    assert response.raise_for_status()
    assert response.json() == [{"article": "string",
                                "ean_13": "string",
                                "name": "string",
                                "cost": 1.0,
                                "min_recommended_price": 0.0,
                                "recommended_price": 1.0,
                                "category_id": 0.0,
                                "ozon_name": "string",
                                "name_1c": "string",
                                "wb_name": "string",
                                "ym_article": "string",
                                "ozon_article": "string",
                                "wb_article_td": "string",
                                "id": 1}]


@pytest.mark.asyncio
async def test_get_company_product():
    async with AsyncClient(app=app, base_url="http://test") as session:
        response = await session.get("/company/products/1/")

    assert response.raise_for_status()
    assert response.json() == {"article": "string",
                               "ean_13": "string",
                               "name": "string",
                               "cost": 1.0,
                               "min_recommended_price": 0.0,
                               "recommended_price": 1.0,
                               "category_id": 0.0,
                               "ozon_name": "string",
                               "name_1c": "string",
                               "wb_name": "string",
                               "ym_article": "string",
                               "ozon_article": "string",
                               "ym_article_td": "string",
                               "id": 1}
