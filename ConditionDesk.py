class Conditions:

    def __init__(self, place_url, keyword, filename=None, radius=None):
        self.place_url = place_url
        self.keyword = keyword
        self.filename = "附近的" + keyword \
            if filename is None or len(filename) == 0 \
            else filename
        self.radius = radius


class ConditionDesk:

    @staticmethod
    def ask_place_url():
        while True:
            place_url = input("請輸入查詢地點的經緯度：ex（23.52,121.64）\n")
            if len(place_url) > 0:
                return place_url
            else:
                print("錯誤：請用逗號隔開小數（緯度,經度）")
                continue

    @staticmethod
    def ask_keyword():
        while True:
            keyword = input("\n你想查詢什麼關鍵字？\n")
            if len(keyword) > 0:
                return keyword
            else:
                print("錯誤：關鍵字不可為空白")
                continue

    @staticmethod
    def ask_filename():
        while True:
            return input("\n輸出的檔案名稱？（按Enter跳過）\n")
