# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import random
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import requests
# import os

# PROXY_LIST = [
#     "203.24.108.161:80",
#     "80.48.119.28:8080",
#     "170.30.189.47:80",
# ]

# USER_AGENTS = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
#     "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
#     "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
#     "Mozilla/5.0 (Android 14; Mobile; rv:123.0) Gecko/123.0 Firefox/123.0",
#     "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
# ]

# # Select a random proxy
# proxy = random.choice(PROXY_LIST)

# # Set up Chrome with a proxy
# options = webdriver.ChromeOptions()
# options.add_argument(f"--proxy-server=http://{proxy}")

# # Set up Chrome options
# options = webdriver.ChromeOptions()
# options.add_argument(random.choice(USER_AGENTS))  # Mimic a real user

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# # add input
# driver.get("https://www.google.com/search?tbm=isch&q=bike+cad+cam+model")

# # time.sleep(10)

# # search_box = driver.find_element(By.NAME, "q")
# # time.sleep(5)
# # search_box.send_keys("bike cad cam model")
# # time.sleep(5)
# # search_box.send_keys(Keys.RETURN)

# time.sleep(2)  # Let Google load results

# # Find all image elements using the given JS path
# # image_elements = driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[14]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div")
# # print(image_elements)

# # Create a folder to store images
# os.makedirs("downloaded_images", exist_ok=True)

# # Download first N images
# n = 5  # Number of images to download
# count = 0

# for i in range(n):  # Loop through first N images
#     #rso > div > div > div.wH6SXe.u32vCb > div > div > div:nth-child(2) > div.czzyk.XOEbc > h3 > a > div > div > div > g-img
#     #rso > div > div > div.wH6SXe.u32vCb > div > div > div:nth-child(3) > div.czzyk.XOEbc > h3 > a > div > div > div > g-img
#     try:
#         img_url = driver.find_elements(By.CSS_SELECTOR, f"#rso > div > div > div.wH6SXe.u32vCb > div > div > div:nth-child({n}) > div.czzyk.XOEbc > h3 > a > div > div > div > g-img")
#         print(img_url)
#         # img_url = img_subdiv.get_attribute("src") or img_subdiv.get_attribute("data-src")  # Get the image URL
#     #     if img_url and "http" in img_url:
#     #         response = requests.get(img_url)
#     #         filename = f"downloaded_images/image_{count + 1}.jpg"

#     #         with open(filename, "wb") as file:
#     #             file.write(response.content)
            
#     #         print(f"Downloaded: {filename}")
#     #         count += 1
        
#     #     if count >= n:
#     #         break

#     except Exception as e:
#         print(f"Error downloading image {count + 1}: {e}")

# # Click on the first search result
# # first_result = driver.find_element(By.CSS_SELECTOR, "h3")  # First result's title (h3)
# # first_result.click()
# # print(first_result)
# driver.quit()


import base64
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in the background
driver = webdriver.Chrome(options=options)

# Open Google Images and search

def get_rough_visualizations(quote):
    driver.get("https://www.google.com/imghp")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("high resolution rowing boat cad cam model images")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    # Scroll to load more images
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

    # Find all g-img elements
    image_elements = driver.find_elements(By.CSS_SELECTOR, "g-img img")

    # Create a folder for images
    os.makedirs("downloaded_images", exist_ok=True)

    n = 10  # Number of images to download
    count = 0

    for img in image_elements[:n]:  # Loop through first N images
        try:
            img_src = img.get_attribute("src")  # Get the src attribute

            if img_src.startswith("data:image"):  # Base64 image
                base64_data = img_src.split(",")[1]  # Remove "data:image/jpeg;base64,"
                filename = f"ImageBasedApproach/downloaded_images/image_{count + 1}.jpg"

                with open(filename, "wb") as file:
                    file.write(base64.b64decode(base64_data))
                print(f"Saved base64 image: {filename}")

            elif "http" in img_src:  # Normal image URL
                response = requests.get(img_src)
                filename = f"downloaded_images/image_{count + 1}.jpg"

                with open(filename, "wb") as file:
                    file.write(response.content)
                print(f"Downloaded image: {filename}")

            count += 1
            if count >= n:
                break

        except Exception as e:
            print(f"Error processing image {count + 1}: {e}")

    # Close WebDriver
    driver.quit()
    print("Download completed!")