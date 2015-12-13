"""ข้อมูลปีพุทธกาล 2554"""

import webbrowser
import folium
from nvd3 import multiBarChart

list_hs = {1 : [[4, 2, 3], [3, 2, 0], [18.78845, 99.02664], "โรงพยาบาลกรุงเทพ"]\
           , 2 : [[0, 0, 0], [2, 1, 1], [13.72831, 100.53215], "โรงพยาบาลกรุงเทพคริสเตียน"]\
           , 3 : [[40, 20, 9], [15, 6, 0], [13.71075, 100.39911], "โรงพยาบาลเกษมราษฏร์บางเเค"]\
           , 4 : [[17, 6, 5], [5, 0, 0], [13.73171, 100.53647], "โรงพยาบาลจุฬาลงกรณ์"]\
           , 5 : [[3, 1, 0], [3, 2, 0], [13.69436, 100.49473], "โรงพยาบาลเจริญกรุงประชารักษ์"]\
           , 6 : [[19, 0, 2], [5, 2, 1], [13.7311, 100.5080], "โรงพยาบาลตากสิน"]\
           , 7 : [[19, 8, 9], [4, 2, 2], [13.74305, 100.53837], "โรงพยาบาลตำรวจ"]\
           , 8 : [[15, 11, 6], [3, 1, 0], [13.66053, 100.43457], "โรงพยาบาลนครธน"]\
           , 9 : [[5, 3, 2], [1, 0, 0], [13.8169, 100.6880], "โรงพยาบาลนพรัตนราชธานี"]\
           , 10 : [[50, 40, ], [24, 16, 22], [13.8116, 100.7216], "โรงพยาบาลนวมินทร์"]\
           , 11 : [[5, 2, 3], [5, 4, 1], [13.7254, 100.4651], "โรงพยาบาลบางไผ่"]\
           , 12 : [[10, 4, 7], [4, 1, 4], [13.8072, 100.5232], "โรงพยาบาลบางโพ"]\
           , 13 : [[8, 7, 2], [2, 2, 2], [13.65167, 100.42214], "โรงพยาบาลพระราม 2"]\
           , 14 : [[4, 3, 2], [3, 3, 0], [13.7428, 100.5945], "โรงพยาบาลเพชรเวช"]\
           , 15 : [[10, 3, 5], [6, 3, 5], [13.7579, 100.5187], "โรงพยาบาลมิชชั่น"]\
           , 16 : [[20, 12, 10], [11, 4, 1], [13.76360, 100.53633], "โรงพยาบาลราชวิถี"]\
           , 17 : [[3, 0, 0], [5, 1, 1], [13.77811, 100.62432], "โรงพยาบาลลาดพร้าว"]\
           , 18 : [[1, 0, 1], [2, 1, 0], [13.78325, 100.53402], "โรงพยาบาลวิชัยยุทธ"]\
           , 19 : [[8, 0, 1], [3, 1, 0], [13.84582, 100.56227], "โรงพยาบาลวิภาวดี"]\
           , 20 : [[1, 0, 1], [2, 0, 0], [13.77176, 100.63703], "โรงพยาบาลเวชธานี"]\
           , 21 : [[15, 7, 3], [10, 7, 2], [13.7079, 100.3608], "โรงพยาบาลศรีวิชัย 2"]\
           , 22 : [[8, 4, 2], [11, 5, 0], [13.8255, 100.6575], "โรงพยาบาลศรีสยาม"]\
           , 23 : [[13, 7, 3], [3, 3, 0], [13.8562, 100.8589], "โรงพยาบาลหนองจอก"]\
           , 24 : [[8, 8, 6], [2, 2, 0], [13.6563, 100.3453], "โรงพยาบาลหลวงพ่อทวีศักดิ์"]\
           , 25 : [[8, 0, 1], [7, 3, 0], [13.7506, 100.5156], "โรงพยาบาลหัวเฉียว"]\
           , 26 : [[10, 5, 3], [7, 7, 0], [13.60832, 100.55148], "โรงพยาบาลกรุงเทพพระประแดง"]\
           , 27 : [[3, 3, 2], [2, 1, 0], [13.6098, 100.5400], "โรงพยาบาลบางจาก"]\
           , 28 : [[23, 20, 6], [4, 3, 1], [13.5695, 100.8362], "โรงพยาบาลบางบ่อ"]\
           , 29 : [[17, 6, 3], [8, 6, 0], [13.6034, 100.7062], "โรงพยาบาลบางพลี"]\
           , 30 : [[20, 16, 10], [13, 8, 3], [13.5844, 100.5970], "โรงพยาบาลสมุทรปราการ"]\
           , 31 : [[11, 4, 4], [4, 3, 0], [13.91296, 100.50925], "โรงพยาบาลกรุงไทย"]\
           , 32 : [[12, 8, 5], [11, 8, 1], [13.9822, 100.3254], "โรงพยาบาลไทรน้อย"]\
           , 33 : [[22, 8, 5], [6, 2, 0], [13.86427, 100.49840], "นนทเวช สหคลินิก"]\
           , 34 : [[7, 6, 4], [4, 3, 1], [13.8045, 100.4719], "โรงพยาบาลบางกรวย"]\
           , 35 : [[23, 17, 12], [7, 6, 1], [13.9186, 100.4226], "โรงพยาบาลบางบัวทอง"]\
           , 36 : [[19, 14, 3], [6, 5, 1], [13.9854, 100.6128], "โรงพยาบาลประชาธิปัตย์"]\
           , 37 : [[12, 11, 3], [6, 5, 0], [13.9569, 100.8579], "โรงพยาบาลลำลูกกา"]\
           , 38 : [[23, 12, 11], [20, 17, 0], [14.2134, 100.5764], "โรงพยาบาลบางปะอิน"]\
           , 39 : [[16, 11, 5], [10, 6, 2], [14.4448, 100.7374], "โรงพยาบาลภาชี"]\
           , 40 : [[19, 10, 11], [10, 8, 0], [14.8556, 100.9853], "โรงพยาบาลพัฒนานิคม"]\
           , 41 : [[54, 41, 27], [44, 31, 5], [14.8049, 100.6526], "โรงพยาบาลลพบุรี"]\
           , 42 : [[24, 17, 5], [24, 19, 1], [14.9221, 100.2747], "โรงพยาบาลบางระจัน"]\
           , 43 : [[22, 11, 9], [24, 14, 1], [14.89682, 100.39753], "โรงพยาบาลสิงห์บุรี"]\
           , 44 : [[44, 28, 16], [21, 19, 0], [15.19135, 100.12742], "โรงพยาบาลชัยนาท"]\
           , 45 : [[73, 63, 39], [46, 38, 5], [14.5337, 100.9147], "โรงพยาบาลสระบุรี"]\
           , 46 : [[32, 25, 17], [11, 9, 0], [14.5339, 100.9146], "โรงพยาบาลหนองแค"]\
           , 47 : [[79, 61, 29], [29, 22, 4], [13.35193, 100.98208], "โรงพยาบาลชลบุรี"]\
           , 48 : [[117, 77, 62], [78, 55, 13], [13.35193, 100.98208], "โรงพยาบาลบางละมุง"]\
           , 49 : [[28, 20, 12], [13, 11, 2], [13.45993, 101.17273], "โรงพยาบาลพนัสนิคม"]\
           , 50 : [[34, 24, 22], [14, 11, 3], [13.4693, 101.0987], "โรงพยาบาลพานทอง"]\
           , 51 : [[90, 64, 43], [41, 34, 4], [12.68226, 101.27624], "โรงพยาบาลระยอง"]\
           , 52 : [[22, 21, 14], [1, 1, 0], [12.4613, 102.2258], "โรงพยาบาลขลุง"]\
           , 53 : [[17, 7, 4], [7, 3, 0], [12.9048, 102.2632], "โรงพยาบาลโป่งน้ำร้อน"]\
           , 54 : [[9, 6, 4], [5, 5, 0], [13.1325, 102.2051], "โรงพยาบาลสอยดาว"]\
           , 55 : [[23, 17, 13], [8, 5, 3], [12.2482, 102.5122], "โรงพยาบาลตราด"]\
           , 56 : [[9, 7, 3], [7, 6, 0], [13.3845, 101.6947], "โรงพยาบาลท่าตะเกียบ"]\
           , 57 : [[17, 14, 8], [19, 19, 1], [13.7475, 101.3623], "โรงพยาบาลพนมสารคาม"]\
           , 58 : [[22, 19, 12], [5, 5, 0], [13.6465, 101.4412], "โรงพยาบาลสนามชัยเขต"]\
           , 59 : [[36, 25, 19], [21, 11, 4], [14.2079, 101.2128], "โรงพยาบาลนครนายก"]\
           , 60 : [[10, 10, 7], [5, 4, 0], [14.1501, 101.2679], "โรงพยาบาลปากพลี"]\
           , 61 : [[20, 11, 14], [9, 7, 0], [13.6527, 102.0978], "โรงพยาบาลเขาฉกรรจ์"]\
           , 62 : [[23, 17, 9], [7, 7, 0], [14.0072, 102.8023], "โรงพยาบาลตาพระยา"]\
           , 63 : [[26, 24, 14], [10, 8, 3], [13.7624, 102.3265], "โรงพยาบาลวัฒนานคร"]\
           , 64 : [[14, 13, 7], [3, 2, 0], [14.96545, 101.94790], "โรงพยาบาลขามทะเลสอ"]\
           , 65 : [[22, 15, 9], [14, 13, 1], [14.5279, 102.2480], "โรงพยาบาลครบุรี"]\
           , 66 : [[42, 20, 22], [17, 10, 3], [14.7339, 102.1574], "โรงพยาบาลโชคชัย"]\
           , 67 : [[48, 31, 21], [19, 11, 0], [14.7448, 102.0324], "โรงพยาบาลปักธงชัย"]\
           , 68 : [[13, 11, 7], [1, 0, 0], [14.4173, 101.8632], "โรงพยาบาลวังน้ำเขียว"]\
           , 69 : [[34, 23, 17], [18, 13, 1], [14.8724, 101.7220], "โรงพยาบาลสีคิ้ว"]\
           , 70 : [[15, 11, 8], [12, 12, 5], [14.7396, 102.3686], "โรงพยาบาลหนองบุนนาก"]\
           , 71 : [[80, 65, 47], [44, 36, 11], [14.8773/103.5034], "โรงพยาบาลสุรินทร์"]\
           , 72 : [[19, 17, 10], [7, 7, 2], [14.8658, 104.0379], "โรงพยาบาลปรางค์กู่"]\
           , 73 : [[59, 43, 29], [34, 21, 3], [15.1158, 104.3202], "โรงพยาบาลศรีสะเกษ"]\
           , 74 : [[35, 32, 23], [18, 15, 3], [15.7820, 104.1611], "โรงพยาบาลยโสธร"]\
           , 75 : [[22, 21, 5], [13, 10, 0], [15.8637, 104.6238], "โรงพยาบาลอำนาจเจริญ"]\
           , 76 : [[42, 34, 22], [12, 6, 2], [16.9660, 102.2816], "โรงพยาบาลศรีบุญเรือง"]\
           , 77 : [[41, 34, 27], [13, 11, 3], [17.1974, 102.4578], "โรงพยาบาลหนองบัวลำภู"]\
           , 78 : [[104, 78, 37], [53, 36, 7], [16.42851, 102.84500], "โรงพยาบาลขอนแก่น"]\
           , 79 : [[17, 14, 14], [7, 6, 7], [16.05870, 102.73042], "โรงพยาบาลบ้านไผ่"]\
           , 80 : [[94, 81, 52], [35, 29, 3], [17.4160, 102.7804], "โรงพยาบาลอุดรธานี"]\
           , 81 : [[35, 24, 17], [20, 14, 2], [17.2827, 101.7559], "โรงพยาบาลวังสะพุง"]\
           , 82 : [[62, 51, 30], [26, 20, 5], [17.88733, 102.75722], "โรงพยาบาลหนองคาย"]\
           , 83 : [[36, 30, 21], [6, 4, 2], [16.1809, 103.2986], "โรงพยาบาลมหาสารคาม"]\
           , 84 : [[18, 15, 11], [1, 1, 0], [16.0479, 103.6529], "โรงพยาบาลร้อยเอ็ด"]\
           , 85 : [[39, 32, 20], [11, 4, 1], [16.4351, 103.5052], "โรงพยาบาลกาฬสินธุ์"]\
           , 86 : [[41, 34, 22], [23, 21, 2], [16.7101, 103.7525], "โรงพยาบาลสมเด็จ"]\
           , 87 : [[7, 5, 4], [6, 6, 1], [16.99219, 104.16035], "โรงพยาบาลเต่างอย"]\
           , 88 : [[32, 30, 22], [17, 16, 0], [17.6235, 103.7506], "โรงพยาบาลวานรนิวาส"]\
           , 89 : [[11, 8, 9], [4, 3, 0], [17.5540, 104.6132], "โรงพยาบาลท่าอุเทน"]\
           , 90 : [[20, 17, 13], [5, 5, 3], [17.4915, 104.0958], "โรงพยาบาลนาหว้า"]\
           , 91 : [[26, 23, 13], [15, 8, 3], [17.6278, 104.2517], "โรงพยาบาลศรีสงคราม"]\
           , 92 : [[16, 16, 12], [11, 11, 3], [18.40639, 98.67434], "โรงพยาบาลจอมทอง"]\
           , 93 : [[11, 9, 3], [2, 2, 1], [19.7055, 99.1369], "โรงพยาบาลไชยปราการ"]\
           , 94 : [[34, 29, 22], [15, 9, 2], [18.86869, 99.12888], "โรงพยาบาลดอยสะเก็ด"]\
           , 95 : [[46, 41, 33], [20, 16, 4], [19.91321, 99.20670], "โรงพยาบาลฝาง"]\
           , 96 : [[40, 30, 24], [42, 29, 8], [18.7892, 98.9753], "โรงพยาบาลมหาราชนครเชียงใหม่"]\
           , 97 : [[25, 23, 12], [13, 12, 0], [18.81270, 98.99102], "โรงพยาบาลล้านนา เชียงใหม่"]\
           , 98 : [[26, 25, 14], [15, 13, 4], [18.5950, 98.8862], "โรงพยาบาลสันป่าตอง"]\
           , 99 : [[33, 27, 23], [11, 10, 4], [18.6809, 98.9185], "โรงพยาบาลหางดง"]\
           , 100 : [[20, 18, 12], [12, 11, 1], [18.4459, 98.8883], "โรงพยาบาลป่าซาง"]\
           , 101 : [[55, 50, 33], [25, 21, 1], [18.58190, 98.99451], "โรงพยาบาลลำพูน"]\
           , 102 : [[71, 61, 39], [32, 27, 8], [18.28654, 99.50721], "โรงพยาบาลลำปาง"]\
           , 103 : [[19, 17, 12], [14, 11, 1], [19.17353, 100.00667], "โรงพยาบาลดอกคำใต้"]\
           , 104 : [[48, 40, 34], [18, 15, 5], [19.1901, 99.8773], "โรงพยาบาลพะเยา"]\
           , 105 : [[77, 68, 43], [40, 33, 8], [19.9004, 99.8273], "โรงพยาบาลเชียงรายประชานุเคราะห์"]\
           , 106 : [[35, 27, 20], [10, 8, 1], [20.42909, 99.87866], "โรงพยาบาลแม่สาย"]\
           , 107 : [[55, 38, 20], [36, 24, 3], [15.70696, 100.13846], "โรงพยาบาลสวรรค์ประชารักษ์"]\
           , 108 : [[55, 48, 32], [26, 21, 4], [16.8729, 99.1319], "โรงพยาบาลสมเด็จพระเจ้าตากสินมหาราช"]\
           , 109 : [[19, 14, 8], [12, 12, 0], [17.0106, 99.7957], "โรงพยาบาลสุโขทัย"]\
           , 110 : [[21, 21, 4], [9, 9, 1], [8.8411, 99.3683], "โรงพยาบาลบ้านนาสาร"]\
           , 111 : [[44, 36, 14], [19, 12, 0], [9.1233, 99.3099], "โรงพยาบาลสุราษฎร์ธานี"]\
           , 112 : [[51, 41, 30], [32, 23, 2], [10.4982, 99.1864], "โรงพยาบาลชุมพร"]\
           , 113 : [[70, 45, 18], [39, 23, 2], [7.14118, 100.56518], "โรงพยาบาลสงขลา"]\
           , 114 : [[88, 55, 39], [50, 29, 5], [7.01654, 100.46756], "โรงพยาบาลหาดใหญ่"]\
           , 115 : [[13, 8, 6], [17, 14, 1], [6.6183, 100.0712], "โรงพยาบาลสตูล"]\
           , 116 : [[29, 17, 12], [12, 5, 1], [7.6143, 100.0743], "โรงพยาบาลพัทลุง"]\
           , 117 : [[28, 23, 8], [15, 14, 2], [6.86913, 101.24949], ["โรงพยาบาลปัตตานี"]]\
           , 118 : [[23, 20, 7], [9, 9, 1], [5.7733, 101.0833], ["โรงพยาบาลเบตง"]]\
           , 119 : [[25, 23, 4], [11, 8, 0], [6.54800, 101.27684], ["โรงพยาบาลยะลา"]]\
           , 120 : [[8, 8, 3], [10, 9, 1], [6.2968, 101.7258], ["โรงพยาบาลระแงะ"]]}

