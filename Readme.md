---
* Title:        Customer Sentiment
* Author:       deez79
* Date:         08/24/2017

---

# Table of Contents
* DESCRIPTION

## DESCRIPTION
### Objective:
To measure customer sentiment pasted into a google spreedsheet.
### Process:
    1. Connect to Google doc
        a. Create new project in Google API Manager:
            https://console.developers.google.com/projectcreate
        b. Add google drive api to it.
    2. read customer comments from spreadsheet
    3. Use TextBlob to analyse sentiment
    4. Post results in new google doc sheet
