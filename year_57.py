"""ข้อมูลปีพุทธกาล 2557"""

import webbrowser
import folium
from nvd3 import multiBarChart

list_hs ={1: [[38, 32, 24], [7, 5, 4], [18.920459, 98.992126], 'โรงพยาบาลสันทราย'], 2: [[6, 2, 4], [3, 3, 0], [16.090665, 102.619365], 'โรงพยาบาลชนบท']
, 3: [[24, 18, 8], [9, 8, 0], [13.53646, 99.965171], 'โรงพยาบาลดำเนินสะดวก'], 4: [[7, 3, 3], [1, 1, 0], [15.004599, 103.111934], 'โรงพยาบาลเอกชนบุรีรัมย์']
, 5: [[7, 7, 2], [4, 4, 0], [7.976007, 99.632119], 'โรงพยาบาลรัษฏา'], 6: [[50, 46, 13], [36, 31, 2], [10.49748, 99.186208], 'โรงพยาบาลชุมพร']
, 7: [[10, 10, 4], [13, 12, 0], [8.469568, 99.080451], 'โรงพยาบาลชัยบุรี'], 8: [[0, 0, 0], [0, 0, 0], [9.148082, 99.333046], 'โรงพยาบาลทักษิณ']
, 9: [[29, 24, 14], [15, 10, 1], [13.28292, 101.41989], 'โรงพยาบาลบ่อทอง'], 10: [[16, 8, 3], [5, 2, 0], [13.168789, 100.92801], 'โรงพยาบาลพญาไทศรีราชา']
, 11: [[19, 9, 5], [7, 3, 0], [17.637699, 99.240057], 'โรงพยาบาลเถิน'], 12: [[37, 27, 17], [19, 17, 3], [13.115932, 100.918839], 'โรงพยาบาลอ่าวอุดม']
, 13: [[11, 9, 3], [2, 2, 0], [7.349007, 100.322283], 'โรงพยาบาลปากพะยูน'], 14: [[15, 13, 5], [4, 2, 1], [18.025252, 103.303296], 'โรงพยาบาลเฝ้าไร่']
, 15: [[0, 0, 0], [0, 0, 0], [13.707272, 100.289484], 'โรงพยาบาลศรีวิชัย3'], 16: [[46, 38, 12], [35, 27, 0], [9.123518, 99.310171], 'โรงพยาบาลสุราษฎร์ธานี']
, 17: [[0, 0, 0], [0, 0, 0], [14.073979, 101.371405], 'โรงพยาบาลค่ายจักรพงษ์'], 18: [[12, 9, 10], [0, 0, 0], [15.878995, 102.910406], 'โรงพยาบาลเปือยน้อย']
, 19: [[1, 0, 0], [0, 0, 0], [14.095035, 100.727125], 'โรงพยาบาลคลองหลวง'], 20: [[21, 15, 10], [8, 5, 1], [17.487771, 101.723753], 'โรงพยาบาลเลย']
, 21: [[15, 11, 5], [8, 5, 0], [8.056884, 99.000305], 'โรงพยาบาลเหนือคลอง'], 22: [[31, 24, 13], [16, 6, 1], [14.8966, 100.39767], 'โรงพยาบาลสิงห์บุรี']
, 23: [[11, 10, 5], [2, 2, 0], [13.852694, 99.408813], 'โรงพยาบาลด่านมะขามเตี้ย'], 24: [[6, 5, 3], [2, 1, 2], [12.770828, 102.033594], 'โรงพยาบาลเขาสุกิม']
, 25: [[7, 3, 0], [13, 11, 0], [7.456231, 100.444472], 'โรงพยาบาลสทิงพระ'], 26: [[52, 44, 35], [21, 19, 5], [16.966112, 102.281689], 'โรงพยาบาลศรีบุญเรือง']
, 27: [[8, 8, 3], [6, 6, 0], [14.650294, 100.408813], 'โรงพยาบาลโพธิ์ทอง'], 28: [[5, 2, 4], [0, 0, 0], [14.728484, 103.15478], 'โรงพยาบาลพลับพลาชัย']
, 29: [[9, 5, 5], [6, 6, 3], [19.335605, 100.134544], 'โรงพยาบาลจุน'], 30: [[28, 25, 9], [19, 19, 1], [5.773771, 101.081852], 'โรงพยาบาลเบตง']
, 31: [[10, 8, 6], [0, 0, 0], [13.884295, 100.611748], 'โรงพยาบาลทุ่งช้าง'], 32: [[3, 0, 1], [0, 0, 0], [15.312301, 105.125045], 'โรงพยาบาลตาลสุม']
, 33: [[1, 0, 0], [0, 0, 0], [19.077588, 98.315293], 'โรงพยาบาลวัดจันทร์'], 34: [[7, 6, 4], [6, 2, 0], [15.345141, 102.914089], 'โรงพยาบาลสำทะเมนชัย']
, 35: [[24, 17, 5], [4, 3, 0], [14.585087, 100.451927], 'โรงพยาบาลอ่างทอง'], 36: [[0, 0, 0], [0, 0, 0], [16.060908, 103.649752], 'โรงพยาบาลหลักเมือง']
, 37: [[17, 12, 9], [4, 4, 1], [18.461935, 99.129666], 'โรงพยาบาลแม่ทา'], 38: [[15, 8, 1], [5, 2, 1], [14.985543, 102.093165], 'โรงพยาบาลเซนต์เมรี']
, 39: [[18, 12, 11], [14, 11, 0], [15.025951, 103.935714], 'โรงพยาบาลสำโรงทาบ'], 40: [[2, 1, 2], [3, 1, 1], [13.912177, 100.498065], 'โรงพยาบาลปากเกร็ดเวชการ']
, 41: [[4, 4, 3], [0, 0, 0], [17.712, 102.208861], 'โรงพยาบาลน้ำโสม'], 42: [[6, 3, 3], [0, 0, 0], [18.27961, 103.986783], 'โรงพยาบาลบุ่งคล้า']
, 43: [[26, 24, 20], [7, 6, 1], [17.054843, 104.678343], 'โรงพยาบาลเรณูนคร'], 44: [[5, 4, 4], [2, 2, 1], [13.155872, 101.377375], 'โรงพยาบาลหนองใหญ่']
, 45: [[13, 13, 7], [2, 2, 0], [15.813813, 102.39044], 'โรงพยาบาลแวงน้อย'], 46: [[4, 1, 2], [1, 0, 0], [15.439649, 101.68822], 'โรงพยาบาลบำเหน็จณรงค์']
, 47: [[37, 23, 20], [17, 12, 1], [16.541643, 104.726904], 'โรงพยาบาลมุกดาหาร'], 48: [[2, 2, 2], [0, 0, 0], [17.472354, 103.261181], 'โรงพยาบาลทุ่งฝน']
, 49: [[2, 2, 1], [5, 4, 1], [6.081901, 101.877341], 'โรงพยาบาลสุไหงปาดี'], 50: [[5, 4, 2], [7, 5, 0], [17.674017, 102.752616], 'โรงพยาบาลสระใคร']
, 51: [[8, 6, 3], [1, 1, 0], [16.406089, 102.343507], 'โรงพยาบาลบ้านแท่น'], 52: [[3, 1, 0], [0, 0, 0], [9.789286, 98.776882], 'โรงพยาบาลพะโต๊ะ']
, 53: [[6, 6, 0], [3, 3, 0], [6.839896, 101.486343], 'โรงพยาบาลปะนาเระ'], 54: [[4, 4, 3], [0, 0, 0], [14.756773, 105.410159], 'โรงพยาบาลบุณฑริก']
, 55: [[3, 3, 1], [0, 0, 0], [13.126923, 99.709371], 'โรงพยาบาลหนองหญ้าปล้อง'], 56: [[46, 36, 22], [18, 16, 0], [13.691166, 102.502583], 'โรงพยาบาลอรัญประเทศ']
, 57: [[13, 12, 8], [6, 5, 1], [17.578554, 104.018704], 'โรงพยาบาลอากาศอำนวย'], 58: [[24, 20, 10], [14, 11, 0], [16.435133, 100.344522], 'โรงพยาบาลพิจิตร']
, 59: [[0, 0, 0], [0, 0, 0], [13.384513, 99.990978], 'โรงพยาบาลแม่กลอง'], 60: [[20, 13, 15], [4, 1, 1], [15.391733, 99.851165], 'โรงพยาบาลหนองฉาง']
, 61: [[28, 20, 16], [21, 15, 0], [14.207941, 101.213871], 'โรงพยาบาลนครนายก'], 62: [[0, 0, 0], [0, 0, 0], [7.000551, 100.48037], 'โรงพยาบาลราษฎรยินดี']
, 63: [[10, 2, 4], [3, 1, 0], [12.564023, 99.959453], 'โรงพยาบาลซานเปาโลหัวหิน'], 64: [[11, 5, 5], [4, 2, 0], [14.985138, 102.104054], 'โรงพยาบาลนครราชสีมา']
, 65: [[8, 7, 5], [4, 4, 0], [13.706781, 100.300792], 'โรงพยาบาลมหาชัย2กระทุ่มแบน'], 66: [[8, 7, 2], [7, 7, 0], [14.754153, 100.074871], 'โรงพยาบาลสามชุก']
, 67: [[4, 4, 0], [2, 2, 0], [6.295854, 101.729587], 'โรงพยาบาลเจาะไอร้อง'], 68: [[3, 1, 0], [2, 2, 0], [6.719902, 101.418074], 'โรงพยาบาลมายอ']
, 69: [[15, 14, 8], [8, 8, 3], [16.756577, 102.632459], 'โรงพยาบาลอุบลรัตน์'], 70: [[16, 13, 10], [9, 7, 0], [8.446277, 99.532948], 'โรงพยาบาลฉวาง']
, 71: [[6, 4, 3], [1, 1, 0], [16.298262, 99.813949], 'โรงพยาบาลทรายทองวัฒนา'], 72: [[38, 27, 24], [14, 10, 0], [14.566062, 100.723524], 'โรงพยาบาลท่าเรือ']
, 73: [[18, 16, 10], [5, 4, 0], [19.299956, 97.971291], 'โรงพยาบาลศรีสังวาลย์'], 74: [[49, 38, 39], [11, 11, 2], [17.694459, 102.461976], 'โรงพยาบาลบ้านผือ']
, 75: [[7, 4, 1], [10, 9, 0], [14.16569, 100.299374], 'โรงพยาบาลลาดบัวหลวง'], 76: [[18, 15, 4], [10, 8, 0], [12.209587, 99.858384], 'โรงพยาบาลสามร้อยยอด']
, 77: [[8, 7, 6], [1, 1, 0], [19.146648, 99.616663], 'โรงพยาบาลวังเหนือ'], 78: [[45, 35, 26], [17, 14, 0], [13.459977, 101.172913], 'โรงพยาบาลพนัสนิคม']
, 79: [[11, 11, 8], [2, 2, 0], [17.089578, 103.821354], 'โรงพยาบาลกุดบาก'], 80: [[6, 4, 1], [5, 2, 0], [15.674075, 100.126867], 'โรงพยาบาลค่ายจิรประวัติ']
, 81: [[35, 18, 9], [21, 6, 0], [7.132738, 100.253101], 'โรงพยาบาลรัตภูมิ'], 82: [[37, 31, 21], [10, 8, 0], [17.623925, 103.749913], 'โรงพยาบาลวานรนิวาส']
, 83: [[6, 4, 1], [5, 1, 0], [15.10521, 100.264074], 'โรงพยาบาลสรรพยา'], 84: [[17, 7, 5], [6, 4, 0], [16.375475, 102.12884], 'โรงพยาบาลภูเขียว']
, 85: [[32, 27, 18], [12, 10, 2], [16.2945, 103.970308], 'โรงพยาบาลโพนทอง'], 86: [[88, 76, 61], [49, 42, 8], [19.901057, 99.828701], 'โรงพยาบาลเชียงรายประชานุเคราะห์']
, 87: [[1, 0, 0], [0, 0, 0], [14.102776, 99.939159], 'โรงพยาบาลจันทรุเบกษา'], 88: [[27, 25, 13], [14, 11, 3], [16.651685, 102.379835], 'โรงพยาบาลภูเวียง']
, 89: [[24, 22, 14], [7, 6, 0], [20.240064, 100.409857], 'โรงพยาบาลเชียงของ'], 90: [[11, 6, 9], [4, 3, 1], [17.226271, 99.048791], 'โรงพยาบาลสามเงา']
, 91: [[93, 74, 50], [46, 36, 6], [16.42916, 102.848114], 'โรงพยาบาลขอนแก่น'], 92: [[4, 2, 3], [5, 4, 1], [13.695299, 101.051569], 'โรงพยาบาลโสธราเวช']
, 93: [[0, 0, 0], [2, 2, 0], [14.442463, 99.129091], 'โรงพยาบาลท่ากระดาน'], 94: [[46, 33, 22], [18, 17, 2], [14.527515, 102.246214], 'โรงพยาบาลครบุรี']
, 95: [[32, 15, 16], [14, 10, 1], [12.718345, 101.126416], 'โรงพยาบาลมาบตาพุด'], 96: [[8, 8, 4], [4, 4, 0], [17.859993, 103.767342], 'โรงพยาบาลคำตากล้า']
, 97: [[74, 50, 27], [39, 27, 2], [7.142202, 100.56623], 'โรงพยาบาลสงขลา'], 98: [[15, 15, 13], [8, 8, 2], [20.271844, 100.077072], 'โรงพยาบาลเชียงแสน']
, 99: [[2, 2, 1], [2, 2, 0], [13.987648, 100.610198], 'โรงพยาบาลปทุมเวช'], 100: [[14, 12, 12], [7, 7, 4], [17.270706, 102.597954], 'โรงพยาบาลหนองวัวซอ']}

