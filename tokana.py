# pip3 install pykakasi
import pykakasi

def toKana(s):
  s = s.replace("一日一創", " いちにちいっそう")
  kakasi = pykakasi.kakasi()
  kakasi.setMode("J","K")
  kakasi.setMode("H","K")
  kakasi.setMode("s", True)
  k = kakasi.getConverter().do(s)
  return k

if __name__ == '__main__':
  print(toKana('福野泰介の一日一創'))
  print(toKana('ダウンロード'))
