#!/usr/bin/env python
# coding: utf-8

# In[1]:


#scraping data from https://www.naukri.com/


# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from selenium.webdriver.common.by import By
import time


# In[7]:


#Answer-01:
#scrapping the first 10 data as 1.) Job title, 2.) Job location, 3.) Company name, 4.) experience required

driver01 = webdriver.Chrome()


# In[8]:


#requesting to get the webpage
driver01.get("https://www.naukri.com/")


# In[10]:


#entering the designation
designation01 = driver01.find_element(By.CLASS_NAME, "suggestor-input ")
designation01.send_keys("Data Scientist")


# In[12]:


#clicking search for the entered designation
search01 = driver01.find_element(By.CLASS_NAME, "qsbSubmit")
search01.click()


# In[15]:


#filtering location wise
locationfilter01 = driver01.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[4]/div[2]/div[3]/label/i")
locationfilter01.click()


# In[16]:


#filtering salary wise
salaryfilter01 = driver01.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[5]/div[2]/div[2]/label/i")
salaryfilter01.click()


# In[19]:


#scarpping the given details for the first 10 itmes

job_title = []
job_location = []
company_name = []
experience_required = []

#scrapping the titles from the given page
title_tags01 = driver01.find_elements(By.XPATH, '//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')
for i in title_tags01[0:10]:
    title01=i.text
    job_title.append(title01)
    
#scrapping the locations from the given page
location_tags01 = driver01.find_elements(By.XPATH, '//span[@class="ni-job-tuple-icon ni-job-tuple-icon-srp-location loc"]')
for i in location_tags01[0:10]:
    location01 = i.text
    job_location.append(location01)
    
#scrapping company name from given page
company_tags01 = driver01.find_elements(By.XPATH, '//div[@class=" row2"]/span/a[1]')
for i in company_tags01[0:10]:
    company01 = i.text
    company_name.append(company01)
    
#scrapping required experience from the given page
experience_tags01 = driver01.find_elements(By.XPATH, '//span[@class="expwdth"]')
for i in experience_tags01[0:10]:
    experience01 = i.text
    experience_required.append(experience01)


# In[20]:


print(len(job_title), len(job_location), len(company_name), len(experience_required))


# In[23]:


import pandas as pd
df = pd.DataFrame({'Title': job_title, 'Location':job_location, 'Company Name': company_name, 'Experience':experience_required})
df


# In[25]:


#Answer-02
#scrapping the first 10 data as 1.) Job title, 2.) Job location, 3.) Company name, 4.) experience required
driver02 = webdriver.Chrome()
driver02.get("https://www.shine.com/")


# In[27]:


#entering designation as per required in the question

designation02 = driver02.find_element(By.CLASS_NAME, "form-control  ")
designation02.send_keys("Data Analyst")

