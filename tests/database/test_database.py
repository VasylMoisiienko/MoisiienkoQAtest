import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')
    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)
    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'Ð¿ÐµÑ‡Ð¸Ð²Ð¾', 'Ñ�Ð¾Ð»Ð¾Ð´ÐºÐµ', 30)
    water_qnt = db.select_product_qnt_by_id(4)
    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'Ñ‚ÐµÑ�Ñ‚Ð¾Ð²Ñ–', 'Ð´Ð°Ð½Ñ–', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)
    assert len(qnt) == 0


@pytest.mark.database
def test_detiled_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Ð—Ð°Ð¼Ð¾Ð²Ð»ÐµÐ½Ð½Ñ�", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'Ñ�Ð¾Ð»Ð¾Ð´ÐºÐ° Ð²Ð¾Ð´Ð°'
    assert orders[0][3] == 'Ð· Ñ†ÑƒÐºÑ€Ð¾Ð¼'
