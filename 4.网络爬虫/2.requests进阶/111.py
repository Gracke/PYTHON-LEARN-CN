import requests

url = "https://m.douban.com/rexxar/api/v2/gallery/hot_items?ck=null&start=0&count=20"

headers ={
    "User-Agent": "Mozilla/5.0 (X11; Mac x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62",
    "Cookie": "ll='118293'; bid=cFKbAi2NjPE; ap_v=0,6.0; push_doumail_num=0; __utma=30149280.595133959.1673356726.1673356726.1673356726.1; __utmc=30149280; __utmz=30149280.1673356726.1.1.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=30149280.24794; push_noty_num=0; __gads=ID=7afd49c73b8041c7-2255810c3cd900fe:T=1673356901:RT=1673356901:S=ALNI_Mbj8Oq-Jrucnqj6ihqyF1kycW2s8Q; __gpi=UID=00000ba14700419e:T=1673356901:RT=1673356901:S=ALNI_MaZoga3R1vWEHIgU8wYv6p_WxF-zg; __utmt=1; __utmt_douban=1; gr_user_id=28ab1355-ab8b-435d-aecd-538b7669045f; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=c3718b69-e653-4fef-9569-a162a6f25da1; gr_cs1_c3718b69-e653-4fef-9569-a162a6f25da1=user_id%3A0; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_c3718b69-e653-4fef-9569-a162a6f25da1=true; __utmb=30149280.80.10.1673356726"
}
resp =requests.get(url,headers=headers)
print(resp.text)
