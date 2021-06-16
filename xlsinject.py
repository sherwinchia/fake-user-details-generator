import random
import xlsxwriter
import names
import calendar
from datetime import datetime, timedelta

def main():
    totalData = 100
    workbook = xlsxwriter.Workbook("GFormBotData.xlsx")
    worksheet = workbook.add_worksheet("Sheet1")
    rowIndex = 8
    for row in range(totalData):
        day,month,year = raw_dob_generator()
        userGender = random.choice(["male","female"])

        worksheet.write('A'+str(rowIndex), name_generator(names.get_first_name(gender=userGender), userGender))
        worksheet.write('B'+str(rowIndex), dob_generator(day,month,year))
        worksheet.write('C'+str(rowIndex), age_generator(year))
        worksheet.write('D'+str(rowIndex), nik_generator(day + month + str(year)))
        worksheet.write('E'+str(rowIndex), phone_generator())
        worksheet.write('F'+str(rowIndex), status_generator(userGender))
        worksheet.write('G'+str(rowIndex), checkbox_generator())
        rowIndex += 1

    workbook.close()

def raw_dob_generator():
    months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"]
    day = random.choice(days)
    month = random.choice(months)
    year = random.randint(1950,2003)
    return day, month, year

def nik_generator(dob):
    areaCode = 217102
    dateOfBirth = dob
    randomEndDigit = random.randint(1000,9999)
    return str(areaCode) + dateOfBirth + str(randomEndDigit)

def phone_generator():
    fronts = ["0812", "0813", "0852", "0856", "0896", "0878", "0828", "0857", "0897", "0811", "0821", "0899"]
    front = random.choice(fronts)
    randomEndDigit = random.randint(14980110,89274382)
    return front+str(randomEndDigit)

def checkbox_generator():
    chocies = ["1","2","1,2"]
    return random.choice(chocies)

def age_generator(year):
    currentYear = datetime.now().year
    return currentYear-year

def dob_generator(day,month,year):
    choice = random.choice([1,2,3,4])

    if (choice == 1):
        return day +"/"+ month +"/"+ str(year)
    elif (choice == 2):
        return day +"-"+ month +"-"+ str(year)
    elif (choice == 3):
        return day +" "+ month +" "+ str(year)
    elif (choice == 4):
        month = calendar.month_name[int(month)]
        return day +" "+ month +" "+ str(year)

