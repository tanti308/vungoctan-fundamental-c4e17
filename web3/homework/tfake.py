from random import choice,randint
def male_name():
    h=['Nguyễn','Trần','Lê','Phạm','Hoàng','Huỳnh','Phan','Vũ','Võ','Đặng','Bùi','Đỗ','Hồ','Ngô','Dương','Lý','Hà','Đào','Phùng','Trương','Nông','Phương','Cao','Mai','Đinh','Lương','Trịnh','Đoàn']
    d=['Anh','Tuấn','Hoàng','Phúc','Khải','Phương','Bá','Tuấn','Hữu','Hải','Nhân','Đức','Trọng','Phú','Minh','Xuân','Trung','Tuấn','Đinh','Khôi','Phước','Hoàng','Bảo','Thành','Lâm','Việt','Đức','Đăng','Nhật','Vinh','','']
    t=['Anh','Tuấn','Hoàng','Phúc','Khải','Phương','Nam','Dũng','Hữu','Hải','Nhân','Đức','Trọng','Phú','Minh','Dương','Trung','Tuấn','Nghĩa','Khôi','Phước','Hoàng','Bảo','Thành','Lâm','Việt','Đức','Nguyên','Nhật','Vinh','Phong','Chung','Quân','Quang','Quốc','Tuấn','Thành','Thiên','Thịnh','Sơn','Việt','Bách','Cường','Đạt','Hiếu','Huy','Hùng','Tuấn Anh']
    while True:
        ho = choice(h)
        dem = choice(d)
        ten = choice(t)
        if ho==dem or dem==ten:
            continue
        else:
            name= ho+' '+dem+' '+ten
            break
    return(name)
def female_name():
    h=['Nguyễn','Trần','Lê','Phạm','Hoàng','Huỳnh','Phan','Vũ','Võ','Đặng','Bùi','Đỗ','Hồ','Ngô','Dương','Lý','Hà','Đào','Phùng','Trương','Nông','Phương','Cao','Mai','Đinh','Lương','Trịnh','Đoàn']
    d=['Mỹ','Khánh','Kiều','Phúc','Thùy','Mai','Hoa','Ngọc','Diễm','Hải','Bích','Nhã','Thúy','Minh','Xuân','Hoàng','Bảo','','Nhật','']
    t=['Anh','Ngọc','Châu','Uyên','Linh','Phương','Chi','Nhi','Thư','Hải','Thùy','Mai','Hoa','Ngọc','Minh','Dương','Hiền','Thủy','Quyên','Hà','Phước','Bích','Trâm','Khuê','Tú','Ngân','Trang','Thúy','Tuyết','Ngà','Oanh','Vân Anh','Quỳnh Anh','Phương Anh','Bảo Anh','Tâm','Bình','Ngọc Ánh']
    while True:
        ho = choice(h)
        dem = choice(d)
        ten = choice(t)
        if ho==dem or dem==ten:
            continue
        else:
            name= ho+' '+dem+' '+ten
            break
    return(name)
def tp():
    tps=['An Giang','Bà Rịa-Vũng Tàu','Bạc Liêu','Bắc Kạn','Bắc Giang','Bắc Ninh','Bến Tre','Bình Dương','Bình Định','Bình Phước','Bình Thuận','Cà Mau','Cao Bằng','Cần Thơ (TP)','Đà Nẵng (TP)','Đắk Lắk','Đắk Nông','Điện Biên','Đồng Nai','Đồng Tháp','Gia Lai','Hà Giang','Hà Nam','Hà Nội (TP)','Hà Tĩnh','Hải Dương','Hải Phòng (TP)','Hòa Bình','Hồ Chí Minh (TP)','Hậu Giang','Hưng Yên','Khánh Hòa','Kiên Giang','Kon Tum','Lai Châu','Lào Cai','Lạng Sơn','Lâm Đồng','Long An','Nam Định','Nghệ An','Ninh Bình','Ninh Thuận','Phú Thọ','Phú Yên','Quảng Bình','Quảng Nam','Quảng Ngãi','Quảng Ninh','Quảng Trị','Sóc Trăng','Sơn La','Tây Ninh','Thái Bình','Thái Nguyên','Thanh Hóa','Thừa Thiên - Huế','Tiền Giang','Trà Vinh','Tuyên Quang','Vĩnh Long','Vĩnh Phúc','Yên Bái']
    tp = choice(tps)
    return(tp)
def sdt():
    s=['096','097','098','086', '0162','0163', '0164', '0165', '0166', '0167', '0168', '0169','091', '094', '088', '0123', '0124', '0125', '0127', '0129','090', '093', '089', '0120', '0121', '0122', '0126', '0128']
    d=['0','1','2','3','4','5','6','7','8','9']
    sdt=choice(s)
    for i in range(7):
        t=choice(d)
        sdt=sdt+t
    return(sdt)

