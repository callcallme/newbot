from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
#from linebot.models import (
#    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
#)
from linebot.models import*


app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('jUj0lW7u/u8xQDwU2H+KF3Up7clElmAWY6PWHMPHbmZpj2+TjK76LiAfXmZLhd+vFlMZd9OVeCDE/9v140/Jv2SxSBpdg7Y9mxOmI2oxuENANbcjJrwuTOj3d4x3hzTx7zpJwGmdxTCCUc+ynMEW3wdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('86e586703b29cb67f92813076f135842')

















#line 訊息回傳
def keySearch(word):
    
    info ={'蘋果':'醫生遠離你','美女':'搜尋中','bike':'中文叫腳踏車','聯成電腦':'good'}
    return info.get(word,'請輸入(樣板)(蘋果)(美女)(bike)(聯成電腦)(新北自行車)(台中日月潭)(日月潭)(新北自行車)(韓國瑜)')
content = ''












# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


result = ''












@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    msg = event.message.text
    
    status = 1
    
    global content
    
    if '新北自行車' in msg:
        #msg = getubike.getBike()
        #result = '自行車'
        tp = NTPUbike.NTPUbike()
        msg = tp.getBike()
        content = 'bike'
        
        
        
        
        
        
        
    elif '韓國瑜' in msg:
        status = 6
        imgurl = queryimage.QueryImage(1)
        


        
    elif '貼圖' in msg:
        msg = StickerSendMessage(package_id = 1,sticker_id = 2)
        status = 3
 

       
    elif '樣板' in msg:
        status = 7
        msg = TemplateSendMessage(
        alt_text = '目錄樣板',
        template = ButtonsTemplate(
                title = '生活請line我',
                text = '請按以下鍵',
                thumbnail_image_url='https://34c.cc/PetUpload/2016-09/0b32aff3c0e8884141e4d61e65b2515c.jpg',
                actions=[
                    MessageTemplateAction(
                        label='請按我!!',
                        text = '按到了~.~'
                        ),MessageTemplateAction(
                        label='台北捷運!!',
                        text = '北捷'
                        ),MessageTemplateAction(
                        label='高雄捷運',
                        text = '高捷'
                        ),MessageTemplateAction(
                        label='日月潭',
                        text = '日月潭'
                        )
                    ]
                )
            )
            
            
        
    
    
    
    
    elif '北捷' in msg:
        status = 2
    elif '高捷' in msg:
        status = 8
    elif '台中日月潭' in msg:
        status = 4
    elif '日月潭' in msg:
        status = 5
        
  
      
    else:
        if content == 'bike':
            tp = NTPUbike.NTPUbike()
            msg = tp.getAreaBike(msg)
            content=''
        else:            
            msg = keySearch(msg)    
        
        
        
        
        
        
        
    if status == 6:
        message = ImageSendMessage(
                original_content_url=imgurl,
                preview_image_url=imgurl)
                #圖片網址必須 https .........jpg(png)
 







               
                
    elif status == 8:
        message = ImageSendMessage(
                original_content_url='https://www.krtco.com.tw/images/newInnerSite/guide/guide_routemap.png',
                preview_image_url='https://www.krtco.com.tw/images/newInnerSite/guide/guide_routemap.png')
                #圖片網址必須 https .........jpg(png)
    elif status == 4:
                message = ImageSendMessage(
                original_content_url='https://i4.achangpro.com/img.nanai.tw/20180115155300_87.jpg',
                preview_image_url='https://i4.achangpro.com/img.nanai.tw/20180115155300_87.jpg')
                
    elif status == 5:           
                message = ImageSendMessage(
                original_content_url='https://i3.achangpro.com/img.snowhy.tw/20190430173629_96.jpg',
                preview_image_url='https://i3.achangpro.com/img.snowhy.tw/20190430173629_96.jpg')
    elif status == 2:
        message = ImageSendMessage(
                original_content_url='https://web.metro.taipei/img/all/routemap2018.jpg',
                preview_image_url='https://web.metro.taipei/img/all/routemap2018.jpg')



    elif status == 7:
        message =msg

    else:
        
        message = TextSendMessage(text=msg) #回傳line文字訊息
    
    
    
    line_bot_api.reply_message(
        event.reply_token,
        message)




import os
import getubike
import queryimage
import NTPUbike







if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)























