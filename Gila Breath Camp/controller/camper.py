from database.database_functions import *


class Camper:
    """
    a class that represent camper which is responsible for validating data before commiting to the database
    """
    def __init__(self, camper_id, first_name = '', last_name = '', birth_date = '', gender = '', address = '', guardian_name = ''):
        """
        initialize a camper object, you can only define a camper id
        """
        self.__camper_id__ = camper_id
        self.__first_name__ = first_name
        self.__last_name__ = last_name
        self.__birth_date__ = birth_date
        self.__gender__ = gender
        self.__address__ = address
        self.__guardian_name__ = guardian_name

    def insert_camper(self):
        """
        insert a camper record into the db after validating
        """
        return insert_camper_into_db(self.__first_name__, self.__last_name__, self.__birth_date__, self.__gender__, self.__address__, self.__guardian_name__)

    def update_camper(self):
        """
        update a camper record to the db after validating
        """
        update_camper_to_db(self.__camper_id__, self.__first_name__, self.__last_name__, self.__birth_date__, self.__gender__, self.__address__)

    def select_camper(self):
        """
        select a camper record from the db after validating
        returns a camper object
        """
        return select_camper_by_id(self.__camper_id__)

    def delete_camper(self):
        """
        delete a camper record from the db after validating
        """
        return delete_camper_by_id(self.__camper_id__)

    @staticmethod
    def get_all_ids():
        return get_all_campers_ids()

    def __str__(self):
        return self.__camper_id__, self.__first_name__, self.__last_name__, self.__birth_date__, self.__gender__, self.__address__

    @staticmethod
    def get_all_ids_assigned_camp(camp_id):
        """
        get all campers registered in this camp ordered by date of birth
        """
        return get_all_ids_assigned_camp_db(camp_id)

    @staticmethod
    def unregister_camper(camper_id):
        data = get_camper_registeration_info(camper_id)
        camp_id = data[0]
        bunkhouse_id = data[1]
        team_id = data[2]
        unregister_camper_db(camper_id, camp_id, bunkhouse_id, team_id)

    @staticmethod
    def get_camper_id_by_name(name):
        name_lst = name.split(' ')
        first_name = name_lst[0]
        last_name = name_lst[1]
        return get_camper_id_by_first_last_name(first_name, last_name)

    @staticmethod
    def get_camper_bunkhouse(camper_id):
        return get_camper_bunkhouse_db(camper_id)

    @staticmethod
    def get_camper_team(camper_id):
        return get_camper_team_db(camper_id)
