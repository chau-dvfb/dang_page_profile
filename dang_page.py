import requests, re, os
from time import sleep
import json
# Count 
dem=0
# =========================== [ CLASS + FUNCTION TOOL ] ===========================
class NguyenNgocBaoChau_Activated_Page:
    # Tool Activated Page Die
    # Code By: Nguyễn Ngọc Bảo Châu
    # Code Share Free. Nghiêm Cấm Bán
    # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng)
    def banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        banner = '''
        [           COPYRIGHT LICENSE: NGUYENNGOCBAOCHAU           ]
        [           NGUYEN NGOC BAO CHAU - ZALO: 0961323610        ]
        [           FB: FB.COM/NGUYEN.NGOC.BAO.CHAU.015            ]              
        [  TOOL KÍCH HOẠT PAGE TRUYỀN THỐNG VIP PRO - VERSION 1.0  ]
        '''
        print(banner)
    def nnbc_delay_tool(self, p):
        while(p>1):
            p=p-1
            print(f'[NGUYENNGOCBAOCHAU][|][LO......][{p}]','     ',end='\r');sleep(1/6)
            print(f'[NGUYENNGOCBAOCHAU][/][LOA.....][{p}]','     ',end='\r');sleep(1/6)
            print(f'[NGUYENNGOCBAOCHAU][-][LOAD....][{p}]','     ',end='\r');sleep(1/6)
            print(f'[NGUYENNGOCBAOCHAU][+][LOADI...][{p}]','     ',end='\r');sleep(1/6)
            print(f'[NGUYENNGOCBAOCHAU][\][LOADIN..][{p}]','     ',end='\r');sleep(1/6)
            print(f'[NGUYENNGOCBAOCHAU][|][LOADING.][{p}]','     ',end='\r');sleep(1/6)
    def GetThongTinFacebook(self, cookie: str):
        # Nhận Code Thuê Theo Yêu Cầu Zalo: 0961323610 - NGUYỄN NGỌC BẢO CHÂU
        headers_get = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','viewport-width': '1184','cookie': cookie}
        try:
            # print("Đang Check Live Cookie...", end="\r")
            url_profile = requests.get('https://www.facebook.com/me', headers = headers_get).url
            get_dulieu_profile = requests.get(url = url_profile, headers = headers_get).text
            with open('dataID.txt', 'w', encoding='utf-8') as file:
                file.write(str(get_dulieu_profile))
        except:
            return {'status': 'error', 'message':'Get Dữ Liệu Thất Bại Vui Lòng Kiểm Tra Lại!!'}
        try:
            uid_get = cookie.split('c_user=')[1].split(';')[0]
            name_get = get_dulieu_profile.split('<h1 class="x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz">')[1].split('<!-- --> <span class=""></span>')[0].strip()
            print("Token:", name_get)

            fb_dtsg_get = get_dulieu_profile.split('"DTSGInitData":{"token":"')[1].split('",')[0]
            print("Token:", fb_dtsg_get)
            jazoest_get = get_dulieu_profile.split('&jazoest=')[1].split('","')[0]
            print("Token:", jazoest_get)
            lsd = get_dulieu_profile.split('["LSD",[],{"token":"')[1].split('"},')[0]
            print("Token:", lsd)
            with open('a.txt', 'w') as file:
                file.write(f"{fb_dtsg_get},{jazoest_get}, {lsd}")
            print("thành công:")
            return {'status':'success', 'name': name_get, '__user': uid_get, 'fb_dtsg': fb_dtsg_get, 'jazoest': jazoest_get, 'lsd': lsd}
            
        except:
            try:
                uid_get = cookie.split('c_user=')[1].split(';')[0]
                print("222:", uid_get)
                name_get = get_dulieu_profile.split(';display:-webkit-box">')[1].split('</span>')[0]
                print("222:", name_get)
                fb_dtsg_get = get_dulieu_profile.split('"DTSGInitData":{"token":"')[1].split('",')[0]
                print("222a:", fb_dtsg_get)
                jazoest_get = get_dulieu_profile.split('&jazoest=')[1].split('","e":"')[0]
                print("222:", jazoest_get)
                lsd = get_dulieu_profile.split('["LSD",[],{"token":"')[1].split('"},')[0]
                print("222:", lsd)
                print("thành công 2:")
                return {'status':'success', 'name': name_get, '__user': uid_get, 'fb_dtsg': fb_dtsg_get, 'jazoest': jazoest_get, 'lsd': lsd}
            except:
                return {'status': 'error', 'message':'Get Dữ Liệu Thất Bại Vui Lòng Kiểm Tra Lại!!2'}
                
    def GetPageDie(self, cookie: str):
        # Nhận Code Thuê Theo Yêu Cầu Zalo: 0961323610 - NGUYỄN NGỌC BẢO CHÂU
        headers_getpage = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6','cache-control': 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"','sec-ch-ua-full-version-list': '"Google Chrome";v="113.0.5672.174", "Chromium";v="113.0.5672.174", "Not-A.Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"10.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36','viewport-width': '1585','cookie': cookie}
        try:
            get_data = requests.get('https://www.facebook.com/pages/?category=your_pages&ref=bookmarks', headers=headers_getpage).text
            data = re.findall(r'"uri_token":"(.*?)"', get_data)
            with open('data.txt', 'w', encoding='utf-8') as file:
                file.write(str(data))
            if data == []:
                return {'status': 'error', 'message':'Không Tìm Thấy Page Die Nào!!'}
            else:
                with open('data.txt', 'w', encoding='utf-8') as file:
                    file.write(str(data))
                return {'status': 'success', 'data': data, 'count': len(data)}
        except:
            return {'status': 'error', 'message':'Get Page Die Thấy Bại. Vui Lòng Kiểm Tra Lại Tài Khoản'}
    def Activated_Page(self, cookie: str, fb_dtsg: str, jazoest: str, lsd: str, uid_page_die):
        global dem
        # Nhận Code Thuê Theo Yêu Cầu Zalo: 0961323610 - NGUYỄN NGỌC BẢO CHÂU
        # headers_activated = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/pages/?category=your_pages&ref=bookmarks','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"','sec-ch-ua-full-version-list': '"Google Chrome";v="113.0.5672.174", "Chromium";v="113.0.5672.174", "Not-A.Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"10.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36','viewport-width': '1585','x-asbd-id': '129477','x-fb-friendly-name': 'ReactivateProfileMutation','x-fb-lsd': lsd,'cookie': cookie}
        headers_activated = {
  'authority': 'www.facebook.com',
  'accept': '*/*',
  'accept-language': 'vi',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': cookie,
  'dpr': '1.25',
  'origin': 'https://www.facebook.com',
  'referer': 'https://www.facebook.com/pages/?category=your_pages&ref=bookmarks',
  'sec-ch-prefers-color-scheme': 'light',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.130", "Google Chrome";v="120.0.6099.130"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'viewport-width': '1087',
  'x-asbd-id': '129477',
  'x-fb-friendly-name': 'ReactivateProfileMutation',
  'x-fb-lsd': lsd
}
        data_activated = {
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'lsd': lsd,
            '__spin_r': '1010616944',
            '__spin_b': 'trunk',
            '__spin_t': '1704056952',
            'fb_api_caller_class': '    ',
            'fb_api_req_friendly_name': 'ReactivateProfileMutation',
            # 'variables': '{"input":{"page_id":"' + uid_page_die + '","publish_mode":"PUBLISHED","actor_id":"' + uid_page_die + '","client_mutation_id":"2"}}',
            'variables': '{"profile_id":"' + uid_page_die + '","delegate_page_id":null}',
            'server_timestamps': 'true',
            'doc_id': '6365256943526229'
        }
        Json_Activated_Page = requests.post('https://www.facebook.com/api/graphql/', headers=headers_activated, data=data_activated).json()
        with open('datave.txt', 'w', encoding='utf-8') as file:
            json.dump(Json_Activated_Page, file, ensure_ascii=False, indent=2)
        try:
            dem+=1
            # print(f'[NNBC] | {dem} | ACTIVATED_PAGE_SUCCESS | [UID_PAGE: '+Json_Activated_Page['data']['reactivate_profile']['name']['id']+']')
            # print(f'[NNBC] | {dem} | ACTIVATED_PAGE_SUCCESS | [UID_PAGE: {Json_Activated_Page["data"]["reactivate_profile"]["name"]["id"]}]')
            print(f'[NNBC] | {dem} | ACTIVATED_PAGE_SUCCESS | [Name: {Json_Activated_Page["data"]["reactivate_profile"]["name"]}, UID_PAGE: {Json_Activated_Page["data"]["reactivate_profile"]["id"]}]')
        except:
            print(f'[NNBC] | {dem} | ACTIVATED_PAGE_ERROR | [UID_PAGE: {uid_page_die}]')
