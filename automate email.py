import pandas as pd
import smtplib
from email.message import EmailMessage


def load_emails(file_path):
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip() 
    return df


def send_email(to_email, name, sender_email, sender_password):
    msg = EmailMessage()
    msg['Subject'] = 'Seeking Entry-Level Opportunity & Referral'
    msg['From'] = sender_email
    msg['To'] = to_email

    msg.set_content(f"""\

Dear {name},

I hope you're doing well.

My name is Raj Singh, and I’m reaching out to express my interest in any suitable entry-level opportunities within your organization. I’m a recent BSc IT graduate (2025) with hands-on experience in Data Analytics, Python, Django, Angular, and SQL.

During my internships at Tata Group (via Forage) and Deloitte, I gained practical exposure to IAM strategy, data analysis using Excel and Python, and dashboard creation in Tableau. I also developed and deployed full-stack web applications such as “Study Buddy,” a Django-based discussion forum for students to share technical queries and collaborate.

I am eager to contribute my technical skills, quick learning ability, and problem-solving mindset to a forward-thinking team. I would truly appreciate it if you could let me know of any relevant openings that match my profile. A referral would mean a lot and be greatly appreciated.

Please find my resume attached for your kind consideration. I’d be happy to provide any further details if needed.

Thank you for your time and support.

Warm regards,  
Raj Singh  
🔗 https://www.linkedin.com/in/raj-singh-297195256/  
📞 8591147733  
✉️ rajsingh301004@gmail.com
""")

   
    resume_path = r"C:\Users\Raj Singh\OneDrive\Desktop\Certificate\Raj Singh Resume .pdf"
    try:
        with open(resume_path, "rb") as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype="application", subtype="pdf", filename="Raj Singh Resume.pdf")
    except FileNotFoundError:
        print("❌ Resume file not found. Please check the path:", resume_path)
        return

    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
            print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")


def main():
    sender_email = 'rajsingh301004@gmail.com'
    sender_password = 'tbvgsowflbslhdvb'  

    excel_path = r"C:\Users\Raj Singh\Downloads\Book1.xlsx"
    contacts = load_emails(excel_path)

    for index, row in contacts.iterrows():
        send_email(row['Email'], row['Name'], sender_email, sender_password)

if __name__ == '__main__':
    main()
