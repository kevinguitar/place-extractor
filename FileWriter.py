import os
import platform
import subprocess
import xlwt
from xlwt import Formula
from xlwt import Workbook

HEADER = [
    'Name',
    'Address',
    'Distance',
    'Drive time',
    'Phone',
    'Rating',
    'Rates',
    'Website',
    'Google Map URL'
]
COLUMN_WIDTH = [
    300,
    150,
    43,
    66,
    74,
    30,
    45,
    260,
    400
]
MAP_URL = 'https://www.google.com/maps/place/?q=place_id:'


def write_to_excel_and_open(places, filename):
    wb = Workbook()

    sheet = wb.add_sheet('Sheet 1')

    # Write header for file
    header_style = xlwt.easyxf('font: bold 1')
    for i, header in enumerate(HEADER):
        sheet.write(0, i, header, header_style)
        sheet.col(i).width = COLUMN_WIDTH[i] * 42

    for i, place in enumerate(places, start=1):
        for j, field in enumerate([
            place.get('name'),
            place.get('vicinity'),
            place.get('distance').get('text'),
            place.get('duration').get('text'),
            place.get('formatted_phone_number'),
            str(place.get('rating')),
            place.get('user_ratings_total'),
            __make_hyperlink(place.get('website')),
            __make_hyperlink(MAP_URL + place.get('place_id'))
        ]):
            sheet.write(i, j, field)

    file_path = os.path.expanduser('~/Desktop/') + filename + '.xls'
    wb.save(file_path)
    __open_file(file_path)


def __make_hyperlink(link):
    # The limit of hyperlink in Excel is 255 characters
    return link if link is None or len(link) > 255 \
        else Formula('HYPERLINK("%s";"%s")' % (link, link))


def __open_file(filepath):
    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':  # Windows
        os.startfile(filepath)
    else:  # linux variants
        subprocess.call(('xdg-open', filepath))
