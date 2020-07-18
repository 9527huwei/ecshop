'''后台搜索订单'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)
wait = WebDriverWait(driver, 10, 0.5)

#一、访问网站并登录
driver.get('http://192.168.1.83/ecshop/admin')
driver.maximize_window()
#1、输入用户名
driver.find_element(By.NAME, 'username').send_keys('admin')
#2、输入密码
driver.find_element(By.NAME, 'password').send_keys('admin')
#3、点击登录
driver.find_element(By.CLASS_NAME, 'button').click()

#二、进入订单页面
# 1、跳转至frame
driver.switch_to.frame('menu-frame')
time.sleep(1)
# 2、点击订单管理
driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[3]').click()
# 3、点击订单查询
wait.until(EC.presence_of_element_located((By.LINK_TEXT, '订单查询')))
driver.find_element(By.LINK_TEXT, '订单查询').click()
# 4、退出当前frame
driver.switch_to.parent_frame()
# 5、进入页面的frame
driver.switch_to.frame('main-frame')
time.sleep(1)

#三、输入查询条件
#1、输入订单号
driver.find_element(By.NAME, 'order_sn').send_keys('1288812333')
# 2、输入购货人
driver.find_element(By.NAME, 'user_name').send_keys('xiaowei')
# 3、输入电话
driver.find_element(By.NAME, 'tel').send_keys('18228954790')
# 4、选择所在地区
country = driver.find_element(By.NAME, 'country')
province  = driver.find_element(By.NAME, 'province')
city = driver.find_element(By.NAME, 'city')
district = driver.find_element(By.NAME, 'district')
Select(country).select_by_value('1')
Select(province).select_by_value('26')
Select(city).select_by_value('342')
Select(district).select_by_value('2909')
# 5、选择下单时间
jst = "document.getElementById('start_time_id').value='2020-06-02 22:00'"
driver.execute_script(jst)
jet = "document.getElementById('end_time_id').value='2020-07-10 22：00'"
driver.execute_script(jet)
#6、选择订单状态
order = driver.find_element(By.NAME, 'order_status')
Select(order).select_by_value('4')
#7、点击搜索
driver.find_element(By.NAME, 'order_status').click()
time.sleep(3)
driver.quit()