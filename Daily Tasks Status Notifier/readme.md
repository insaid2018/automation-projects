<a href="https://github.com/insaid2018/automation-projects/tree/main/Daily%20Tasks%20Status%20Notifier"><img src="https://raw.githubusercontent.com/insaid2018/automation-projects/main/Daily%20Tasks%20Status%20Notifier/images/logo.png"></a>

# Overview
**Daily Tasks Status Notifier** is a tool for extracting status updates from Trello cards and sending details using email to the specified audience.

# Table of Contents
1. [Trello Setup](#Section1)<br>
  1.1 [Getting of an API Key & Token](#Section11)<br>
  1.2 [Getting of list id from Trello Board](#Section12)<br>
  1.3 [URL Creation](#Section13)<br>  
2. [Gmail Setup](#Section2)<br>
  2.1 [Project Initiation](#Section21)<br>
  2.2 [Getting of Client Secret](#Section22)<br>  
3. [Email Template Setup](#Section3)<br>
4. [Execution](#Section4)<br>
5. [Developer](#Section5)</br>

<a name=Section1></a>
# 1. Trello Setup

<a name=Section11></a>
### 1.1 Getting of an API Key & Token

You can get your API key by logging into Trello and visiting https://trello.com/app-key. 
Be sure to read and agree to Trello Developer Terms of Service. 
Your API key will be clearly labeled at the top of that page.
Your API key should be a 32 character string comprised of random alphanumeric characters. 
Because of the way the authorization flow works, the API key is intended to be publicly accessible. 
An API key by itself doesn't grant access to a user's Trello data. 
However, because API tokens grant access to the user's data, they should be kept secret.
Your users will always see this screen when granting your application access as shown <a href="https://developer.atlassian.com/cloud/trello/guides/rest-api/images/rest-api-auth.png">here</a>. 
The permissions, duration of access, and application name displayed are all configured via the URL parameters. 
More on that at Authorization. But we'll leave everything as is, and click "Allow".
Once you click Allow you'll grant your own app (identified via your API key) access to your account and be redirected to a page that contains the API token.
This token, along with your API key, can be used to read and write for your entire Trello account. Tokens should be kept secret!

<a name=Section12></a>
### 1.2 Getting of list id from Trello Board

You can convert your Trello board into JSON data just by typing .json at the end of the board URL. For visual clarification click <a href="https://raw.githubusercontent.com/insaid2018/automation-projects/main/Daily%20Tasks%20Status%20Notifier/images/trellojsonbefore.PNG">here</a>.
To retrieve the id of the list press CTRL + F and type the list name in the popped-up search bar.
Just before the name of the list, you will see the id of the list. For visual clarification click <a href="https://raw.githubusercontent.com/insaid2018/automation-projects/main/Daily%20Tasks%20Status%20Notifier/images/trellojsonafter.PNG">here</a>. Save this id into your notepad as it will be used later to extract the card details.

<a name=Section13></a>
### 1.3 URL Creation

Now that we have got all the required components, we can move ahead and create a URL that will extract the details from the Trello board list.
The URL consists of 4 components base URL, REST API, API key, and token.

- base URL: https://api.trello.com
- REST API = /1/lists/{id}
- API key = "?key=Paste your API key here"
- token = "&token=Paste your token here"
- URL = base URL + REST API + API key + token

