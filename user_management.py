'''用户管理编辑用户'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

# 1、登录
driver.get('http://192.168.1.83/ecshop')
driver.find_element(By.LINK_TEXT, '登录').click()    #点击登录
driver.find_element(By.NAME, 'username').send_keys('huwei1')    #输入用户名
driver.find_element(By.NAME, 'password').send_keys('9527huwei')  #输入用户名
driver.find_element(By.NAME, 'submit').click()  #点击登录

# 2、点击我的账户
driver.find_element(By.LINK_TEXT, '我的账户').click()
#3、点击用户信息
driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div/div/div/a[2]').click()
#4、修改出生日期
bsyear = driver.find_element(By.NAME, 'birthdayYear')
bsmonth = driver.find_element(By.NAME, 'birthdayMonth')
bsday = driver.find_element(By.NAME, 'birthdayDay')
Select(bsyear).select_by_value('1993')
Select(bsmonth).select_by_value('12')
Select(bsday).select_by_value('8')
#5、修改性别
driver.find_elements(By.XPATH, '/html/body/div[8]/div[2]/div/div/div/form[1]/table/tbody/tr[2]/td[2]/input[3]')[0].click()
#6、修改电子邮箱
driver.find_element(By.NAME, 'email').clear()
driver.find_element(By.NAME, 'email').send_keys('1320124794@qq.com')
#修改msn
driver.find_element(By.NAME, 'extend_field1').clear()
driver.find_element(By.NAME, 'extend_field1').send_keys('1320124794@qq.com')
#修改QQ
driver.find_element(By.NAME, 'extend_field2').clear()
driver.find_element(By.NAME, 'extend_field2').send_keys('1320124794')
#修改办公电话
driver.find_element(By.NAME, 'extend_field3').clear()
driver.find_element(By.NAME, 'extend_field3').send_keys('026-5265846')
#修改家庭电话
driver.find_element(By.NAME, 'extend_field4').clear()
driver.find_element(By.NAME, 'extend_field4').send_keys('026-5265847')
#修改手机电话
driver.find_element(By.NAME, 'extend_field5').clear()
driver.find_element(By.NAME, 'extend_field5').send_keys('18228954790')
#7、修改密码提示问题
question = driver.find_element(By.NAME, 'sel_question')
Select(question).select_by_value('old_address')
#8、修改问题答案
driver.find_element(By.NAME, 'passwd_answer').clear()
driver.find_element(By.NAME, 'passwd_answer').send_keys('泸州')
#点击确认修改
driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div/form[1]/table/tbody/tr[11]/td/input[2]').click()
#返回至修改页面
driver.find_element(By.LINK_TEXT, '返回上一页').click()
#输入原始密码、新密码、确认密码
driver.find_element(By.NAME, 'old_password').send_keys('9527huwei')
driver.find_element(By.NAME, 'new_password').send_keys('huwei123')
driver.find_element(By.NAME, 'comfirm_password').send_keys('huwei123')
#点击下面个确认修改
driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div/form[2]/table/tbody/tr[4]/td/input[2]').click()
time.sleep(3)
driver.quit()