from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def send_whatsapp_message(to, message):
    # تحديد المسار إلى متصفح الويب (تأكد من تنزيل المتصفح WebDriver المناسب)
    driver_path = 'path/to/chromedriver'
    driver = webdriver.Chrome(driver_path)
    
    # فتح WhatsApp Web
    driver.get('https://web.whatsapp.com')

    # انتظر حتى يقوم المستخدم بمسح رمز QR وتسجيل الدخول
    input("اضغط Enter بعد تسجيل الدخول إلى WhatsApp Web")

    # البحث عن جهة الاتصال أو رقم الهاتف
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(to)
    search_box.send_keys(Keys.ENTER)

    # الانتظار قليلاً حتى يتم تحميل المحادثة
    time.sleep(5)

    # إدخال الرسالة وإرسالها
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')
    message_box.click()
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

    # الانتظار قليلاً قبل إغلاق المتصفح
    time.sleep(5)
    driver.quit()
