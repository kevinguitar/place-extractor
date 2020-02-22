from FitSheetWrapper import FitSheetWrapper
import xlwt
from xlwt import Workbook

HEADER = [
    '名稱',
    '地址',
    '距離',
    '預估開車時間',
    '電話',
    '評分',
    '評分人數',
    '網站',
    'Google Map連結'
]
MAP_URL = 'https://www.google.com/maps/place/?q=place_id:'


def extract_to_excel(places, filename):
    wb = Workbook()

    sheet = FitSheetWrapper(wb.add_sheet('Sheet 1'))

    # Write header for file
    header_style = xlwt.easyxf('font: bold 1')
    for i, header in enumerate(HEADER):
        sheet.write(0, i, header, header_style)

    for i, place in enumerate(places, start=1):
        sheet.write(i, 0, place.get('name'))
        sheet.write(i, 1, place.get('vicinity'))
        sheet.write(i, 2, place.get('distance').get('text'))
        sheet.write(i, 3, place.get('duration').get('text'))
        sheet.write(i, 4, place.get('formatted_phone_number'))
        sheet.write(i, 5, str(place.get('rating')))
        sheet.write(i, 6, str(place.get('user_ratings_total')))
        sheet.write(i, 7, place.get('website'))
        sheet.write(i, 8, MAP_URL + place.get('place_id'))

    return wb.save(filename + '.xls')