def status_generator(gender):
    status = ""
    if (gender == "male"):
        status = random.choice(["Porter", "Bengkel", "Montir", "Kerja","Asisten Rumah Tangga","Kuli","ART","Kuliah","Pensiun","Pengangguran","Guru", "Tidak bekerja", "Sales","IT","Petani","Wiraswasta","Ilmuwan","Satpam", "Nelayan", "Sopir", "Perawat","Teknisi","Jualan","Kerja di pasar","Porter", "Bengkel", "Montir", "Kerja","Asisten Rumah Tangga","Kuli","ART","Kuliah","Pensiun","Pengangguran","Guru", "Tidak bekerja", "Sales","IT","Petani","Wiraswasta","Ilmuwan","Satpam", "Nelayan", "Sopir", "Perawat","Teknisi","Jualan","Kerja di pasar","Porter", "Bengkel", "Montir", "Kerja","Asisten Rumah Tangga","Kuli","ART","Kuliah","Pensiun","Pengangguran","Guru", "Tidak bekerja", "Sales","IT","Petani","Wiraswasta","Ilmuwan","Satpam", "Nelayan", "Sopir", "Perawat","Teknisi","Jualan","Kerja di pasar", "Farmasi","Arsitek","Akuntan","Respsionis","Toko", "Bidan","Pengacara", "Programmer", "Peternak", "Tukang", "Jual koran", "Pramusaji","Penulis", "Dokter", "Pramusaji", "Pramusaji", "Pramusaji" ,"Anak Mafia", "Presiden"])
    else:
        status = random.choice(["Ibu Rumah Tangga","Asisten Rumah Tangga", "Pramusaji", "Pramusaji", "Peternak", "Tukang", "Porter", "Bengkel", "Montir", "Kerja", "Dokter","Asisten Rumah Tangga","Kuli","ART","Kuliah","Pensiun","Pengangguran","Guru", "Tidak bekerja", "Sales","IT","Petani","Ibu Rumah Tangga","Asisten Rumah Tangga", "Peternak", "Tukang", "Porter", "Bengkel", "Montir", "Kerja", "Dokter","Asisten Rumah Tangga","Kuli","ART","Kuliah","Pensiun","Pengangguran","Guru", "Tidak bekerja", "Sales","IT","Petani","Ibu Rumah Tangga","Asisten Rumah Tangga", "Peternak", "Tukang", "Porter", "Bengkel", "Montir", "Kerja", "Dokter","Asisten Rumah Tangga","Kuli","ART","Kuliah","Pensiun","Pengangguran","Guru", "Tidak bekerja", "Sales","IT","Petani","Wiraswasta","Ilmuwan","Satpam", "Nelayan", "Sopir", "Perawat","Teknisi","Jualan","Kerja di pasar","Farmasi","Arsitek","Akuntan","Respsionis","Toko", "Bidan","Pengacara", "Programmer", "Penulis", "Jual koran", "Pramusaji","Anak Mafia", "Presiden"])

    stringFormat = length = random.choice([0,0,0,0,0,1,1])
    if (stringFormat == 1):
        status = status.lower()

    return status


