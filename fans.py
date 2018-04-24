import json
import urllib.request
import csv
import os

# 获取access_token
accessTokenURL = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx3ed7aaca56894fe4&secret=5b0dfdf468e99d2e904817128d0da0d7"
accessTokenBytes = urllib.request.urlopen(accessTokenURL).read()  #access_token页面的Bytes格式
accessTokenStr = str(accessTokenBytes, encoding = "utf-8")        #access_token页面的Str格式
accessTokenDict = json.loads(accessTokenStr)                      #获取JSON中的access_token
accessToken = accessTokenDict.get("access_token")

openIdURL = ('https://api.weixin.qq.com/cgi-bin/user/get?access_token='+accessToken+'&next_openid=')
openIdBytes = urllib.request.urlopen(openIdURL).read()
openIdStr = str(openIdBytes, encoding = "utf-8")
openIdDict = json.loads(openIdStr)
total = int(openIdDict.get("total"))

if not(os.path.exists("/Users/admin/Desktop/wechatUserID/UserInfo.csv")):
    with open("/Users/admin/Desktop/wechatUserID/UserInfo.csv",'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["No","subscribe","openid","nickname","sex","language","city","province","country","headimgurl","subscribetime","remark","groupid","tagid_list"])
    nextOpenId = ""
        #print (userCount)

with open("/Users/admin/Desktop/wechatUserID/UserInfo.csv","r", newline='') as csvfile:
    lineNum = 0
    lineCount = 0
    userCount = 0
    userCSV=csv.reader(csvfile)
    for row in userCSV:
        #print (row)
        lineNum += 1
#    print("linenumber=", lineNum)
    userCount = lineNum - 1
with open("/Users/admin/Desktop/wechatUserID/UserInfo.csv","r", newline='') as csvfile:
    userCSV=csv.reader(csvfile)
    for row in userCSV:
        # print (row)
        lineCount += 1
        if lineCount > 1:
            rowInt = int(row[0])
            print(rowInt)
            if (rowInt == lineNum-1):
                print("nextOpenID=", row[2])
                nextOpenId = row[2]

# 获取openid数组
while total > userCount :
    # 获取access_token(每次获取openidlist都重新获取accesstoken）
    accessTokenURL = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx3ed7aaca56894fe4&secret=5b0dfdf468e99d2e904817128d0da0d7"
    accessTokenBytes = urllib.request.urlopen(accessTokenURL).read()  #access_token页面的Bytes格式
    accessTokenStr = str(accessTokenBytes, encoding = "utf-8")        #access_token页面的Str格式
    accessTokenDict = json.loads(accessTokenStr)                      #获取JSON中的access_token
    accessToken = accessTokenDict.get("access_token")
    openIdURL = ('https://api.weixin.qq.com/cgi-bin/user/get?access_token='+accessToken+'&next_openid='+nextOpenId)
    openIdBytes = urllib.request.urlopen(openIdURL).read()
    openIdStr = str(openIdBytes, encoding = "utf-8")
    openIdDict = json.loads(openIdStr)
    openIdData = openIdDict.get("data")
    openIdList = openIdData.get("openid")
    total = int(openIdDict.get("total"))
    # print (total)
    #信息写入表格
    for openid in openIdList:
        userInfoURL = ('https://api.weixin.qq.com/cgi-bin/user/info?access_token='+accessToken+'&openid='+openid+'&lang=zh_CN')
        #userInfoURL = ('https://api.weixin.qq.com/cgi-bin/user/info?access_token='+accessToken+'&openid='+openid+'&lang=zh_CN')
        userInfoBytes = urllib.request.urlopen(userInfoURL).read()
        userInfoStr = str(userInfoBytes, encoding = "utf-8")
    # 逗逗的方法
        userInfoDict = json.loads(userInfoStr)
        userInfo_Number = userCount + 1
        userInfo_subscribe = userInfoDict.get("subscribe")
        userInfo_openid = userInfoDict.get("openid")
        userInfo_nickname = userInfoDict.get("nickname").encode('gbk', 'ignore').decode('gbk')
        userInfo_sex = userInfoDict.get("sex")
        userInfo_laguage = userInfoDict.get("language")
        userInfo_city = userInfoDict.get("city")
        userInfo_province = userInfoDict.get("province")
        userInfo_country = userInfoDict.get("country")
        userInfo_headimgurl = userInfoDict.get("headimgurl")
        userInfo_subscribetime = userInfoDict.get("subscribe_time")
        userInfo_remark = userInfoDict.get("remark")
        userInfo_groupid = userInfoDict.get("groupid")
        userInfo_tagid_list = userInfoDict.get("tagid_list")
        userInfoList = [userInfo_Number,userInfo_subscribe,userInfo_openid,userInfo_nickname,userInfo_sex,userInfo_laguage,userInfo_city,userInfo_province,userInfo_country,userInfo_headimgurl,userInfo_subscribetime,userInfo_remark,userInfo_groupid,userInfo_tagid_list]
        with open("/Users/admin/Desktop/wechatUserID/UserInfo.csv","a+",encoding='gbk',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(userInfoList)
        userCount = userCount + 1
        print(userCount)

print("I'm done!")
# # 逗逗的方法END
