import pymysql
import os
class Model:
    conn=pymysql.Connect('localhost','root','','farmgaptest')
    def loginid(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("select Email,Password from Employee")
            rows = cur.fetchall()
            print(rows)
        return rows

    def checkuname(self,u):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("select Emp_ID,FarmID,RoleID from Employee where Email = %s",(u))
            rows = cur.fetchall()
            print("id =",rows)
        return rows    

    def cheack(self,u,p,x):
        total=0
        for i in x :
            if(u == i[0] and p == i[1]) :
                total = 1
                break
            else:
                print ("False")
        return total

    def Showdata(self,x):
        with self.conn:
            cur = self.conn.cursor()
            row = cur.execute("select * from employee where Emp_ID=%s",(x) )
            row = cur.fetchall()
        return row

    def create1(self,x):
        with self.conn:
            cur = self.conn.cursor()
            row = cur.execute("Insert into `checklist` (`Nameofchecklist`,`FarmID`) values('สถานที่',%s)",(x))
            self.conn.commit()
            cur.execute("select MAX(No) from checklist where Nameofchecklist='สถานที่' AND FarmID=%s",(x))
            row = cur.fetchall()
            self.conn.commit()
        return row

    def create2(self,x):
        with self.conn:
            cur = self.conn.cursor()
            row = cur.execute("Insert into `checklist` (`Nameofchecklist`,`FarmID`) values('การจัดการฟาร์ม',%s)",(x))
            self.conn.commit()
            cur.execute("select MAX(No) from checklist where Nameofchecklist='การจัดการฟาร์ม' AND FarmID=%s",(x))
            row = cur.fetchall()
            self.conn.commit()
        return row

    def create3(self,x):
        with self.conn:
            cur = self.conn.cursor()
            row = cur.execute("Insert into `checklist` (`Nameofchecklist`,`FarmID`) values('การจัดการดูแลสุขภาพสัตว์น้ำ',%s)",(x))
            self.conn.commit()
            cur.execute("select MAX(No) from checklist where Nameofchecklist='การจัดการดูแลสุขภาพสัตว์น้ำ' AND FarmID=%s",(x))
            row = cur.fetchall()
            self.conn.commit()
        return row

    def create4(self,x):
        with self.conn:
            cur = self.conn.cursor()
            row = cur.execute("Insert into `checklist` (`Nameofchecklist`,`FarmID`) values('สุขลักษณะฟาร์ม',%s)",(x))
            self.conn.commit()
            cur.execute("select MAX(No) from checklist where Nameofchecklist='สุขลักษณะฟาร์ม' AND FarmID=%s",(x))
            row = cur.fetchall()
            self.conn.commit()
        return row

    def create5(self,x):
        with self.conn:
            cur = self.conn.cursor()
            row = cur.execute("Insert into `checklist` (`Nameofchecklist`,`FarmID`) values('การเก็บเกี่ยวและการขนส่ง',%s)",(x))
            self.conn.commit()
            cur.execute("select MAX(No) from checklist where Nameofchecklist='การเก็บเกี่ยวและการขนส่ง' AND FarmID=%s",(x))
            row = cur.fetchall()
            self.conn.commit()
        return row

    def insertDataLocation(self,Ch,b0,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,q10,q11,q12,q13,q14):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'แหล่งน้ำที่ใช้',%s)",(Ch,q10))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ปริมาณน้ำ',%s)",(Ch,b0))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ผลตรวจคุณภาพน้ำ',%s)",(Ch,q11))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'แหล่งกำเนิดมลพิษ',%s)",(Ch,b))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปแหล่งกำเนิดมลพิษ',%s)",(Ch,q12))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ระยะห่าง',%s)",(Ch,b1))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ฟาร์มสามารถถ่ายเทน้ำได้',%s)",(Ch,b2))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการถ่ายเทน้ำ',%s)",(Ch,q13))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การคมนาคม',%s)",(Ch,b3))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ถนนภายในฟาร์ม',%s)",(Ch,b4))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'มีสาธารณูปโภคที่จำเป็น',%s)",(Ch,b5))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ไฟฟ้า',%s)",(Ch,b6))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'เฟสของไฟฟ้า',%s)",(Ch,b7))
            self.conn.commit()


            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'น้ำใช้',%s)",(Ch,b8))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ระบุน้ำที่ใช้',%s)",(Ch,b9))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'อื่นๆ',%s)",(Ch,b10))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ระบุอื่นๆ',%s)",(Ch,b11))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ระบบสำรอง',%s)",(Ch,b12))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูประบบสำรอง',%s)",(Ch,q14))
            self.conn.commit()

            row = cur.fetchall()
            print(row)
        return row

