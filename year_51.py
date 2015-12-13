"""ข้อมูลปีพุทธกาล 2551"""

import webbrowser
import folium
from nvd3 import multiBarChart

list_hs = {1: [[8, 5, 3], [11, 9, 1], [14.566062, 100.723524], 'โรงพยาบาลท่าเรือ']\
, 2: [[36, 31, 17], [40, 31, 1], [13.117891, 99.93869], 'โรงพยาบาลพระจอมเกล้า']\
, 3: [[7, 7, 4], [6, 2, 1], [16.80994, 100.259556], 'โรงพยาบาลรวมแพทย์']\
, 4: [[10, 7, 4], [7, 6, 1], [13.634144, 100.709816], 'โรงพยาบาลจุฬารัตน์']\
, 5: [[15, 10, 10], [3, 2, 1], [13.912177, 100.498065], 'โรงพยาบาลปากเกร็ดเวชการ']\
, 6: [[15, 14, 14], [6, 6, 2], [16.95783, 102.890536], 'โรงพยาบาลโนนสะอาด']\
, 7: [[53, 38, 35], [17, 16, 6], [13.115932, 100.918839], 'โรงพยาบาลอ่าวอุดม']\
, 8: [[38, 33, 15], [18, 18, 0], [8.645874, 99.940802], 'โรงพยาบาลท่าศาลา']\
, 9: [[26, 8, 8], [13, 0, 0], [17.879431, 99.339879], 'โรงพยาบาลสบปราบ']\
, 10: [[11, 7, 8], [5, 2, 0], [15.236071, 104.865344], 'โรงพยาบาลสรรพสิทธิประสงค์']\
, 11: [[7, 7, 4], [1, 1, 0], [9.318233, 99.695167], 'โรงพยาบาลดอนสัก']\
, 12: [[5, 5, 4], [0, 0, 0], [14.5215, 105.2432], 'โรงพยาบาลนาจะหลวย']\
, 13: [[20, 19, 15], [7, 7, 2], [18.00853, 103.708413], 'โรงพยาบาลพรเจริญ']\
, 14: [[8, 6, 6], [1, 1, 1], [16.991744, 104.16064], 'โรงพยาบาลเต่างอย']\
, 15: [[2, 2, 0], [3, 3, 0], [13.7140, 100.5775], 'โรงพยาบาลเทพธารินทร']\
, 16: [[7, 7, 4], [1, 1, 0], [18.056445, 102.28037], 'โรงพยาบาลสังคม']\
, 17: [[20, 15, 10], [11, 10, 0], [13.845751, 100.410695], 'โรงพยาบาลบางใหญ่']\
, 18: [[4, 2, 1], [3, 1, 0], [6.839896, 101.486343], 'โรงพยาบาลปะนาเระ']\
, 19: [[10, 9, 4], [8, 8, 0], [6.297097, 101.726715], 'โรงพยาบาลระแงะ']\
, 20: [[13, 11, 7], [8, 8, 0], [18.56547, 100.727102], 'โรงพยาบาลเวียงสา']\
, 21: [[12, 10, 7], [1, 1, 0], [16.017741, 98.866285], 'โรงพยาบาลอุ้มผาง']\
, 22: [[23, 18, 15], [4, 3, 1], [17.449557, 101.353932], 'โรงพยาบาลภูเรือ']\
, 23: [[1, 1, 0], [1, 1, 0], [17.632355, 100.100854], 'โรงพยาบาลลับแล']\
, 24: [[17, 14, 9], [2, 1, 0], [16.158901, 100.603648], 'โรงพยาบาลทับคล้อ']\
, 25: [[15, 4, 3], [2, 0, 1], [13.7429, 100.5946], 'โรงพยาบาลเพชรเวช']\
, 26: [[11, 6, 5], [3, 2, 0], [14.004233, 100.554576], 'โรงพยาบาลกรุงสยามเนต์คาร์ลอส']\
, 27: [[26, 10, 17], [12, 5, 2], [7.906692, 98.390681], 'โรงพยาบาลมิชชั่นภูเก็ต']\
, 28: [[21, 17, 11], [7, 7, 0], [8.834682, 99.160655], 'โรงพยาบาลเคียนซา']\
, 29: [[11, 3, 5], [10, 6, 0], [16.809878, 100.259567], 'โรงพยาบาลรวมแพทย์พิษณุโลก']\
, 30: [[15, 11, 8], [5, 2, 0], [16.805814, 100.254964], 'โรงพยาบาลอินเตอร์เวชการ']\
, 31: [[2, 1, 1], [3, 3, 1], [17.835291, 103.080193], 'โรงพยาบาลสร้างคอม']\
, 32: [[44, 43, 26], [23, 21, 1], [19.518153, 100.29685], 'โรงพยาบาลเชียงคำ']\
, 33: [[5, 5, 1], [6, 4, 2], [18.185919, 103.737752], 'โรงพยาบาลศรีวิไล']\
, 34: [[2, 2, 0], [1, 1, 0], [6.170912, 101.178412], 'โรงพยาบาลธารโต']\
, 35: [[13, 10, 7], [4, 4, 0], [15.065094, 101.123541], 'โรงพยาบาลท่าหลวง']\
, 36: [[9, 7, 5], [3, 3, 0], [6.250866, 102.046226], 'โรงพยาบาลตากใบ']\
, 37: [[16, 15, 7], [4, 4, 0], [16.797436, 102.187947], 'โรงพยาบาลสีชมพู']\
, 38: [[9, 5, 4], [6, 3, 0], [15.577877, 99.862664], 'โรงพยาบาลสว่างอารมณ์']\
, 39: [[8, 5, 5], [4, 3, 0], [15.608631, 102.125576], 'โรงพยาบาลบ้านเหลื่อม']\
, 40: [[19, 18, 7], [8, 7, 1], [14.584071, 99.770313], 'โรงพยาบาลเลาขวัญ']\
, 41: [[30, 10, 16], [15, 6, 1], [14.878861, 101.828467], 'โรงพยาบาลสูงเนิน'],\
 42: [[8, 4, 3], [3, 3, 2], [13.66455, 100.602438], 'โรงพยาบาลมโนรมย์'],\
 43: [[71, 34, 31], [25, 13, 0], [13.8169, 100.6880], 'โรงพยาบาลนพรัตนราชธานี'],\
 44: [[68, 55, 50], [13, 11, 3], [16.778328, 101.236435], 'โรงพยาบาลหล่มสัก'],\
 45: [[5, 2, 0], [0, 0, 0], [13.7588006,100.4829159], 'โรงพยาบาลนิติเวชศริราช'],\
 46: [[29, 23, 20], [21, 19, 2], [13.691166, 102.502583], 'โรงพยาบาลอรัญประเทศ'],\
 47: [[11, 2, 2], [1, 0, 0], [13.8072, 100.5232], 'โรงพยาบาลบางโพ'],\
 48: [[3, 2, 1], [2, 1, 0], [14.585806, 100.625657], 'โรงพยาบาลดอนพุด'],\
 49: [[13, 12, 8], [4, 3, 2], [16.376248, 104.546429], 'โรงพยาบาลนิคมคำสร้อย'],\
 50: [[17, 15, 7], [13, 10, 3], [14.398315, 100.593795], 'โรงพยาบาลสมเด็จพระสังฆราช(นครหลวง)'],\
 51: [[19, 12, 9], [9, 5, 1], [14.398421, 100.166613], 'โรงพยาบาลบางปลาม้า'],\
 52: [[26, 23, 15], [13, 10, 0], [16.059608, 99.861274], 'โรงพยาบาลขาณุวรลักษบุรี'],\
 53: [[5, 5, 2], [3, 3, 0], [17.552094, 103.053453], 'โรงพยาบาลพิบูลย์รักษ์'],\
 54: [[25, 24, 18], [27, 22, 2], [16.134618, 102.534385], 'โรงพยาบาลมัญจาคีรี'],\
 55: [[9, 8, 3], [2, 1, 0], [7.092349, 99.766653], 'โรงพยาบาลทุ่งหว้า'],\
 56: [[5, 5, 5], [1, 0, 1], [15.336352, 104.045854], 'โรงพยาบาลบึงบูรพ์'],\
 57: [[5, 4, 1], [3, 3, 0], [18.278431, 100.179541], 'โรงพยาบาลหนองม่วงไข่'],\
 58: [[44, 37, 29], [12, 9, 3], [16.651685, 102.379835], 'โรงพยาบาลภูเวียง'],\
 59: [[11, 6, 6], [4, 4, 2], [13.694038, 99.92196], 'โรงพยาบาลบางแพ'],\
 60: [[38, 32, 16], [13, 11, 4], [15.068953, 100.738346], 'โรงพยาบาลโคกสำโรง'],\
 61: [[12, 9, 6], [9, 8, 2], [14.650294, 100.408813], 'โรงพยาบาลโพธิ์ทอง'],\
 62: [[50, 29, 23], [32, 23, 1], [10.49748, 99.186208], 'โรงพยาบาลชุมพร'],\
 63: [[28, 26, 14], [13, 10, 0], [6.635133, 100.406757], 'โรงพยาบาลสะเดา'],\
 64: [[40, 18, 16], [17, 6, 3], [13.892695, 100.509306], 'โรงพยาบาลชลประทาน'],\
 65: [[1, 1, 0], [1, 1, 0], [14.023272, 101.762719], 'โรงพยาบาลสถานพยาบาลโสธราเวช'],\
 66: [[5, 4, 3], [0, 0, 0], [17.352287, 103.856201], 'โรงพยาบาลพระอาจารย์ฝั้นอาจาโร'],\
 67: [[16, 10, 7], [11, 6, 2], [8.863767, 98.334406], 'โรงพยาบาลตะกั่วป่า'],\
 68: [[23, 20, 13], [6, 5, 2], [17.273254, 100.601302], 'โรงพยาบาลชาติตระการ'],\
 69: [[8, 5, 1], [6, 5, 2], [17.229771, 98.226164], 'โรงพยาบาลท่าสองยาง'],\
 70: [[13, 12, 0], [2, 2, 0], [14.754153, 100.074871], 'โรงพยาบาลสามชุก'],\
 71: [[16, 12, 10], [11, 9, 1], [13.132299, 102.20504], 'โรงพยาบาลสอยดาว'],\
 72: [[15, 10, 12], [5, 5, 0], [16.523859, 100.151558], 'โรงพยาบาลวชิรบารมี'],\
 73: [[24, 19, 11], [8, 5, 0], [18.162804, 97.939891], 'โรงพยาบาลแม่สะเรียง'],\
 74: [[42, 29, 26], [27, 18, 2], [13.817139, 102.072014], 'โรงพยาบาลสมเด็จพระยุพราชสระแก้ว'],\
 75: [[25, 19, 9], [25, 20, 0], [14.476882, 103.590472], 'โรงพยาบาลกาบเชิง'],\
 76: [[26, 26, 12], [7, 7, 1], [13.677395, 100.722301], 'โรงพยาบาลจุฬารัตน์9'],\
 77: [[80, 68, 30], [32, 29, 5], [14.342832, 100.560061], 'โรงพยาบาลพระนครศรีอยุธยา'],\
 78: [[5, 3, 2], [0, 0, 0], [13.7802, 100.4703], 'โรงพยาบาลเจ้าพระยา'],\
 79: [[5, 5, 0], [4, 4, 0], [12.564023, 99.959453], 'โรงพยาบาลซานเปาโลหัวหิน'],\
 80: [[13, 9, 9], [4, 3, 1], [9.258247, 99.187942], 'โรงพยาบาลท่าฉาง']}

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

def bulid_map_51():
    """Buile html for thailand map."""
# [ละติจูด,ลองติดจูด] และการซูมลำดับ 5
map_osm = folium.Map(location=[15.0000, 100.0000], zoom_start=7)
for number in range(1, len(list_hs)+1):
    map_osm.polygon_marker(location=list_hs[number][2], popup=list_hs[number][3]+"<iframe frameBorder='0' src='"+chart("Output", number)+"'></iframe>",
                         fill_color='#FF0000', num_sides=3, radius=10, rotation=60)
map_osm.create_map(path='thailandmap_51.html')
