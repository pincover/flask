import os
from model import Model
from flask import Flask, request, redirect, jsonify
# from cleandata import read_files
from flask_cors import CORS

app = Flask('__name__')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

CORS(app)

Model = Model()

print("OK")

v,v1,v2 = 'No','No','No'
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
q1,q2,q3,q4,q5,q6,q7,q8,q9 = 0,0,0,0,0,0,0,0,0
q10,q11,q12,q13,q14,q15,q16,q17,q18,q19 = 0,0,0,0,0,0,0,0,0,0

ALLOWED_EXTENSIONS = set(['jpg','jpeg','png','BMP','EPS','PEG','GIF'])
ALLOWED_EXTENSIONS_File = set(['doc','docx','pdf','่jpg','jpeg','png','PNG','BMP','EPS','PEG','GIF'])
def allowed_image(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_File

@app.route('/', methods=['GET'])
def showData():
    row = Model.Showdata()
    return jsonify(datas=row)

@app.route('/showEmp', methods=['POST'])
def showDataEmp():
    id = request.get_json(['id']) 
    x = id['userid'] 
    a = Model.ShowEmp(x)
    return jsonify(a)

@app.route('/showFeed', methods=['GET'])
def showDataFeed():
    row = Model.ShowFeed()
    return jsonify(datas=row)

@app.route('/showEvent', methods=['GET'])
def showDataEvent():
    row = Model.ShowEvent()
    return jsonify(datas=row)

@app.route('/showChDetail', methods=['GET'])
def showDataChDetail():
    row = Model.ShowChDetail()
    return jsonify(datas=row)

@app.route('/showChNo', methods=['POST'])
def showDataChNo():
    Fid = request.get_json(['Fid']) 
    x = Fid['FNo'] 
    a = Model.ShowEmp(x)
    return jsonify(a)

@app.route('/CheckChNo', methods=['POST'])
def CheckDataChNo():
    w = Model.ShowChecklistNo()
    n = w[0][0]
    f = w[0][1]
    print(w)
    print(n)
    print(f)
    total =Model.checkChNo(n,f,w)
    a = True
    print(total,'No & FarmID',w)
    if(total==1):
        return jsonify(a)
    else:
        a=False
        print("Error")
        return jsonify(a)
# createEmpOwner
@app.route('/insertOwn', methods=['POST'])
def insertOwn():
    print(request.is_json)
    req = request.get_json(['obj'])
    a = req['Farmid']
    b = req['Email']
    b1 = req['Password']
    b2 = req['NameTh']
    b3 = req['LastnameTh']
    b4 = req['NameEn']
    b5 = req['LastnameEn']
    b6 = req['Idcard']
    b7 = req['Birth']
    b8 = req['Phone']
    b9 = req['Line']
    b10 = req['HouseNo']
    b11 = req['VillageNo']
    b12 = req['Lane']
    b13 = req['Road']
    b14 = req['Subarea']
    b15 = req['Area']
    b16 = req['Province']
    x = Model.insertOwn(a,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16)
    return jsonify(x)
# createEmp
@app.route('/insertEmp', methods=['POST'])
def insertEmp():
    print(request.is_json)
    req = request.get_json(['obj'])
    b = req['Email']
    b1 = req['Password']
    b2 = req['NameTh']
    b3 = req['LastnameTh']
    b4 = req['NameEn']
    b5 = req['LastnameEn']
    b6 = req['Idcard']
    b7 = req['Birth']
    b8 = req['Phone']
    b9 = req['Line']
    b10 = req['HouseNo']
    b11 = req['VillageNo']
    b12 = req['Lane']
    b13 = req['Road']
    b14 = req['Subarea']
    b15 = req['Area']
    b16 = req['Province']
    a1 = req['Farmname']
    print(b6)
    a = Model.FarmnametoId(a1)
    print(b6)
    x = Model.insertEmp(a,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16)
    return jsonify(x)
# login-new
@app.route('/login', methods=['POST'])
def Login():
    print(request.is_json)
    uname = request.get_json(['user'])
    u = uname['user']
    p = uname['pass']
    x = Model.loginid()
    total = Model.cheack(u, p, x)
    a = Model.checkuname(u)
    # print(total, 'id&pass', x)
    if(total == 1):
        return jsonify(a)
    else:
        a = False
        print("Error")
        return jsonify(a)
# insertdataFarm
@app.route('/insert', methods=['POST'])
def insert():
    print(request.is_json)
    req = request.get_json(['Datafarm'])
    a = req['FarmName']
    b = req['FarmOwner']
    b1 = req['FarmNumber']
    b2 = req['FarmGroup']
    b3 = req['FarmCanton']
    b4 = req['FarmDistrict']
    b5 = req['FarmProvince']
    b6 = req['lattitube']
    b7 = req['longtitube']
    b8 = req['Farmregistration']
    b9 = req['Documentfarm']
    b10 = req['Year']
    b11 = req['Startoperation']
    b12 = req['NumberOfYears']
    b13 = req['TotalFarmArea']
    b14 = req['Pond']
    b15 = req['NumberOfReservoirs']
    b16 = req['NumberOfAcresAndPondareas']
    b17 = req['Lenstorage']
    b18 = req['NumberOfLensStorage']
    b19 = req['NumberOfAcresAndLensStorage']
    b20 = req['SewagetreatmentSystem']
    b21 = req['Pondperiod']
    b22 = req['NumberofYearsOfOldDiggingwell']
    b23 = req['Culture']
    b24 = req['Allculturedareas']
    b25 = req['NumberofFloatingcages']
    b26 = req['Lastyearfarmoutput']
    b27 = req['PastInvestmentSituation']
    b28 = req['Farmstatus']
    print('req =',v)
    ins = Model.insert(v,v1,v2,a,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28)
    return jsonify(ins)

#ส่งข้อมูล location
@app.route('/insertChLocation', methods=['POST'])
def insertDataChecklocation():
    print(request.is_json)
    req = request.get_json(['Datachlocation'])
    Ch = req['ChecklistNo']
    b0 = req['Watercontent']
    b = req['Sourceofpollution']
    b1 = req['Distance']
    b2 = req['cantransferwater']
    b3 = req['Convenienttransportation']
    b4 = req['roadinsidethefarm']
    b5 = req['necessaryutilities']
    b6 = req['electricity']
    b7 = req['electricityvolume']
    b8 = req['waterused']
    b9 = req['waterusedvolume']
    b10 = req['Othernecessaryutilities']
    b11 = req['Othernecessaryutilitiesdetail']
    b12 = req['Backupsystem']
    print('req =',b0)
    DataCh1 = Model.insertDataLocation(Ch,b0,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,q10,q11,q12,q13,q14)
    return jsonify(DataCh1)

# createlite 1 เพื่อสร้างdataในตารางcheacklist
@app.route('/create1', methods=['POST'])
def createchlocation():
    Fid = request.get_json(['Fid']) 
    x = Fid['Farmid'] 
    print(x)
    a = Model.create1(x)
    return jsonify(a)

#ส่งข้อมูล Managefarm
@app.route('/insertChManagefarm', methods=['POST'])
def insertDataCheckManagefarm():
    print(request.is_json)
    req = request.get_json(['Managementfarm'])
    Ch = req['CheckListNo']
    b0 = req['Soilbottomingconditions']
    b = req['Exterminationofaquaticpests']
    b1 = req['Disinfectionofponds']
    b2 = req['Otheraction']
    b3 = req['Waterfiltering']
    b4 = req['Disinfectionofwater']
    b5 = req['Waterqualityadjustment']
    b6 = req['OtherManagement']
    b7 = req['Numberofoffspring']
    b8 = req['Dischargingwaterfromthefarm']
    b9 = req['reportofsewage']
    b10 = req['thewastewaterquality']
    b11 = req['Complaintsfromfarms']
    b12 = req['Cleanlinessofgrass']
    b13 = req['equipment']
    b14 = req['Preventcontamination']
    b15 = req['notusefreshmanure']
    b16 = req['Storagelocation']
    b17 = req['Containerused']
    b18 = req['Storagecondition']
    b19 = req['Cradleofinputs']
    b20 = req['Storage']
    b21 = req['Management']
    b22 = req['Animaldisposalsystem']
    print('req =',b0)
    DataChManage = Model.insertDataManage(Ch,b0,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13)
    return jsonify(DataChManage)

# createlite 2 เพื่อสร้างdataในตารางcheacklist copy 1 แล้วทำความเข้าใจ
@app.route('/create2', methods=['POST'])
def createchManageFarm():
    Fid = request.get_json(['Fid']) 
    x = Fid['Farmid'] 
    print(x)
    a = Model.create2(x)
    return jsonify(a)

#ส่งข้อมูล health
@app.route('/insertChhealth', methods=['POST'])
def insertDataCheckhealth():
    print(request.is_json)
    req = request.get_json(['health'])
    Ch = req['CheckListNo']
    b1 = req['pondisproperlyprepared']
    b2 = req['Cleaning']
    b3 = req['Fishhealth']
    b4 = req['Abnormalsymptomsaremanaged']
    b5 = req['Abnormalsymptomsaremanageddetail']
    b6 = req['Sendingaquaticanimalsforinspection']
    b7 = req['Notification']
    b8 = req['Carcassmanagement']
    b9 = req['Wastewatermanagement']
    print('req =',Ch)
    DataChhealth = Model.insertDatahealth(Ch,b1,b2,b3,b4,b5,b6,b7,b8,b9,c14,c15,c16,c17,c18,c19)
    return jsonify(DataChhealth)

# createlite 3 เพื่อสร้างdataในตารางcheacklistcopy 1 แล้วทำความเข้าใจ
@app.route('/create3', methods=['POST'])
def createchhealth():
    Fid = request.get_json(['Fid']) 
    x = Fid['Farmid'] 
    print(x)
    a = Model.create3(x)
    return jsonify(a)

@app.route('/insertChHygiene', methods=['POST'])
def insertDataHygiene():
    print(request.is_json)
    req = request.get_json(['Hygiene'])
    Ch = req['ChecklistNo']
    b0 = req['Splitsystem']
    b = req['Cleanlinesssystem']
    b1 = req['Bathroom']
    b2 = req['Hygiene']
    b3 = req['Contamination']
    b4 = req['Garbagecollectionsystem']
    b5 = req['Scrabble']
    b6 = req['carrier']
    b7 = req['Prevention']
    print('req =')
    print(q5)
    DataChHygiene = Model.insertDataHygiene(Ch,b0,b,b1,b2,b3,b4,b5,b6,b7,q1,q2,q3,q4,q5)
    return jsonify(DataChHygiene)

# createlite 4 เพื่อสร้างdataในตารางcheacklistcopy 1 แล้วทำความเข้าใจ
@app.route('/create4', methods=['POST'])
def createchHygiene():
    Fid = request.get_json(['Fid']) 
    x = Fid['Farmid'] 
    print(x)
    a = Model.create4(x)
    return jsonify(a)

@app.route('/insertChharvesting', methods=['POST'])
def insertDataharvesting():
    print(request.is_json)
    req = request.get_json(['harvesting'])
    Ch = req['ChecklistNo']
    b1 = req['Catching']
    b2 = req['Catchingfish']
    b3 = req['Aquacultureplans']
    b4 = req['captureplan']
    b5 = req['Cleaningaquatic']
    b6 = req['Captureandsortingarea']
    b7 = req['Details']
    b8 = req['MD']
    b9 = req['FMD']
    b10 = req['Formofsale']
    b11 = req['Transportation']
    b12 = req['Methodandmaintaintemperature']
    b13 = req['examinationresults']
    print('req =')
    print(q9)
    DataChharvesting = Model.insertDataharvesting(Ch,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,q6,q7,q8,q9)
    return jsonify(DataChharvesting)

# createlite 5 เพื่อสร้างdataในตารางcheacklistcopy 1 แล้วทำความเข้าใจ
@app.route('/create5', methods=['POST'])
def createchharvesting():
    Fid = request.get_json(['Fid']) 
    x = Fid['Farmid'] 
    print(x)
    a = Model.create5(x)
    return jsonify(a)


@app.route('/insertFeed', methods=['POST'])
def insertdataFeed():
    print(request.is_json)
    req = request.get_json(['Datafeed'])
    b = req['type']
    b1 = req['FoodforCulture']
    b2 = req['FoodNumber']
    b3 = req['Productiondate']
    b4 = req['expdate']
    b5 = req['Physicalconditionoffood']
    b6 = req['FrequencyofOrderingfood']
    x = Model.insertFeed(b,b1,b2,b3,b4,b5,b6)
    print(x)
    return jsonify(True)
# insertProblem-Even
@app.route('/insertEven', methods=['POST'])
def insertEven():
    print(request.is_json)
    req = request.get_json(['obj'])
    # FPNO
    b = req['pondsaffectedbyexternalfactors']
    b1 = req['DayMonthYear']
    b2 = req['Factorsproblems']
    b3 = req['ImpactofExternal']
    b4 = req['NameofResponsibleperson']
    b5 = req['SurnameofResponsibleperson']
    b6 = req['Howtosolvetheproblem']
    b7 = req['DayMonthYearstart']
    b8 = req['DayMonthYearstop']
    Empid = Model.FindEmp(b4,b5)
    EVNO = Model.insertEven(b1,b2,b3,b,Empid)
    Model.inserttreatment(EVNO,b6,b7,b8)
    return jsonify(True)
# insertgivefood
@app.route('/insertFood', methods=['POST'])
def insertDatagivefeed():
    req = request.get_json(['Datagivefeed'])
    b = req['Typeproduct']
    b1 = req['Nameproduct']
    b2 = req['time']
    b3 = req['volume']
    b4 = req['RoundNo']
    b5 = req['PondNo']
    x = Model.selectFLNO(b4,b5) 
    # x=FLNO
    m = Model.FindMTNO(b1,b)
    # m=MTNO
    z = Model.insertfishmanagement(x,m,b,b2,b3)
    return jsonify(z)
# insertPond-lotpond
@app.route('/insertPond', methods=['POST'])
def insertPond():
    req = request.get_json(['Datafeed'])
    b = req['type']  
    b1 = req['Pond']
    b2 = req['size']
    b3 = req['Fishtype']
    b4 = req['Round']
    b5 = req['Numberofdays']
    b6 = req['startdate']
    b7 = req['Enddate']
    a = req['Farmid']
    x = Model.insertFishtype(b3)
    print(x)
    # x=FTNO
    Model.insertPone(b1,b,a,b2)
    c = Model.FindpondNo(b1,a)
    # c=FPNO
    z = Model.insertLot(b5,b4,c,x,b6,b7)
    print(c)
    return jsonify(z)
#showFarmPlan
@app.route('/datafarm', methods=['GET'])
def showfarm():
    row = Model.ShowFarm()
    return jsonify(datas=row)
#upload image to FarmPlan
@app.route('/img', methods=['POST'])
def insertfarmplan():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        print(file)
        if file and allowed_image or allowed_file(file.filename):
            f = request.files['image'] 
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Farm\\Farmplan\\' + f.filename
            f.save(path)
            path2 = '..\\assets\\Farm\\Farmplan\\' + f.filename
            global v
            v = path2
            print(v)
            print("Upload image Success")
            return jsonify(True)
        else:
            return jsonify(False)

#show path of file document registration Farm
@app.route('/docRegfarm', methods=['GET'])
def ShowRegFarm():
    row = Model.ShowDocRegFarm()
    return jsonify(datas=row)

#upload file document registration Farm
@app.route('/documentRegFarm', methods=['POST'])
def insertFileRegFarm():
    print('....Try to Upload file....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['file']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_file(file.filename):
            f = request.files['file']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Farm\\Reg Farm document\\' + f.filename
            f.save(path)
            path2 = '..\\assets\\Farm\\Reg Farm document\\' + f.filename
            global v1 
            v1 = path2
            print(path2)
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#upload image to SewageSystem
@app.route('/SewageSystem', methods=['POST'])
def insertSewageSystem():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        print(file)
        if file and allowed_image or allowed_file(file.filename):
            f = request.files['image'] 
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Farm\\SewageSystem\\' + f.filename
            f.save(path)
            path2 = '..\\assets\\Farm\\SewageSystem\\' + f.filename
            global v2 
            v2 = path2
            print(path2)
            print("Upload image2 Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-1
#show path of Soil
@app.route('/Soil', methods=['GET'])
def ShowSoil():
    row = Model.ShowimgSoil()
    return jsonify(datas=row)

#upload file Soil to database
@app.route('/img--soil', methods=['POST'])
def insertimageSoil():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading img1')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image or allowed_file(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\Soil\\' + f.filename
            f.save(path)
            path2 = '..\\assets\\Checklist\\1\\Soil\\' + f.filename
            global c1 
            c1 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-2
#show path of ExtermAquatic
@app.route('/ExtermAquatic', methods=['GET'])
def ShowExtermAquatic():
    row = Model.ShowimgExtermAquatic()
    return jsonify(datas=row)

#upload file ExtermAquatic to database
@app.route('/img--ExtermAquatic', methods=['POST'])
def insertimageExtermAquatic():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading img2')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\ExtermAquatic\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\ExtermAquatic\\' + f.filename
            global c2 
            c2 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-3
#show path of Disinfection
@app.route('/Disinfection', methods=['GET'])
def ShowDisinfection():
    row = Model.ShowimgDisinfection()
    return jsonify(datas=row)

#upload file Disinfection to database
@app.route('/img--Disinfection', methods=['POST'])
def insertimageDisinfection():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading img3')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\Disinfection\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\Disinfection\\' + f.filename
            global c3 
            c3 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-4
#show path of otherAction
@app.route('/otheractionfile', methods=['GET'])
def Showotheraction():
    row = Model.ShowDocOtherAct()
    return jsonify(datas=row)

#upload file otheraction to database
@app.route('/documentofotheraction', methods=['POST'])
def insertFileotheraction():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading img4')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\OtherAction\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\OtherAction\\' + f.filename
            global c4 
            c4 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-5
#show path of Waterfiltering
@app.route('/Waterfiltering', methods=['GET'])
def ShowWaterfiltering():
    row = Model.ShowimgWaterfiltering()
    return jsonify(datas=row)

#upload file Waterfiltering to database
@app.route('/img--Waterfiltering', methods=['POST'])
def insertimageWaterfiltering():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading img5')
        print(request.files['image'])
        print('image5 OK')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\Waterfiltering\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\Waterfiltering\\' + f.filename
            global c5 
            c5 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)


#Checklist1-6
#show path of DisinfectionWater
@app.route('/DisinfectionWater', methods=['GET'])
def ShowDisinfectionWater():
    row = Model.ShowimgDisinfectionWater()
    return jsonify(datas=row)

#upload file DisinfectionWater to database
@app.route('/img--DisinfectionWater', methods=['POST'])
def insertimageDisinfectionWater():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading img6')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\DisinfectionWater\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\DisinfectionWater\\' + f.filename
            global c6
            c6 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-7
#show path of Wateradjustment
@app.route('/Wateradjustment', methods=['GET'])
def ShowWateradjustment():
    row = Model.ShowimgWateradjustment()
    return jsonify(datas=row)

#upload file Wateradjustment to database
@app.route('/img--Wateradjustment', methods=['POST'])
def insertimageWateradjustment():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading img7')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\Wateradjustment\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\Wateradjustment\\' + f.filename
            global c7 
            c7 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)


#Checklist1-8
#show path of othermanagement
@app.route('/otherManagement', methods=['GET'])
def ShowotherManage():
    row = Model.ShowDocOtherManage()
    return jsonify(datas=row)

#upload file othermanagement to database
@app.route('/other--Management', methods=['POST'])
def insertFileotherManage():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading img8')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\OtherManagement\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\OtherManagement\\' + f.filename
            global c8 
            c8 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-9
#show path of ReportWasteWater
@app.route('/ReportWasteWater--file', methods=['GET'])
def ShowReportWater():
    row = Model.ShowDocReportWater()
    return jsonify(datas=row)

#upload file ReportWasteWater to database
@app.route('/docReport-waste-water', methods=['POST'])
def insertFileReportWater():
    print('....Try to Upload file....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['file']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_file(file.filename):
            f = request.files['file']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\ReportWasteWater\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\ReportWasteWater\\' + f.filename
            global c9 
            c9 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-10
#show path of waterquality
@app.route('/waterquality--file', methods=['GET'])
def ShowWaterQuality():
    row = Model.ShowDocWaterQuality()
    return jsonify(datas=row)

#upload file waterquality to database
@app.route('/document-of-water-quality', methods=['POST'])
def insertFileWaterQuality():
    print('....Try to Upload file....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['file']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_file(file.filename):
            f = request.files['file']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\WaterQuality\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\WaterQuality\\' + f.filename
            global c10 
            c10 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-11
#show path of CleanGrass
@app.route('/CleanGrass--pic', methods=['GET'])
def ShowCleanGrass():
    row = Model.ShowDocCleanGrass()
    return jsonify(datas=row)

#upload file CleanGrass
@app.route('/pic-of-Clean-Grass', methods=['POST'])
def insertFileCleanGrass():
    print('....Try to Upload Image....')
    if request.method == 'POST':
        print('Uploading image11')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\CleanGrass\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\CleanGrass\\' + f.filename
            global c11 
            c11 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-12
#show path of Equipmaintenance
@app.route('/Equipmaintenance--pic', methods=['GET'])
def ShowimgEquipmaintenance():
    row = Model.ShowEquipmaintenance()
    return jsonify(datas=row)

#upload file Equipmaintenance
@app.route('/pic-of-Equipmaintenance', methods=['POST'])
def insertimgEquipmaintenance():
    print('....Try to Upload Image....')
    if request.method == 'POST':
        print('Uploading image12')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\Equipmaintenance\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\Equipmaintenance\\' + f.filename
            global c12 
            c12 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-13
#show path of Implementation
@app.route('/Implementation--file', methods=['GET'])
def ShowImplementation():
    row = Model.ShowDocImplementation()
    return jsonify(datas=row)

#upload file Implementation to database
@app.route('/document-of-Implementation', methods=['POST'])
def insertFileImplementation():
    print('....Try to Upload file....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['file']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_file(file.filename):
            f = request.files['file']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\Implementation\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\Implementation\\' + f.filename
            global c13
            c13 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-14
#show path of PreparationofPonds
@app.route('/img--PreparationofPonds', methods=['GET'])
def ShowPreparationofPonds():
    row = Model.ShowDocPreparationofPonds()
    return jsonify(datas=row)

#upload file PreparationofPonds to database
@app.route('/image-of-Preparation--of--Ponds', methods=['POST'])
def insertFilePreparationofPonds():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading img14')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\PreparationofPonds\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\PreparationofPonds\\' + f.filename
            global c14
            c14 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)


#Checklist1-15
#show path of Cleaningequipment
@app.route('/Cleaningequipment--pic', methods=['GET'])
def ShowCleaningequipment():
    row = Model.ShowDocCleaningequipment()
    return jsonify(datas=row)

#upload file Cleaningequipment to database
@app.route('/image-of-Cleaning-equipment', methods=['POST'])
def insertFileCleaningequipment():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading img15')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\CleanEquipment\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\CleanEquipment\\' + f.filename
            global c15
            c15 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)


#Checklist1-16
#show path of aquatichealth
@app.route('/aquatichealth--pic', methods=['GET'])
def Showaquatichealth():
    row = Model.ShowDocaquatichealth()
    return jsonify(datas=row)

#upload file aquatichealth to database
@app.route('/image-of-aquatic-health', methods=['POST'])
def insertFileaquatichealth():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading img16')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\AquaticHealth\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\AquaticHealth\\' + f.filename
            global c16
            c16 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-17
#show path of Sending
@app.route('/Sending--pic', methods=['GET'])
def ShowimgSending():
    row = Model.ShowSending()
    return jsonify(datas=row)

#upload file Sending to database
@app.route('/image-of-Sending', methods=['POST'])
def insertSending():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading img17')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\Sending\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\Sending\\' + f.filename
            global c17
            c17 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-18
#show path of Carcass
@app.route('/Carcass--image', methods=['GET'])
def ShowCarcass():
    row = Model.ShowDocCarcass()
    return jsonify(datas=row)

#upload file Carcass to database
@app.route('/image-of-Carcass', methods=['POST'])
def insertCarcass():
    print('....Try to Upload img....')
    if request.method == 'POST':
        print('Uploading img18')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\Carcass\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\Carcass\\' + f.filename
            global c18
            c18 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-19
#show path of Wastewater
@app.route('/Wastewater--image', methods=['GET'])
def ShowWastewater():
    row = Model.ShowDocWastewater()
    return jsonify(datas=row)

#upload file Wastewater to database
@app.route('/image-of-Wastewater', methods=['POST'])
def insertFileWastewater():
    print('....Try to Upload image....')
    if request.method == 'POST':
        print('Uploading img19')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\1\\Wastewater\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\1\\Wastewater\\' + f.filename
            global c19
            c19 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist2-1
#show path of Toilet
@app.route('/Toilet--image', methods=['GET'])
def ShowimgToilet():
    row = Model.ShowToilet()
    return jsonify(datas=row)

#upload file Toilet to database
@app.route('/image-of-Toilet', methods=['POST'])
def insertimgToilet():
    print('....Try to Upload image....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\2\\Toilet\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\2\\Toilet\\' + f.filename
            global q1
            q1 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist2-2
#show path of Contamination
@app.route('/Contamination--image', methods=['GET'])
def ShowimgContamination():
    row = Model.ShowContamination()
    return jsonify(datas=row)

#upload file Contamination to database
@app.route('/image-of-Contamination', methods=['POST'])
def insertimgContamination():
    print('....Try to Upload image....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\2\\Contamination\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\2\\Contamination\\' + f.filename
            global q2
            q2 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist2-3
#show path of Garbage
@app.route('/Garbage--image', methods=['GET'])
def ShowimgGarbage():
    row = Model.ShowGarbage()
    return jsonify(datas=row)

#upload file Garbage to database
@app.route('/image-of-Garbage', methods=['POST'])
def insertimgGarbage():
    print('....Try to Upload image....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\2\\Garbage\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\2\\Garbage\\' + f.filename
            global q3
            q3 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist2-4
#show path of Scraping
@app.route('/Scraping--image', methods=['GET'])
def ShowimgScraping():
    row = Model.ShowScraping()
    return jsonify(datas=row)

#upload file Scraping to database
@app.route('/image-of-Scraping', methods=['POST'])
def insertimgScraping():
    print('....Try to Upload image....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\2\\Scraping\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\2\\Scraping\\' + f.filename
            global q4
            q4 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist2-5
#show path of Contagion
@app.route('/Contagion--image', methods=['GET'])
def ShowDocContagion():
    row = Model.ShowContagion()
    return jsonify(datas=row)

#upload image Contagion to database
@app.route('/Document-of-Contagion', methods=['POST'])
def insertDocContagion():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\2\\Contagion\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\2\\Contagion\\' + f.filename
            global q5
            q5 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist2-6
#show path of MD
@app.route('/MD--image', methods=['GET'])
def ShowMD():
    row = Model.ShowDocMD()
    return jsonify(datas=row)

#upload file MD to database
@app.route('/document-of-MD', methods=['POST'])
def insertFileMD():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading')
        for i in request.files:
            print(i)
        file = request.files['file']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_file(file.filename):
            f = request.files['file']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\2\\MD\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\2\\MD\\' + f.filename
            global q6
            q6 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist2-7
#show path of FMD
@app.route('/FMD--file', methods=['GET'])
def ShowFMD():
    row = Model.ShowDocFMD()
    return jsonify(datas=row)

#upload file FMD to database
@app.route('/document-of-FMD', methods=['POST'])
def insertFileFMD():
    print('....Try to Upload file....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['file']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_file(file.filename):
            f = request.files['file']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\2\\FMD\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\2\\FMD\\' + f.filename
            global q7
            q7 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist2-8
#show path of OtherMDFMD
@app.route('/OtherMDFMD--file', methods=['GET'])
def ShowOtherMDFMD():
    row = Model.ShowDocOtherMDFMD()
    return jsonify(datas=row)

#upload file OtherMDFMD to database
@app.route('/document-of-Other-MD-FMD', methods=['POST'])
def insertFileOtherMDFMD():
    print('....Try to Upload file....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['file']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_file(file.filename):
            f = request.files['file']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\2\\OtherMDFMD\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\2\\OtherMDFMD\\' + f.filename
            global q8
            q8 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist2-9
#show path of Aquaticmeat
@app.route('/Aquaticmeat--file', methods=['GET'])
def ShowAquaticmeat():
    row = Model.ShowDocAquaticmeat()
    return jsonify(datas=row)

#upload image Aquaticmeat to database
@app.route('/document-of-Aquaticmeat', methods=['POST'])
def insertFileAquaticmeat():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['file']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_file(file.filename):
            f = request.files['file']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\2\\Aquaticmeat\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\2\\Aquaticmeat\\' + f.filename
            global q9
            q9 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist3-1
#show path of WaterSource
@app.route('/WaterSource--image', methods=['GET'])
def ShowimgWaterSource():
    row = Model.ShowWaterSource()
    return jsonify(datas=row)

#upload image WaterSource to database
@app.route('/image-of-WaterSource', methods=['POST'])
def insertimgWaterSource():
    print('....Try to Upload image....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\3\\WaterSource\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\3\\WaterSource\\' + f.filename
            global q10
            q10 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist3-2
#show path of WaterQualitytest
@app.route('/WaterQualitytest--file', methods=['GET'])
def ShowWaterQualitytest():
    row = Model.ShowDocWaterQualitytest()
    return jsonify(datas=row)

#upload file WaterQualitytest to database
@app.route('/document-of-Water-Quality-test', methods=['POST'])
def insertFileWaterQualitytest():
    print('....Try to Upload file....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['file']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_file or allowed_image(file.filename):
            f = request.files['file']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\3\\WaterQualitytest\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\3\\WaterQualitytest\\' + f.filename
            global q11
            q11 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist3-3
#show path of Sourceofpollution
@app.route('/Sourceofpollution--image', methods=['GET'])
def ShowimgSourceofpollution():
    row = Model.ShowSourceofpollution()
    return jsonify(datas=row)

#upload image Sourceofpollution to database
@app.route('/image-of-Sourceofpollution', methods=['POST'])
def insertimgSourceofpollution():
    print('....Try to Upload image....')
    if request.method == 'POST':
        print('Uploading file')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\3\\Sourceofpollution\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\3\\Sourceofpollution\\' + f.filename
            global q12
            q12 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist3-4
#show path of Watertransfer
@app.route('/Watertransfer--pic', methods=['GET'])
def ShowWatertransfer():
    row = Model.ShowDocWatertransfer()
    return jsonify(datas=row)

#upload file Watertransfer to database
@app.route('/image-of-Water-transfer', methods=['POST'])
def insertFileWatertransfer():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\3\\Watertransfer\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\3\\Watertransfer\\' + f.filename
            global q13
            q13 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist3-5
#show path of Backup
@app.route('/Backup--pic', methods=['GET'])
def ShowimgBackup():
    row = Model.ShowBackup()
    return jsonify(datas=row)

#upload file Backup to database
@app.route('/image-of-Backup', methods=['POST'])
def insertBackup():
    print('....Try to Upload....')
    if request.method == 'POST':
        print('Uploading')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\KMITL\\Project Smart Farm\\GAP\\my-project\\src\\assets\\Checklist\\3\\Backup\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\Checklist\\3\\Backup\\' + f.filename
            global q14
            q14 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)




@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8081)