def chart(name, hs):
    """13.71888 100.52578"""
    chart = multiBarChart(width=250, height=150, x_axis_format=None)
    xdata = ['จำนวนทั้งหมด', 'ไม่สวมหมวก', 'ดื่มสุรา']
    ydata1 = list_hs[hs][0]
    ydata2 = list_hs[hs][1]
    chart.add_serie(name="ชาย", y=ydata1, x=xdata)
    chart.add_serie(name="หญิง", y=ydata2, x=xdata)
    chart.buildhtml()
    file_name = name + ".html"
    text_file = open(file_name, "w")
    text_file.write(chart.htmlcontent)
    print(chart.htmlcontent)
    text_file.close()
    return file_name

def bulid_map_54():
    """Buile html for thailand map."""
# [ละติจูด,ลองติดจูด] และการซูมลำดับ 5
map_osm = folium.Map(location=[15.0000, 100.0000], zoom_start=7)
for number in range(1, len(list_hs)+1):
    map_osm.polygon_marker(location=list_hs[number][2], popup=list_hs[number][3]+"<iframe frameBorder='0' src='"+chart("Output", number)+"'></iframe>",
                         fill_color='#FF0000', num_sides=3, radius=10, rotation=60)
map_osm.create_map(path='thailandmap_54.html')
