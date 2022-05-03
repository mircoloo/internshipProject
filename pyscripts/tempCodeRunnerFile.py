for i,url in enumerate(imgUrls):
        req = requests.get(url)
        file = open(f"../images/sample_image{i}.png", "wb")
        file.write(req.content)
        file.close()