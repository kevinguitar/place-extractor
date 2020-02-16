from Utils import is_int


class Conditions:

    def __init__(self, location, keyword,
                 distance=5, filename=None):
        self.location = location
        self.keyword = keyword
        self.distance = int(distance)
        self.filename = "附近的" + keyword \
            if filename is None or len(filename) == 0 \
            else filename


class ConditionDesk:

    @staticmethod
    def ask_location():
        while True:
            loc = input("請輸入查詢地點的經緯度：ex（23.52,121.64）")
            if loc.count(',') == 1 and loc.count('.') == 2:
                return loc
            else:
                print("錯誤：請用逗號隔開小數（緯度,經度）")
                continue

    @staticmethod
    def ask_keyword():
        while True:
            keyword = input("你想查詢什麼關鍵字？")
            if len(keyword) > 0:
                return keyword
            else:
                print("錯誤：關鍵字不可為空白")
                continue

    @staticmethod
    def ask_distance():
        while True:
            distance = input("你想搜尋方圓幾公尺以內的結果？")
            if is_int(distance):
                return distance
            else:
                continue

    @staticmethod
    def ask_filename():
        while True:
            return input("輸出的檔案名稱？（按Enter跳過）")
