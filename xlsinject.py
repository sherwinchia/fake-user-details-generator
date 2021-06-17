import random
import numpy
import xlsxwriter
import names
import calendar
import time
import json
import os
from datetime import datetime, timedelta
from selenium import webdriver

def main():
    #read JSON data
    json_file = open("data.json")
    json_array = json.load(json_file)

    #set global variables
    global male_names, female_names,occupations,non_male_occupations
    male_names = json_array['malenames']
    female_names = json_array['femalenames']
    occupations = json_array['occupations']
    non_male_occupations = json_array['non_male_occupations']

    while (True):
        clearConsole()
        print( 
            "=========================================" + "\n"
            "       Fake User Details Generator" + "\n"
            "=========================================" + "\n"
            "(1) Generate User Details" + "\n"
            "(2) Generate User Details for Excel File" + "\n"
            "(3) Direct Inject to Form (Require Code Editing)" + "\n"
            "(4) Exit" + "\n"
        )
        user_option = int(input("Select option: "))

        if(user_option==1):
            generate_locally()
        elif(user_option==2):
            generate_excel()
        elif(user_option==3):
            inject_directly()
        elif(user_option==4):
            break;


def generate_locally():
    totalData = input("Select number of data to be generated: ")
    for x in range(int(totalData)):
        name, dob, age, nik, phonenumber, occupation, option = generate_data()
        print(
            "==================================" + "\n"
            "Injected Data Count :" + str(int(x)+1) + "\n"
            "==================================" +"\n"
            "NIK       : " + str(nik) + "\n"
            "Nama      : " + name + "\n"
            "DOB       : " + dob + "\n"
            "Umur      : " + str(age) + "\n"
            "No HP     : " + str(phonenumber) + "\n"
            "Pekerjaan : " + occupation + "\n"
        )
    input("Press Enter to continue...")

def generate_excel():
    totalData = input("Select number of data to be generated: ")
    fileName = input("Enter file name (include .xlsx extension): ")
    sheetName = input("Enter sheet name: ")
    startRow = input("Enter starting row: ")
    workbook = xlsxwriter.Workbook(fileName)
    worksheet = workbook.add_worksheet(sheetName)
    rowIndex = int(startRow)
    for row in range(int(totalData)):
        name, dob, age, nik, phonenumber, occupation, option = generate_data()
        worksheet.write('A'+str(rowIndex), name)
        worksheet.write('B'+str(rowIndex), dob)
        worksheet.write('C'+str(rowIndex), age)
        worksheet.write('D'+str(rowIndex), nik)
        worksheet.write('E'+str(rowIndex), phonenumber)
        worksheet.write('F'+str(rowIndex), occupation)
        worksheet.write('G'+str(rowIndex), option)
        rowIndex += 1
    workbook.close()

    input("Data Generated. Press Enter to continue...")

def inject_directly():
    totalData = input("Select number of data to be injected: ")
    googleFormLink = "https://docs.google.com/forms/d/e/1FAIpQLScajZqdye35dJpi0abhiuyX51C50XLAo6ZahOQTN37_zX5cjg/viewform"
    for x in range (int(totalData)):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        options  = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument("-incognito")
        browser = webdriver.Chrome(executable_path="D:/Coding/Python/chromedriver.exe", options=options)
        browser.get(googleFormLink)
        time.sleep(2) 
        name, dob, age, nik, phonenumber, occupation, option = generate_data()
        nama = browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea")
        nama.send_keys(name)
        tanggalLahir = browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea")
        tanggalLahir.send_keys(dob)
        umur = browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea")
        umur.send_keys(age)
        nik = browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea")
        nik.send_keys(nik)
        nomorHp = browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea")
        nomorHp.send_keys(phonenumber)
        toko = browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea")
        toko.send_keys(occupation)
        checkboxes = browser.find_elements_by_class_name("appsMaterialWizTogglePapercheckboxCheckbox")       
        time.sleep(1) 
        if(option == 1):
            checkboxes[0].click()
        else:
            checkboxes[1].click()
        submitButton = browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div")
        time.sleep(1)
        submitButton.click()

        browser.close()

        print(
            "==================================" + "\n"
            "Injected Data Count :" + str(int(user_option)+1) + "\n"
            "==================================" +"\n"
            "NIK       : " + str(nik) + "\n"
            "Nama      : " + name + "\n"
            "DOB       : " + dob + "\n"
            "Umur      : " + str(age) + "\n"
            "No HP     : " + str(phonenumber) + "\n"
            "Pekerjaan : " + occupation + "\n"
        )
    input("Data Injected. Press Enter to continue...")

def generate_data():
    day,month,year = raw_dob_generator()
    userGender = random.choice(["male","female"])

    #generate all other details
    generatedName = name_generator(names.get_first_name(gender=userGender), userGender) 
    generatedDob = dob_generator(day,month,year)
    generatedAge = age_generator(year)
    generatedNik = nik_generator(day + month + str(year))
    generatedPhoneNumber = phone_generator()
    generatedOcuppation = occupation_generator(userGender)
    generatedOption = checkbox_generator()
    
    return generatedName, generatedDob, generatedAge, generatedNik, generatedPhoneNumber, generatedOcuppation, generatedOption

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
    return random.choice(["1","2"])

def age_generator(year):
    currentYear = datetime.now().year
    return currentYear-year

def dob_generator(day,month,year):
    choice = random.choice([1,2,3])

    if (choice == 1):
        return day +"/"+ month +"/"+ str(year)
    elif (choice == 2):
        return day +"-"+ month +"-"+ str(year)
    elif (choice == 3):
        month = calendar.month_name[int(month)]
        return day +" "+ month +" "+ str(year)

def occupation_generator(gender):
    list_of_occupations = occupations.copy()
    if (gender == "male"):
        for item in non_male_occupations:
            list_of_occupations.remove(item)
    return format_string(random.choice(list_of_occupations))


def name_generator(name, gender):
    length = numpy.random.choice([0,1,2,3], p=[0.2,0.5,0.25,0.05])
    name = name + " "
    for x in range(length):
        if(gender=="male"):
            name += random.choice(male_names) +" "
        else:
            name += random.choice(female_names) +" "
    return format_string(name);

def format_string(text):
    stringFormat = numpy.random.choice([0,1], p=[0.15,0.85])
    if (stringFormat == 1):
        return text.lower()
    else:
        return text

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    

main()