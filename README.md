install the modules:<br />
  pip install mysql-connector<br />
  pip install fastapi[all]<br />
  pip install uvicorn<br />


How to run the backend:<br />
  cd backend<br />
  python -m uvicorn main:app --reload<br />

ngrok for https tunneling:<br />
 1. Download ngrok and place ngrok.exe in a folder.<br />
 2. ngrok config add-authtoken "your auth key sign up to get it"<br />
 3. ngrok http 80000<br />


![Alt text](frontend/preview/site-preview.png)
![Alt text](frontend/preview/chatbot-preview.png)