#ส่งข้อมูล Checklist-ManageFarm
    def insertDataManage(self,Ch,b0,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การปรับสภาพดินก้นบ่อ',%s)",(Ch,b0))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการปรับสภาพดิน',%s)",(Ch,c1))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การกำจัดศัตรูสัตว์น้ำ',%s)",(Ch,b))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการกำจัดศัตรูสัตว์น้ำ',%s)",(Ch,c2))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การฆ่าเชื้อโรคจากศัตรูสัตว์น้ำ',%s)",(Ch,b1))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการฆ่าเชื้อโรคจากศัตรูสัตว์น้ำ',%s)",(Ch,c3))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การปฏิบัติอื่นๆ',%s)",(Ch,b2))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการปฏิบัติ',%s)",(Ch,c4))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การกรองน้ำก่อนเข้าบ่อ',%s)",(Ch,b3))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการกรองน้ำก่อนเข้าบ่อ',%s)",(Ch,c5))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การฆ่าเชื้อโรค',%s)",(Ch,b4))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการฆ่าเชื้อโรค',%s)",(Ch,c6))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การปรับคุณภาพน้ำ',%s)",(Ch,b5))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการปรับคุณภาพน้ำ',%s)",(Ch,c7))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การจัดการอื่นๆ',%s)",(Ch,b6))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการจัดการ',%s)",(Ch,c8))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'จำนวนลูกพันธุ์',%s)",(Ch,b7))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การทิ้งน้ำออกจากฟาร์ม',%s)",(Ch,b8))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รายงานน้ำทิ้ง',%s)",(Ch,b9))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปรายงานน้ำทิ้ง',%s)",(Ch,c9))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ผลวิเคราะห์คุณภาพน้ำทิ้ง',%s)",(Ch,b10))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปผลวิเคราะห์คุณภาพน้ำทิ้ง',%s)",(Ch,c10))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ข้อร้องเรียนจากฟาร์ม/ชุมชนข้างเคียง',%s)",(Ch,b11))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ความสะอาดหญ้ารอบบ่อ',%s)",(Ch,b12))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปความสะอาดหญ้ารอบบ่อ',%s)",(Ch,c11))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'อุปกรณ์ ความสะอาด/การดูแล',%s)",(Ch,b13))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการดูแลอุปกรณ์',%s)",(Ch,c12))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ป้องกันไม่ให้มีการปนเปื้อนของมูลสัตว์ลงในบ่อเลี้ยง',%s)",(Ch,b14))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ไม่ใช้มูลสัตว์สดในขั้นตอนการเลี้ยงสัตว์น้ำ',%s)",(Ch,b15))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปขั้นตอนในการนำมูลสัตว์สดมาใช้',%s)",(Ch,c13))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'สถานที่จัดเก็บ',%s)",(Ch,b16))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ภาชนะที่ใช้',%s)",(Ch,b17))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'สภาพสถานที่จัดเก็บ',%s)",(Ch,b18))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'แท่นรองปัจจัยการผลิตกันความชื้น',%s)",(Ch,b19))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การจัดเก็บ',%s)",(Ch,b20))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การจัดวาง',%s)",(Ch,b21))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ระบบกำจัดสัตว์ที่เป็นพาหะนำโรค/สัตว์อื่นๆ',%s)",(Ch,b22))
            self.conn.commit()

            row = cur.fetchall()
            print(row)
        return row

    #ส่งข้อมูล Checklist-health
    def insertDatahealth(self,Ch,b1,b2,b3,b4,b5,b6,b7,b8,b9,c14,c15,c16,c17,c18,c19):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'มีการเตรียมบ่อที่ถูกวิธี',%s)",(Ch,b1))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการเตรียมบ่อ',%s)",(Ch,c14))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การทำความสะอาดอุปกรณ์/เครื่องมือ',%s)",(Ch,b2))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการทำความสะอาดอุปกรณ์/เครื่องมือ',%s)",(Ch,c15))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'มีการเฝ้าระวังสุขภาพสัตว์น้ำ',%s)",(Ch,b3))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการเฝ้าระวังสุขภาพสัตว์น้ำ',%s)",(Ch,c16))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'เมื่อสัตว์น้ำมีอาการผิดปกติมีการจัดการ',%s)",(Ch,b4))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การจัดการอื่นๆ',%s)",(Ch,b5))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การส่งสัตว์น้ำตรวจก่อนใช้ยา/สารเคมี',%s)",(Ch,b6))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการส่งสัตว์น้ำตรวจก่อนใช้ยา/สารเคมี',%s)",(Ch,c17))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การแจ้งเหตุ',%s)",(Ch,b7))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'วิธีการจัดการซาก',%s)",(Ch,b8))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปวิธีการจัดการซาก',%s)",(Ch,c18))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'วิธีการจัดการน้ำทิ้งเมื่อเกิดการระบาดของโรค',%s)",(Ch,b9))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปวิธีการจัดการน้ำทิ้งเมื่อเกิดการระบาดของโรค',%s)",(Ch,c19))
            self.conn.commit()

            row = cur.fetchall()
            print(row)
        return row
    
    #ส่งข้อมูล Checklist-hygiene
    def insertDataHygiene(self,Ch,b0,b,b1,b2,b3,b4,b5,b6,b7,q1,q2,q3,q4,q5):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การแยกระบบระบายน้ำ',%s)",(Ch,b0))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ความสะอาด',%s)",(Ch,b))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การแยกห้องน้ำ/สุขา',%s)",(Ch,b1))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปห้องน้ำ/สุขา',%s)",(Ch,q1))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'สุขอนามัยของห้องน้ำ/ห้องสุขา',%s)",(Ch,b2))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การปนเปื้อนลงสู่บ่อ/แหล่งน้ำใช้',%s)",(Ch,b3))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการปนเปื้อนลงสู่บ่อ/แหล่งน้ำใช้',%s)",(Ch,q2))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ระบบจัดเก็บ/กำจัดขยะ',%s)",(Ch,b4))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูประบบการกำจัดขยะแบบอื่นๆ',%s)",(Ch,q3))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การคุ้ยเขี้ยของสัตว์เลี้ยงในฟาร์ม',%s)",(Ch,b5))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปการคุ้ยเขี้ยของสัตว์เลี้ยงในฟาร์ม',%s)",(Ch,q4))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'พาหะนำโรค',%s)",(Ch,b6))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปพาหะนำโรค',%s)",(Ch,q5))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'วิธีการป้องกัน',%s)",(Ch,b7))
            self.conn.commit()

            row = cur.fetchall()
            print(row)
        return row

    #ส่งข้อมูล Checklist-Harvest
    def insertDataharvesting(self,Ch,b0,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,q6,q7,q8,q9):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การจับ',%s)",(Ch,b1))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การจับสัตว์น้ำ',%s)",(Ch,b2))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'แผนการจับสัตว์น้ำ',%s)",(Ch,b3))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ระบุแผนการจับ',%s)",(Ch,b4))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การทำความสะอาดสัตว์หลังการจับ',%s)",(Ch,b5))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'พื้นที่จับและคัดแยก',%s)",(Ch,b6))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รายละเอียดของการคัดแยก',%s)",(Ch,b7))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'MD',%s)",(Ch,b8))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูป MD',%s)",(Ch,q6))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'FMD',%s)",(Ch,b9))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูป FMD',%s)",(Ch,q7))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปหลักฐานประกอบอื่นๆ',%s)",(Ch,q8))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'รูปแบบการจำหน่าย',%s)",(Ch,b10))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'การขนส่ง',%s)",(Ch,b11))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'วิธีการและการรักษาอุุณหภูมิ',%s)",(Ch,b12))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'ผลตรวจเนื้อสัตว์น้ำ',%s)",(Ch,b13))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`CNo`,`Namelist`,`value`) values(%s,'เอกสารหลักฐาน',%s)",(Ch,q9))
            self.conn.commit()

            row = cur.fetchall()
            print(row)
        return row