def chart(name, hs):
    """13.71888 100.52578"""
    chart = multiBarChart(width=250, height=150, x_axis_format=None)
    xdata = ['จำนวนทั้งหมด', 'ไม่สวมหมวก', 'ดื่มสุรา']
    ydata1 = list_hs[hs][0]
    ydata2 = list_hs[hs][1]
    chart.add_serie(name="ชาย", y=ydata1, x=xdata)
    chart.add_serie(name="หญิง", y=ydata2, x=xdata)
    chart.buildhtml()
    file_name = name + str(hs) + ".html"
    text_file = open(file_name, "w")
    text_file.write(chart.htmlcontent)
    print(chart.htmlcontent)
    text_file.close()
    return file_name

def bulid_map_57():
    """Buile html for thailand map."""
# [ละติจูด,ลองติดจูด] และการซูมลำดับ 5
map_osm = folium.Map(location=[15.0000, 100.0000], zoom_start=7)
for number in range(1, len(list_hs)+1):
    map_osm.polygon_marker(location=list_hs[number][2], popup=list_hs[number][3]+"<iframe frameBorder='0' src='"+chart("Output", number)+"'></iframe>",
                         fill_color='#FF0000', num_sides=3, radius=10, rotation=60)
map_osm.create_map(path='thailandmap_57.html')
