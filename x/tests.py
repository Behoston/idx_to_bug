import pytest

from x.models import Item


@pytest.mark.django_db
def test_x():
    i, c = Item.objects.get_or_create(name='test', value=1)
    assert c is True
