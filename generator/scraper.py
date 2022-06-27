import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROMEDRIVER_PATH = "/opt/homebrew/bin/chromedriver"
options = Options()
options.headless = True
options.add_argument("--log-level=3")
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

url = "https://leetcode.com/problems/two-sum/"
driver.get(url)
# Wait 20 secs or until div with id initial-loading disappears
element = WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.ID, "initial-loading")))

title = "Two Sum"
# Get current tab page source
html = driver.page_source
soup = bs4.BeautifulSoup(html, "html.parser")
# print(soup)
# print()
# print(str(soup.find("div", {"class": "content__u3I1 question-content__JfgR"})))
# Construct HTML
# title_decorator = '*' * 5
# problem_title_html = title_decorator + f'<div id="title">{title}</div>' + '\n' + title_decorator
# problem_html = problem_title_html + str(soup.find("div", {"class": "content__u3I1 question-content__JfgR"})) + '<br><br><hr><br>'
#
# # Append Contents to a HTML file
# with open("out.html", "ab") as f:
#     f.write(problem_html.encode(encoding="utf-8"))
# driver.find_element_by_class_name("select__2iyW select-container__29U9")
# driver.find_element(By.CLASS_NAME, "select-container__29U9").click()
driver.find_element(By.CLASS_NAME, "ant-select-selection--single").click()
driver.find_element(By.XPATH, "//*[contains(text(), 'Python3')]").click()
driver.find_element(By.XPATH, "//span[@role=\"presentation\"]")
# driver.find_element(By.CSS_SELECTOR, "[data-cy: \"lang-select-Python3\"]")
html = driver.page_source
soup = bs4.BeautifulSoup(html, "html.parser")
elements = soup.find_all('span', {'role': 'presentation'})

tags = []
for e in elements:
    for tag in e:
        # if tag.text != ' ':
        tags.append(tag.text)
# index = 0
# signature = []
# while index < len(tags) and tags[index] != 'pub':
#     index += 1
# index += 2
#
# while index < len(tags) and tags[index] != ' {':
#     signature.append(tags[index])
#     index += 1
#
# signature = ''.join(signature)
# definition, return_type = map(lambda x: x.strip(), signature.split('->'))
# print(definition)
# print(return_type)

for t in tags:
    print(t)

print(''.join(tags))
