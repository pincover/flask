import os
from model import Model
from flask import Flask, request, redirect, jsonify
# from cleandata import read_files
from flask_cors import CORS

app = Flask('__name__')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

CORS(app)

Model = Model()

ALLOWED_EXTENSIONS = set(['jpg', 'png', 'BMP', 'EPS', 'PEG', 'GIF','PNG','JPG'])
ALLOWED_EXTENSIONS_File = set(['doc', 'docx', 'pdf',  'xlxs'])

v,v1,v2 = 'No','No','No'
q10,q11,q12,q13,q14,q15,q16,q17,q18,q19 = 0,0,0,0,0,0,0,0,0,0
x=''

def allowed_image(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_File


@app.route('/test2', methods=['GET'])
def test2():
    x = Model.test2()
    print(x)
    name=[x[0]]
    print('name =',name)
    return jsonify(name)

@app.route('/showEmp', methods=['POST'])
def showDataemp():
    id = request.get_json(['id']) 
    x = id['userid'] 
    a = Model.Showdata(x)
    return jsonify(a)

@app.route('/showFeed', methods=['POST'])
def showDatafeed():
    id = request.get_json(['Farmid'])
    x = id['Farmid'] 
    a = Model.Showdatafeed(x)
    return jsonify(a)

@app.route('/showEven', methods=['POST'])
def showDataeven():
    id = request.get_json(['Farmid'])
    x = id['Farmid'] 
    a = Model.ShowdataEven(x)
    return jsonify(a)

@app.route('/showFishpond', methods=['POST'])
def showFishpond():
    id = request.get_json(['Farmid'])
    x = id['Farmid']
    a = Model.ShowFishpond(x)
    return jsonify(a)


@app.route('/showNameFeed', methods=['POST'])
def showNamefeed():
    id = request.get_json(['Farmid'])
    x = id['Farmid']
    a = Model.ShowNamefeed(x)
    return jsonify(a)

@app.route('/showFood', methods=['POST'])
def showFood():
    id = request.get_json(['Farmid'])
    x = id['Farmid'] 
    a = Model.Showdatafood(x)
    return jsonify(a)

@app.route('/insertChLocation', methods=['POST'])
def insertDataChecklocation():
    print(request.is_json)
    req = request.get_json(['Datachlocation'])
    Fid = req['Farmid']
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
    Ch = Model.create1(Fid)
    DataCh1 = Model.insertDataLocation(Ch,b0,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,q10,q11,q12,q13,q14)
    return jsonify(DataCh1)

# @app.route('/', methods=['GET'])
    # def showData():
    #     row = Model.Showdata()
    #     return jsonify(row)

# showimg1
@app.route('/farmplan', methods=['GET'])
def showfarmplan():
    row = Model.ShowFarmplan()
    return jsonify(datas=row)

# upload image1 farm
@app.route('/img', methods=['POST'])
def insertfarmplan():
    print('....Try to Upload image....')
    if request.method == 'POST':
        print('Uploading image')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            img = request.files['image']
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\imgfarm1\\' + img.filename
            img = img.save(path)
            global v
            v = path
            print(v)
            print("Upload image Success")
            return jsonify(True)
        else:
            return jsonify(False)

# show path of file document registration Farm
@app.route('/docRegfarm', methods=['GET'])
def ShowRegFarm():
    row = Model.ShowDocRegFarm()
    return jsonify(datas=row)

# upload file document registration Farm
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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\filefarm\\' + f.filename
            f.save(path)
            global v1 
            v1 = path
            print(v1)
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

# showimg2 farm
@app.route('/showfarmimg2', methods=['GET'])
def showfarmimg2():
    row = Model.showfarmimg2()
    return jsonify(row)

# upload image2 Farm
@app.route('/img2', methods=['POST'])
def insertfarmimg2():
    print('....Try to Upload image....')
    if request.method == 'POST':
        print('Uploading image')
        for i in request.files:
            print(i)
        file = request.files['image']
        if file.filename == '':
            return jsonify(False)
        if file and allowed_image(file.filename):
            f = request.files['image']
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\imgfarm2\\' + f.filename
            f = f.save(path)
            global v2 
            v2 = path
            print("img2 =",v2)
            print("Upload image2 Success")
            return jsonify(True)
        else:
            return jsonify(False)

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

@app.route('/insert', methods=['POST'])
def insert():
    print(request.is_json)
    req = request.get_json(['obj'])
    a = req['FarmName']
    b = req['FarmOwner']
    b1 = req['FarmNumber']
    b2 = req['FarmGroup']
    b3 = req['FarmCanton']
    b4 = req['FarmDistrict']
    b5 = req['FarmProvince']
    b7 = req['Farmregistration']
    b8 = req['Documentfarm']
    b9 = req['Year']
    b10 = req['Startoperation']
    b11 = req['NumberOfYears']
    b12 = req['TotalFarmArea']
    b13 = req['Pond']
    b14 = req['NumberOfReservoirs']
    b15 = req['NumberOfAcresAndPondareas']
    b16 = req['Lenstorage']
    b17 = req['NumberOfLensStorage']
    b18 = req['NumberOfAcresAndLensStorage']
    b19 = req['SewagetreatmentSystem']
    b20 = req['Pondperiod']
    b21 = req['NumberofYearsOfOldDiggingwell']
    b22 = req['Culture']
    b23 = req['Allculturedareas']
    b24 = req['NumberofFloatingcages']
    b25 = req['Lastyearfarmoutput']
    b26 = req['PastInvestmentSituation']
    b27 = req['Farmstatus']
    b6 = req['lattitube']
    b28 = req['longtitube']
    print('req =',v)
    ins = Model.insert(v,v1,v2,a,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28)
    return jsonify(ins)

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
    a = Model.FarmnametoId(a1)
    x = Model.insertEmp(a,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16)
    return jsonify(x)

@app.route('/insertFeed', methods=['POST'])
def insertFeed():
    req = request.get_json(['Datafeed'])
    a = req['Farmid']
    b = req['type']
    b1 = req['FoodforCulture']
    b2 = req['FoodNumber']
    b3 = req['Productiondate']
    b4 = req['expdate']
    b5 = req['Physicalconditionoffood']
    b6 = req['FrequencyofOrderingfood']
    x = Model.insertFeed(b,b1,b2,b3,b4,b5,b6,a)
    print(x)
    return jsonify(True)

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
    a  = req['Farmid']
    x = Model.insertFishtype(b3)
    print('x =',x)
    # x=FTNO
    check = Model.CheckPond(b1,b,a,b2)
    print('check =',check)
    if(check == 1):
        return jsonify(False)
    else:
        Model.insertPond(b1,b,a,b2)
    c = Model.FindpondNo(b1,a)
    print('c =',c)
    # c=FPNO
    z = Model.insertLot(b5,b4,c,x,b6,b7)
    print('z =',z)
    return jsonify(z)

@app.route('/insertEven', methods=['POST'])
def insertEven():
    print(request.is_json)
    req = request.get_json(['obj'])
    # FPNO
    b = req['pondsaffectedbyexternalfactors']
    a = req['Farmid']
    b1 = req['DayMonthYear']
    b2 = req['Factorsproblems']
    b3 = req['ImpactofExternal']
    b4 = req['NameofResponsibleperson']
    b5 = req['SurnameofResponsibleperson']
    b6 = req['Howtosolvetheproblem']
    b7 = req['DayMonthYearstart']
    b8 = req['DayMonthYearstop']
    Empid = Model.FindEmp(b4,b5)
    pondno = Model.FindPond(b,a)
    EVNO = Model.insertEven(b1,b2,b3,pondno,Empid)
    Model.inserttreatment(EVNO,b6,b7,b8)
    return jsonify(True)

@app.route('/insertFood', methods=['POST'])
def insertDatagivefeed():
    req = request.get_json(['Datagivefeed'])
    a = req['Farmid']
    b = req['Typeproduct']
    b1 = req['Nameproduct']
    b2 = req['time']
    b3 = req['volume']
    b4 = req['RoundNo']
    b5 = req['PondNo']
    pondno = Model.FindPondFood(b5,a,b4)
    print('pondno=',pondno)
    x = Model.selectFLNO(b4,pondno)
    print('FLNO=',pondno)
    # x=FLNO
    m = Model.FindMTNO(b1,b)
    print('MTNO=',pondno)
    # m=MTNO
    z = Model.insertfishmanagement(x,m,b,b2,b3)
    return jsonify(z)

#Checklist1-1
 #show path of Soil
 # @app.route('/Soil', methods=['GET'])
 # def ShowSoil():
 #     row = Model.ShowimgSoil()
 #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\management\\timageSoil\\' + f.filename
            f.save(path)
            path2 = '..\\assets\\file\\management\\timageSoil\\' + f.filename
            global c1 
            c1 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-2
    #show path of ExtermAquatic
    # @app.route('/ExtermAquatic', methods=['GET'])
    # def ShowExtermAquatic():
    #     row = Model.ShowimgExtermAquatic()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\management\\ExtermAquatic\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\file\\management\\ExtermAquatic\\' + f.filename
            global c2 
            c2 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-3
    #show path of Disinfection
    # @app.route('/Disinfection', methods=['GET'])
    # def ShowDisinfection():
    #     row = Model.ShowimgDisinfection()
    #     return jsonify(datas=row)

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
    # @app.route('/otheractionfile', methods=['GET'])
    # def Showotheraction():
    #     row = Model.ShowDocOtherAct()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\management\\documentofotheraction\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\management\\documentofotheraction\\' + f.filename
            global c4 
            c4 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-5
    #show path of Waterfiltering
    # @app.route('/Waterfiltering', methods=['GET'])
    # def ShowWaterfiltering():
    #     row = Model.ShowimgWaterfiltering()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\management\\Waterfiltering\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\management\\Waterfiltering\\' + f.filename
            global c5 
            c5 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)