def description():
    characters = ['dễ tính', 'vui vẻ', 'hòa đồng', 'lạc quan',
                  'khéo léo', 'hài hước', 'nóng tính', 'ích kỉ',
                  'nhẹ nhàng', 'thảo mai', 'thân thiện', 'cẩn thận',
                  'tỉ mỉ', 'cầu toàn', 'kỹ tính']
    description = []
    for i in range(4):
        character = choice(characters)
        description.append(character)
    return (description)

def cty():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    url="http://s.cafef.vn/danh-sach-tap-doan-doanh-nghiep-lon.chn"
    conn = urlopen(url)
    raw_data=conn.read()
    text = raw_data.decode("utf8")

    soup = BeautifulSoup(text,"html.parser")

    table=soup.find("table",id='table_list')
    tr_list = table.find_all("tr")
    data=[]
    for tr in tr_list:
        list=[]
        td_list=tr.find_all("td")
        for td in td_list:
            a=td.a
            i=a.string
            list.append(i)
        if list:
            d=list[1].strip()
            data.append(d)
    cty=choice(data)
    return(cty)
def job():
    jobs=['Giám đốc','Phó Giám đốc','Chủ tịch Hội đồng quản trị','Trưởng phòng','Phó phòng','Kế toán','Nhân viên','Tạp vụ','Lao công','Bảo vệ','Chủ tịch Công đoàn','Thực tập','Quản lý','Thu ngân','Thư kí']
    job = choice(jobs)
    return(job)

def measurements():
    mesurements = [randint(80,100), randint(55,80), randint(80,100)]
    return (mesurements)

def male_image():
    images=["https://znews-photo-td.zadn.vn/w1024/Uploaded/ohunua2/2017_10_23/14334429_966481333479105_2642026523426553856_n.jpg","https://kenh14cdn.com/2016/photo-2-1473181350922.jpg","http://s2.chacha.vn/albums/s2/4/36137/36137.jpg","https://2.bp.blogspot.com/-yToitZjBlyQ/WlxXETUC7QI/AAAAAAAASOg/e07Jl1-g64o7mQx0GKz5k6W_IRfJRI3pACLcBGAs/s1600/15940614_1839963919625975_8086361825789331208_n_2.jpg","https://i.ytimg.com/vi/zAVr9gr7MX4/maxresdefault.jpg","http://media.phunutoday.vn/files/upload_images/2014/06/23/kenny%20sang.jpg","https://kenh14cdn.com/thumb_w/660/2017/img-7310-1506166016665-1513419731695.jpg",
    "https://kenh14cdn.com/2017/2227893452184799150108335628580o-1507174784235-1513420021801.jpg",
    "https://kenh14cdn.com/2017/13606444-1140457839344783-7664756729118038695-n-1501511320935-1513421477115.jpg",
    "https://kenh14cdn.com/2017/20664687-1931280623811540-2633903832468491112-n-1505389713725-1513421614447.jpg",
    "https://kenh14cdn.com/2017/1622868314584899174946357171376438241656832n-1507019479650-1513420491197.jpg",
    "https://kenh14cdn.com/thumb_w/660/2017/2131471613739253460582874150518321823079014n-1507020328709-1513420681816.jpg"]
    image = choice(images)
    return(image)

def female_image():
    images=["https://baomoi-photo-1-td.zadn.vn/w1000_r1/15/09/16/105/17513189/8.jpg","http://nguoinoitieng.tv/images/nnt/95/3/ba9x.jpg","https://znews-photo-td.zadn.vn/w1024/Uploaded/oqivovbt/2018_03_04/vu_zing_1.jpg","http://designs-by-sara.com/wp-content/uploads/2016/01/hot-girl-kha-ngan-xinh-dep2-1024x768-1414054504.jpg", "https://pbs.twimg.com/profile_images/547955426885517314/dvF2D1fr.jpeg","https://image.thanhnien.vn/1600/uploaded/thuyhang/2017_10_29/img_0255_lpou.jpg","http://hotshowbiz.com/wp-content/uploads/2017/12/Ribi-Sachi-Mot-thanh-vien-ky-cuu-cua-FAPtv.jpg","https://giaitrinews.vn/wp-content/uploads/2017/10/2-Lan-Huong-trong-phim-cua-FAPtv.jpg","https://znews-photo-td.zadn.vn/w820/Uploaded/kcwvouvs/2017_04_18/15624155_1264609093595675_8005514290339512320_n.jpg","http://file.vforum.vn/hinh/2018/01/top-nhung-hot-girl-viet-nam-xinh-nhat-hien-nay-2018-1.png","http://file.vforum.vn/hinh/2018/01/top-nhung-hot-girl-viet-nam-xinh-nhat-hien-nay-2018-5.png",
    "http://file.vforum.vn/hinh/2018/01/top-nhung-hot-girl-viet-nam-xinh-nhat-hien-nay-2018-27.png",
    "http://file.vforum.vn/hinh/2018/01/top-nhung-hot-girl-viet-nam-xinh-nhat-hien-nay-2018-29.png"]
    image = choice(images)
    return(image)
