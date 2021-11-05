import pytest
from schema import Or, Schema


@pytest.fixture
def tag_detail_schema():
    schema = Schema(
        {
            "id": int,
            "type": str,
            "name": str,
            "menuId": int,
        }
    )
    return schema


@pytest.fixture
def item_detail_schema():
    schema = Schema(
        {
            "id": int,
            "name": str,
            "size": str,
            "price": int,
            "isSold": bool,
            "menuId": int,
        }
    )
    return schema


@pytest.fixture
def menu_detail_schema(item_detail_schema, tag_detail_schema):
    schema = Schema(
        {
            "name": str,
            "description": str,
            "isSold": bool,
            "badge": str,
            "category": int,
            "tags": [tag_detail_schema],
            "items": [item_detail_schema],
        }
    )
    return schema


@pytest.fixture
def menu_list_schema(menu_detail_schema):
    schema = Schema(
        {
            "count": int,
            "next": Or(str, None),
            "previous": Or(str, None),
            "results": [menu_detail_schema],
        }
    )
    return schema
