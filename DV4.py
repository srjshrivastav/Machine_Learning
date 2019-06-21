import requests
import bs4
import matplotlib.pyplot as plt

url="https://en.wikipedia.org/wiki/Machine_learning"
data=requests.get(url)
soup=bs4.BeautifulSoup(data.text,'html.parser')
data=""
for i in soup.findAll('p'):
    data=data+i.text.lower()

word_count=0
word=""
words=[]
repitation=[]
for i in data:
    if i!='\n' and i!=' ':
        word=word+i.lower()
    if i==' 'and len(word)>3:
        word_count=word_count+1 
        words.append(word)
        count=data.count(word)
        word=""

count_dic={}
for i in words:
    count=words.count(i)
    count_dic[i]=count
word_3=[]
count_3=[]
for key,value in count_dic.items():
    if value > 3:
        word_3.append(key)
        count_3.append(value)
count_dic_values=[]
for i in count_dic.values():
    count_dic_values.append(i)
count_dic=sorted(count_dic,key=count_dic.get,reverse=True)
count_dic_values.sort(reverse=True)
#Plot A Scatter Graph
plt.figure(figsize=(200,10))
plt.scatter(word_3,count_3)
plt.xticks(rotation=90)

plt.xlabel("Words More Than Three Times")
plt.ylabel("Word Count")
plt.show()
# Pie Chart For top twenty repeated Words
plt.pie(count_dic_values[0:20],labels=count_dic[0:20],autopct='%1.1f%%',radius=1.2,shadow=True)
plt.legend()
plt.show()
plt.title('Web Scrapping')
#Bar Chart for top Twenty Words
plt.barh(count_dic[0:20],count_dic_values[0:20])
plt.xlabel('No. Of Repetations')
plt.ylabel('Top 20 Words')
plt.show()