#upload path of image1(FarmPlan)
    def insertPathforFarmplan(self,path):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("Insert into `farm` (`FarmPlan`) values(%s)",(path))
            rows = cur.fetchall()
            self.conn.commit()
            print(rows)
            a = True
        return a
#Show path image FarmPlan
    def ShowFarmplan(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("select FarmPlan from farm")
            row = cur.fetchall()
        return row

#upload path image2(FarmPlan)
    def insertPathimg2(self,path):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("Insert into `farm` (`SewageImage`) values(%s)",(path))
            rows = cur.fetchall()
            self.conn.commit()
            print(rows)
            a = True
        return a

#Show path image2 Farm
    def showfarmimg2(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("select SewageImage from farm")
            row = cur.fetchall()
        return row

#upload path of Document file registration farm to database 
    def insertPathforRegFarm(self,path):
        with self.conn:
            p=path
            cur = self.conn.cursor()
            print('ok')
            print(p)
            cur.execute("Insert into `farm` (`File`) values(%s)",(p))
            print('ok2')
            rows = cur.fetchall()
            self.conn.commit()
            print(rows)
            a = True
        return a

#show path of ducument file 
    def ShowDocRegFarm(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("select File from farm")
            row = cur.fetchall()
        return row

# insertdataoffarm
    def insert(self,v,v1,v2,a,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28):
            with self.conn:
                cur = self.conn.cursor()
                cur.execute("Insert into `farm` (`FarmPlan`,`File`,`SewageSystem`,`Farmname`,`FarmOwnName`,`FarmNo`,`Moo`,`Tambon`,`Amphure`,`Province`,`lattitube`,`longtitube`,`Registration`,`Document`,`StartOperation`,`Ownership`,`Year`,`Area`,`Clarifier`,`NumberofCarifier`,`AreaofCarifier`,`StorageTank`,`NumberofStorTank`,`AreaofStorTank`,`Sewage`,`Pondbreed`,`YearofPondBreed`,`Culture`,`CultArea`,`NumofCulture`,`LastYearProduct`,`PastInvestment`,`FarmStatus`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(v,v1,v2,a,b,b1,b2,b3,b4,b5,b6,b28,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27))
                self.conn.commit()
                cur.execute("select MAX(ID) from Farm")
                row = cur.fetchall()
                print(row)
            return row
# insert ch1
    def insertDatachecklist1(self,Ch,b0,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การปรับสภาพดินก้นบ่อ',%s)",(Ch,b0))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปการปรับสภาพดิน',%s)",(Ch,c1))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การกำจัดศัตรูสัตว์น้ำ',%s)",(Ch,b))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปการกำจัดศัตรูสัตว์น้ำ',%s)",(Ch,c2))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การฆ่าเชื้อโรคจากศัตรูสัตว์น้ำ',%s)",(Ch,b1))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปการฆ่าเชื้อโรคจากศัตรูสัตว์น้ำ',%s)",(Ch,c3))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การปฏิบัติอื่นๆ',%s)",(Ch,b2))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปการปฏิบัติ',%s)",(Ch,c4))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การกรองน้ำก่อนเข้าบ่อ',%s)",(Ch,b3))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปการกรองน้ำก่อนเข้าบ่อ',%s)",(Ch,c5))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การฆ่าเชื้อโรค',%s)",(Ch,b4))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปการฆ่าเชื้อโรค',%s)",(Ch,c6))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การปรับคุณภาพน้ำ',%s)",(Ch,b5))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปการปรับคุณภาพน้ำ',%s)",(Ch,c7))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การจัดการอื่นๆ',%s)",(Ch,b6))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปการจัดการ',%s)",(Ch,c8))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'จำนวนลูกพันธุ์',%s)",(Ch,b7))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การทิ้งน้ำออกจากฟาร์ม',%s)",(Ch,b8))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รายงานน้ำทิ้ง',%s)",(Ch,b9))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปรายงานน้ำทิ้ง',%s)",(Ch,c9))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'ผลวิเคราะห์คุณภาพน้ำทิ้ง',%s)",(Ch,b10))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปผลวิเคราะห์คุณภาพน้ำทิ้ง',%s)",(Ch,c10))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'ข้อร้องเรียนจากฟาร์ม/ชุมชนข้างเคียง',%s)",(Ch,b11))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'ความสะอาดหญ้ารอบบ่อ',%s)",(Ch,b12))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปความสะอาดหญ้ารอบบ่อ',%s)",(Ch,c11))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'อุปกรณ์ ความสะอาด/การดูแล',%s)",(Ch,b13))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปการดูแลอุปกรณ์',%s)",(Ch,c12))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'ป้องกันไม่ให้มีการปนเปื้อนของมูลสัตว์ลงในบ่อเลี้ยง',%s)",(Ch,b14))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'ไม่ใช้มูลสัตว์สดในขั้นตอนการเลี้ยงสัตว์น้ำ',%s)",(Ch,b15))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปขั้นตอนในการนำมูลสัตว์สดมาใช้',%s)",(Ch,c13))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'สถานที่จัดเก็บ',%s)",(Ch,b16))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'ภาชนะที่ใช้',%s)",(Ch,b17))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'สภาพสถานที่จัดเก็บ',%s)",(Ch,b18))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'แท่นรองปัจจัยการผลิตกันความชื้น',%s)",(Ch,b19))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การจัดเก็บ',%s)",(Ch,b20))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การจัดวาง',%s)",(Ch,b21))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'ระบบกำจัดสัตว์ที่เป็นพาหะนำโรค/สัตว์อื่นๆ',%s)",(Ch,b22))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'มีการเตรียมบ่อที่ถูกวิธี',%s)",(Ch,b23))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปการเตรียมบ่อ',%s)",(Ch,c14))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การทำความสะอาดอุปกรณ์/เครื่องมือ',%s)",(Ch,b24))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปการทำความสะอาดอุปกรณ์/เครื่องมือ',%s)",(Ch,c15))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'มีการเฝ้าระวังสุขภาพสัตว์น้ำ',%s)",(Ch,b25))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปการเฝ้าระวังสุขภาพสัตว์น้ำ',%s)",(Ch,c16))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'เมื่อสัตว์น้ำมีอาการผิดปกติมีการจัดการ',%s)",(Ch,b26))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การจัดการอื่นๆ',%s)",(Ch,b27))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การส่งสัตว์น้ำตรวจก่อนใช้ยา/สารเคมี',%s)",(Ch,b28))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปการส่งสัตว์น้ำตรวจก่อนใช้ยา/สารเคมี',%s)",(Ch,c17))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'การแจ้งเหตุ',%s)",(Ch,b29))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'วิธีการจัดการซาก',%s)",(Ch,b30))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปวิธีการจัดการซาก',%s)",(Ch,c18))
            self.conn.commit()

            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'วิธีการจัดการน้ำทิ้งเมื่อเกิดการระบาดของโรค',%s)",(Ch,b31))
            self.conn.commit()
            cur.execute("Insert into `Checklistdetail` (`C-No`,`Namelist`,`value`) values(%s,'รูปวิธีการจัดการน้ำทิ้งเมื่อเกิดการระบาดของโรค',%s)",(Ch,c19))
            self.conn.commit()


            row = cur.fetchall()
            print(row)
        return row
