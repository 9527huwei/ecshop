'''ecshop注册用户'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

# 1、登录192.168.1.83/ecshop
driver.get('http://192.168.1.83/ecshop')
#点击注册
driver.find_element(By.LINK_TEXT, '注册').click()
time.sleep(3)
# 2、输入用户名huwei
driver.find_element(By.ID, 'username').send_keys("huwei12")
# 3、email1289738628@qq.com
driver.find_element(By.ID, 'email').send_keys('128973862@qq.com')
# 4、密码9527huwei
driver.find_element(By.ID, 'password1').send_keys('9527huwei')
#确认密码
driver.find_element(By.ID, 'conform_password').send_keys('9527huwei')
# 5、输入msn:12897@hotmail.com
driver.find_element(By.NAME, 'extend_field1').send_keys('12897@hotmail.com')
# 6、输入qq:1289738628
driver.find_element(By.NAME, 'extend_field2').send_keys('1289738628')
# 7、办公电话:026-5265843
driver.find_element(By.NAME, 'extend_field3').send_keys('026-5265843')
# 8、家庭电话：026-5265842
driver.find_element(By.NAME, 'extend_field4').send_keys('026-5265842')
# 9、手机：18228954790
driver.find_element(By.NAME, 'extend_field5').send_keys('18228954790')
# 10、下拉框选择：我最大的爱好？
box = driver.find_element(By.NAME, 'sel_question')
select1 = Select(box)
select1.select_by_visible_text('我最大的爱好？')
# 11、答案：喝茶
driver.find_element(By.NAME, 'passwd_answer').send_keys('喝茶')
# 12、点击注册
driver.find_element(By.NAME, 'Submit').click()
driver.quit()