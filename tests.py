import pytest
from httpx import AsyncClient

from src.main import app


client = AsyncClient(app)


@pytest.mark.asyncio
async def test_matching_matching():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get('/company/machine-matching/1')
    assert response.raise_for_status()
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_company_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get('/company/products/')
    assert response.raise_for_status()
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_one_company_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get('/company/products/1/')
    assert response.raise_for_status()
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_dealers_products():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get('/dealers/products/')
    assert response.raise_for_status()
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_one_dealer_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get('/dealers/products/1/')
    assert response.raise_for_status()
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_all_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get('/dealers/')
    assert response.raise_for_status()
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_one_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get('/dealers/1/')
    assert response.raise_for_status()
    assert len(response.json()) > 0
