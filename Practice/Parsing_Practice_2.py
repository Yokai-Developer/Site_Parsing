#  Парсинг сайтов через запросы HTTP
import requests

# Создаем функцию для HTTP запросов
# Нужно знать URL, params={HEADER, BODY, METHOD}
def fetch(url, params):
    headers = params['headers']
    body = params['body']
    method = params['method']
    if method == 'POST':
        return requests.post(url, headers=headers, data=body)
    if method == 'GET':
        return requests.get(url, headers=headers)


bmw = fetch("https://auto.ru/-/ajax/desktop/listing/", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-site": "same-origin",
    "x-client-app-version": "174.0.10149016",
    "x-client-date": "1665556568780",
    "x-csrf-token": "15d94c5770b0c4883d5239e11f76163dea4893d5f1b7644a",
    "x-page-request-id": "c55593c6aee63d3d069de5d57dca4ccb",
    "x-requested-with": "XMLHttpRequest",
    "x-retpath-y": "https://auto.ru/moskva/cars/bmw/5er/2305607/all/",
    "x-yafp": "{\"a1\":\"YtIs26HgPmaOFw==;0\",\"a2\":\"9xbmEsxorsQmzzJh2s+bsViFbMiPiQ==;1\",\"a3\":\"XAZUXdmg6wtN8FNgCm"
              "IIXQ==;2\",\"a4\":\"h6/l9xTFusG2Vs5i779/Y+lQfsHOPMbIDjK0ccVybvRcsw==;3\",\"a5\":\"ORYIXSzLvciFFg==;4\","
              "\"a6\":\"RWE=;5\",\"a7\":\"f/SzMjSF18ZOyA==;6\",\"a8\":\"Gh1010RJtfo=;7\",\"a9\":\"saEIlLtw8+e6YA==;8\","
              "\"b1\":\"8D55UFKmIXI=;9\",\"b2\":\"6UTJTguvQsqYnA==;10\",\"b3\":\"7vXeroGqng5A1g==;11\",\"b4\":\"mKWX/iz"
              "AWp0=;12\",\"b5\":\"G7iRIkviLo2ouA==;13\",\"b6\":\"k2Mm0xP0gr06QA==;14\",\"b7\":\"JCoD/6ole/CxtQ==;15\","
              "\"b8\":\"ko9pTnBQw7jiqQ==;16\",\"b9\":\"3Gzhnr0pt76pQw==;17\",\"c1\":\"r/ZV3w==;18\",\"c2\":\"VaTimv0OtT"
              "Cd/IZKzlaZKebq;19\",\"c3\":\"vT64fs2jfBhF67RL7pxiBSRV;20\",\"c4\":\"ARcjKjK15SY=;21\",\"c5\":\"dm+180bOE"
              "Nw=;22\",\"c6\":\"rSr3ag==;23\",\"c7\":\"yY1WfWggY2Y=;24\",\"c8\":\"Cfs=;25\",\"c9\":\"OXcUKEfwMuM=;26\""
              ",\"d1\":\"nl4vf6/CN3w=;27\",\"d2\":\"yS49ww==;28\",\"d3\":\"3UZ1KJYG7iJbtg==;29\",\"d4\":\"DBxWNMiIY2k=;"
              "30\",\"d5\":\"mkaIlaKGqlU=;31\",\"d7\":\"W8k01PHi18c=;32\",\"d8\":\"BQXacXUMTlYGRNS495fNa+GZXfVvPyHfYiY="
              ";33\",\"d9\":\"Bw3FG0CthnI=;34\",\"e1\":\"HMJjLvaiNGxbpg==;35\",\"e2\":\"2Yvf0Fm4Ak4=;36\",\"e3\":\"5iRV"
              "RwxYXDY=;37\",\"e4\":\"DNTwiIobmDU=;38\",\"e5\":\"lQlo58ZFCV06cw==;39\",\"e6\":\"2SImXnZysus=;40\",\"e7"
              "\":\"TuPrnBZWz0FyPQ==;41\",\"e8\":\"0DdXx1k9GN0=;42\",\"e9\":\"XmYJSmqGzUU=;43\",\"f1\":\"HoCXCpZSXTK1lg"
              "==;44\",\"f2\":\"TBCgdLM8RJ4=;45\",\"f3\":\"/eruSt+pymOU3A==;46\",\"f4\":\"wP4lPFFgr4s=;47\",\"f5\":\"k2"
              "NiuLXj8kbyaQ==;48\",\"f6\":\"2ORfMNnCIgFO7g==;49\",\"f7\":\"ACDNszqynPtF/w==;50\",\"f8\":\"UeuuBCUhtDBqr"
              "A==;51\",\"f9\":\"5X7r+3p83EM=;52\",\"g1\":\"VVWUIjnaVkcDRw==;53\",\"g2\":\"o9avbI0yDiMZUw==;54\",\"g3\""
              ":\"iPB9yQR0Dcc=;55\",\"g4\":\"guBc+5yVwSh0Sw==;56\",\"g5\":\"1fC3iIAvB+8=;57\",\"g6\":\"+p/KeTYOXzc=;58"
              "\",\"g7\":\"fo/LE6+9QqQ=;59\",\"g8\":\"wFyy+ZqdXhQ=;60\",\"g9\":\"3KCIc5u/YXA=;61\",\"h1\":\"TbCe42W7ipn"
              "Lhg==;62\",\"h2\":\"LRlsbdSbAntPog==;63\",\"h3\":\"zFF+YmqTIvRegA==;64\",\"h4\":\"M0OwV0mYlbR1Og==;65\","
              "\"h5\":\"m1VKjNf3JB4=;66\",\"h6\":\"vU+6l/DqngoQiw==;67\",\"h7\":\"5ufLo06VOr92rRE4sZZfV/bgVmAmh7kDcYjVG"
              "jLQf/P+j/z/;68\",\"h8\":\"unwI979BX4xR5g==;69\",\"h9\":\"fP3MT7ptXQ25FA==;70\",\"i1\":\"2B76SteyevY=;71"
              "\",\"i2\":\"UM3z3iyhO4jf/w==;72\",\"i3\":\"W7DOxHyTR5Iztw==;73\",\"i4\":\"Wk2VVM/+na4BoA==;74\",\"i5\":"
              "\"rsHg/guPoG6f9g==;75\",\"z1\":\"kBVaUIGpsP+0umT+9/s82JaXR/ZFc9HuLgnh+sMDwpHIHdtWl9VzOpdJQN6BTyuVCn7eK6r"
              "tpBXD2d7UqW50Uw==;76\",\"z2\":\"0zgOkG2y0Y9d3NsIlqkVyGjkekCG0P3B2nddcY4KtIroS1MOoLSUn+y1Ct5hfxAVBvrUNhAK"
              "tHEztP3tWWWsdA==;77\",\"y2\":\"ZZ95PbHbmas16Q==;78\",\"y3\":\"b6wjL6R9urfWLQ==;79\",\"y6\":\"8ph/Wze0o44"
              "OEw==;80\",\"y8\":\"K0DAUkZ5LJtmCw==;81\",\"x4\":\"tBACNyx3vPnnIg==;82\",\"z5\":\"gDFUzCa8puc=;83\",\"z4"
              "\":\"lY2KhITKsm33gw==;84\",\"z6\":\"mMMLkkprgHltNS1O;85\",\"z7\":\"KLiBOqlvpv84wrNI;86\",\"z8\":\"lZ+uhI"
              "Dva/5EupvPHrA=;87\",\"z9\":\"JgoEmIEvYyQkgXld;88\",\"y1\":\"+NmAZ8+/w2AqIQFb;89\",\"y4\":\"bT+4kuRG2b+aJ"
              "KRO;90\",\"y5\":\"Nx03BU5JkRB0j6OjPdU=;91\",\"y7\":\"hoj29CpK20TSSFei;92\",\"y9\":\"UdEjrT97SzmdOlMIjqw="
              ";93\",\"y10\":\"5m/BGt0+Jnq1b2zGYSY=;94\",\"x1\":\"fsfE0nMXFwUwOWCn;95\",\"x2\":\"FqqJ6cb+Gs6bO1X/lyE=;9"
              "6\",\"x3\":\"VCcjEAlBuY3iOjBH;97\",\"x5\":\"wZEBahwQn8oL3Hly;98\",\"z3\":\"D2GC3ADoqQTo2KYQaIUr2Th7y0TSq"
              "w9xUFoAiS/TIbU=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"fRKHOZf0jaY8Iu7XnWepx+n6tl0=;100\",\"pgrd\":\"i41b/3pML"
              "9YQqkBXtsWo7EjPGKYoqFYASDA7QqrQ/9I9agiP93iT+6nHd5OVgYgeUnbQJ0+5XFiEqKo7THvOf6i4enWdgLM1MsNXmEYldOIKJKo7M"
              "2DJterw5tj/aY1ImxLdsf/fv0q8KRn3yalQthK/nkvpKYJxAt3lQkhSbS/TcqcmV6A17LcSoGjS9bw+aV+pakE3225YJUfVdBngFZ/9Q"
              "EQ=\"}",
    "cookie": "suid=700dd4a1e974b70704b0f3989933a6ad.efb5151718216403ff84c2b188366119; _csrf_token=15d94c5770b0c4883d52"
              "39e11f76163dea4893d5f1b7644a; autoru_sid=a%3Ag63465d8f29k90rfihth9gu0perimqg6.a71785c9b531415556e29acb2b"
              "2103ff%7C1665555855147.604800.Bn0FNf7_jo8YvIVoldHD9w.8960hqxZNsKiNqHZhS-9dzm93T0WkagNw6rIaEL8CE4; autoru"
              "uid=g63465d8f29k90rfihth9gu0perimqg6.a71785c9b531415556e29acb2b2103ff; from=google-search; counter_ga_al"
              "l7=1; yuidlt=1; yandexuid=5520552951662130583; my=YwA%3D; crookie=eONKdqoiFvvEoN7p3GC4FtydI4QNC9J0kuFgI1"
              "/cNuT5R0nTbWgd7N8lWRW+Lz1A5eii/nog4RqJvL2ddXHF8Ow0C9I=; cmtchd=MTY2NTU1NTg1ODgzMg==; Session_id=3:166555"
              "5857.5.0.1662132854829:HXoyTQ:14.1.2:1|1493859612.0.2|61:10008055.637171.i_WF6I6HmF6YahLknFOl2_tNWxE; ya"
              "ndex_login=QoptT; ys=udn.cDohUW9wVA%3D%3D#c_chck.161589749; i=QpNfI7bbB/UPs8/sP6yGL5FzZy4M8AfNpiFdv6j1aF"
              "2BCL9eiDE48GyGJG7wasgus8fao4DIiA5qvTfUYXIH0yJpLW0=; mda2_beacon=1665555858015; sso_status=sso.passport.y"
              "andex.ru:synchronized; gdpr=0; _ym_uid=16655558601026138640; _ym_isad=1; _yasc=1eMB/0jdDT5cY6cMDyqXdLf0T"
              "y9CRUq+Xs5PjO9Mn9XKWT2l; layout-config={\"win_width\":1236,\"win_height\":1290}; from_lifetime=166555655"
              "8076; _ym_d=1665556561",
    "Referer": "https://auto.ru/moskva/cars/bmw/5er/2305607/all/",
    "Referrer-Policy": "no-referrer-when-downgrade"
  },
  "body": "{\"catalog_filter\":[{\"mark\":\"BMW\",\"model\":\"5ER\",\"generation\":\"2305607\"}],\"section\":\"all\",\""
          "category\":\"cars\",\"exclude_catalog_filter\":[{}],\"output_type\":\"list\",\"geo_radius\":200,\"geo_id\":["
          "213]}",
  "method": "POST"
})

print(bmw.status_code)
offers = bmw.json()['offers']
for offer in offers:
    price = offer["price_info"]["USD"]
    name = offer["vehicle_info"]["model_info"]["name"]
    mileage = offer["state"]["mileage"]
    print(f"Найден {name} всего за ${price}, пробег всего {mileage} км")
