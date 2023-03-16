from bs4 import BeautifulSoup
import requests

def get_insta_followers(profile_url:str):
    result = requests.get(f'https://www.instagram.com/{profile_url}/')
    soup = BeautifulSoup(result.content, 'html.parser')
    soup_str = str(soup)
    index = soup_str.find('Followers')
    text = soup_str[index-15:index+9]
    final_num = ""
    for char in text:
        if char.isdigit():
            final_num += char
    return final_num
