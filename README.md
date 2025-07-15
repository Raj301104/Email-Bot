📧 Email Automation Bot
This Python script automates sending personalized emails with a resume attachment to multiple recipients using data from an Excel sheet.

🚀 Features
Reads recipient names and emails from Excel

Sends personalized emails with custom body

Attaches a PDF resume to each email

Uses Gmail SMTP (with App Password)

📁 Project Structure
bash
Copy
Edit
.
├── automate email.py
├── Book1.xlsx           # Your Excel with 'Name' and 'Email' columns
├── Raj Singh Resume.pdf # Attached resume
└── README.md
🛠️ Requirements
Install the required libraries:

bash
Copy
Edit
pip install pandas openpyxl
📤 How to Use
Update your file paths in automate email.py:

Excel path (Book1.xlsx)

Resume path

Sender email & app password

Run the script:

bash
Copy
Edit
python "automate email.py"
🧾 Example Excel Format (Book1.xlsx)
Name	Email
Akanksha	akanksha@email.com
Shubham	shubham@email.com

🔐 Gmail App Password Note
If you're using Gmail:

Enable 2-Step Verification

Generate an App Password for "Mail"

Use that in place of your actual password in the script

More info: Google App Passwords

📬 Sample Output
bash
Copy
Edit
✅ Email sent to akanksha@email.com
✅ Email sent to shubham@email.com
