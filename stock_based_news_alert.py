import requests
import smtplib
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = 'yourapikey'
NEWS_API_KEY = "yourapikey"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
my_email = 'yourmailid'
my_password = "yourpassword"
receiver_id = 'yourmailid'


stock_parameter = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'datatype': 'json',
    'outputsize': 'compact',
    'apikey': STOCK_API_KEY
}

news_parameter = {
    'q': STOCK_NAME,
    'apikey': NEWS_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameter)

stock_data = response.json()['Time Series (Daily)']
data = [value for (key, value) in stock_data.items()]
yesterday_price = data[0]['4. close']
day_before_yesterday_price = data[1]['4. close']
difference = float(yesterday_price)-float(day_before_yesterday_price)
percentage_change = (abs(difference)/(float(yesterday_price)+float(day_before_yesterday_price))/2)*100
price_change_in_percentage = round(percentage_change, 2)
if price_change_in_percentage > 0.5:
    response = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    title_list = (response.json()['articles'])
    message_list = (response.json()['articles'])
    connect = smtplib.SMTP('smtp.gmail.com')
    connect.starttls()
    connect.login(user=my_email, password=my_password)
    for i in range(0, 3):
        headline = title_list[i]['title']
        brief = message_list[i]['description']
        print(headline)
        print(brief)
        connect.sendmail(from_addr=my_email,
                         to_addrs=receiver_id,
                         msg=f'subject: {headline} \n\n {brief}')


