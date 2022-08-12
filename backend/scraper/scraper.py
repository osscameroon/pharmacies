import csv
from time import sleep

from IPython.core import error
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from parsel import Selector
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.errorhandler import NoSuchElementException, InvalidSelectorException, \
    ElementClickInterceptedException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.google.com/maps/')
search_input = driver.find_element(By.NAME, 'q')

search_input.send_keys('Pharmacies')
sleep(3)
search_input.send_keys(Keys.ENTER)

sleep(14)

query_results = driver.find_element(
    By.CSS_SELECTOR,
    'div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd>div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd'
)

vertical_ordinate = 100

fields = ['Name', 'Location', 'Contact', 'Rating', 'Latitude', 'Longitude']

while True:
    driver.execute_script(
        "arguments[0].scrollTop = arguments[1]", query_results, vertical_ordinate)
    vertical_ordinate += 100
    sleep(1)
    try:
        driver.find_element(
            By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]'
                      '/div[243]/div/p/span/span[1]'
        )
        print(
            driver.find_element(
                By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]'
                          '/div[243]/div/p/span/span[1]'
            ).text
        )
        break
    except InvalidSelectorException:
        pass
    except NoSuchElementException:
        pass
sel = Selector(text=driver.page_source)

total_elements = driver.find_elements(
    By.CSS_SELECTOR, 'div.lI9IFe>div.y7PRA>div>div>div>div.NrDZNb>div>span'
)

[print(f'{total_elements.index(item) + 1} ==> {item.text.capitalize()}') for item in total_elements]

pharmacies_locations = []
iterator = 3

for item in range(len(total_elements)):
    print(iterator)
    try:
        driver.find_element(
            By.XPATH,
            f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{iterator}]/div/a'
        ).click()
    except ElementClickInterceptedException:
        driver.execute_script(
            "arguments[0].click();", driver.find_element(
                By.XPATH,
                f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{iterator}]/div/a'
            )
        )
    sleep(30)
    location = driver.find_element(
        By.CSS_SELECTOR,
        'div:nth-child(3)>button>div.AeaXub>div.rogA2c>div.Io6YTe.fontBodyMedium'
    ).text
    iterator = iterator + 2
    pharmacies_locations.append(location)

with open('pharmacies.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(fields)
    for code in pharmacies_locations:
        driver.find_element(By.TAG_NAME('body')).send_keys(Keys.CONTROL + 't')
        sleep(3)
        driver.get('https://developers.google.com/maps/documentation/geocoding/overview')
        sleep(12)
        code_converter_input = driver.find_element(By.CSS_SELECTOR, '#query-input')
        code_converter_input.send_keys(Keys.CLEAR)
        sleep(1)
        code_converter_input.send_keys(code)
        code_converter_input.send_keys(Keys.ENTER)
        sleep(3)
        if driver.find_element(By.CSS_SELECTOR, '#status-line>span.OK'):
            full_location = driver.find_element(
                By.CSS_SELECTOR,
                '#result-0>table>tbody>tr>td:nth-child(2)>p.result-location'
            ).text.replace('Location:', '').replace('', '').replace(',,', ',').split()
            longitude = full_location[0]
            latitude = full_location[1]
        elif driver.find_element(By.CSS_SELECTOR, '#status-line>span.ZERO_RESULTS'):
            new_converter_query = [code].pop(1)
            code_converter_input.send_keys(new_converter_query)
            code_converter_input.send_keys(Keys.ENTER)
            full_location = driver.find_element(
                By.CSS_SELECTOR,
                '#result-0>table>tbody>tr>td:nth-child(2)>p.result-location'
            ).text.replace('Location:', '').replace('', '').replace(',,', ',').split()
            longitude = full_location[0]
            latitude = full_location[2]
        else:
            full_location = ['unknown', 'unknown']
            location = full_location[0]
            latitude = full_location[1]
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        name = driver.find_element(
            By.XPATH,
            f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/'
            f'div[{iterator}]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/span'
        ).text
        location = pharmacies_locations[pharmacies_locations.index(code)]
        latitude = latitude
        longitude = longitude
        contact = driver.find_element(
            By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{iterator}]/'
                      f'div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[2]/span[2]/jsl/span[2]'
        ).text

        try:
            rating = driver.find_element(
                By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/'
                          f'div[{iterator}]/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/span[2]/'
                          f'span[2]/span[1]'
            ).text
        except InvalidSelectorException:
            rating = driver.find_element(
                By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{iterator}]'
                          f'/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/span[2]/span[1]'
            ).text

        except NoSuchElementException:
            rating = driver.find_element(
                By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{iterator}]'
                          f'/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/span[2]/span[1]'
            ).text
        except error:
            rating = f'No reviews'
        iterator = +2
        writer.writerow([name, location, contact, rating, latitude, longitude])
        sleep(1)
    csv_file.close()
