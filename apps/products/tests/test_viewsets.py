import pytest
from rest_framework import status
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


class TestProductsViewSet:
    def test_menu_list(
        self,
        client,
        menu_list_schema,
    ):

        menu_list_url = reverse("products:menu-list")

        # Test menu list
        resp = client.get(menu_list_url)
        assert resp.status_code == status.HTTP_200_OK
        assert menu_list_schema.is_valid(resp.json())

    # def test_create_menu_list(
    #     self,
    #     client,
    #     menu_detail_schema,
    # ):
    #     payload = {
    #         "name": "리코타 하베스트 샐러드",
    #         "description": "브런치 스타일 샐러드",
    #         "isSold": False,
    #         "badge": "NEW",
    #         "category": 1,
    #         "items": [
    #             {"name": "미디움", "size": "M", "price": 8000, "isSold": False},
    #             {"name": "라지", "size": "L", "price": 10000, "isSold": False},
    #         ],
    #         "tags": [{"type": "vegetarianism", "name": "락토베지테리언"}],
    #     }

    #     create_menu_url = reverse("products:menu-list")

    #     resp = client.post(create_menu_url, data=payload, format="json")
    #     assert resp.status_code == status.HTTP_201_CREATED
    #     assert menu_detail_schema.is_valid(resp.json())
