# Discord AI Member (Bot)
A basic discord bot that understands the message history and can answer according to it using Google Gemini.<br><br>
![Google](https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)
![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=Cloudflare&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)<br>

## Requirements:
- Discord Account
- Cloudflare Account
- Google Account (Age 18+)
- Python 3.8 or higher

## Setup
Complete the steps below to get the Bot running
### Get the Google API Key
1. Go to **https://aistudio.google.com/apikey** and login with your account credentials
2. Once on the dashboard, click on **Create API Key**
3. Save that key somewhere, you're going to need it later

### Get your Cloudflare domain
1. Go to **https://workers.dev/** and click on **Sign up**
2. Verify your E-Mail to save your progress
3. On the left bar, navigate to **Compute (Workers)** and to **Workers and Pages**
4. Click on **create** and create a Hello-World-Worker
5. Create a domain name of your liking
6. Click on **Edit Code** and wait for the code editor to load
7. Paste my **[worker.js script](https://github.com/einfachniemmand/discord_ai_member/blob/main/src/worker.js)** there and change the context to your liking
8. Finally, replace your api key from google with *YOUR_API_KEY*
9. Click on **Deploy** to save your changes

### Get your bot token
1. Visit [My Applications in the Discord Developer Forum](https://discord.com/developers/applications) and log in with your discord account
2. Start by clicking on **New Application**, you can change the name at any time
3. You get loaded onto the dashboard where you can customize your bot
4. Navigate to **Bot** on the left bar
5. Activate the **Message Content Intent** Option and click save
6. Click on **Reset token** and fulfill the next steps
7. Save your token for later
