from flask import Blueprint, render_template, request, jsonify
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_amazon_jobs(query="python", max_jobs=10):
    url = f"https://www.amazon.jobs/en/search?base_query={query}&industry_experience=one_to_three_years&country%5B%5D=IND&state%5B%5D=Karnataka"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        xpath = "/html/body/div[2]/div[1]/div[4]/div/div/div[2]/content/div/div/div[2]/div[2]/div"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        print("Found the target div!")
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        container = soup.find('div', class_=['job-tile-lists'])
        container = soup.find('div',class_=['job-tile'])
        container = soup.find('div',class_=['job'])
        
        
        for element in container.find_all(class_=True)[:1]:
            print("++++++++++++++++++++++++++")
            contents = element.contents
            contents = contents[0]
            href = contents.find('h3').find('a')['href']
            print(href)
            details_div = contents.find('div').find('span').find('ul').find_all('li')
            location = details_div[0].string
            job_id = details_div[-1].string
            job_id = job_id.split(':')[1]
            job_id = int(job_id.strip())
            print(location,job_id)
            print("++++++++++++++++++++++++++")
        return "Hello"
    except Exception as e:
        print(e)
        return {"error": str(e)}
    finally:
        driver.quit()


job_postings_bp = Blueprint('job_postings', __name__)

@job_postings_bp.route('/job-postings')
def job_postings():
    job_urls = scrape_amazon_jobs()
    #Aggregate job postings from various sites
    """
    Product Based or Service Based
    Company Name
    Position Name
    Date posted
    YOE Required
    Location
    """
    return render_template('jobPostings.html',job_urls=job_urls)


#TODO:Scrape Jon Postings Data from Amazon, Microsoft, IBM, Cognizant, Concentrix