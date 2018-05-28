from django.contrib.auth.models import User
from api.models import *
import requests
from bs4 import BeautifulSoup
# user create
for i in range(10) :
    username = "user{0}".format(i+1)
    password = i+1
    user = User.objects.create_user(username, password = password)
    user.save()

# tag create
tag_list = ['수업', '입학', '등록/복학/휴학/재입학', '졸업', '학사 (학부)', '학사 (대학원)', '제2전공/전과', '교환학생/유학',
'장학', '학부 지도교수', '박사학위예비심사', '자료실', '외부 행사/프로그램', '인턴/취업 (공식 게시)', '기업게시판', '전문연구요원', '미분류']

for i in tag_list :
    tag = Tag(name = i)
    tag.save()

# notice create
# for i in range(50) :
#     title = "Notice{0}".format(i+1)
#     content = "Content{0}".format(i+1)
#     author = "user{0}".format(i+1)
#     user = User.objects.get(id = i % 10 + 1)
#     notice = Notice(title = title, content = content, author = author, user = user)
#     notice.save()
notice_url = "http://cse.snu.ac.kr/node/"
notice_list = [31861, 31860, 31854, 31853, 31852, 31851, 31848, 31842,31773, 31772, 31770]
for i in notice_list :
    idx = str(i)
    html = requests.get(notice_url+idx).text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1', class_ = "title").text
    content = soup.find('div', class_ ="field field-name-body field-type-text-with-summary field-label-hidden").text
    author = soup.find('span', class_ = "username").text
    tag = soup.find('span', class_ = "field-item even").text
    notice = Notice(title = title, content = content, author = author)
    notice.save()
    notice.tag_set.set([Tag.objects.get(name = tag)])
    notice.save()

# professor create
import requests
import os
from bs4 import BeautifulSoup
from api.models import *
from django.core.files import File

def field_return(list_) :
    result = []
    for i in list_ :
        result.append(i.text)
    if len(result) == 0 :
        return ""
    else :
        return result

def text_return(list_) :
    result = []
    for i in list_ :
        result.append(i.text)
    if len(result) == 0 :
        return ""
    if len(result) == 1 :
        return result[0]
    else :
        return result


prof_url = 'http://cse.snu.ac.kr/professor/'
html = requests.get("http://cse.snu.ac.kr/people/faculty").text
soup = BeautifulSoup(html, 'html.parser')
prof_list = []
image = 1234

k = soup.find_all('div', class_="views-field views-field-title")
for i in k :
    name = i.find('a')
    if name :
        prof_list.append ({'name' : name.text.replace(" ", "-")})



for i, j in enumerate(prof_list) :
    url = prof_url + j['name']
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    section = soup.find('div', class_="section clearfix2")
    position = text_return(section.select(".field-name-field-title .field-item"))
    lab = text_return(section.select(".field-name-field-lab .field-item"))
    location = text_return(section.select(".field-name-field-office .field-item" ))
    phone = text_return(section.select(".field-name-field-phone .field-item" ))
    fax = text_return(section.select(".field-name-field-fax .field-item" ))
    email =text_return(section.select(".field-name-field-email .field-item" ))
    website = text_return(section.select(".field-name-field-website .field-item" ))
    education = field_return(section.select("div.field-name-field-education .field-item"))
    research = field_return(section.select("div.field-name-field-research-area .field-item"))
    biography =  field_return(section.select("div.field-name-field-biography .field-item li"))
    image_url = section.select(".field-name-field-profile-picture img")[0]['src']
    image = requests.get(image_url).content
    filetype = os.path.basename(image_url)[-4:]
    filename = j['name'] + filetype
    image = File(open('./media/professor/' + filename, 'rb'))
    educations = []
    for i in education :
        edu = Education(education = i)
        edu.save()
        educations.append(edu)
    researches = []
    for i in research :
        res = Research(research = i)
        res.save()
        researches.append(res)
    biographies = []
    for i in biography :
        bio = Biography(biography = i)
        bio.save()
        biographies.append(bio)
    data = {'name' : j['name'], 'position' : position, 'lab' : lab, 'location' :location, 'phone' : phone,'fax' : fax, 'email' : email, 'website' : website,'image' : image}
    prof = Professor(**data)
    prof.save()
    prof.education.set(educations)
    prof.biography.set(biographies)
    prof.research.set(researches)
    prof.save()
