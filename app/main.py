from flask import Flask, jsonify, request
import datetime
import requests
import csv

app = Flask(__name__)

token = '5441208078:AAGddUv_cJRUttGoOTIrKrduSYv0rNh8Ntw'

tempArray = []
membersInClasses = []

today = datetime.datetime.today()
day = datetime.datetime.today().weekday()


with open("database.csv", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        tempRow = []
        tempRow.append(row[0])
        tempRow.append(row[1])
        tempRow.append(row[2])
        tempRow.append(row[3])
        tempRow.append(row[4])
        tempRow.append(row[5])
        tempRow.append(row[6])
        tempArray.append(tempRow)

csvfile.close()


def welcome_msg(item):
    global token
    if item["text"].lower() == "/start" or item["text"].lower() == "start" or item["text"].lower() == "شروع" or item[
        "text"].lower() == "آغاز":
        LogMessageString = item
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, 93590816,
                                                                                                        LogMessageString)
        resp = requests.get(to_url)

        msg = 'سلام، به بات تلگرامی دستیار دانشجویی دانشگاه صنعتی شاهرود خوش آمدید.\n برای اطلاعات بیشتر درباره کار با بات، می توانید عبارت \'راهنمایی\' یا \'help\' را ارسال کنید'
        chat_id = item["chat"]["id"]
        welcome_msg = '''{}'''.format(msg)
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, chat_id,
                                                                                                        welcome_msg)
        resp = requests.get(to_url)

    if item["text"].lower() == "/help" or item["text"].lower() == "help" or item["text"].lower() == "راهنمایی" or item[
        "text"].lower() == "راهنما":
        LogMessageString = item
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, 93590816,
                                                                                                        LogMessageString)
        resp = requests.get(to_url)
        msg = 'شما می توانید با ارسال متن تعیین شده برای هر دستور، فعالیت مربوط به آن را انجام دهید.\n`لیست` یا `list` ==> دانلود جدول زمانبندی کلاس ها\n `افزودن` یا `add` همراه شماره و گروه درس ==> اضافه شدن به درس مورد نظر\n `حذف` یا `remove` به همراه شماره و گروه درس ==> حذف درس از لیست دروس\n `امروز` یا `today` ==> مشاهده برنامه درسی امروز'
        chat_id = item["chat"]["id"]
        help_mgs = '''{}'''.format(msg)
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, chat_id,
                                                                                                        help_mgs)
        resp = requests.get(to_url)

    if item["text"].lower() == "لیست" or item["text"].lower() == "کلاس ها" or item["text"].lower() == "کلاس" or item[
        "text"].lower() == "list" or item[
        "text"].lower() == "class":
        LogMessageString = item
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, 93590816,
                                                                                                        LogMessageString)
        resp = requests.get(to_url)
        msg = 'https://t.me/c/1640016110/4'
        chat_id = item["chat"]["id"]
        list_msg = '''{}'''.format(msg)
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, chat_id,
                                                                                                        list_msg)
        resp = requests.get(to_url)

    if item["text"].lower().count('add') == 1 or item["text"].lower().count('افزودن') or item["text"].lower().count('/add') == 1 or item["text"].lower().count('/افزودن') == 1 == 1:

        LogMessageString = item
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, 93590816,
                                                                                                        LogMessageString)
        resp = requests.get(to_url)

        chat_id = item["chat"]["id"]
        tempString = item["text"].lower()
        tempString = tempString.replace("add ", "")
        tempString = tempString.replace("افزودن ", "")
        tempString = tempString.replace("/add ", "")
        tempString = tempString.replace("/افزودن ", "")
        msg = 'متاسفانه مشکلی در فرآیند افزودن درس رخ داده است، لطفا دوباره تلاش کنید.'

        membersInClasses = []
        membersFileReader = open("members.txt", "r")
        for i in membersFileReader:
            temp = i.replace("\n", "").split(", ")
            temp[0] = str(temp[0])
            temp[1] = str(temp[1])
            membersInClasses.append(temp)
        membersFileReader.close()
        MemberClass_msg = membersInClasses
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, 93590816,
                                                                                                        MemberClass_msg)
        resp = requests.get(to_url)

        flag = False
        for i in tempArray:
            string = i[0] + i[1]
            if (string == tempString):
                flag = True
                tempClass = [str(chat_id), tempString]
                if membersInClasses.count(tempClass) > 0:
                    msg = "درس مورد نظر قبلا برای شما ثبت شده است."
                    break
                else:
                    msg = "درس مورد نظر یافت شد و برای شما ثبت شد"
                    membersFileWriter = open("members.txt", "a")
                    membersFileWriter.write(str(tempClass[0]) + ", " + str(tempClass[1]) + "\n")
                    membersFileWriter.close()
                    break

        if flag == False:
            msg = "متاسفانه درسی با مشخصات وارد شده یافت نشد، لطفا دوباره تلاش کنید"

        addLesson_msg = '''{}'''.format(msg)
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, chat_id,
                                                                                                        addLesson_msg)
        resp = requests.get(to_url)

    if item["text"].lower() == "today" or item["text"].lower() == "/today" or item["text"].lower() == "/امروز" or item["text"].lower() == "امروز":
        chat_id = item["chat"]["id"]

        LogMessageString = item
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, 93590816,
                                                                                                        LogMessageString)
        resp = requests.get(to_url)

        tempString = []
        membersInClasses = []
        membersFileReader = open("members.txt", "r")
        for i in membersFileReader:
            temp = i.replace("\n", "").split(", ")
            temp[0] = str(temp[0])
            temp[1] = str(temp[1])
            membersInClasses.append(temp)
        membersFileReader.close()

        for i in membersInClasses:
            if i[0] == str(chat_id):
                for j in tempArray:
                    string = j[0] + j[1]
                    if string == i[1]:
                        tempString.append(j[2] + " - " + j[3] + " - " + j[5] + " - " + j[6])

        for i in tempString:
            msg = i
            todayLesson_msg = '''{}'''.format(msg)
            to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token,
                                                                                                            chat_id,
                                                                                                            todayLesson_msg)
            resp = requests.get(to_url)

    if item["text"].lower().count('remove') == 1 or item["text"].lower().count('حذف') or item["text"].lower().count('/remove') == 1 or item["text"].lower().count('/حذف') == 1 == 1:
        chat_id = item["chat"]["id"]

        tempString = item["text"].lower()
        tempString = tempString.replace("remove ", "")
        tempString = tempString.replace("حذف ", "")
        tempString = tempString.replace("/remove ", "")
        tempString = tempString.replace("/حذف ", "")
        msg = 'متاسفانه مشکلی در فرآیند حذف درس رخ داده است، لطفا دوباره تلاش کنید.'

        membersInClasses = []

        membersFileReader = open("members.txt", "r")
        for i in membersFileReader:
            temp = i.replace("\n", "").split(", ")
            temp[0] = str(temp[0])
            temp[1] = str(temp[1])
            membersInClasses.append(temp)
        membersFileReader.close()

        flag = False
        for i in membersInClasses:
            msg = i
            removeLesson_msg = '''{}'''.format(msg)
            to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(
                token,
                chat_id,
                removeLesson_msg)
            resp = requests.get(to_url)
            if (str(i[0]) == str(chat_id)):
                if (str(i[1]) == str(tempString)):
                    msg =  "درس مورد نظر یافت شد و از حساب کاربری شما حذف شد"
                    removeLesson_msg = '''{}'''.format(msg)
                    to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(
                        token,
                        chat_id,
                        removeLesson_msg)
                    resp = requests.get(to_url)
                    flag = True
                    lineRemoveString = "{}, {}\n".format(str(chat_id), str(tempString))
                    with open("members.txt", "r") as f:
                        lines = f.readlines()
                    with open("members.txt", "w") as f:
                        for line in lines:
                            if line != lineRemoveString:
                                f.write(line)

            if flag == False:
                msg = "متاسفانه درسی با مشخصات وارد شده یافت نشد، لطفا دوباره تلاش کنید"
                removeLesson_msg = '''{}'''.format(msg)
                to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(
                    token,
                    chat_id,
                    removeLesson_msg)
                resp = requests.get(to_url)

    else:
        LogMessageString = item
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, 93590816,
                                                                                                        LogMessageString)
        resp = requests.get(to_url)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        data = data["message"]
        welcome_msg(data)
        return {'statusCode': 200, 'body': 'Success', 'data': data}
    else:
        return {'statusCode': 200, 'body': 'Success'}
