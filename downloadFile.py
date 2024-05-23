import urllib.request

def download_file(url, dst_path):
    with urllib.request.urlopen(url) as web_file:
        with open(dst_path, 'wb') as local_file:
            local_file.write(web_file.read())