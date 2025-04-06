from flask import Blueprint, render_template, request, jsonify
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

job_postings_bp = Blueprint('job_postings', __name__)

def scrape_amazon_jobs(query="python",yoe="one_to_three_years"):
    url = f"https://www.amazon.jobs/en/search?base_query={query}&industry_experience={yoe}&country%5B%5D=IND&state%5B%5D=Karnataka"
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
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        container = soup.find('div', class_=['job-tile-lists'])
        job_details = []
        for product_div in soup.find_all('div', class_='job-tile'):
            container = product_div.find('div',class_=['job'])
            
            for element in container.find_all(class_=True)[:1]:
                details:dict = {}
                contents = element.contents
                contents = contents[0]
                href = contents.find('h3').find('a')['href']
                title = href.split('/')[-1].replace("-"," ")
                details_div = contents.find('div').find('span').find('ul').find_all('li')
                location = details_div[0].string
                job_id = details_div[-1].string
                job_id = job_id.split(':')[1]
                job_id = int(job_id.strip())
                details.update({"job_id":job_id, "title":title, "location":location, "href":href})
                job_details.append(details)

        return job_details

    except Exception as e:
        print(e)
        return [{"error": str(e)}]
    finally:
        driver.quit()


@job_postings_bp.route('/job-postings')
def job_postings():
    amazon_jobs  = scrape_amazon_jobs()
    #Aggregate job postings from various sites
    """
    Company Name
    Position Name
    Date posted
    YOE Required
    Location
    """
    return jsonify(amazon_jobs)
    # return render_template('jobPostings.html',job_urls=job_urls)


#TODO:Scrape Jon Postings Data from Amazon, Microsoft, IBM, Cognizant, Concentrix