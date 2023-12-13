### NEWSPAPER DOWNLOAD TASK

from newspaper import Article
import nltk
urlOfArticle="https://www.thehindu.com/incoming/crime-cases-in-hyderabad-remain-almost-the-same-as-compared-to-2021/article66289244.ece"
instanceOfArticle=Article(urlOfArticle, language="en")
instanceOfArticle.download() #downloading the article
instanceOfArticle.parse()  #parsing the article
print(instanceOfArticle.text)
