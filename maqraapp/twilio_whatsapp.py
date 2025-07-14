# from twilio.rest import Client
# import os

# # Your Account SID and Auth Token from twilio.com/console
# # It's recommended to store these in environment variables
# account_sid = "AC57642159703109804f21b558696e35eb"
# auth_token = "fb2b70472dbd081fc6068b27bdfafb80"
# client = Client(account_sid, auth_token)

# def send_registration_success_whatsapp(to_whatsapp_number):
#     """
#     Sends a WhatsApp message to the specified number upon successful registration using Content API.
#     """
#     # Replace 'YOUR_ACTUAL_AUTH_TOKEN' with your actual Twilio Auth Token in line 7
#     # Verify that 'HXb5b62575e6e4ff6129ad7c8efe1f983e' is a valid and approved Content SID in your Twilio account.
#     # Also, ensure the variables {"1": "...", "2": "..."} match the placeholders (e.g., {{1}}, {{2}}) in the template associated with this SID.
#     try:
#         message = client.messages.create(
#             from_='whatsapp:+14155238886', # Replace with your actual Twilio WhatsApp number
#             content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e', # Verify this SID in your Twilio console
#             content_variables='{"1":"12/1مرحبا بك في المقرأة اليمنية سيتم التواصل بك لاحقا يمكن التواصل معنا من خلال النقر على رمز الواتس اب الموجود في صفحتنا","2":"24pm"}', # Verify these variables match your template
#             to=f'whatsapp:{to_whatsapp_number}'
#         )
#         print(f"WhatsApp message sent successfully to {to_whatsapp_number}. SID: {message.sid}")
#         return True
#     except Exception as e:
#         print(f"Error sending WhatsApp message: {e}")
#         return False