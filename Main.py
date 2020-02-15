from ConditionDesk import ConditionDesk
from ConditionDesk import Conditions
from ApiManager import get_places
from FileExtractor import extract_to_excel

if __name__ == '__main__':

    print("歡迎光臨！告訴我搜尋地點的條件吧～\n")

    # Ask for all conditions
    lat = ConditionDesk.ask_latitude()
    lon = ConditionDesk.ask_longitude()
    keyword = ConditionDesk.ask_keyword()
    distance = ConditionDesk.ask_distance()
    filename = ConditionDesk.ask_filename()

    # lat = '25.0264233'
    # lon = '121.5279489'
    # keyword = '飯店'
    # distance = '1000'
    # filename = 'test'

    conditions = Conditions(
        latitude=lat, longitude=lon, keyword=keyword,
        distance=distance, filename=filename
    )

    # Make Google Map API requests
    print("\n取得資料中... 嘟嘟嘟...\n")
    places = get_places(conditions)

    # Extract result into Excel file
    extract_to_excel(places, conditions.filename)
    print("大功告成！檔案已輸出 <3\n")
