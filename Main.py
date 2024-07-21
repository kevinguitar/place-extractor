from ConditionDesk import ConditionDesk
from ConditionDesk import Conditions
from ApiManager import get_places
from FileWriter import write_to_excel_and_open

if __name__ == '__main__':
    print("Hello, let me build a table of places for you!\n")

    # Ask for the search conditions
    place_url = ConditionDesk.ask_place_url()
    keyword = ConditionDesk.ask_keyword()
    filename = ConditionDesk.ask_filename()
    radius = ConditionDesk.ask_radius()

    conditions = Conditions(
        place_url=place_url,
        keyword=keyword,
        filename=filename,
        radius=radius
    )

    # Make Google Map API requests
    print("\nSearching places, hang tight...")
    places = get_places(conditions)

    # Extract result into Excel file
    write_to_excel_and_open(places, conditions.filename)
    print("\nThe search has completed, see you again!")
