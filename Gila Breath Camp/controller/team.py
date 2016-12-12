from database.database_functions import *


class Team(object):
    """docstring for Team."""
    def __init__(self, camp_id, team_name , num_campers = 18):
        self.__camp_id__ = camp_id
        self.__team_name__ = team_name
        self.__num_campers__ = num_campers

    def insert_team(self):
        insert_team_db(self.__camp_id__, self.__team_name__, self.__num_campers__)

    @staticmethod
    def select_team(team_id):
        return select_team_by_id(team_id)

    @staticmethod
    def get_available_team(camp_id):
        return select_available_team(camp_id)

    @staticmethod
    def increment_checked_in(team_id):
        increment_checked_in_num_team(team_id)

    @staticmethod
    def decrement_checked_in(team_id):
        decrement_checked_in_num_team(team_id)

    @staticmethod
    def update_teams_num(num):
        update_teams_num_db(num)

    @staticmethod
    def update_team_id(camper_id, camp_id, team_id):
        update_team_id_checked_in(camper_id, camp_id, team_id)

    @staticmethod
    def get_all_ids():
        return get_all_teams_id_db()

    @staticmethod
    def update_team_options(camper_id, my_str):
        update_team_options_db(camper_id, my_str)
