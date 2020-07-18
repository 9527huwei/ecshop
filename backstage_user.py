'''后台添加用户'''
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

#二、进入添加管理会员页面
#1、跳转到menuframe
driver.switch_to.frame('menu-frame')
time.sleep(1)
#2、点击会员管理
driver.find_element(By.XPATH,'//li[@key_data2="lis ico2_7"]').click()
wait.until(EC.presence_of_element_located((By.LINK_TEXT, '添加会员')))
#3、点击添加会员
driver.find_element(By.LINK_TEXT, '添加会员').click()
#4、退出当前frame
driver.switch_to.parent_frame()
#5、进入mainframe
driver.switch_to.frame('main-frame')

#三、输入会员信息
#1、输入会员名称
driver.find_element(By.NAME, 'username').send_keys('xiaowei')
#2、输入邮箱
driver.find_element(By.NAME, 'email').send_keys('1320124795@qq.com')
#3、输入密码
driver.find_element(By.NAME, 'password').send_keys('123456')
#4、输入确认密码
driver.find_element(By.NAME, 'confirm_password').send_keys('123456')
# 5、设置会员等级
userrank = driver.find_element(By.NAME, 'user_rank')
Select(userrank).select_by_value('3')
# 6、设置性别
driver.find_element(By.XPATH, '/html/body/div[1]/form/table/tbody/tr[6]/td[2]/input[2]').click()
# 7、设置出生日期
year = driver.find_element(By.NAME, 'birthdayYear')
month = driver.find_element(By.NAME, 'birthdayMonth')
day = driver.find_element(By.NAME, 'birthdayDay')
Select(year).select_by_visible_text('1993')
Select(month).select_by_visible_text('12')
Select(day).select_by_visible_text('08')
# 8、设置信用额度
driver.find_element(By.NAME, 'credit_line').clear()
driver.find_element(By.NAME, 'credit_line').send_keys('6000')
# 9、设置msn
driver.find_element(By.NAME, 'extend_field1').send_keys('12897@hotmail.com')
# 10、设置QQ
driver.find_element(By.NAME, 'extend_field2').send_keys('1289738628')
# 11、设置办公电话
driver.find_element(By.NAME, 'extend_field3').send_keys('028-9527')
# 12、设置家庭电话
driver.find_element(By.NAME, 'extend_field4').send_keys('028-9528')
# 13、设置手机
driver.find_element(By.NAME, 'extend_field5').send_keys('18228954790')

#三点击确定
driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody/tr[14]/td/input[1]').click()

time.sleep(3)
driver.quit()
