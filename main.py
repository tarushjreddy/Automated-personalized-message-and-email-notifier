import pandas as pd
import datetime
import smtplib
# print("hello")
GMAIL_ID = 'developerkingpro@gmail.com'

GMAIL_PASS = 'Tarushjreddy9*'


def SendMail(to, sub, msg):
    print(f"Email to {to } {msg} this is a b day")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PASS)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub} \n\n\n\n {msg}")
    s.quit()


if __name__ == "__main__":
    SendMail(GMAIL_ID, "sub", "msg")
    # exit()
    df = pd.read_excel("Data_for_analysis.xlsx")
    # print(df)
    today = datetime.datetime.now().strftime("%d-%m-%y")
    Year = datetime.datetime.now().strftime("%y")
print(Year)
writeInd = []
for index, item in df.iterrows():
    # print(index, item['Name'])
    bday = item['Date'].strftime("%d-%m-%y")
    # print(bday)
    msg = item['Dialogue']
    if(today == bday) and Year not in str(item['Year']):
        SendMail(item['Email'], "Happy BDAY bro", msg)
        # print(f"its a b day")
        writeInd.append(index)
    else:
        print("oms")
# print(writeInd)
# print(today)
for i in writeInd:
    hu = df.loc[i, 'Year']
    print(hu)
    df.loc[i, 'Year'] = str(hu) + "," + Year
# print(df.loc[i, 'Year'])
df.to_excel("Data_for_analysis.xlsx")
