import os
import pytest
from shutil import copyfile

os.environ['gila_testing_mode'] = "1"
from controller.authenticate import *
from controller.camp import *
from controller.camper import *
from controller.payment import * 
from gui.camper_forum import *

def setup():
    copyfile('gila_init.db', 'gila_testing.db')


def teardown():
    pass

def test_login_guest():
    auth_guest = AuthUser(username="guest", password="guest")
    assert auth_guest.authenticate() == True
    assert auth_guest.is_admin() == False

def test_login_admin():
    auth_guest = AuthUser(username="admin", password="admin")
    assert auth_guest.authenticate() == True
    assert auth_guest.is_admin() == True

@pytest.mark.incremental
class TestInsertCamper:
    def test_birthday_validation(self):
        # test is_valid_date
        birth_date = "blahblah"
        assert is_valid_date(birth_date) == False
        birth_date = "1995-13-13"
        assert is_valid_date(birth_date) == False
        birth_date = "1995-01-01"

        assert is_valid_date(birth_date) == True 
        assert validate_age_9_18(birth_date) == False
        birth_date = "2005-01-01"
        assert validate_age_9_18(birth_date) == True

    def test_insert_camper(self):
        # check if we are working on a clean database
        assert len(Camper.get_all_ids()) == 0

        # check the number of camps
        all_camps = Camp.get_all_ids()
        assert len(all_camps) == 3
    
        # pick camp_id 
        camp_id = all_camps[0][0]

        # describe camper
        gender = "Male"
        name1 = "Joe"
        name2 = "Smith"
        address = "NY" 
        guardian_name = "Guardian Name"
        birth_date = "2005-01-01"

        # insert camper into database
        camper = Camper(camp_id, name1, name2, birth_date, gender, address, guardian_name)
        camper_id = camper.insert_camper()

        # test that camper_id inserted into database
        assert ((camper_id,) in Camper.get_all_ids()) == True

    def test_assign_camper_to_bunkhouses(self):
        # get camp and camper
        camp_id = Camp.get_all_ids()[0][0]
        camper_id = Camper.get_all_ids()[0][0]

        # get camper data
        camper = Camper(camper_id)
        data_camper = camper.select_camper()

        # get camp_id and gender from camper_data
        gender = data_camper[3]
        # test that there are some bunkhouses
        bunkhouses_ids = Bunkhouse.get_available_bunkgouses(gender, camp_id)
        assert len(bunkhouses_ids) > 0

        # test that there are some available teams
        teams_ids = Team.get_available_team(camp_id)
        assert len(teams_ids) > 0

        # increment checked in
        Bunkhouse.increment_checked_in(bunkhouses_ids[0][0])
        Team.increment_checked_in(teams_ids[0][0])

        # insert into bunkhouse
        Bunkhouse.insert_check_in(camper_id,camp_id)

        # check if inserted successfully
        data_camp = Bunkhouse.select_camp_team_bunkhouse(camper_id)
        assert str(camp_id) in data_camp[0]

    def test_camper_payment(self):
        payment_ids = Payment.get_all_ids()
        assert len(payment_ids) == 0 

        print(payment_ids)
        camp_id = Camp.get_all_ids()[0][0]
        camper_id = Camper.get_all_ids()[0][0]
        payment_date = "2017-03-03"
        assert is_valid_date(payment_date)==True 
        paid_amount = 1000

        payment = Payment(1,camper_id, camp_id, payment_date, paid_amount)
        payment.insert_payment()        

        assert len(Payment.get_all_ids()) == 1



    def test_delete_camper(self):
        camper_id = Camper.get_all_ids()[0][0]

        # delete camper
        camper = Camper(camper_id)
        camper.delete_camper()

        # check if there is no more campers
        assert len(Camper.get_all_ids()) == 0
