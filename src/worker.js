export default {
    async fetch(request) {
        if (request.method === 'OPTIONS') {
            return new Response(null, {
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Max-Age': '86400', // You can also set custom preflight headers
                },
            });
        }
        const API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'; //Adjust the URL to your API version of Gemini
        const API_KEY = 'YOUR_API_KEY'; // Add your google API key here
        const requestBody = await request.json();#
        var textToPrepend = "" // Add additional context
        const modifiedContent = textToPrepend + requestBody.content;
        const urlWithKey = `${API_URL}?key=${API_KEY}`;
        const apiResponse = await fetch(urlWithKey, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                contents: [{
                    parts: [{
                        text: modifiedContent,
                    }],
                }],
            }),
        });
        if (request.method === 'GET') {
            return new Response("GET Method is not supportet.", { // Blocking GET requests
                headers: {
                    "Content-Type": "text/html",
                },
            });
        }
        const apiResponseBody = await apiResponse.json();
        return new Response(JSON.stringify(apiResponseBody), {
            status: apiResponse.status,
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
        });
    },
  };
  
