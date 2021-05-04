import requests
from datetime import datetime


def parse_date(get_data):
    row_date = datetime.strptime(get_data, '%Y-%m-%dT%H:%M:%S%z')
    return row_date


def parse_three_date(dates, weathers):
    weather_context = []
    for date, weather in zip(dates, weathers):
        date = parse_date(date)
        weather = "".join(weather.split())
        weather_dict = {'date': date, 'weather': weather}
        weather_context.append(weather_dict)
    return weather_context


def read_weather():
    url = "https://www.jma.go.jp/bosai/forecast/data/forecast/040000.json"
    header = {"content-type": "application/json"}

    response = requests.get(url, headers=header)
    data = response.json()

    publishing_office = data[0]['publishingOffice']  # 仙台管区気象台
    report_datetime = parse_date(data[0]['reportDatetime'])  # 発表日時
    area = data[0]['timeSeries'][0]['areas'][0]['area']['name']  # 場所。今回は仙台市東部のみ
    three_dates = data[0]['timeSeries'][0]['timeDefines']    # 3日間の日付
    three_weathers = data[0]['timeSeries'][0]['areas'][0]['weathers']    # ３日間の天気
    forecasts = parse_three_date(three_dates, three_weathers)    # リスト化

    context = {
        'publishing_office': publishing_office,
        'report_datetime': report_datetime,
        'area': area,
        'forecasts': forecasts,
    }

    return context


if __name__ == '__main__':
    read_weather()
