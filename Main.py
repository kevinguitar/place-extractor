from ConditionDesk import ConditionDesk
from ConditionDesk import Conditions
from ApiManager import get_places
from FileWriter import extract_to_excel

if __name__ == '__main__':
    print("歡迎光臨！告訴我搜尋地點的條件吧～\n")

    # Ask for all conditions
    place_url = ConditionDesk.ask_place_url()
    keyword = ConditionDesk.ask_keyword()
    filename = ConditionDesk.ask_filename()

    conditions = Conditions(
        place_url=place_url,
        keyword=keyword,
        filename=filename
    )

    # location = '25.0264233,121.5279489'
    # keyword = '飯店'
    # filename = 'test'
    # radius = 1000   # Just for test
    #
    # conditions = Conditions(
    #     location=location,
    #     keyword=keyword,
    #     filename=filename,
    #     radius=radius
    # )

    # Make Google Map API requests
    print("\n取得資料中... 嘟嘟嘟...\n")
    places = get_places(conditions)

    # Extract result into Excel file
    extract_to_excel(places, conditions.filename)
    print("大功告成！檔案已輸出 <3\n")
