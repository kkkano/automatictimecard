from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.devtools.v85.debugger import step_out
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time  # 确保导入了time模块
from selenium.common.exceptions import WebDriverException

def set_hours(driver, hours):
    # 找到输入框
    hours_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.el-input__inner[role='spinbutton']"))
    )
    
    # 清除当前值并输入新值
    hours_input.clear()
    hours_input.send_keys(str(hours))
def closeBrowser(driver):
    # 关闭浏览器窗口
    driver.quit()
    print("浏览器已关闭")


def scroll_and_select(driver, xpath):
    # 等待下拉菜单出现
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    
    # 使用 ActionChains 悬停在下拉菜单上
    actions = ActionChains(driver)
    actions.move_to_element(dropdown).perform()
    
    # 滚动到目标选项
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
    
    # 等待目标选项可点击
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    
    # 点击目标选项
    dropdown.click()

def login(driver):
    time.sleep(2)
    driver.maximize_window()
    time.sleep(1)
    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    username_input.send_keys("")
    # 定位密码输入框并输入密码
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    password_input.send_keys("")
    # 定位登录按钮并点击
    login_button = driver.find_element(By.CSS_SELECTOR, ".el-button.el-button--primary.el-button--medium")
    login_button.click()

def selectTimeCard(driver):
    #work_menu = driver.find_element(By.XPATH,  "//div[contains(@class, 'el-submenu__title')]") 
    #driver.execute_script("arguments[0].scrollIntoView(true);", work_menu)
    #driver.execute_script("arguments[0].mouseover();", work_menu)
    # 使用 ActionChains 来模拟鼠标悬停
    #actions = ActionChains(driver)
    #actions.move_to_element(work_menu).perform()  # 悬停在 'Work' 上
    #work_menu.click()
    # 点击 'Time Card'
    #time_card_link = driver.find_element(By.XPATH, "//span[contains(text(), 'Time Card')]")  # 根据实际情况调整选择器
    #time_card_link.click()
    time.sleep(2)
    driver.get("")

def newTimeCard(driver):
    new_time_card_button = driver.find_element(By.CSS_SELECTOR, "button.el-button--primary.el-button--small")
    new_time_card_button.click()
    date_input = driver.find_element(By.CSS_SELECTOR, "input.el-input__inner[placeholder='选择日期']")
    date_input.click()

def clickCurrentDate(driver):
    # 使用 CSS 选择器定位当前日期
    
    today_date = driver.find_element(By.XPATH, "//td[contains(@class, 'available') and contains(@class, 'today') and contains(@class, 'current')]")
    today_date.click()

def clickNewTask(driver):
    new_task_button = driver.find_element(By.CSS_SELECTOR, "button.el-button.el-button--primary.el-button--default.is-circle")
    new_task_button.click()
    new_type_select = driver.find_element(By.CSS_SELECTOR, "input.el-input__inner[placeholder='Select']")
    new_type_select.click()
    time.sleep(2)
    new_type_other = driver.find_element(By.XPATH, "//li[contains(@class, 'el-select-dropdown__item') and contains(., 'Others')]")
    new_type_other.click()
    new_Item_select = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/section/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[4]/div/div/div/input')
    new_Item_select.click()
    time.sleep(2)
    new_Item_IA = driver.find_element(By.XPATH, "//li[contains(@class, 'el-select-dropdown__item') and contains(., 'IA')]")
    new_Item_IA.click()
    new_SubTask_select = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/section/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[5]/div/span/div/div/input')
    new_SubTask_select.click()
    sub_task_xpath = "//li[contains(@class, 'el-select-dropdown__item') and contains(., '其它_CN03I006B_自我学习')]"
    scroll_and_select(driver, sub_task_xpath)

def clickOk(driver):
    try:
        # 尝试点击 OK 按钮
        ok_button = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div[2]/section/div/div[1]/div[1]/div/div[3]/span/button[1]")
        actions = ActionChains(driver)
        actions.double_click(ok_button).perform()
    except WebDriverException as e:
        print("点击 OK 按钮失败，尝试再次点击: ", str(e))
        # 稍作等待后重试
        time.sleep(1)
        actions = ActionChains(driver)
        actions.double_click(ok_button).perform()
def clickConfirm(driver):
    confirm_button = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div[2]/section/div/div[1]/div[2]/div/div/div[3]/span/button[1]")
    confirm_button.click()
def she():
        #创建浏览器选项
    q1 = Options()
        # 禁用沙盒模式
    q1.add_argument('--no-sandbox')
        # 保持浏览器打开状态 默认是执行完毕关闭
    q1.add_experimental_option('detach', True)
    a1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=q1)
    a1.get("")
    username_input = a1.find_elements(By.CSS_SELECTOR, "input[name='username']")
    if len(username_input) > 0:
           username_input = username_input[0]
           login(a1)
           selectTimeCard(a1)
           time.sleep(2)
           newTimeCard(a1)
           time.sleep(2)
           clickCurrentDate(a1)
           clickNewTask(a1)
           set_hours(a1, 8)
           time.sleep(1)
           clickOk(a1)
           clickConfirm(a1)
           print("已完成")
           closeBrowser(a1)
    else:
        print("已登录")
        selectTimeCard(a1)
        time.sleep(2)
        newTimeCard(a1)
        time.sleep(2)
        clickCurrentDate(a1)
        clickNewTask(a1)
        set_hours(a1, 8)
        clickOk(a1)
        clickConfirm(a1)
        print("已完成")
if __name__ == "__main__":
    she()

