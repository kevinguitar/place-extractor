# PlaceExtractor

A simple python script developed using Google Map API, you can extract all the places
matching your conditions into an excel file.

## How To Use?

### Prepare Python environment

1. Clone the project
2. Install Python, you can refer to [the guide](https://realpython.com/installing-python/).
3. Install required libs [googlemaps](https://pypi.org/project/googlemaps/) and [xlwt](https://pypi.org/project/xlwt/)

### Create LocalProperties.py

To be able to run the python script, you need to create a LocalProperties.py file with the following information:

```python
API_KEY = 'your_google_map_API_key'
LOCALE = 'en-US'
```

To generate an API_KEY, you can refer
to [this guide](https://github.com/googlemaps/google-maps-services-python?tab=readme-ov-file#api-keys).

### Run the script!

```bash
python Main.py
```

### Provide the information to search places

- **URL of the place**: Full URL of the place that you want to search against, the format looks like this

```
https://www.google.com/maps/place/{name}/@{location},15z/
```

- **Search keyword**: e.g. Restaurant
- **Output filename** (optional): e.g. Restaurants nearby home
- **Radius** (optional): Search radius in meters, leave it empty to search by most relevant places regardless the
  distance

### View the results

The results will be stored on Desktop, and the script will open the file automatically by the default application.

## License

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

```
Copyright (c) 2024 kevinguitar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```