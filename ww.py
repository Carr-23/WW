from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import keyboard
import time

driver = webdriver.Edge(executable_path='msedgedriver.exe')

driver.get('https://waterlooworks.uwaterloo.ca/home.htm')

languages = ['Java', 'Python', 'C,', 'C++', r'C#', 'python', 'java', ' C ', ' C.', 'C/']
titleKeyWords = ['Programmer', 'Developer', 'Software', 'Engineer', 'Machine', 'ML', 'AI', 'Artificial', 'Deep', 'Engineering']
titleKeyWordsBad = ['Quality', 'Assurance', 'QA', 'Test', 'Analyst', 'Data', 'Cloud', 'Frontend', 'UX', 'UI', 'IT', 'Embedded', 'Technician']
locations = ['Waterloo', 'Kitchener', 'Toronto', 'Remote','waterloo', 'kitchener', 'toronto', 'remote', 'North York', 'north york']
# keyWords4Misc = []

# wait for login to be done

keyboard.wait('esc')

# goes through all jobs and clicks on them

window_before  = driver.current_window_handle

while(True):


        tablePost = driver.find_element_by_xpath('//*[@id="postingsTable"]/tbody')
        postings = tablePost.find_elements_by_xpath('./tr')

        for post in postings:

            code = post.get_attribute('class')[20:26]
            print('this is the class: ')
            print(code)
            
            classCode = 'np-view-btn-' + code

            postClick = post.find_element_by_class_name(classCode)
            
            postText = postClick.text 
            
            if (any(x in postText for x in titleKeyWords)):
                if (any(x in postText for x in titleKeyWordsBad)):
                    continue
                else:

                    postClick.click()

                    time.sleep(1)

                    try:
                        driver.switch_to.window(driver.window_handles[1])
                    except NoSuchElementException as e:
                        print (e)

                    location = driver.find_element_by_xpath('/html/body/main/div[4]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[10]/td[2]/span').text
                

                    if (('remote' or 'Remote') in driver.page_source) or any(x in location for x in locations): 
                        if (any(x in driver.page_source for x in languages)):
                            if (driver.page_source.count(' test') > 3):
                                pass
                                
                            else:
                                driver.find_element_by_xpath('/html/body/div[2]/header/div[3]/div[1]/div[2]/nav/div/div[2]/button').click()
                                
                    
                    driver.close()
                    time.sleep(1)

                    try:
                        driver.switch_to.window(window_before)
                    except NoSuchElementException as e:
                        print (e)
                    
                time.sleep(1.5)
        
        driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[4]/div/ul/li[16]/a').click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, 0)") 



# press next
# shortlist
