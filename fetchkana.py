import tohalf
import fetchtext
import tokana

def fetchKana(url):
  t = fetchtext.fetchText(url)
  t = tokana.toKana(t)
  t = tohalf.toHalf(t)
  return t

if __name__ == '__main__':
  #url = "https://ichigojam.net/"
  url = "https://fukuno.jig.jp/"
  print(fetchKana(url))