def name_generator(name, gender):
    malesName = ["Abichandra","Abimana","Abimanyu","Abinaya","Abyasa","Adhi","Adika","Adinata","Adipramana","Aditya","Adiwangsa","Agam","Agnibrata","Agung","Aji","Andaru","Andi","Angkasa","Apta","Aradhana","Ardhi","Ardiyanto","Arga","Arief","Arjanta","Arya","Asmaralaya","Astaguna","Aswangga","Bagas","Bagaskoro","Bajradaka","Bakti","Bamantara","Bambang","Banyu","Baskoro","Basuki","Baswara","Batara","Bayu","Bhagawanta","Bhanu","Bimo","Birawa","Bisma","Brahma","Bramantya","Brawijaya","Buana","Budi","Budiono","Cakra","Cakrawala","Candra","Cipta","Damar","Daniswara","Danurdara","Darsa","Dewangga","Dharma","Dipa","Dimas","Dirga","Edi","Endaru","Estu","Endang","Fadh","Fadhly","Fajar","Gadhing","Ganendra","Gardara","Gentala","Galih","Ganesh","Gibran","Gilang","Guinandra","Gumelar","Gunawan","Guntur","Guritno","Gusti","Hadi","Hakim","Halim","Hamdan","Hanafi","Handaru","Hapsari","Hardana","Haribawa","Haris","Harjita","Hartadi","Hartanto","Haryanto","Herdian","Herjuno","Hendro","Henry","Hery","Ihsan","Ihsan","Ismoyono","Jamal","Janu","Jati","Jatmika","Jaya","Jenaka","Jenggala","Jiwa","Joko","Jumanta","Jumantara","Kala","Kamajaya","Kamandaka","Karisma","Karno","Karunia","Kawindra","Kresna","Lakeswara","Langit","Lasmana","Leksana","Lesmana","Luthfi","Malik","Manggala","Mardhi","Margi","Mulyadi","Naresh","Nareswara","Naufal","Nugraha","Nusantara","Panca","Perdana","Perkasa","Praba","Pradigta","Pradipto","Pradnyana","Pradnyana","Pramuditha","Pramudya","Pranadipa","Pranawa","Prasaja","Prasetyo","Putra","Raden","Raditya","Rahardian","Raharja","Madyana","Madya","Mahadri","Mahajana","Mahapraja","Mahaprana","Mahardika","Mahatma","Mahendra","Raka","Rama","Randika","Rangga","Reswara","Reza","Rezvan","Ricky","Rudi","Sadana","Sakti","Samudra","Santoso","Satria","Satriya","Satya","Sigit","Siswanto","Sobiyanto","Sudiro","Sugiarto","Surya","Suryana","Susilo","Tamawijaya","Tegar","Teja","Tirta","Tohpati","Tulus","Ulung","Wardana","Wajendra","Wibisana","Wibowo","Widayaka","Widura","Widodo","Wijaya","Wirya","Yoga","Yuda","Yudayana"]

    femalesName = ["Adiratna","Adriani","Airani","Amanda","Anatari","Anindya","Anjani","April","Arkadewi","Aruna","Arsyana","Asri","Ayu","Ayudisha","Bandiani","Banurasmi","Basagita","Batari","Binar","Bintang","Bratarini","Bulan","Cahaya","Candramaya","Cempaka","Citra","Citta","Cyntia","Danastri","Danurdara","Dewi","Dhatu","Diajeng","Dianti","Diatmika","Ditya","Dwi","Elok","Erina","Estiana","Fitri","Gadis","Gahyaka","Gantari","Garini","Gayatri","Gema","Gemani","Gemintang","Gempita","Genta","Ginanita","Gyandra","Halim","Haira","Hanasta","Hanna","Harini","Hasana","Hasya","Hayu","Ika","Ina","Indah","Indira","Indri","Indriaya","Intan","Istari","Isthika","Isty","Iswari","Jayanti","Jelita","Jenar","Juwita","Kahyang","Kamala","Kana","Kani","Kanista","Karina","Karmika","Kartana","Kasidya","Kasih","Kasyaira","Kayshila","Keinan","Kemala","Kencana","Keswari","Kila","Kinnas","Kirana","Laksita","Laksmi","Lalita","Lanita","Laras","Larasati","Lasmaya","Lawana","Laya","Lelana","Lestari","Lestia","Lika","Limar","Lily","Lingga","Listia","Listu","Lituhayu","Lukita","Mada","Madaharsa","Madana","Madarsana","Mahadewi","Maharani","Mahawirya","Maktika","Malya","Manda","Manika","Mataya","Maya","Mega","Melati","Mentari","Mirah","Miratussany","Mustika","Nada","Nadia","Nadindra","Naeswari","Nala","Nanda","Nara","Nararya","Narasnama","Nata","Ndari","Nehan","Nidya","Ningrum","Ningsih","Nirmala","Numatya","Padmana","Paramastri","Paramita","Parmadita","Pawana","Permata","Pertiwi","Pramata","Pramidita","Pratista","Puri","Purnama","Puspa","Puspita","Putri","Radmila","Rahmi","Rajini","Rananta","Rani","Ranupatma","Rara","Ratih","Ratimaya","Ratna","Ratu","Rawika","Rembulan","Rosa","Sada","Saktika","Sakya","Samada","Saraswati","Sasi","Sasmaya","Sekar","Septha","Dwi","Seta","Sitaresmi","Sukma","Swasti","Tantri","Tanya","Tarasari","Tisna","Tiwi","Tri","Tyas","Utami","Utari","Wangi","Wasana","Waskita","Wening","Widati","Widhiani","Widi","Widia","Widuri","Wikasita","Wiyana","Wulan","Wulandari","Wuri","Yanti","Yatiwara","Yatna","Yetri","Yulianti","Yuni"]
    length = random.choice([0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,3])
    name = name + " "
    for x in range(length):
        if(gender=="male"):
            name += random.choice(malesName) +" "
        else:
            name += random.choice(femalesName) +" "

    stringFormat = length = random.choice([0,0,0,0,0,1,1])
    if (stringFormat == 1):
        name = name.lower()

    return name;

main()