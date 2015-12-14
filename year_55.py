"""ข้อมูลปีพุทธกาล 2555"""

import webbrowser
import folium
from nvd3 import multiBarChart

list_hs = {1: [[9, 8, 6], [4, 3, 1], [14.547984, 100.849938], 'โรงพยาบาลเสาไห้']\
            , 3: [[21, 9, 11], [13, 6, 0], [14.878861, 101.828467], 'โรงพยาบาลสูงเนิน']\
            , 4: [[21, 18, 6], [15, 13, 0], [14.348691, 99.872154], 'โรงพยาบาลอู่ทอง']\
            , 5: [[9, 8, 6], [3, 2, 0], [16.809878, 100.259567], 'โรงพยาบาลรวมแพทย์พิษณุโลก']\
            , 6: [[17, 10, 5], [15, 10, 0], [13.239197, 99.82468], 'โรงพยาบาลเขาย้อย']\
            , 7: [[20, 15, 5], [12, 9, 1], [13.53646, 99.965171], 'โรงพยาบาลดำเนินสะดวก']\
            , 8: [[4, 4, 0], [2, 2, 0], [16.765176, 101.674805], 'โรงพยาบาลน้ำหนาว']\
            , 9: [[14, 8, 4], [5, 3, 1], [15.706287, 100.130975], 'โรงพยาบาลศรีสวรรค์']\
            , 10: [[11, 0, 4], [9, 1, 1], [14.975982, 102.086531], 'โรงพยาบาลโคราชเมโมเรียล']\
            , 12: [[11, 6, 7], [2, 2, 0], [13.99546, 101.219046], 'โรงพยาบาลบ้านสร้าง']\
            , 13: [[9, 8, 1], [5, 4, 0], [9.008333, 99.903839], 'โรงพยาบาลสิชล']\
            , 14: [[11, 10, 4], [20, 19, 1], [8.364996, 99.800055], 'โรงพยาบาลลานสะกา']\
            , 15: [[23, 20, 12], [8, 8, 0], [13.132299, 102.20504], 'โรงพยาบาลสอยดาว']\
            , 16: [[23, 17, 10], [5, 3, 2], [15.866462, 100.592316], 'โรงพยาบาลหนองบัว']\
            , 17: [[12, 8, 4], [13, 10, 0], [9.161794, 99.492931], 'โรงพยาบาลกาญจนดิษฐ์']\
            , 18: [[94, 88, 49], [52, 40, 5], [17.414825, 102.780201], 'โรงพยาบาลอุดรธานี']\
            , 19: [[6, 6, 5], [2, 2, 0], [15.850829, 103.57166], 'โรงพยาบาลจตุรพักตรพิมาน']\
            , 20: [[54, 47, 33], [21, 18, 5], [19.518153, 100.29685], 'โรงพยาบาลเชียงคำ']\
            , 21: [[19, 14, 14], [6, 3, 0], [15.79756, 103.031674], 'โรงพยาบาลนาเชือก']\
            , 22: [[6, 1, 2], [4, 2, 0], [13.087674, 100.91745], 'โรงพยาบาลแหลมฉบังอินเตอร์เนชั่นแนล']\
            , 23: [[1, 0, 0], [1, 1, 0], [15.699812, 100.133519], 'โรงพยาบาลร่มฉัตร']\
            , 24: [[8, 7, 2], [7, 7, 1], [7.737105, 99.395517], 'โรงพยาบาลวังวิเศษ']\
            , 25: [[2, 1, 1], [1, 0, 0], [14.585806, 100.625657], 'โรงพยาบาลดอนพุด']\
            , 26: [[4, 4, 2], [1, 0, 0], [13.592682, 100.578108], 'โรงพยาบาลพระสมุทรเจดีย์']\
            , 27: [[1, 0, 0], [2, 1, 0], [16.833765, 100.244748], 'โรงพยาบาลค่ายสมเด็จพระนเรศวร']\
            , 28: [[12, 6, 6], [9, 4, 1], [13.59518, 100.600984], 'โรงพยาบาลเมืองสมทรปากน้ำ']\
            , 29: [[1, 1, 0], [0, 0, 0], [17.362102, 103.104525], 'โรงพยาบาลหนองหาน']\
            , 30: [[16, 8, 3], [7, 5, 0], [18.179448, 98.611803], 'โรงพยาบาลฮอด']\
            , 32: [[13, 9, 6], [8, 8, 0], [13.45019, 102.298896], 'โรงพยาบาลคลองหาด']\
            , 33: [[10, 7, 5], [3, 2, 2], [13.594138, 100.804839], 'โรงพยาบาลบางนา2']\
            , 34: [[6, 6, 2], [1, 1, 0], [15.19434, 100.842303], 'โรงพยาบาลสระโบสถ์']\
            , 37: [[9, 8, 4], [5, 3, 0], [18.49794, 98.364922], 'โรงพยาบาลแม่แจ่ม']\
            , 38: [[4, 3, 0], [0, 0, 0], [18.911013, 98.942887], 'โรงพยาบาลดารารัศมี']\
            , 40: [[0, 0, 0], [0, 0, 0], [14.520421, 100.915191], 'โรงพยาบาลมิตรภาพเมโมเรียล']\
            , 41: [[55, 43, 36], [24, 14, 0], [16.181373, 103.299023], 'โรงพยาบาลมหาสารคาม']\
            , 42: [[39, 31, 18], [19, 9, 0], [10.49748, 99.186208], 'โรงพยาบาลชุมพร']\
            , 43: [[16, 13, 6], [12, 11, 1], [8.841915, 99.367733], 'โรงพยาบาลบ้านนาสาร']\
            , 44: [[4, 2, 0], [9, 6, 0], [6.547894, 101.276422], 'โรงพยาบาลยะหา']\
            , 45: [[23, 18, 7], [8, 8, 0], [15.477501, 100.139215], 'โรงพยาบาลพยุหะคีรี']\
            , 46: [[17, 11, 8], [5, 2, 1], [13.082925, 99.945446], 'โรงพยาบาลเมืองเพชร']\
            , 47: [[15, 12, 8], [4, 3, 0], [14.85048, 102.69065], 'โรงพยาบาลหนองหงส์']\
            , 48: [[4, 4, 4], [1, 1, 0], [15.69573, 104.492419], 'โรงพยาบาลหัวตะพาน']\
            , 49: [[25, 21, 11], [6, 6, 1], [14.453919, 102.727217], 'โรงพยาบาลปะคำ']\
            , 50: [[36, 25, 18], [27, 13, 0], [12.68256, 101.27685], 'โรงพยาบาลระนอง']\
            , 51: [[10, 9, 3], [12, 10, 0], [9.757757, 99.085212], 'โรงพยาบาลละแม']\
            , 52: [[6, 5, 2], [3, 3, 0], [15.282259, 99.607291], 'โรงพยาบาลห้วยคต']\
            , 53: [[8, 8, 0], [10, 8, 0], [6.618147, 100.070241], 'โรงพยาบาลสตูล']\
            , 54: [[11, 10, 11], [2, 1, 1], [15.210446, 103.754882], 'โรงพยาบาลสนม']\
            , 55: [[18, 14, 8], [15, 15, 0], [15.740812, 102.269], 'โรงพยาบาลแก้งสนามนาง']\
            , 56: [[22, 21, 6], [13, 10, 0], [14.307915, 102.734332], 'โรงพยาบาลโนนดินแดง']\
            , 57: [[44, 32, 24], [20, 15, 3], [15.112228, 104.138182], 'โรงพยาบาลอุทุมพรพิสัย']\
            , 58: [[27, 26, 18], [2, 2, 0], [14.924735, 104.686388], 'โรงพยาบาลโนนคูณ']\
            , 59: [[20, 18, 6], [19, 13, 0], [11.487984, 99.60103], 'โรงพยาบาลทับสะแก']\
            , 60: [[4, 3, 1], [3, 2, 0], [7.717587, 99.87943], 'โรงพยาบาลศรีบรรพต']\
            , 61: [[48, 33, 18], [18, 13, 3], [13.115932, 100.918839], 'โรงพยาบาลอ่าวอุดม']\
            , 62: [[6, 4, 3], [0, 0, 0], [18.830623, 97.936807], 'โรงพยาบาลขุนยวม']\
            , 63: [[3, 3, 3], [4, 4, 1], [17.472354, 103.261181], 'โรงพยาบาลทุ่งฝน']\
            , 64: [[2, 2, 1], [0, 0, 0], [13.634144, 100.709816], 'โรงพยาบาลจุฬารัตน์']\
            , 65: [[3, 3, 1], [1, 1, 0], [16.538226, 103.076027], 'โรงพยาบาลซำสูง']\
            , 66: [[0, 0, 0], [0, 0, 0], [14.798359, 104.667708], 'โรงพยาบาลเบ็ญจลักษณ์เฉลิมพระเกียรติ']\
            , 67: [[5, 4, 1], [0, 0, 0], [8.469568, 99.080451], 'โรงพยาบาลชัยบุรี']\
            , 68: [[46, 36, 12], [35, 30, 1], [8.390617, 99.971126], 'โรงพยาบาลมหาราชนครศรีธรรมราช']\
            , 69: [[20, 17, 9], [10, 9, 1], [13.845751, 100.410695], 'โรงพยาบาลบางใหญ่']\
            , 70: [[1, 1, 0], [0, 0, 0], [15.378373, 105.029651], 'โรงพยาบาลดอนมดแดง']\
            , 71: [[1, 0, 0], [0, 0, 0], [17.698709, 102.909614], 'โรงพยาบาลเพ็ญ']\
            , 72: [[12, 12, 7], [2, 2, 0], [20.011483, 100.057895], 'โรงพยาบาลเวียงเชียงรุ้ง']\
            , 73: [[24, 20, 13], [13, 12, 6], [18.363753, 103.651541], 'โรงพยาบาลบึงกาฬ']\
            , 74: [[9, 8, 7], [5, 5, 1], [17.786885, 104.088492], 'โรงพยาบาลนาทม']\
            , 75: [[15, 5, 6], [3, 1, 0], [19.52345, 98.241714], 'โรงพยาบาลปางมะผ้า']\
            , 76: [[1, 1, 0], [0, 0, 0], [6.170912, 101.178412], 'โรงพยาบาลธารโต']\
            , 77: [[14, 9, 6], [5, 5, 0], [14.141203, 100.823802], 'โรงพยาบาลหนองเสือ']\
            , 78: [[1, 1, 1], [0, 0, 0], [17.038748, 102.931932], 'โรงพยาบาลห้วยเกิ้ง']\
            , 79: [[10, 9, 6], [7, 5, 1], [18.272023, 99.651994], 'โรงพยาบาลแม่เมาะ']\
            , 80: [[14, 14, 4], [3, 3, 0], [7.567698, 99.347508], 'โรงพยาบาลสิเกา']\
            , 81: [[3, 3, 0], [2, 0, 0], [13.912177, 100.498065], 'โรงพยาบาลปากเกร็ดเวชการ']\
            , 82: [[5, 3, 2], [1, 1, 0], [16.615269, 101.914517], 'โรงพยาบาลคอนสาร']\
            , 83: [[49, 43, 38], [6, 5, 1], [16.954274, 104.470382], 'โรงพยาบาลนาแก']\
            , 84: [[2, 2, 0], [2, 2, 0], [6.719902, 101.418074], 'โรงพยาบาลมายอ']\
            , 85: [[17, 13, 8], [11, 9, 2], [16.310231, 104.201093], 'โรงพยาบาลหนองพอก']\
            , 86: [[61, 42, 19], [27, 15, 1], [14.342832, 100.560061], 'โรงพยาบาลพระนครศรีอยุธยา']\
            , 87: [[13, 8, 8], [6, 5, 1], [15.043548, 100.142548], 'โรงพยาบาลสรรคบุรี']\
            , 88: [[62, 50, 15], [25, 22, 0], [12.786049, 101.671302], 'โรงพยาบาลแกลง']\
            , 89: [[8, 8, 4], [5, 5, 0], [16.596199, 103.229526], 'โรงพยาบาลห้วยเม็ก']\
            , 90: [[0, 0, 0], [0, 0, 0], [7.563889, 99.617225], 'โรงพยาบาลวัฒนแพทย์']\
            , 91: [[7, 4, 0], [5, 3, 0], [8.455814, 99.966805], 'โรงพยาบาลนครินทร์']\
            , 92: [[6, 3, 4], [5, 5, 0], [14.564876, 102.932022], 'โรงพยาบาลเฉลิมพระเกียรติ']\
            , 93: [[15, 8, 8], [6, 3, 1], [16.759336, 100.118714], 'โรงพยาบาลบางระกำ']\
            , 94: [[7, 5, 2], [7, 6, 0], [14.98512, 102.103985], 'โรงพยาบาลมหาราช']\
            , 95: [[13, 12, 9], [7, 6, 2], [16.068989, 104.433312], 'โรงพยาบาลไทยเจริญ']\
            , 96: [[5, 4, 4], [0, 0, 0], [14.479134, 104.98458], 'โรงพยาบาลน้ำยืน']\
            , 97: [[0, 0, 0], [0, 0, 0], [14.225682, 100.027899], 'โรงพยาบาลสมเด็จพระสังฆราชองค์ที่']\
            , 98: [[4, 3, 3], [1, 0, 1], [15.736519, 101.773483], 'โรงพยาบาลหนองบัวระเหว']\
            , 99: [[9, 9, 8], [0, 0, 0], [17.089578, 103.821354], 'โรงพยาบาลกุดบาก']\
            , 100: [[35, 25, 22], [15, 11, 4], [16.541643, 104.726904], 'โรงพยาบาลมุกดาหาร']\
            , 101: [[5, 3, 2], [4, 4, 0], [13.126923, 99.709371], 'โรงพยาบาลหนองหญ้าปล้อง']\
            , 102: [[23, 22, 13], [12, 9, 1], [15.103853, 104.573146], 'โรงพยาบาลกันทรารมย์']\
            , 103: [[23, 18, 13], [12, 9, 0], [16.10308, 100.247504], 'โรงพยาบาลโพทะเล']\
            , 104: [[0, 0, 0], [0, 0, 0], [16.817895, 100.271728], 'โรงพยาบาลรัตนเวช']\
            , 105: [[6, 6, 4], [1, 0, 0], [17.265987, 103.63418], 'โรงพยาบาลวาริชภูมิ']\
            , 106: [[42, 34, 19], [30, 23, 2], [14.723842, 100.800725], 'โรงพยาบาลพระพุทธบาท']\
            , 107: [[29, 25, 4], [14, 14, 1], [14.321096, 100.38792], 'โรงพยาบาลเสนา']\
            , 108: [[4, 3, 3], [2, 2, 0], [17.185045, 103.715394], 'โรงพยาบาลนิคมน้ำอูน']\
            , 109: [[11, 10, 7], [2, 2, 0], [15.71326, 103.233157], 'โรงพยาบาลนาดูน']\
            , 110: [[29, 18, 7], [10, 9, 0], [13.65046, 100.5939], 'โรงพยาบาลสำโรงการแพทย์']\
            , 111: [[3, 2, 3], [5, 3, 0], [14.794662, 100.385534], 'โรงพยาบาลท่าช้าง']\
            , 112: [[11, 7, 3], [8, 7, 0], [8.25725, 99.045212], 'โรงพยาบาลเขาพนม']\
            , 113: [[24, 18, 3], [11, 8, 0], [6.914849, 100.739766], 'โรงพยาบาลจะนะ']\
            , 114: [[3, 2, 2], [1, 1, 0], [15.358872, 99.931102], 'โรงพยาบาลหนองขาหย่าง']\
            , 115: [[19, 13, 7], [14, 8, 3], [13.733949, 100.645077], 'โรงพยาบาลชัยภูมิ']\
            , 116: [[29, 18, 16], [8, 2, 0], [13.677395, 100.722301], 'โรงพยาบาลจุฬารัตน์9']\
            , 117: [[3, 3, 3], [1, 1, 1], [19.300411, 100.716522], 'โรงพยาบาลสองแคว']\
            , 119: [[1, 1, 0], [7, 7, 0], [13.205123, 99.978982], 'โรงพยาบาลบ้านแหลม']\
            , 120: [[10, 10, 9], [4, 4, 0], [15.831744, 104.383304], 'โรงพยาบาลป่าติ้ว']\
            , 121: [[14, 9, 1], [6, 5, 0], [13.583625, 100.597046], 'โรงพยาบาลสมุทรปราการ']\
            , 122: [[17, 15, 9], [15, 15, 0], [7.387326, 99.667203], 'โรงพยาบาลย่านตาขาว']\
            , 123: [[0, 0, 0], [0, 0, 0], [6.393557, 101.692961], 'โรงพยาบาลยี่งอเฉลิมพระเกียรติ']\
            , 124: [[18, 12, 7], [5, 3, 3], [17.578554, 104.018704], 'โรงพยาบาลอากาศอำนวย']\
            , 126: [[10, 8, 9], [2, 2, 0], [16.062894, 99.410913], 'โรงพยาบาลปางศิลาทอง']\
            , 127: [[15, 15, 3], [11, 9, 0], [7.456774, 100.13679], 'โรงพยาบาลเขาชัยสน']\
            , 128: [[10, 8, 4], [9, 7, 0], [16.523859, 100.151558], 'โรงพยาบาลวชิรบารมี']\
            , 129: [[27, 17, 11], [7, 6, 1], [13.792523, 100.194065], 'โรงพยาบาลนครชัยศรี']\
            , 130: [[35, 31, 13], [16, 13, 3], [17.166295, 99.864574], 'โรงพยาบาลศรีสังวร']\
            , 131: [[45, 32, 16], [16, 12, 0], [13.351771, 100.982519], 'โรงพยาบาลชลบุรี']\
            , 132: [[12, 8, 6], [6, 4, 0], [13.648883, 100.569742], 'โรงพยาบาลชัยปราการ']\
            , 133: [[14, 8, 6], [2, 0, 0], [13.502212, 101.001707], 'โรงพยาบาลบางปะกง']\
            , 134: [[62, 35, 21], [52, 31, 5], [12.603376, 102.1013], 'โรงพยาบาลพระปกเกล้า']\
            , 135: [[8, 7, 0], [1, 1, 0], [13.908118, 100.49851], 'โรงพยาบาลปากเกร็ด']\
            , 137: [[13, 9, 4], [6, 2, 0], [6.931373, 99.786389], 'โรงพยาบาลละงู']\
            , 138: [[9, 3, 5], [12, 3, 1], [10.229976, 99.109092], 'โรงพยาบาลสวี']\
            , 139: [[13, 8, 6], [4, 2, 1], [19.299956, 97.971291], 'โรงพยาบาลศรีสังวาลย์']\
            , 140: [[39, 16, 19], [15, 9, 4], [13.469506, 101.098578], 'โรงพยาบาลพานทอง']\
            , 141: [[27, 24, 7], [13, 9, 2], [8.402172, 98.741917], 'โรงพยาบาลอ่าวลึก']\
            , 142: [[24, 16, 8], [10, 7, 1], [9.736091, 99.991109], 'โรงพยาบาลเกาะพงัน']\
            , 143: [[31, 27, 21], [16, 11, 2], [15.816415, 102.607971], 'โรงพยาบาลพล']\
            , 144: [[24, 17, 13], [18, 14, 3], [16.24056, 103.066873], 'โรงพยาบาลโกสุมพิสัย']\
            , 145: [[8, 3, 2], [1, 0, 0], [13.675214, 100.722127], 'โรงพยาบาลบางนา3']\
            , 146: [[4, 3, 3], [3, 2, 0], [15.933162, 102.281729], 'โรงพยาบาลคอนสวรรค์']\
            , 147: [[43, 34, 23], [14, 14, 2], [16.030932, 103.941855], 'โรงพยาบาลเสลภูมิ']\
            , 148: [[27, 19, 15], [17, 12, 1], [16.966112, 102.281689], 'โรงพยาบาลศรีบุญเรือง']\
            , 149: [[9, 8, 5], [5, 5, 0], [16.30914, 100.274828], 'โรงพยาบาลโพธิ์ประทับช้าง']\
            , 150: [[19, 14, 8], [8, 8, 1], [17.938802, 103.947982], 'โรงพยาบาลเซกา']\
            , 151: [[4, 3, 0], [4, 4, 0], [15.365865, 104.361126], 'โรงพยาบาลค้อวัง']\
            , 152: [[11, 10, 6], [11, 9, 0], [16.885604, 101.23024], 'โรงพยาบาลหล่มเก่า']\
            , 153: [[27, 25, 17], [24, 19, 4], [18.595003, 98.884742], 'โรงพยาบาลสันป่าตอง']\
            , 154: [[24, 21, 16], [5, 4, 0], [15.650113, 103.578461], 'โรงพยาบาลเกษตรวิสัย']\
            , 155: [[12, 11, 8], [6, 4, 1], [16.376248, 104.546429], 'โรงพยาบาลนิคมคำสร้อย']\
            , 156: [[98, 64, 55], [65, 42, 2], [14.98513, 102.104007], 'โรงพยาบาลมหาราชนครราชสีมา']\
            , 157: [[10, 6, 2], [5, 4, 0], [13.608701, 100.551038], 'โรงพยาบาลกรุงเทพพระประแดง']\
            , 158: [[6, 5, 1], [1, 1, 0], [9.343346, 98.431045], 'โรงพยาบาลสุขสำราญ']\
            , 159: [[45, 42, 13], [14, 13, 3], [5.773771, 101.081852], 'โรงพยาบาลเบตง']\
            , 160: [[7, 7, 5], [8, 8, 2], [8.062138, 99.302128], 'โรงพยาบาลลำทับ']\
            , 161: [[26, 23, 12], [14, 12, 0], [18.049639, 103.085882], 'โรงพยาบาลโพนพิสัย']\
            , 162: [[9, 8, 3], [9, 9, 0], [18.024211, 101.881639], 'โรงพยาบาลปากชม']\
            , 163: [[5, 5, 1], [4, 3, 0], [6.776284, 100.095126], 'โรงพยาบาลควนโดน']\
            , 164: [[2, 1, 1], [0, 0, 0], [15.321888, 105.48739], 'โรงพยาบาลโขงเจียม']\
            , 165: [[5, 1, 2], [1, 1, 0], [14.149921, 101.268007], 'โรงพยาบาลปากพลี']\
            , 166: [[28, 16, 17], [4, 4, 0], [14.636406, 101.197686], 'โรงพยาบาลมวกเหล็ก']\
            , 167: [[20, 14, 12], [9, 3, 0], [17.574609, 103.543831], 'โรงพยาบาลเจริญศิลป์']\
            , 168: [[10, 8, 4], [3, 1, 0], [15.610015, 105.019432], 'โรงพยาบาลตระการพืชผล']\
            , 169: [[15, 10, 12], [1, 0, 0], [15.654208, 104.305516], 'โรงพยาบาลคำเขื่อนแก้ว']\
            , 170: [[7, 7, 4], [1, 1, 0], [15.386086, 100.823465], 'โรงพยาบาลโคกเจริญ']\
            , 171: [[2, 2, 0], [2, 2, 0], [19.077588, 98.315293], 'โรงพยาบาลวัดจันทร์']\
            , 172: [[18, 14, 8], [4, 2, 0], [7.132738, 100.253101], 'โรงพยาบาลรัตภูมิ']\
            , 173: [[11, 7, 2], [14, 8, 0], [14.566062, 100.723524], 'โรงพยาบาลท่าเรือ']\
            , 174: [[5, 5, 2], [1, 1, 0], [16.406089, 102.343507], 'โรงพยาบาลบ้านแท่น']\
            , 175: [[10, 9, 6], [1, 0, 0], [12.674067, 101.985173], 'โรงพยาบาลสองพี่น้อง']\
            , 176: [[26, 21, 14], [16, 14, 1], [18.40651, 98.674431], 'โรงพยาบาลจอมทอง']\
            , 177: [[13, 10, 2], [18, 11, 1], [18.281324, 99.485458], 'โรงพยาบาลเขลางค์นคร']\
            , 178: [[4, 3, 3], [5, 5, 1], [18.616086, 98.774538], 'โรงพยาบาลแม่วาง']\
            , 179: [[12, 3, 2], [4, 2, 0], [16.433074, 102.820804], 'โรงพยาบาลขอนแก่นราม']\
            , 180: [[19, 16, 9], [9, 7, 0], [16.215004, 99.709371], 'โรงพยาบาลคลองขลุง']\
            , 182: [[22, 22, 9], [14, 14, 3], [12.969889, 101.219551], 'โรงพยาบาลปลวกแดง']\
            , 183: [[0, 0, 0], [0, 0, 0], [19.878469, 99.835535], 'โรงพยาบาลศรีบุรินทร์']\
            , 184: [[7, 5, 2], [9, 7, 1], [13.102444, 99.93622], 'โรงพยาบาลเพชรรัตน(เก่า50)']\
            , 185: [[7, 7, 7], [0, 0, 0], [16.182885, 99.325128], 'โรงพยาบาลคลองลาน']\
            , 186: [[24, 15, 5], [10, 6, 0], [12.807103, 102.116317], 'โรงพยาบาลเขาคิชฌกูฏ']\
            , 187: [[11, 10, 4], [5, 5, 0], [17.802013, 98.361453], 'โรงพยาบาลอมก๋อย']\
            , 188: [[20, 16, 10], [7, 7, 1], [15.846156, 103.875243], 'โรงพยาบาลอาจสามารถ']\
            , 189: [[16, 13, 9], [10, 7, 0], [12.792295, 100.956528], 'โรงพยาบาลวัดญาณสังวราราม']\
            , 190: [[2, 1, 0], [2, 1, 0], [15.878995, 102.910406], 'โรงพยาบาลเปือยน้อย']\
            , 191: [[26, 23, 17], [9, 7, 0], [12.904866, 102.263152], 'โรงพยาบาลโป่งน้ำร้อน']\
            , 192: [[47, 36, 19], [29, 24, 3], [16.423463, 101.157662], 'โรงพยาบาลเพชรบูรณ์']\
            , 193: [[11, 5, 3], [6, 3, 0], [13.805036, 100.472195], 'โรงพยาบาลบางกรวย']\
            , 194: [[11, 9, 5], [8, 6, 0], [7.203228, 99.693903], 'โรงพยาบาลปะเหลียน']\
            , 195: [[23, 19, 6], [10, 10, 1], [13.691166, 102.502583], 'โรงพยาบาลอรัญประเทศ']\
            , 196: [[20, 11, 11], [4, 4, 2], [14.52389, 100.932948], 'โรงพยาบาลเกษมราษฏร์สระบุรี']\
            , 197: [[10, 10, 9], [7, 7, 0], [18.322461, 98.817518], 'โรงพยาบาลบ้านโฮ่ง']\
            , 198: [[19, 12, 8], [10, 9, 1], [16.530293, 104.041515], 'โรงพยาบาลกุฉินารายณ์']\
            , 199: [[18, 13, 5], [4, 2, 0], [13.569562, 100.836399], 'โรงพยาบาลบางบ่อ']\
            , 200: [[52, 47, 30], [18, 14, 2], [13.551171, 100.278932], 'โรงพยาบาลสมุทรสาคร']\
            , 201: [[31, 23, 14], [14, 12, 1], [11.801121, 99.795825], 'โรงพยาบาลประจวบคีรีขันธ์']
            , 202: [[12, 9, 4], [10, 5, 0], [18.561655, 99.037778], 'โรงพยาบาลศิริเวชลำพูน']
            , 203: [[16, 13, 1], [16, 12, 1], [14.585087, 100.451927], 'โรงพยาบาลอ่างทอง']
            , 204: [[5, 4, 2], [1, 1, 0], [13.406752, 99.998441], 'โรงพยาบาลสมเด็จพระพุทธเลิศหล้า']
            , 206: [[3, 2, 0], [3, 2, 0], [6.240274, 101.49864], 'โรงพยาบาลศรีสาคร']
            , 207: [[17, 13, 14], [7, 5, 0], [15.025951, 103.935714], 'โรงพยาบาลสำโรงทาบ']
            , 208: [[39, 31, 12], [11, 8, 0], [14.007679, 99.975448], 'โรงพยาบาลกำแพงแสน']
            , 209: [[26, 22, 13], [8, 7, 2], [14.098288, 101.777765], 'โรงพยาบาลนาดี']
            , 210: [[5, 3, 4], [3, 2, 2], [17.051407, 104.26602], 'โรงพยาบาลโคกศรีสุพรรณ']
            , 211: [[14, 10, 2], [9, 7, 0], [16.058547, 102.729915], 'โรงพยาบาลบ้านไผ่']
            , 212: [[26, 14, 2], [8, 2, 0], [14.213761, 100.576781], 'โรงพยาบาลบางปะอิน']
            , 213: [[0, 0, 0], [2, 2, 1], [8.386944, 99.978655], 'โรงพยาบาลนครภัฒณ์']
            , 214: [[17, 12, 8], [6, 4, 0], [13.871805, 101.052696], 'โรงพยาบาลบางน้ำเปรี้ยว']
            , 215: [[5, 5, 2], [2, 2, 0], [14.442463, 99.129091], 'โรงพยาบาลท่ากระดาน']
            , 216: [[18, 14, 6], [7, 7, 0], [8.572453, 99.242992], 'โรงพยาบาลพระแสง']
            , 217: [[3, 3, 1], [0, 0, 0], [15.824075, 103.719119], 'โรงพยาบาลเมืองสรวง']
            , 218: [[0, 0, 0], [0, 0, 0], [12.935802, 100.886612], 'โรงพยาบาลพัทยาเมโมเรียล']
            , 219: [[23, 14, 11], [8, 5, 1], [14.048846, 100.617858], 'โรงพยาบาลภัทร-ธนบุรี']
            , 220: [[19, 13, 12], [14, 10, 1], [13.981321, 100.325542], 'โรงพยาบาลไทรน้อย']
            , 221: [[15, 14, 12], [12, 9, 2], [16.334176, 102.655286], 'โรงพยาบาลพระยืน']
            , 223: [[48, 38, 27], [21, 16, 3], [17.161584, 104.156889], 'โรงพยาบาลสกลนคร']
            , 224: [[45, 38, 25], [21, 16, 2], [14.941232, 103.80526], 'โรงพยาบาลศีขรภูมิ']
            , 225: [[13, 9, 2], [3, 1, 0], [13.603591, 100.706054], 'โรงพยาบาลบางพลี']
            , 226: [[20, 16, 9], [13, 12, 0], [12.939097, 101.529073], 'โรงพยาบาลวังจันทร์']
            , 228: [[37, 27, 22], [32, 16, 3], [16.808557, 100.263], 'โรงพยาบาลพุทธชินราช']
            , 229: [[58, 45, 27], [25, 17, 5], [14.534011, 100.915405], 'โรงพยาบาลสระบุรี']
            , 230: [[15, 10, 5], [10, 8, 0], [14.640969, 100.149815], 'โรงพยาบาลศรีประจันต์']
            , 231: [[16, 12, 10], [5, 4, 1], [15.341652, 104.151835], 'โรงพยาบาลราษีไศล']
            , 232: [[1, 1, 0], [1, 1, 0], [5.942659, 101.88754], 'โรงพยาบาลแว้ง']
            , 233: [[27, 26, 17], [4, 2, 1], [17.771736, 98.958061], 'โรงพยาบาลลี้']
            , 234: [[82, 73, 39], [45, 38, 1], [15.005535, 103.100794], 'โรงพยาบาลบุรีรัมย์']
            , 235: [[2, 2, 0], [0, 0, 0], [16.044367, 104.669006], 'โรงพยาบาลเสนางคนิคม']
            , 236: [[16, 13, 11], [3, 2, 0], [16.448846, 102.653779], 'โรงพยาบาลบ้านฝาง']
            , 237: [[22, 18, 10], [9, 9, 0], [13.545898, 99.439303], 'โรงพยาบาลสวนผึ้ง']
            , 238: [[0, 0, 0], [0, 0, 0], [13.576114, 100.27139], 'โรงพยาบาลศรีวิชัย5']
            , 239: [[15, 5, 3], [8, 6, 1], [13.583851, 100.854362], 'โรงพยาบาลรวมชัยประชารักษ์']
            , 240: [[23, 19, 6], [9, 6, 1], [14.334772, 99.513401], 'โรงพยาบาลบ่อพลอย']
            , 241: [[29, 27, 23], [22, 20, 2], [16.651685, 102.379835], 'โรงพยาบาลภูเวียง']
            , 242: [[5, 4, 4], [5, 5, 0], [15.320417, 103.10851], 'โรงพยาบาลแคนดง']
            , 243: [[17, 13, 11], [8, 6, 0], [13.646022, 101.441072], 'โรงพยาบาลสนามชัยเขต']
            , 244: [[16, 15, 13], [10, 10, 3], [17.454992, 104.468754], 'โรงพยาบาลโพนสวรรค์']
            , 245: [[17, 13, 7], [9, 8, 0], [13.384672, 101.695129], 'โรงพยาบาลท่าตะเกียบ']
            , 246: [[86, 75, 55], [53, 38, 12], [19.901057, 99.828701], 'โรงพยาบาลเชียงรายประชานุเคราะห์']
            , 247: [[11, 10, 2], [5, 4, 0], [13.694038, 99.92196], 'โรงพยาบาลบางแพ']
            , 248: [[49, 39, 25], [29, 21, 6], [15.115478, 104.320361], 'โรงพยาบาลศรีสะเกษ']
            , 249: [[13, 6, 4], [6, 4, 1], [13.66455, 100.602438], 'โรงพยาบาลมโนรมย์']
            , 250: [[17, 15, 6], [7, 6, 0], [15.211966, 100.666112], 'โรงพยาบาลหนองม่วง']
            , 251: [[21, 13, 10], [9, 5, 0], [14.754153, 100.074871], 'โรงพยาบาลสามชุก']
            , 252: [[33, 26, 18], [24, 18, 5], [15.947189, 99.979907], 'โรงพยาบาลบรรพตพิสัย']
            , 253: [[10, 6, 2], [7, 6, 0], [15.696045, 100.122586], 'โรงพยาบาลปากน้ำโพ']
            , 254: [[12, 9, 9], [7, 5, 0], [16.991744, 104.16064], 'โรงพยาบาลเต่างอย']
            , 255: [[7, 6, 3], [5, 4, 1], [15.553461, 100.066086], 'โรงพยาบาลโกรกพระ']
            , 256: [[16, 11, 7], [5, 2, 1], [12.68612, 102.200195], 'โรงพยาบาลมะขาม']
            , 257: [[34, 32, 19], [12, 12, 0], [16.463239, 99.528912], 'โรงพยาบาลกำแพงเพชร']
            , 258: [[30, 17, 16], [16, 15, 0], [14.733734, 102.156555], 'โรงพยาบาลโชคชัย']
            , 259: [[33, 30, 13], [10, 9, 0], [15.391733, 99.851165], 'โรงพยาบาลหนองฉาง']
            , 260: [[18, 15, 8], [12, 8, 3], [19.361642, 98.437636], 'โรงพยาบาลปาย']
            , 261: [[4, 4, 1], [0, 0, 0], [17.949963, 98.690327], 'โรงพยาบาลดอยเต่า']
            , 262: [[3, 3, 3], [1, 1, 1], [14.448869, 103.301583], 'โรงพยาบาลพนมดงรัษ์']
            , 265: [[24, 11, 6], [11, 5, 0], [15.64167, 100.48601], 'โรงพยาบาลท่าตะโก']
            , 266: [[7, 7, 4], [8, 7, 1], [16.928185, 103.242795], 'โรงพยาบาลท่าคันโท']
            , 267: [[19, 16, 6], [10, 9, 0], [12.685098, 101.274751], 'โรงพยาบาลรวมแพทย์ระยอง']
            , 268: [[17, 17, 14], [10, 9, 0], [19.35261, 99.509976], 'โรงพยาบาลเวียงป่าเป้า']
            , 269: [[28, 20, 18], [11, 9, 2], [14.430495, 102.463267], 'โรงพยาบาลเสิงสาง']
            , 270: [[21, 18, 12], [4, 4, 0], [13.717186, 100.707166], 'โรงพยาบาลสิรินธร']
            , 271: [[4, 2, 0], [0, 0, 0], [13.715574, 100.59053], 'โรงพยาบาลร้านหมอสวนิตย์']
            , 272: [[15, 14, 8], [3, 3, 1], [13.652357, 102.097364], 'โรงพยาบาลเขาฉกรรจ์']
            , 273: [[5, 5, 4], [1, 1, 0], [17.4769, 101.973321], 'โรงพยาบาลนาด้วง']
            , 274: [[1, 1, 0], [2, 2, 0], [17.097455, 103.005304], 'โรงพยาบาลกุมภวาปี']
            , 275: [[2, 2, 1], [0, 0, 0], [10.438882, 99.248907], 'โรงพยาบาลปากน้ำชุมพร']
            , 276: [[29, 22, 16], [9, 7, 1], [16.042314, 103.114262], 'โรงพยาบาลบรบือ']
            , 278: [[11, 7, 6], [6, 5, 2], [12.247906, 102.511652], 'โรงพยาบาลตราด']
            , 279: [[10, 4, 5], [3, 3, 0], [9.583108, 98.589187], 'โรงพยาบาลกะเปอร์']
            , 280: [[17, 14, 14], [2, 1, 1], [14.948409, 104.229462], 'โรงพยาบาลวังหิน']
            , 281: [[13, 11, 8], [4, 4, 0], [19.367638, 99.199824], 'โรงพยาบาลพร้าว']
            , 282: [[15, 13, 8], [10, 9, 0], [16.083326, 101.810111], 'โรงพยาบาลหนองบัวแดง']
            , 283: [[32, 28, 23], [20, 20, 1], [19.520836, 99.744442], 'โรงพยาบาลพาน']
            , 284: [[1, 1, 0], [1, 1, 1], [18.002977, 100.883133], 'โรงพยาบาลฟากท่า']
            , 227: [[9, 8, 4], [8, 6, 0], [16.416282, 100.520545], 'โรงพยาบาลวังทรายพูน']
            , 222: [[10, 9, 6], [1, 1, 0], [19.507776, 99.990591], 'โรงพยาบาลป่าแดด']
            , 205: [[56, 51, 29], [42, 38, 2], [13.957378, 101.727267], 'โรงพยาบาลกบินทร์บุรี']
            , 181: [[9, 6, 4], [4, 3, 0], [14.748256, 100.458163], 'โรงพยาบาลพรหมบุรี']
            , 136: [[25, 17, 8], [6, 5, 1], [9.983193, 99.066301], 'โรงพยาบาลหลังสวน']
            , 125: [[8, 6, 2], [2, 1, 2], [9.538586, 100.069566], 'โรงพยาบาลสมุยอินเตอร์เนชั่นแนล']
            , 118: [[3, 3, 2], [6, 5, 0], [14.650294, 100.408813], 'โรงพยาบาลโพธิ์ทอง']
            , 39: [[2, 2, 1], [0, 0, 0], [14.595206, 99.113757], 'โรงพยาบาลศุกร์ศิริศรีสวัสดิ์']
            , 36: [[13, 12, 4], [6, 4, 0], [17.95791, 104.207386], 'โรงพยาบาลบ้านแพง']
            , 35: [[99, 73, 32], [53, 43, 1], [13.819422, 100.074742], 'โรงพยาบาลนครปฐม']
            , 31: [[0, 0, 0], [0, 0, 0], [13.161597, 100.918551], 'โรงพยาบาลสมเด็จพระบรมราชเทวี']
            , 11: [[6, 6, 5], [4, 3, 1], [17.956635, 102.59075], 'โรงพยาบาลศรีเชียงใหม่']
            , 2: [[4, 4, 4], [0, 0, 0], [14.997801, 102.650614], 'โรงพยาบาลห้วยแถลง']
            , 277: [[2, 0, 0], [6, 5, 0], [10.502059, 99.143677], 'โรงพยาบาลธนบุรี-ชุมพร']
            , 289: [[24, 17, 9], [8, 8, 1], [13.581994, 101.281648], 'โรงพยาบาลแปลงยาว']


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

def bulid_map_55():
    """Buile html for thailand map."""
# [ละติจูด,ลองติดจูด] และการซูมลำดับ 5
map_osm = folium.Map(location=[15.0000, 100.0000], zoom_start=7)
for number in range(1, len(list_hs)+1):
    map_osm.polygon_marker(location=list_hs[number][2], popup=list_hs[number][3]+"<iframe frameBorder='0' src='"+chart("Output", number)+"'></iframe>",
                         fill_color='#FF0000', num_sides=3, radius=10, rotation=60)
map_osm.create_map(path='thailandmap_55.html')