#entering location as per required in the question
location02 = driver02.find_element(By.XPATH, "/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location02.send_keys("Bangalore")


# In[35]:


#clciking on search button

search02 = driver02.find_element(By.CLASS_NAME, "searchForm_btnWrap_advance__VYBHN")
search02.click()


# In[40]:


#scarpping the given details for the first 10 itmes

job_title = []
job_location = []
company_name = []
experience_required = []

#scrapping the titles from the given page
title_tags02 = driver02.find_elements(By.XPATH, '//strong[@class="jobCard_pReplaceH2__xWmHg"]/p/a')
for i in title_tags02[0:10]:
    title02=i.text
    job_title.append(title02)
    
#scrapping the locations from the given page
location_tags02 = driver02.find_elements(By.XPATH, '//div[@class="jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags02[0:10]:
    location02 = i.text
    job_location.append(location02)
    
#scrapping company name from given page
company_tags02 = driver02.find_elements(By.XPATH, '//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags02[0:10]:
    company02 = i.text
    company_name.append(company02)
    
#scrapping required experience from the given page
experience_tags02 = driver02.find_elements(By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags02[0:10]:
    experience02 = i.text
    experience_required.append(experience02)


# In[41]:


import pandas as pd
df = pd.DataFrame({'Title': job_title, 'Location':job_location, 'Company Name': company_name, 'Experience':experience_required})
df


# In[17]:


#Asnswer-03:
#Scrapping the 100 reviews from the flipkart.com for iphone11 phone

driver03 = webdriver.Chrome()
driver03.get("https://www.flipkart.com/apple-iphone-11-white-128-gb/product-reviews/itme32df47ea6742?pid=MOBFWQ6B7KKRXDDS&lid=LSTMOBFWQ6B7KKRXDDSULUZ0N&marketplace=FLIPKART")


# In[20]:


#scrapping the first 10 webpages for 100 reviews details

rating03 = []
review_summary03 = []
full_review03 = []


for page in range(0,10): #for looping for the particular page
    ratings = driver03.find_elements(By.XPATH, '//div[@class="XQDdHH Ga3i8K"]') #scrapping the ratings from given page
    for i in ratings:
        rating03.append(i.text)
    review_summaries = driver03.find_elements(By.XPATH, '//p[@class="z9E0IG"]') #scrapping the review summary from given page
    for i in review_summaries:
        review_summary03.append(i.text)
    full_reviews = driver03.find_elements(By.XPATH, '//div[@class="ZmyHeo"]') #scrapping the full review from given page
    for i in full_reviews:
        full_review03.append(i.text)
        
    next_button03 = driver03.find_element(By.XPATH, '//nav[@class="WSL9JP"]/a[12]/span') #To scrap data from next poge
    next_button03.click()
    time.sleep(3)


# In[21]:


import pandas as pd
df = pd.DataFrame({'Ratings': rating03[0:100], 'Review Summary':review_summary03[0:100], 'Full review': full_review03[0:100]})
df


# In[150]:


#Answer-04:
#Scrapping the details from the flipkart.com for 100 items

driver04 = webdriver.Chrome()
driver04.get("https://www.flipkart.com/")


# In[151]:


#entering search keyword "sneakers" as per required in the question

search_item04 = driver04.find_element(By.CLASS_NAME, "Pke_EE")
search_item04.send_keys("Sneakers")

click04 = driver04.find_element(By.CLASS_NAME, '_2iLD__')
click04.click()


# In[157]:


#scrapping the details for 100 items

brand04 = []
product_description04 = []
price04 = []


for page in range(0,3): #'for' looping for the particular page
    brands = driver04.find_elements(By.XPATH, '//div[@class="syl9yP"]') #scrapping the brand name from given page
    for i in brands:
        brand04.append(i.text)
    product_details = driver04.find_elements(By.XPATH, '//div[@class="hCKiGj"]/a[1]') #scrapping the product description from given page
    for i in product_details:
        product_description04.append(i.text)
    prices = driver04.find_elements(By.XPATH, '//div[@class="Nx9bqj"]') #scrapping the prices from given page
    for i in prices:
        price04.append(i.text)
        
    next_button04 = driver04.find_element(By.XPATH, '//nav[@class="WSL9JP"]/a[12]/span') #To scrap data from next poge
    next_button04.click()
    time.sleep(3)


# In[158]:


import pandas as pd
df = pd.DataFrame({'Brand Name':brand04[0:100], 'Product Description':product_description04[0:100], 'Price':price04[0:100]})
df


# In[125]:


#Answer-05:
#Scrapping the 100 reviews from the amazon.com for Laptop phone

driver05 = webdriver.Chrome()
driver05.get(" https://www.amazon.in/")


# In[126]:


#entering search keyword "Laptop" as per required in the question

search_item05 = driver05.find_element(By.XPATH, '//div[@class="nav-search-field "]/input')
search_item05.send_keys("Laptop")

click05 = driver05.find_element(By.XPATH, '//span[@class="nav-search-submit-text nav-sprite nav-progressive-attribute"]/input')
click05.click()


# In[127]:


#filter with cpu type as intel core i7
filtering_cpu_type = driver05.find_element(By.XPATH, '//li[@id="p_n_feature_thirteen_browse-bin/12598163031"]/span/a/div/label/i')
filtering_cpu_type.click()


# In[138]:


#scrapping the first 10 items

title = []
rating = []
price = []

    
titles05 = driver05.find_elements(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]') #scrapping the title name from given page
for i in titles05[0:10]:
    title.append(i.text)
rating05 = driver05.find_elements(By.XPATH, '//span[@class="a-size-base s-underline-text"]') #scrapping the ratings from given page
for i in rating05[0:10]:
    rating.append(i.text)
price05 = driver05.find_elements(By.XPATH, '//span[@class="a-price"]/span/span[2]') #scrapping the prices from given page
for i in price05[0:10]:
    price.append(i.text)


# In[139]:


print(len(title), len(rating), len(price))


# In[140]:


print(rating)


# In[141]:


import pandas as pd
df = pd.DataFrame({'Item Title':title, 'Ratings':rating, 'Price':price})
df


# In[201]:


#Answer-06:
#scrapping the top 1000 quotes of all time from https://www.azquotes.com/ 

driver06 = webdriver.Chrome()
driver06.get("https://www.azquotes.com/")


# In[202]:


#clicking on top quotes

click06 = driver06.find_element(By.XPATH, '//div[@class="mainmenu"]/ul/li[5]/a')
click06.click()


# In[204]:


quote = []
author = []
quote_type = []

for page in range(0,10): #'for' looping for the particular page
    quotes = driver06.find_elements(By.XPATH, '//ul[@class="list-quotes"]/li/div/p/a[2]') #scrapping the quotes from given page
    for i in quotes:
        quote.append(i.text)
    authors = driver06.find_elements(By.XPATH, '//ul[@class="list-quotes"]/li/div/div/a') #scrapping the authors from given page
    for i in authors:
        author.append(i.text)
    quote_types = driver06.find_elements(By.XPATH, '//ul[@class="list-quotes"]/li/div/div[2]') #scrapping the type of quotes from given page
    for i in quote_types:
        list_i = []
        list_i.append(i.text)
        quote_type.append(list_i)
        
    next_button06 = driver06.find_element(By.XPATH, '//li[@class="next"][1]') #To scrap data from next poge
    next_button06.click()
    time.sleep(2)


# In[205]:


print(len(quote), len(author), len(quote_types))


# In[208]:


import pandas as pd
df = pd.DataFrame({'Quote':quote[0:1000], 'Author':author[0:1000]})
df


# In[3]:


#Answer-07:
#scrapping the details of respected former prime ministers of india

driver07 = webdriver.Chrome()
driver07.get("https://www.jagranjosh.com/general-knowledge/list-ofall-prime-ministers-of-india-1473165149-1")


# In[ ]:


#scarpping the details of respected former prime ministers

name = []
born_dead = []
office_term = []
remarks = []

#scrapping the Names from the given page
names = driver07.find_elements(By.XPATH, '//div[@class="TableData"]/table/tbody/tr/td[2]/div')
for i in names:
    names07=i.text
    name.append(names07)
    
#scrapping the Born-dead from the given page
born_deads = driver07.find_elements(By.XPATH, '//div[@class="TableData"]/table/tbody/tr/td[3]/div')
for i in born_deads:
    born_deads07 = i.text
    born_dead.append(born_deads07)
    
#scrapping office term from given page
term_of_office = driver07.find_elements(By.XPATH, '//div[@class="TableData"]/table/tbody/tr/td[4]')
for i in term_of_office:
    office_term07 = i.text
    office_term.append(office_term07)

    #scrapping remarks from the given page
remarks = driver07.find_elements(By.XPATH, '//div[@class="TableData"]/table/tbody/tr/td[5]')
for i in remarks:
    remark07 = i.text
    remarks.append(remark07)


# In[ ]:


import pandas as pd
df = pd.DataFrame({'Names':name, 'Born-Dead':born_dead}, 'Term of office':office_term, 'Remarks':remarks)
df


# In[14]:


#Answer-08
#scrapping the list of 50 most expensive cars in the world

driver08 = webdriver.Chrome()
driver08.get("https://www.motor1.com/")


# In[15]:


#searching the keywords
search08 = driver08.find_element(By.XPATH, '/html/body/div[9]/div[2]/div/div/div[3]/div/div/div/form/input')
search08.send_keys("50 most expensive cars in the world")

#clicking the search button
click08 = driver08.find_element(By.XPATH, '/html/body/div[9]/div[2]/div/div/div[3]/div/div/button/svg')
click08.click()


# In[ ]:


#scrapping car details
car_name = []
price = []

cars = driver.find_element(By.XPATH, '//h3[@class="subheader"]')
for i in cars:
    car08 = i.text
    car_name.append(car08)
prices=driver.find_element(By.XPATH, '/html/body/div[9]/div[7]/div[2]/div[1]/div[2]/div[2]/p[4]/strong')
for i in prices:
    price08 = i.text
    price.append(price08)


# In[ ]:


import pandas as pd
df = pd.DataFrame({'Car Name':car_name, 'Price':price})
df

