import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

if __name__ == "__main__":
    print(":)") 
    message = Mail(
        from_email='cenation092@gmail.com',
        to_emails='cenation092@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('API KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