#Checklist1-6
    #show path of DisinfectionWater
    # @app.route('/DisinfectionWater', methods=['GET'])
    # def ShowDisinfectionWater():
    #     row = Model.ShowimgDisinfectionWater()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\management\\ExtermAquatic\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\management\\ExtermAquatic\\' + f.filename
            global c6
            c6 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-7
    #show path of Wateradjustment
    # @app.route('/Wateradjustment', methods=['GET'])
    # def ShowWateradjustment():
    #     row = Model.ShowimgWateradjustment()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\management\\Wateradjustment\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\management\\Wateradjustment\\' + f.filename
            global c7 
            c7 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)


#Checklist1-8
    #show path of othermanagement
    # @app.route('/otherManagement', methods=['GET'])
    # def ShowotherManage():
    #     row = Model.ShowDocOtherManage()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\management\\OtherManagement\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\management\\OtherManagement\\' + f.filename
            global c8 
            c8 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-9
    #show path of ReportWasteWater
    # @app.route('/ReportWasteWater--file', methods=['GET'])
    # def ShowReportWater():
    #     row = Model.ShowDocReportWater()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\management\\ReportWasteWater\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\management\\ReportWasteWater\\' + f.filename
            global c9 
            c9 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-10
    #show path of waterquality
    # @app.route('/waterquality--file', methods=['GET'])
    # def ShowWaterQuality():
    #     row = Model.ShowDocWaterQuality()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\management\\WaterQuality\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\management\\WaterQuality\\' + f.filename
            global c10 
            c10 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-11
    #show path of CleanGrass
    # @app.route('/CleanGrass--pic', methods=['GET'])
    # def ShowCleanGrass():
    #     row = Model.ShowDocCleanGrass()
    #     return jsonify(datas=row)

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
    # @app.route('/Equipmaintenance--pic', methods=['GET'])
    # def ShowimgEquipmaintenance():
    #     row = Model.ShowEquipmaintenance()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\management\\Equipmaintenance\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\management\\Equipmaintenance\\' + f.filename
            global c12 
            c12 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-13
    #show path of Implementation
    # @app.route('/Implementation--file', methods=['GET'])
    # def ShowImplementation():
    #     row = Model.ShowDocImplementation()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\management\\Implementation\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\management\\Implementation\\' + f.filename
            global c13
            c13 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist1-14
    #show path of PreparationofPonds
    # @app.route('/img--PreparationofPonds', methods=['GET'])
    # def ShowPreparationofPonds():
    #     row = Model.ShowDocPreparationofPonds()
    #     return jsonify(datas=row)

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
    # @app.route('/Cleaningequipment--pic', methods=['GET'])
    # def ShowCleaningequipment():
    #     row = Model.ShowDocCleaningequipment()
    #     return jsonify(datas=row)

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
    # @app.route('/aquatichealth--pic', methods=['GET'])
    # def Showaquatichealth():
    #     row = Model.ShowDocaquatichealth()
    #     return jsonify(datas=row)

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
    # @app.route('/Sending--pic', methods=['GET'])
    # def ShowimgSending():
    #     row = Model.ShowSending()
    #     return jsonify(datas=row)

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
    # #show path of Carcass
    # @app.route('/Carcass--image', methods=['GET'])
    # def ShowCarcass():
    #     row = Model.ShowDocCarcass()
    #     return jsonify(datas=row)

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
    # @app.route('/Wastewater--image', methods=['GET'])
    # def ShowWastewater():
    #     row = Model.ShowDocWastewater()
    #     return jsonify(datas=row)

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
    # @app.route('/Toilet--image', methods=['GET'])
    # def ShowimgToilet():
    #     row = Model.ShowToilet()
    #     return jsonify(datas=row)

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
    # @app.route('/Contamination--image', methods=['GET'])
    # def ShowimgContamination():
    #     row = Model.ShowContamination()
    #     return jsonify(datas=row)

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
    # @app.route('/Garbage--image', methods=['GET'])
    # def ShowimgGarbage():
    #     row = Model.ShowGarbage()
    #     return jsonify(datas=row)

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
    # @app.route('/Scraping--image', methods=['GET'])
    # def ShowimgScraping():
    #     row = Model.ShowScraping()
    #     return jsonify(datas=row)

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
    # @app.route('/Contagion--image', methods=['GET'])
    # def ShowDocContagion():
    #     row = Model.ShowContagion()
    #     return jsonify(datas=row)

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
    # @app.route('/MD--image', methods=['GET'])
    # def ShowMD():
    #     row = Model.ShowDocMD()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\harvesting\\MD\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\harvesting\\MD' + f.filename
            global q6
            q6 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist2-7
    #show path of FMD
    # @app.route('/FMD--file', methods=['GET'])
    # def ShowFMD():
    #     row = Model.ShowDocFMD()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\harvesting\\FMD\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\harvesting\\FMD\\' + f.filename
            global q7
            q7 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist2-8
    #show path of OtherMDFMD
    # @app.route('/OtherMDFMD--file', methods=['GET'])
    # def ShowOtherMDFMD():
    #     row = Model.ShowDocOtherMDFMD()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\harvesting\\OtherMDFMD\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\harvesting\\OtherMDFMD\\' + f.filename
            global q8
            q8 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist2-9
    #show path of Aquaticmeat
    # @app.route('/Aquaticmeat--file', methods=['GET'])
    # def ShowAquaticmeat():
    #     row = Model.ShowDocAquaticmeat()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\harvesting\\Aquaticmeat\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\harvesting\\Aquaticmeat\\' + f.filename
            global q9
            q9 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist3-1
    #show path of WaterSource
    # @app.route('/WaterSource--image', methods=['GET'])
    # def ShowimgWaterSource():
    #     row = Model.ShowWaterSource()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\location\\imgWaterSource\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\location\\imgWaterSource\\' + f.filename
            global q10
            q10 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist3-2
    #show path of WaterQualitytest
    # @app.route('/WaterQualitytest--file', methods=['GET'])
    # def ShowWaterQualitytest():
    #     row = Model.ShowDocWaterQualitytest()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\location\\FileWaterQualitytest\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\file\\location\\FileWaterQualitytest\\' + f.filename
            global q11
            q11 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist3-3
    #show path of Sourceofpollution
    # @app.route('/Sourceofpollution--image', methods=['GET'])
    # def ShowimgSourceofpollution():
    #     row = Model.ShowSourceofpollution()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\location\\imgSourceofpollution\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\img\\location\\imgSourceofpollution\\' + f.filename
            global q12
            q12 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist3-4
    #show path of Watertransfer
    # @app.route('/Watertransfer--pic', methods=['GET'])
    # def ShowWatertransfer():
    #     row = Model.ShowDocWatertransfer()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\location\\FileWatertransfer\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\file\\location\\FileWatertransfer\\' + f.filename
            global q13
            q13 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)

#Checklist3-5
    #show path of Backup
    # @app.route('/Backup--pic', methods=['GET'])
    # def ShowimgBackup():
    #     row = Model.ShowBackup()
    #     return jsonify(datas=row)

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
            path = 'D:\\Project-P4 V.1\\my-project\\src\\assets\\img\\location\\Backup\\' + f.filename
            f.save(path)
            path2 = '..\\src\\assets\\file\\location\\Backup\\' + f.filename
            global q14
            q14 = path2
            print("Upload Success")
            return jsonify(True)
        else:
            return jsonify(False)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response

print(v)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8081)
