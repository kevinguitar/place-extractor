from ConditionDesk import ConditionDesk
from ConditionDesk import Conditions

if __name__ == '__main__':

    # Ask for all conditions
    lat = ConditionDesk.ask_latitude()
    lon = ConditionDesk.ask_longitude()
    keyword = ConditionDesk.ask_keyword()
    distance = ConditionDesk.ask_distance()
    filename = ConditionDesk.ask_filename()
    sort = ConditionDesk.ask_sort()

    conditions = Conditions(
        latitude=lat, longitude=lon, keyword=keyword,
        distance=distance, filename=filename, sort=sort
    )
