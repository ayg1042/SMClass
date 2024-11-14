from bs4 import BeautifulSoup
# flight.html
# 불러와서 금액이 8만원 미만 항공권을 출력하세요.
# 김포 - 제주 8만원 이하 항공권 개수 15개
# 제주 - 김포 8만원 이하 항공권 개수 30개

with open('flight.html', 'r', encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'lxml')

data = soup.select_one('#__next > div > main > div.domestic_flight_content__vYDHd > div > div.domestic_results__gp5WB')
data_list = data.select('div.domestic_Flight__8bR_b')
print(len(data_list))
#__next > div > main > div.domestic_flight_content__vYDHd > div > div.domestic_results__gp5WB > div:nth-child(2) > div > div.domestic_schedule__3uLrb > div > div.domestic_heading__eXCgv > div > div > span.airline_text__WWkbY > b
#__next > div > main > div.domestic_flight_content__vYDHd > div > div.domestic_results__gp5WB > div:nth-child(3) > div > div.domestic_schedule__3uLrb > div > div.domestic_heading__eXCgv > div > div > span.airline_text__WWkbY > b
for i in data_list:
  flight_name = i.select_one('div > div.domestic_schedule__3uLrb > div > div.domestic_heading__eXCgv > div > div > span.airline_text__WWkbY > b').text.strip()
  money = i.select_one('div > div.domestic_prices__WBiv_ > div.domestic_item__5CAye > b > i').text.strip().replace(',', '')
  if int(money) <= 80000:
    print(f'항공사 : {flight_name},\t 금액 : {int(money):,d}')
  # print(money)
  # print(flight_name)