import requests
import bs4
import collections  # this is the best

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')


def print_header():
    print('-------------------------')
    print('        WEATHER APP      ')
    print('-------------------------')


def get_web_html(zipcode):
    # check out urllib (python3) or urllib2 (python2)
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)

    response = requests.get(url)
    # response.status_code returns status on accessing url
    # response.text returns url text
    # print(response.text[0:250]) #slicing

    return response.text


def parse_weather_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # if a parser argument is not given to bs4,
    # it'll use the best fit, and print a warning.

    # CSS selectors from wunderground.com:
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'

    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = clean_text(loc).split('\n')
    loc = loc[0].strip()
    condition = clean_text(condition)
    temp = clean_text(temp)
    scale = clean_text(scale)

    # look at how the tuple is created!
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def clean_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


def main():
    print_header()

    ZipCode = input('Enter the zip code you wish to check the weather for:\n')

    html = get_web_html(ZipCode)

    report = parse_weather_html(html)

    # look at how the tuple elements are accessed!
    print('The temp in {} is {} {} and the forecast is {}'. format(
        report.loc, report.temp, report.scale, report.cond
    ))


if __name__ == '__main__':
    main()
