#URLから画像を取得
import datetime
import downloadFile

filename = ''
path = 'file/' + filename

with open(path,'r',encoding="utf-8_sig") as file:
    str = file.readlines()

#str[24]は対象のHTMLが入った要素
#文字列個数計算
sNum = str[24].count('検索URL始まり文字')
eNum = str[24].count('検索UR終わり文字')

nUrlList = []
thumbUrlList = []
if sNum == eNum:
    #画像URL抜き出し
    startP = 0
    endP = 0
    for i in range(sNum):
        startP = str[24].find('検索URL始まり文字', startP)
        endP = str[24].find('検索UR終わり文字', endP) + 4
        #thumb.jpg check
        thumbC = str[24][startP:endP].find('thumb.jpg')
        if thumbC > 1:
            nUrlList.append(str[24][startP:endP])
            url = str[24][startP:endP]
            dst_path = 'output/normal/' + filename + '-' + '%i' % i + '.jpg'
            print(dst_path)
            downloadFile.download_file(url, dst_path)
        else:
            thumbUrlList.append(str[24][startP:endP ])
            url = str[24][startP:endP]
            dst_path = 'output/thumb/' + filename + '-' + '%i' % i + '.jpg'
            downloadFile.download_file(url, dst_path)
        startP += 1
#URLテキスト書き出し
dt_now = datetime.datetime.now()
with open('output/nUrlList.txt','a') as urlFile:
    urlFile.write(filename + dt_now.strftime('%Y/%m/%d %H:%M:%S') + '\n')
    urlFile.write('\n'.join(nUrlList))
    urlFile.write('\n-------------------------------------------------------------------------------------------------------------------------------\n')

with open('output/thumbUrlList.txt','a') as thumbUrlFile:
    thumbUrlFile.write(filename + dt_now.strftime('%Y/%m/%d %H:%M:%S') + '\n')
    thumbUrlFile.write('\n'.join(thumbUrlList))
    thumbUrlFile.write('\n-------------------------------------------------------------------------------------------------------------------------------\n')