# =========================== [ START TOOL ] ===========================         
NguyenNgocBaoChau_Tool = NguyenNgocBaoChau_Activated_Page()
NguyenNgocBaoChau_Tool.banner()
while True:
    cookie = input('VUI LÒNG NHẬP COOKIE FACEBOOK: ')
    if cookie != '':
        break
    continue
# Setting Config
NguyenNgocBaoChau_Tool.banner()
delay = int(input('VUI LÒNG NHẬP DELAY KÍCH HOẠT TRANG: '))
Check_Live_Account = NguyenNgocBaoChau_Tool.GetThongTinFacebook(cookie)
if Check_Live_Account['status'] != 'error':
    name = Check_Live_Account['name']
    uid = Check_Live_Account['__user']
    fb_dtsg = Check_Live_Account['fb_dtsg']
    print('111'+ fb_dtsg)
    jazoest = Check_Live_Account['jazoest']
    lsd = Check_Live_Account['lsd']
    print('─'*50)
    print('NAME_FB: {0} | UID_FB: {1}'.format(name,uid))
    print('─'*50)
    Check_Count_Page = NguyenNgocBaoChau_Tool.GetPageDie(cookie)
    print('Đã Tìm Thấy: '+str(Check_Count_Page['count'])+' Page Pro5 Cần Kích Hoạt', end='\r')
    for data_trang in Check_Count_Page['data']:
        # code 1
        uid_page_die = data_trang.replace('":{"id":"', '{"uri_token":"').replace('"},"profilePic40"', '","profilePic40":')
        # code 2
        # uid_page_die = data_trang.replace('"uri_token":"').replace('","profilePic40":')
        NguyenNgocBaoChau_Tool.Activated_Page(cookie, fb_dtsg, jazoest, lsd, uid_page_die)
        NguyenNgocBaoChau_Tool.nnbc_delay_tool(delay)
else:
    print(Check_Live_Account['message'])