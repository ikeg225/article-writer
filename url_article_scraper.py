from newspaper import Article
url = 'https://www.cnn.com/2021/06/21/politics/weisselberg-trump-organization/index.html'
article = Article(url)
article.download()
html = article.html
print(html)
