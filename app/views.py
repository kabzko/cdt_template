import json

from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, "index.html")

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Get email details from the request
            to_email = data.get('to_email')
            subject = data.get('subject')
            context = data.get('context', {})
            
            # Debug prints
            print("Starting email send process...")
            print("Email Context Data:", context)
            print("To Email:", to_email)
            print("Subject:", subject)
            
            if not to_email:
                print("Error: No recipient email provided")
                return JsonResponse({'error': 'Recipient email is required'}, status=400)
            try:
                html_content = render_to_string('email/default.html', context)
                
                email = EmailMessage(
                    subject=subject,
                    body=html_content,
                    from_email='yahshua.systech.developers@gmail.com',
                    to=[to_email],
                )
                email.content_subtype = 'html'
                
                print("Attempting to send email...")
                email.send()
                print("Email sent successfully")
                
                return JsonResponse({
                    'message': 'Email sent successfully',
                    'to': to_email,
                    'subject': subject
                })
                
            except Exception as e:
                print(f"Error sending email: {str(e)}")
                return JsonResponse({
                    'error': f'Failed to send email: {str(e)}'
                }, status=500)
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
            
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

