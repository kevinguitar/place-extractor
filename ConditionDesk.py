class Conditions:

    def __init__(self, place_url, keyword, filename, radius):
        self.place_url = place_url
        self.keyword = keyword
        self.filename = keyword + '_nearby' if filename == "" else filename
        self.radius = None if radius == "" else int(radius)


class ConditionDesk:

    @staticmethod
    def ask_place_url():
        while True:
            place_url = input("Enter the full URL of your place:\n")
            if len(place_url) > 0:
                return place_url
            else:
                print("Error: URL is required")
                continue

    @staticmethod
    def ask_keyword():
        while True:
            keyword = input("\nEnter the keyword:\n")
            if len(keyword) > 0:
                return keyword
            else:
                print("Error: Keyword is required")
                continue

    @staticmethod
    def ask_filename():
        while True:
            return input("\nEnter the output file name (Optional):\n")

    @staticmethod
    def ask_radius():
        while True:
            return input("\nEnter the radius of search in meter (Optional):\n")
