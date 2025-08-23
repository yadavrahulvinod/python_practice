import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime , timedelta
import sys
from pprint import pprint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


sys.stdout.reconfigure(encoding="utf-8")

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


EMAIL_SENDER = "info@circ###.com"
EMAIL_PASSWORD = "kzxh###"
EMAIL_RECEIVER = ["rahul.yadav@circo#######","pranav.kumbhar@circ#######"]
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

SHEET_ID ="1IFml343K4###########"
SERVICE_FILE_PATH ="C:\\Users\\ADMIN\\Desktop\\office\\global-450106-c4-44e7eb13fa5c.json"
SHEET_NAME="Main Master"


logger.info("🔐 Authenticating with Google Sheets...")
scope =["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name(SERVICE_FILE_PATH,scope)
client = gspread.authorize(creds)

try:
    logger.info("📄 Opening Google Sheets...")
    master_ws = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
    logger.info("✅ sheets opened successfully.")
except Exception as e:
  logger.error(f"❌ Failed to open one or more worksheets: {e}")
  sys.exit(1)        

logger.info("📥 Loading data from Master and Contact Sheets...")
try:
 master_data = master_ws.get_all_records(head=1)
except Exception as e:
    print(f" Failed to read source sheet: {e}")
    exit()

logger.info(f"✅ Loaded {len(master_data)} rows from Master")



payment_due_cust= set()
Offline_but_extended = set()
Online_but_extended = set()
Grace_extended = set()

hi_all="All"
tommorow  = datetime.now().date()+timedelta(days=1)
formatted_date = tommorow.strftime("%d %B %Y")


for row in master_data:
  billing_name =str(row.get("Billing Name","")).strip()
  customer_name =str(row.get("Customer Name","")).strip()
  connectivity_status =str(row.get("Connectivity Status","")).strip()
  extension_status =str(row.get("Extension Status","")).strip()

  if billing_name == "" or billing_name =="N/A":
     name =customer_name
  else:
     name = billing_name

  expiry_date_str =str(row.get("Expiry Date","")).strip()

  if expiry_date_str:
    try: 
      expiry_date = datetime.strptime(expiry_date_str,"%Y-%m-%d").date()
    except ValueError:
        expiry_date = None
  else:
    expiry_date = None
  
  extension_category =str(row.get("Extension Category","")).strip()

  if expiry_date == tommorow and extension_category == "Payment Due":
   payment_due_cust.add(name)

  if expiry_date == tommorow and extension_category == "Payment Done" and connectivity_status == "ONLINE":
   Online_but_extended.add(name)
  
  if expiry_date == tommorow and extension_category == "Payment Done" and connectivity_status == "Offline":
   Offline_but_extended.add(name)
  
  if expiry_date == tommorow and extension_category == "Grace Extension":
   Grace_extended.add(name)


print("payment due customers mentioned below"+"--------"*10)
for i, row in enumerate(list(payment_due_cust)):
    pprint(row)

print("extended but online customers mentioned below"+"--------"*10)
for i, row1 in enumerate(list(Online_but_extended)):
    pprint(row1)

print("extended but offline customers mentioned below"+"--------"*10)
for i, row2 in enumerate(list(Offline_but_extended)):
    pprint(row2)

print("grace extension customer mentioned below"+"--------"*10)
for i, row3 in enumerate(list(Grace_extended)):
  
    pprint(row3)

def send_email_alert(subject, body, is_html=False, attachments=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = ", ".join(EMAIL_RECEIVER)
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "html" if is_html else "plain"))

        if attachments:
            for attachment in attachments:
                part = MIMEApplication(attachment['data'], Name=attachment['filename'])
                part['Content-Disposition'] = f'attachment; filename="{attachment["filename"]}"'
                msg.attach(part)

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        logging.info("Email alert sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email alert: {e}")


def format_set_html(data_set):
    if not data_set:
        return "<i>None</i>"
    return "<ul>" + "".join(f"<li>{name}</li>" for name in sorted(data_set)) + "</ul>"

email_body = f"""
<html>
  <body style="font-family: Arial, sans-serif; line-height: 1.5; color: #333;">
    <p>👋 <b>Hello Team,</b></p>
    <p>Here is the <b>Preventive Update —{formatted_date} </b>:</p>

    <h3>📌 Customers with outstanding dues who are likely to face a "00" error tomorrow:</h3>
    {format_set_html(payment_due_cust)}

    <h3>📌 Customers who were unavailable during the call and did not respond to the WhatsApp update and might face a "00" error:</h3>
    {format_set_html(Offline_but_extended)}

    <h3>📌 Customers whose devices are <span style="color:green;">online</span> and extended:</h3>
    {format_set_html(Online_but_extended)}

    <h3>📌 Customers whose devices are <span style="color:orange;">Grace Extended</span> and are updated through WhatsApp Message:</h3>
    {format_set_html(Grace_extended)}

    <p>✅ Please take note and follow up accordingly. Thank you.</p>
  </body>
</html>
"""


send_email_alert(f"{tommorow} Preventive Update",email_body,is_html=True)

