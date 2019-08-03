import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def verify(to):
    message = Mail(
        from_email='cenation092@gmail.com',
        to_emails=to,
        subject='Verify Your ',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
    
    return "Verification Send"
