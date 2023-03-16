from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import FileResponse
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image
import csv
import pandas as pd
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import webbrowser
import img2pdf
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import textwrap
import configparser
import hashlib
# from oauth2client.service_account import ServiceAccountCredentials
from .forms import generatee

# Create your views here.
def home(request):
    # if request.method == 'POST':
    form=generatee()
    # context={'form':form}
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('dashboardapp/cc.json', scope)

    # authorize the clientsheet
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet
    sheet = client.open('Task: Shreeya Singhal: NoQs')

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(0)
    values = sheet_instance.get_all_values()
    # print(12)
    if request.method == 'POST':
        form=generatee(request.POST)
        user = form.save()
        stu=user.index-1
        i=user.choicee
        row=values[stu]
        if i == "Letter":
            # with open('database.csv') as file_obj:
            #     reader_obj = csv.reader(file_obj)
            #     j = 0
            #     for row in reader_obj:
            #         j = j+1
            #         if j == stu:
            email = row[2]
            img = Image.open(r'static\media\letter.png').convert('RGB')
            # img.convert('RGB')
            I1 = ImageDraw.Draw(img)
            myFont = ImageFont.truetype(r'static\media\ll.ttf', 37)
            texto="It brings me great pleasure to write this letter to recommend Ms."+ row[0]+" "+row[1]+" for the post of " + row[3] +" at NoQs Digital for the past " + row[4] +" . She has been a part of quite a few complex projects and played a pivotal role." 
            t1=row[0] + " has grasped the modern technologies very quickly that most software companies use nowadays including us. I can vouch that she is an excellent professional and rewarding to work with. She is a great team worker and on many occasions and at difficult times, she has also shown her amazing leadership qualities."
            t2="I believe having an internee/employee of the calibre of " + row[0] +" will add great value to the company and play important role in achieving the upcoming goals of the company."
            novo = textwrap.wrap(texto, width=86)
            if(row[8]=="f"):
                offset=490
                myfont1= ImageFont.truetype(r'static\media\bb.TTF', 37)
                
                for jj in novo:
                    lenn=165
                    jjj=jj.split()
                    for ii in jjj:
                        if ii=="Ms."+row[0] or ii==""+row[1] or ii==""+row[3] or ii==""+row[4]:
                            I1.multiline_text((lenn, offset), ii,
                                font=myfont1, fill=(0, 0, 0))
                            lenn=myfont1.getsize(ii)[0]+lenn+9
                        else:
                            I1.multiline_text((lenn, offset), ii,
                                    font=myFont, fill=(0, 0, 0))
                            lenn=myFont.getsize(ii)[0]+lenn+9
                        
                    offset=offset+60
                offset=offset+60
                novo = textwrap.wrap(t1, width=86)
                for jj in novo:
                    lenn=165
                    jjj=jj.split()
                    for ii in jjj:
                        if ii==""+row[0] or ii==''+row[1] or ii==''+row[3] or ii==''+row[4]:
                            I1.multiline_text((lenn, offset), ii,
                                font=myfont1, fill=(0, 0, 0))
                            lenn=myfont1.getsize(ii)[0]+lenn+9
                        else:
                            I1.multiline_text((lenn, offset), ii,
                                    font=myFont, fill=(0, 0, 0))
                            lenn=myFont.getsize(ii)[0]+lenn+9
                        
                    offset=offset+60
                offset=offset+60
                novo = textwrap.wrap(t2, width=86)
                for jj in novo:
                    lenn=165
                    jjj=jj.split()
                    for ii in jjj:
                        if ii==''+row[0] or ii==''+row[1] or ii==''+row[3] or ii==''+row[4]:
                            I1.multiline_text((lenn, offset), ii,
                                font=myfont1, fill=(0, 0, 0))
                            lenn=myfont1.getsize(ii)[0]+lenn+9
                        else:
                            I1.multiline_text((lenn, offset), ii,
                                    font=myFont, fill=(0, 0, 0))
                            lenn=myFont.getsize(ii)[0]+lenn+9
                        
                    offset=offset+60
            else:
                myFont = ImageFont.truetype(r'static\media\ll.ttf', 37)
                texto="It brings me great pleasure to write this letter to recommend Mr."+ row[0]+" "+row[1]+" for the post of " + row[3] +" at NoQs Digital for the past " + row[4] +" . He has been a part of quite a few complex projects and played a pivotal role." 
                t1=row[0] + " has grasped the modern technologies very quickly that most software companies use nowadays including us. I can vouch that he is an excellent professional and rewarding to work with. He is a great team worker and on many occasions and at difficult times, he has also shown his amazing leadership qualities."
                t2="I believe having an internee/employee of the calibre of " + row[0] +" will add great value to the company and play important role in achieving the upcoming goals of the company."
                novo = textwrap.wrap(texto, width=86)
                offset=490
                myfont1= ImageFont.truetype(r'static\media\bb.TTF', 37)
                
                for jj in novo:
                    lenn=165
                    jjj=jj.split()
                    for ii in jjj:
                        if ii=="Mr."+row[0] or ii==""+row[1] or ii==""+row[3] or ii==""+row[4]:
                            I1.multiline_text((lenn, offset), ii,
                                font=myfont1, fill=(0, 0, 0))
                            lenn=myfont1.getsize(ii)[0]+lenn+9
                        else:
                            I1.multiline_text((lenn, offset), ii,
                                    font=myFont, fill=(0, 0, 0))
                            lenn=myFont.getsize(ii)[0]+lenn+9
                        
                    offset=offset+60
                offset=offset+60
                novo = textwrap.wrap(t1, width=86)
                for jj in novo:
                    lenn=165
                    jjj=jj.split()
                    for ii in jjj:
                        if ii==""+row[0] or ii==''+row[1] or ii==''+row[3] or ii==''+row[4]:
                            I1.multiline_text((lenn, offset), ii,
                                font=myfont1, fill=(0, 0, 0))
                            lenn=myfont1.getsize(ii)[0]+lenn+9
                        else:
                            I1.multiline_text((lenn, offset), ii,
                                    font=myFont, fill=(0, 0, 0))
                            lenn=myFont.getsize(ii)[0]+lenn+9
                        
                    offset=offset+60
                offset=offset+60
                novo = textwrap.wrap(t2, width=86)
                for jj in novo:
                    lenn=165
                    jjj=jj.split()
                    for ii in jjj:
                        if ii==''+row[0] or ii==''+row[1] or ii==''+row[3] or ii==''+row[4]:
                            I1.multiline_text((lenn, offset), ii,
                                font=myfont1, fill=(0, 0, 0))
                            lenn=myfont1.getsize(ii)[0]+lenn+9
                        else:
                            I1.multiline_text((lenn, offset), ii,
                                    font=myFont, fill=(0, 0, 0))
                            lenn=myFont.getsize(ii)[0]+lenn+9
                        
                    offset=offset+60

            pdfpath = r"static\Letters\letter" + \
                str(stu)+".pdf"

            img.save(
                r"static\LetterImages\letter"+str(stu)+".png")
            img_path = r"static\LetterImages\letter" + \
                str(stu)+".png"
            image = Image.open(img_path)
            pdf_bytes = img2pdf.convert(image.filename)
            file = open(pdfpath, "wb")
            file.write(pdf_bytes)
            image.close()

            file.close()
            file = open(pdfpath, "rb")
            # file.show()
            return FileResponse(file, content_type='application/pdf')
            file.close()
            # break
        elif i == "Certificate":
            # with open('database.csv') as file_obj:
            #     reader_obj = csv.reader(file_obj)
            #     j = 0
            #     for row in reader_obj:
            #         j = j+1
            #         if j == stu:
            email = row[2]
            img = Image.open(r'static\media\certificate.png').convert('RGB')
            # img.convert('RGB')
            I1 = ImageDraw.Draw(img)
            myFont = ImageFont.truetype(r'static\media\ll.ttf', 40)
            texto="This is to certify that Ms."+row[0]+ " "+row[1]+" , a student of " + row[5]+" has \ncompleted the internship program as a " + row[3]+" at NoQs Digital Pvt. Ltd. from "+ row[6]+" to "+row[7]+" . During her internship program with us, we found her disciplined, hardworking and inquisitive."        
            t1="We wish her all the best in her future endeavours!"
            novo = textwrap.wrap(texto, width=86)
            if(row[8]=="f"):
                off=795
                myfont1= ImageFont.truetype(r'static\media\bb.TTF', 40)
                for jj in novo:
                    lenn=145
                    jjj=jj.split()
                    for ii in jjj:
                        if ii=='Ms.'+row[0] or ii==''+row[1] or ii==''+row[3] or ii==''+row[5] or ii==''+row[6] or ii==''+row[7]:
                            I1.text((lenn,off), ii,
                                    font=myfont1, fill=(0, 0, 0))
                            lenn=myfont1.getsize(ii)[0]+lenn+9
                        else:
                            I1.text((lenn,off), ii,
                                    font=myFont, fill=(0, 0, 0))
                            lenn=myFont.getsize(ii)[0]+lenn+9
                    off=off+60
                off=off+100
                lenn=145
                I1.text((lenn,off), t1,
                                    font=myFont, fill=(0, 0, 0))
            else:
                texto="This is to certify that Mr."+row[0]+ " "+row[1]+" , a student of " + row[5]+" has \ncompleted the internship program as a " + row[3]+" at NoQs Digital Pvt. Ltd. from "+ row[6]+" to "+row[7]+" . During his internship program with us, we found him disciplined, hardworking and inquisitive."        
                t1="We wish him all the best in his future endeavours!"
                off=795
                myfont1= ImageFont.truetype(r'static\media\bb.TTF', 40)
                for jj in novo:
                    lenn=145
                    jjj=jj.split()
                    for ii in jjj:
                        if ii=='Mr.'+row[0] or ii==''+row[1] or ii==''+row[3] or ii==''+row[5] or ii==''+row[6] or ii==''+row[7]:
                            I1.text((lenn,off), ii,
                                    font=myfont1, fill=(0, 0, 0))
                            lenn=myfont1.getsize(ii)[0]+lenn+9
                        else:
                            I1.text((lenn,off), ii,
                                    font=myFont, fill=(0, 0, 0))
                            lenn=myFont.getsize(ii)[0]+lenn+9
                    off=off+60
                off=off+100
                lenn=145
                I1.text((lenn,off), t1,
                                    font=myFont, fill=(0, 0, 0))

            pdfpath = r"static\Certificates\certificate" + \
                str(stu)+".pdf"

            img.save(
                r"static\CertificateImages\certificate"+str(stu)+".png")
            img_path = r"static\CertificateImages\certificate" + \
                str(stu)+".png"
            image = Image.open(img_path)
            pdf_bytes = img2pdf.convert(image.filename)
            file = open(pdfpath, "wb")
            file.write(pdf_bytes)
            image.close()
            file.close()
            file = open(pdfpath, "rb")
            # file.show()
            return FileResponse(file, content_type='application/pdf')
            file.close()
                # break
        elif i == "Email":
            pdfpath = r"static\Letters\letter" + \
                str(stu)+".pdf"
            isExisting = os.path.exists(pdfpath)
            if(isExisting == False):
                # with open('database.csv') as file_obj:
                #     reader_obj = csv.reader(file_obj)
                #     j = 0
                #     for row in reader_obj:
                #         j = j+1
                #         if j == stu:
                email = row[2]
                img = Image.open(r'static\media\letter.png').convert('RGB')
            # img.convert('RGB')
                I1 = ImageDraw.Draw(img)
                myFont = ImageFont.truetype(r'static\media\ll.ttf', 37)
                texto="It brings me great pleasure to write this letter to recommend Ms."+ row[0]+" "+row[1]+" for the post of " + row[3] +" at NoQs Digital for the past " + row[4] +" . She has been a part of quite a few complex projects and played a pivotal role." 
                t1=row[0] + " has grasped the modern technologies very quickly that most software companies use nowadays including us. I can vouch that she is an excellent professional and rewarding to work with. She is a great team worker and on many occasions and at difficult times, she has also shown her amazing leadership qualities."
                t2="I believe having an internee/employee of the calibre of " + row[0] +" will add great value to the company and play important role in achieving the upcoming goals of the company."
                novo = textwrap.wrap(texto, width=86)
                if(row[8]=="f"):
                    offset=490
                    myfont1= ImageFont.truetype(r'static\media\bb.TTF', 37)
                    
                    for jj in novo:
                        lenn=165
                        jjj=jj.split()
                        for ii in jjj:
                            if ii=="Ms."+row[0] or ii==""+row[1] or ii==""+row[3] or ii==""+row[4]:
                                I1.multiline_text((lenn, offset), ii,
                                    font=myfont1, fill=(0, 0, 0))
                                lenn=myfont1.getsize(ii)[0]+lenn+9
                            else:
                                I1.multiline_text((lenn, offset), ii,
                                        font=myFont, fill=(0, 0, 0))
                                lenn=myFont.getsize(ii)[0]+lenn+9
                            
                        offset=offset+60
                    offset=offset+60
                    novo = textwrap.wrap(t1, width=86)
                    for jj in novo:
                        lenn=165
                        jjj=jj.split()
                        for ii in jjj:
                            if ii==""+row[0] or ii==''+row[1] or ii==''+row[3] or ii==''+row[4]:
                                I1.multiline_text((lenn, offset), ii,
                                    font=myfont1, fill=(0, 0, 0))
                                lenn=myfont1.getsize(ii)[0]+lenn+9
                            else:
                                I1.multiline_text((lenn, offset), ii,
                                        font=myFont, fill=(0, 0, 0))
                                lenn=myFont.getsize(ii)[0]+lenn+9
                            
                        offset=offset+60
                    offset=offset+60
                    novo = textwrap.wrap(t2, width=86)
                    for jj in novo:
                        lenn=165
                        jjj=jj.split()
                        for ii in jjj:
                            if ii==''+row[0] or ii==''+row[1] or ii==''+row[3] or ii==''+row[4]:
                                I1.multiline_text((lenn, offset), ii,
                                    font=myfont1, fill=(0, 0, 0))
                                lenn=myfont1.getsize(ii)[0]+lenn+9
                            else:
                                I1.multiline_text((lenn, offset), ii,
                                        font=myFont, fill=(0, 0, 0))
                                lenn=myFont.getsize(ii)[0]+lenn+9
                            
                        offset=offset+60
                else:
                    myFont = ImageFont.truetype(r'static\media\ll.ttf', 37)
                    texto="It brings me great pleasure to write this letter to recommend Mr."+ row[0]+" "+row[1]+" for the post of " + row[3] +" at NoQs Digital for the past " + row[4] +" . He has been a part of quite a few complex projects and played a pivotal role." 
                    t1=row[0] + " has grasped the modern technologies very quickly that most software companies use nowadays including us. I can vouch that he is an excellent professional and rewarding to work with. He is a great team worker and on many occasions and at difficult times, he has also shown his amazing leadership qualities."
                    t2="I believe having an internee/employee of the calibre of " + row[0] +" will add great value to the company and play important role in achieving the upcoming goals of the company."
                    novo = textwrap.wrap(texto, width=86)
                    offset=490
                    myfont1= ImageFont.truetype(r'static\media\bb.TTF', 37)
                    
                    for jj in novo:
                        lenn=165
                        jjj=jj.split()
                        for ii in jjj:
                            if ii=="Mr."+row[0] or ii==""+row[1] or ii==""+row[3] or ii==""+row[4]:
                                I1.multiline_text((lenn, offset), ii,
                                    font=myfont1, fill=(0, 0, 0))
                                lenn=myfont1.getsize(ii)[0]+lenn+9
                            else:
                                I1.multiline_text((lenn, offset), ii,
                                        font=myFont, fill=(0, 0, 0))
                                lenn=myFont.getsize(ii)[0]+lenn+9
                            
                        offset=offset+60
                    offset=offset+60
                    novo = textwrap.wrap(t1, width=86)
                    for jj in novo:
                        lenn=165
                        jjj=jj.split()
                        for ii in jjj:
                            if ii==""+row[0] or ii==''+row[1] or ii==''+row[3] or ii==''+row[4]:
                                I1.multiline_text((lenn, offset), ii,
                                    font=myfont1, fill=(0, 0, 0))
                                lenn=myfont1.getsize(ii)[0]+lenn+9
                            else:
                                I1.multiline_text((lenn, offset), ii,
                                        font=myFont, fill=(0, 0, 0))
                                lenn=myFont.getsize(ii)[0]+lenn+9
                            
                        offset=offset+60
                    offset=offset+60
                    novo = textwrap.wrap(t2, width=86)
                    for jj in novo:
                        lenn=165
                        jjj=jj.split()
                        for ii in jjj:
                            if ii==''+row[0] or ii==''+row[1] or ii==''+row[3] or ii==''+row[4]:
                                I1.multiline_text((lenn, offset), ii,
                                    font=myfont1, fill=(0, 0, 0))
                                lenn=myfont1.getsize(ii)[0]+lenn+9
                            else:
                                I1.multiline_text((lenn, offset), ii,
                                        font=myFont, fill=(0, 0, 0))
                                lenn=myFont.getsize(ii)[0]+lenn+9
                            
                        offset=offset+60

                pdfpath = r"static\Letters\letter" + \
                    str(stu)+".pdf"

                img.save(
                r"static\LetterImages\letter"+str(stu)+".png")
                img_path = r"static\LetterImages\letter" + \
                str(stu)+".png"
                image = Image.open(img_path)
                pdf_bytes = img2pdf.convert(image.filename)
                file = open(pdfpath, "wb")
                file.write(pdf_bytes)
                image.close()

                file.close()
                # break

            pdfpath = r"static\Certificates\certificate" + \
                str(stu)+".pdf"
            isExisting2 = os.path.exists(pdfpath)
            if(isExisting2 == False):
                # with open('database.csv') as file_obj:
                #     reader_obj = csv.reader(file_obj)
                # #    reader_obj = csv.reader(file_obj)
                #     j = 0
                #     for row in reader_obj:
                #         j = j+1
                #         if j == stu:
                email = row[2]
                img = Image.open(r'static\media\certificate.png').convert('RGB')
                            # img.convert('RGB')
                I1 = ImageDraw.Draw(img)
                myFont = ImageFont.truetype(r'static\media\ll.ttf', 40)
                texto="This is to certify that Ms."+row[0]+ " "+row[1]+" , a student of " + row[5]+" has \ncompleted the internship program as a " + row[3]+" at NoQs Digital Pvt. Ltd. from "+ row[6]+" to "+row[7]+" . During her internship program with us, we found her disciplined, hardworking and inquisitive."        
                t1="We wish her all the best in her future endeavours!"
                novo = textwrap.wrap(texto, width=86)
                if(row[8]=="f"):
                    off=795
                    myfont1= ImageFont.truetype(r'static\media\bb.TTF', 40)
                    for jj in novo:
                        lenn=145
                        jjj=jj.split()
                        for ii in jjj:
                            if ii=='Ms.'+row[0] or ii==''+row[1] or ii==''+row[3] or ii==''+row[5] or ii==''+row[6] or ii==''+row[7]:
                                I1.text((lenn,off), ii,
                                        font=myfont1, fill=(0, 0, 0))
                                lenn=myfont1.getsize(ii)[0]+lenn+9
                            else:
                                I1.text((lenn,off), ii,
                                        font=myFont, fill=(0, 0, 0))
                                lenn=myFont.getsize(ii)[0]+lenn+9
                        off=off+60
                    off=off+100
                    lenn=145
                    I1.text((lenn,off), t1,
                                        font=myFont, fill=(0, 0, 0))
                else:
                    texto="This is to certify that Mr."+row[0]+ " "+row[1]+" , a student of " + row[5]+" has \ncompleted the internship program as a " + row[3]+" at NoQs Digital Pvt. Ltd. from "+ row[6]+" to "+row[7]+" . During his internship program with us, we found him disciplined, hardworking and inquisitive."        
                    t1="We wish him all the best in his future endeavours!"
                    off=795
                    myfont1= ImageFont.truetype(r'static\media\bb.TTF', 40)
                    for jj in novo:
                        lenn=145
                        jjj=jj.split()
                        for ii in jjj:
                            if ii=='Mr.'+row[0] or ii==''+row[1] or ii==''+row[3] or ii==''+row[5] or ii==''+row[6] or ii==''+row[7]:
                                I1.text((lenn,off), ii,
                                        font=myfont1, fill=(0, 0, 0))
                                lenn=myfont1.getsize(ii)[0]+lenn+9
                            else:
                                I1.text((lenn,off), ii,
                                        font=myFont, fill=(0, 0, 0))
                                lenn=myFont.getsize(ii)[0]+lenn+9
                        off=off+60
                    off=off+100
                    lenn=145
                    I1.text((lenn,off), t1,
                                        font=myFont, fill=(0, 0, 0))

                pdfpath = r"static\Certificates\certificate" + \
                    str(stu)+".pdf"

                img.save(
                r"static\CertificateImages\certificate"+str(stu)+".png")
                img_path = r"static\CertificateImages\certificate" + \
                str(stu)+".png"
                image = Image.open(img_path)
                pdf_bytes = img2pdf.convert(image.filename)
                file = open(pdfpath, "wb")
                file.write(pdf_bytes)
                image.close()

                file.close()
                # break
            isExisting = True 
            isExisting = True
            if(isExisting == True and isExisting == True):
                message = "Thankyou for your valuable time. Here your tenure ends. Please find the attached Letter of recommendation and the certificate."
                fromaddr = "shreeyasinghal36@gmail.com"
                email = row[2]
                            
                smtp = smtplib.SMTP('smtp.gmail.com', 587)
                smtp.ehlo()
                smtp.starttls()
                config = configparser.ConfigParser()
                config.read("config.ini")

                password = config.get("email", "password")
                hashed_password = hashlib.sha256(password.encode()).hexdigest() 
                smtp.login('shreeyasinghal36@gmail.com',
                        hashed_password)
                msg = MIMEMultipart()

            # Add Subject       subject=
                subject = "Thank You "+row[0]+" !! Internship Certificate and LoR"
                text = "Dear " +row[0]+ " "+row[1]+",\n\n\nOn behalf of the NoQs Digital management team, we would like to appreciate you for the amazing work that you did. Your professionalism reflects in the countless hours that you put into the project to ensure it gets completed smoothly. This has impressed the entire team. Your self-motivation, dedication and diligence are an inspiration for your team.\n\nThank you for doing a great job!\n\nPS: Please find attached herewith your Internship Certificate and the Letter of Recommendation letters for your perusal.\n\nWishing you all the best in your career ahead.\n\nStay in touch!\n\nKind Regards,\nThe NoQs Digital management team"
                attachment2 = r"static\Certificates\certificate" + \
                    str(stu)+".pdf"
                attachment = r"static\Letters\letter" + \
                    str(stu)+".pdf"
                msg['Subject'] = subject

                # Add text contents
                msg.attach(MIMEText(text))

                            # Check if we have anything
                            # given in the img parameter
                if attachment2 is not None:

                                # Check whether we have the
                                # lists of attachments or not!
                    if type(attachment2) is not list:

                                    # if it isn't a list, make it one
                        attachment2 = [attachment2]

                    for one_attachment in attachment2:

                        with open(one_attachment, 'rb') as f:

                                        # Read in the attachment
                                        # using MIMEApplication
                            file = MIMEApplication(
                                            f.read(),
                                            name=os.path.basename(one_attachment)
                                        )
                            file['Content-Disposition'] = f'attachment;\
                                    filename="{os.path.basename(one_attachment)}"'

                                    # At last, Add the attachment to our message object
                            msg.attach(file)

                            # We do the same for
                            # attachments as we did for images
                if attachment is not None:

                                # Check whether we have the
                                # lists of attachments or not!
                    if type(attachment) is not list:

                                    # if it isn't a list, make it one
                        attachment = [attachment]

                    for one_attachment in attachment:

                        with open(one_attachment, 'rb') as f:

                                        # Read in the attachment
                                        # using MIMEApplication
                            file = MIMEApplication(
                                            f.read(),
                                            name=os.path.basename(one_attachment)
                                        )
                            file['Content-Disposition'] = f'attachment;\
                                    filename="{os.path.basename(one_attachment)}"'

                                    # At last, Add the attachment to our message object
                            msg.attach(file)
                            # Make a list of emails, where you wanna send mail
                to = ["shreeya1803singhal@gmail.com"]

                            # Provide some data to the sendmail function!
                smtp.sendmail(from_addr='shreeyasinghal36@gmail.com',
                                        to_addrs=to, msg=msg.as_string())

                            # Finally, don't forget to close the connection
                smtp.quit()
        print("Success")
    valuess={'values':values,'form':form}
    return render(request,'dashboardapp/home.html',valuess)
        