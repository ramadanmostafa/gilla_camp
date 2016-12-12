from database.database_functions import *


class Camp:
    """
    a class that represent a camp which is responsible for validating data before commiting to the database
    """
    def __init__(self, camp_id, start_date = '', end_date = '', bunck_num = '', team_num = '', cost = ''):
        """
        initialize a camper object, you can only define a camper id
        """
        self.__camp_id__ = camp_id
        self.__start_date__ = start_date
        self.__end_date__ = end_date
        self.__bunck_num__ = bunck_num
        self.__team_num__ = team_num
        self.__cost__ = cost

    def insert_camp(self):
        """
        insert a camp record into the db after validating
        """
        insert_camp_into_db(self.__start_date__, self.__end_date__, self.__bunck_num__, self.__team_num__, self.__cost__)

    def update_camp(self):
        """
        update a camp record to the db after validating
        """
        update_camp_to_db(self.__camp_id__, self.__start_date__, self.__end_date__, self.__bunck_num__, self.__team_num__, self.__cost__)

    def select_camp(self):
        """
        select a camp record from the db after validating
        returns a camp object
        """
        return select_camp_by_id(self.__camp_id__)

    def delete_camp(self):
        """
        delete a camp record from the db after validating
        """
        return delete_camp_by_id(self.__camp_id__)

    def get_camp_id(self):
        return select_camp_id_by_date(self.__start_date__, self.__end_date__)

    def get_camp_num_bunkhouse_team(self):
        return get_camp_num_bunkhouse_team_db(self.__camp_id__)

    @staticmethod
    def get_all_ids():
        return get_all_camps_ids()

    ###################updated 11-10-2016
    @staticmethod
    def camper_check_in(camper_id):
        update_bunkhouse_id_checked_in(camper_id)

    @staticmethod
    def get_start_end_data(camps):
        lst = []
        for camp_id in camps.split(','):
            lst.append(get_start_end_data_db(camp_id.strip()))
        start_date = ""
        end_date = ""
        for item in lst:
            start_date += item[0] + ", "
            end_date += item[1] + ", "
        return start_date[:-2], end_date[:-2]

    @staticmethod
    def increment_registered(camp_id):
        increment_campers_registered_count(camp_id)

    @staticmethod
    def update_max_capacity(bunkhouses_capacity):
        for camp_id in Camp.get_all_ids():
            update_max_capacity_db(int(bunkhouses_capacity))

    def get_number_campers_registered(self):
        data = get_number_campers_registered_db(self.__camp_id__)
        return str(data[0]) + "/" + str(data[1])


    def __str__(self):
        return self.__camp_id__, self.__start_date__, self.__end_date__, self.__bunck_num__, self.__team_num__, self.__cost__
