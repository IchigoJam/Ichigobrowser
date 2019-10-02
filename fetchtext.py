# pip3 install requests
# pip3 install BeautifulSoup4
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag, Comment
import urllib

def test():
  for ele in soup.find("head"):
    print(ele.name)
    if not isinstance(ele, NavigableString):
      print(ele.get_text())

def fetchText(url):
  def show(output, p):
    for ele in p.children:
      if isinstance(ele, Comment):
        pass
      elif isinstance(ele, NavigableString):
        output.append(ele)
      else:
        if ele.name == 'style' or ele.name == 'script':
          continue
        if ele.name == 'a':
          show(output, ele)
          link = ele.get("href")
          link = urllib.parse.urljoin(url, link)
          output.append(link)
        elif ele.name == 'img':
          pass # output.append("IMG " + ele.get("src"))
        else:
          show(output, ele)

  html = requests.get(url)
  soup = BeautifulSoup(html.content, "html.parser")
  output = []
  output.append(soup.find("title").text)
  #print(soup.find("body").text)
  show(output, soup.find("body"))
  output = [line.strip() for line in output]
  text = '\n'.join(line for line in output if line)
  text += '\n'
  return text

if __name__ == '__main__':
  #url = "https://ichigojam.net/"
  url = "https://fukuno.jig.jp/"
  text = fetchText(url)
  print(text)
