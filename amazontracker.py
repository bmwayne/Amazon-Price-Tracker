import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/Marvels-Spider-Man-Morales-Ultimate-Launch-PlayStation/dp/B08FC66ZV4?ref_=Oct_s9_apbd_ps_hd_bw_b1xuk&pf_rd_r=F1PBHYZK4MARNXTFVPCF&pf_rd_p=070db0d2-97f0-558c-8192-47383e9476d7&pf_rd_s=merchandised-search-13&pf_rd_t=BROWSE&pf_rd_i=468642'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

html_page = request.get(url, header)
soup = BeautifulSoup(html_page.content, 'lxml')