# insert ch 2

    def insertOwn(self,a,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16):
            with self.conn:
                cur = self.conn.cursor()
                cur.execute("Insert into `employee` (`Emp_ID`,`FName_th`,`LName_th`,`FName_en`,`LName_en`,`Date`,`Tel`,`LineID`,`Email`,`HouseNo`,`Moo`,`Soi`,`Road`,`Tambon`,`Amphure`,`Province`,`Password`,`FarmID`,`RoleID`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(b6,b2,b3,b4,b5,b7,b8,b9,b,b10,b11,b12,b13,b14,b15,b16,b1,a,1))
                self.conn.commit()
                row = cur.fetchall()
                print(row)
            return row

    def FarmnametoId(self,a1):
            with self.conn:
                cur = self.conn.cursor()
                cur.execute("select ID from farm where Farmname=%s",(a1))
                row = cur.fetchall()
                print(row)
            return row 

    def insertEmp(self,a,b,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16):
            with self.conn:
                cur = self.conn.cursor()
                cur.execute("Insert into `employee` (`Emp_ID`,`FName_th`,`LName_th`,`FName_en`,`LName_en`,`Date`,`Tel`,`LineID`,`Email`,`HouseNo`,`Moo`,`Soi`,`Road`,`Tambon`,`Amphure`,`Province`,`Password`,`FarmID`,`RoleID`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(b6,b2,b3,b4,b5,b7,b8,b9,b,b10,b11,b12,b13,b14,b15,b16,b1,a,2))
                self.conn.commit()
                row = cur.fetchall()
                print(row)
            return row

    def insertFeed(self,b,b1,b2,b3,b4,b5,b6,a):
            with self.conn:
                cur = self.conn.cursor()
                cur.execute("Insert into `managementtype` (`Name`,`NameType`,`Register`,`InspectionResults`,`MonthlyPurchaseRate`,`Startdate`,`Enddate`,`farmid`) values(%s,%s,%s,%s,%s,%s,%s,%s)",(b1,b,b2,b5,b6,b3,b4,a))
                self.conn.commit()
                row = cur.fetchall()
                print(row)
            return row
    
    def insertFishtype(self,b3):
            with self.conn:
                cur = self.conn.cursor()
                cur.execute("Insert into `fishtype` (`FishName`) values(%s)",(b3))
                self.conn.commit()
                cur.execute("select No from fishtype where FishName=%s",(b3))
                row = cur.fetchone()
                print(row)
            return row

    def CheckPond(self,b1,b,a,b2):
            with self.conn:
                row = '()'
                print('a=',a,'b1=',b1,'b=',b,'b2=',b2,'row =',row)
                cur = self.conn.cursor()
                cur.execute("SELECT PondNo,FarmID From fishpond WHERE PondNo=%s and PondType=%s and FarmID=%s and Size=%s",(b1,b,a,b2))
                row = cur.fetchall()
                print(row)               
                total = 0
                if (row == () ):
                    total = 0
                    print("Neverdata")  
                else:
                     total = 1
                print('total =',total)
            return total

    def insertPond(self,b1,b,a,b2):
            with self.conn:
                print('a=',a,'b1=',b1,'b=',b,'b2=',b2)
                cur = self.conn.cursor()
                cur.execute("Insert into `fishpond` (`PondNo`,`PondType`,`FarmID`,`Size`) values(%s,%s,%s,%s)",(b1,b,a,b2))
                self.conn.commit()
                row = cur.fetchall()
                print(row)
            return True

    def FindpondNo(self,b1,a):
                with self.conn:
                    cur = self.conn.cursor()
                    cur.execute("select No from fishpond where PondNo=%s and FarmID=%s",(b1,a))
                    row = cur.fetchone()
                    print(row)
                return row

    def insertLot(self,b5,b4,c,x,b6,b7):
            with self.conn:
                cur = self.conn.cursor()
                cur.execute("Insert into `fishlot` (`NumberofDays`,`Round`,`FPNo`,`FTNo`,`Startdate`,`Enddate`) values(%s,%s,%s,%s,%s,%s)",(b5,b4,c,x,b6,b7))
                self.conn.commit()
                # cur.execute("select Max(No) from fishlot ")
                row = cur.fetchall()
                print(row)
            return True

    def FindPondFood(self,b5,a,b4):
                with self.conn:
                    cur = self.conn.cursor()
                    cur.execute("SELECT fishpond.`No` from fishpond INNER JOIN fishlot ON fishlot.FPNo = fishpond.`No`  where PondNo=%s and FarmID=%s AND fishlot.Round = %s",(b5,a,b4))
                    row = cur.fetchall()
                    print('fishpondNo',row)
                return row

    def selectFLNO(self,b4,b5):
                with self.conn:
                    print(b4,b5)
                    cur = self.conn.cursor()
                    cur.execute("select No from fishlot where Round=%s and FPNo=%s",(b4,b5))
                    row = cur.fetchall()
                    print('fishlot =',row)
                return row

    def FindMTNO(self,b1,b):
                with self.conn:
                    cur = self.conn.cursor()
                    cur.execute("select No from managementtype where Name=%s and NameType=%s",(b1,b))
                    row = cur.fetchall()
                    print('Managementtype =',row)
                return row

    def insertfishmanagement(self,x,m,b,b2,b3):
            with self.conn:
                print(x,m,b,b2,b3)
                cur = self.conn.cursor()
                cur.execute("Insert into `managefish` (`FLNo`,`MTNo`,`List`,`time`,`volume`) values(%s,%s,%s,%s,%s)",(x,m,b,b2,b3))
                self.conn.commit()
                # cur.execute("select Max(No) from fishlot ")
                row = cur.fetchall()
                print(row)
            return True

    def insertEven(self,b1,b2,b3,pondno,Empid):
            with self.conn:
                print('b1=',b1,'b2=',b2,'b3=',b3,'b=',pondno,'Empid=',Empid)
                cur = self.conn.cursor()
                cur.execute("Insert into `event` (`Date`,`Name`,`Problem`,`FPNo`,`EmpID`) values(%s,%s,%s,%s,%s)",(b1,b2,b3,pondno,Empid))
                self.conn.commit()
                cur.execute("select Max(No) from event ")
                row = cur.fetchall()
                print(row)  
            return row

    def FindEmp(self,b4,b5):
            with self.conn:
                cur = self.conn.cursor()
                cur.execute("select id from employee where FName_th=%s and LName_th=%s",(b4,b5))
                row = cur.fetchall()
                print('ok',row)
            return row

    def FindPond(self,b,a):
            with self.conn:
                cur = self.conn.cursor()
                cur.execute("select No from fishpond where PondNo=%s and FarmID=%s",(b,a))
                row = cur.fetchall()
                print('ok',row)
            return row

    def inserttreatment(self,EVNO,b6,b7,b8):
            with self.conn:
                print('EVNO=',EVNO,'b6=',b6,'b7=',b7,'b8=',b8)
                cur = self.conn.cursor()
                cur.execute("Insert into `treatment` (`EvNo`,`Treatment`,`TMSdate`,`TMEdate`) values(%s,%s,%s,%s)",(EVNO,b6,b7,b8))
                self.conn.commit()
                # cur.execute("select Max(No) from fishlot ")
                row = cur.fetchall()
                print(row)
            return True

    def Showdatafeed(self,x):
        with self.conn:
            cur = self.conn.cursor()
            row = cur.execute("SELECT @row:=@row+1 AS `row`,Name,NameType,Register,InspectionResults,MonthlyPurchaseRate,Startdate,Enddate from managementtype,(SELECT @row:=0) AS r  where farmid=%s ",(x) )
            row = cur.fetchall()
        return row

    def ShowFishpond(self,x):
        with self.conn:
            cur = self.conn.cursor()
            row = cur.execute("SELECT @row:=@row+1 AS `row`,PondNo,Round,pondtype.Name,Size,FishName  FROM fishlot INNER JOIN fishpond ON fishlot.FPNo = fishpond.`No` INNER JOIN fishtype ON fishlot.FTNo = fishtype.`No` INNER JOIN pondtype ON fishpond.PondType = pondtype.`No`,(SELECT @row:=0) AS r WHERE fishpond.FarmID = %s ",(x)  )
            row = cur.fetchall()
        return row

    def ShowNamefeed(self,x):
            with self.conn:
                cur = self.conn.cursor()
                row = cur.execute("select Name from managementtype WHERE FarmID = %s ",(x)  )
                row = cur.fetchall()
            return row

    def Showdatafood(self,x):
        with self.conn:
            cur = self.conn.cursor()
            row = cur.execute("SELECT @row:=@row+1 AS `row`,managefish.Date,managefish.Time,fishpond.PondNo,fishlot.Round,managementtype.NameType,managementtype.Name,managefish.Volume  FROM  managefish INNER JOIN managementtype ON managefish.MTNo = managementtype.`No`  INNER JOIN fishlot ON managefish.FLNo = fishlot.`No` INNER JOIN fishpond ON fishlot.FPNo = fishpond.`No`,(SELECT @row:=0) AS r WHERE fishpond.FarmID = %s ",(x) )
            row = cur.fetchall()
        return row

    def ShowdataEven(self,x):
        with self.conn:
            cur = self.conn.cursor()
            row = cur.execute("SELECT @row:=@row+1 AS `row`,event.Date,fishpond.PondNo, event.Name, event.Problem , treatment.Treatment, treatment.TMSdate, treatment.TMEdate, employee.FName_th, employee.LName_th FROM  event INNER JOIN treatment ON event.`No` = treatment.EvNo  INNER JOIN employee ON event.EmpID = employee.id INNER JOIN fishpond ON event.FPNo = fishpond.`No`, (SELECT @row:=0) AS r  WHERE fishpond.FarmID = %s ",(x) )
            row = cur.fetchall()
        return row

    def test2(self):
        with self.conn:
            cur = self.conn.cursor()
            row = cur.execute("SELECT part from test2 ")
            row = cur.fetchall()
        return row