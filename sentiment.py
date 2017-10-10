######################################################################
#       Sentiment
#       Use google doc spreedsheet to test sentiment of customer comments
#       08/24/2017
######################################################################

################################################################################
#import libraries:{{{
from textblob import TextBlob
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# prettyPrinter is just used to cean up python output.  Will not be needed in final application
import pprint
pp = pprint.PrettyPrinter()

#}}} End of Libraries

################################################################################
# authorization to google sheet {{{
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('../client_secret.json', scope)
client = gspread.authorize(creds)

#}}} End of Authorization

################################################################################
# Import Data From Google SpreedSheet {{{

# open sheet to work with raw customer comments
sh = client.open('Customer Sentiment')
worksheet = sh.worksheet('Sheet1')
resultsheet = sh.worksheet('Results')


#debug:
print(worksheet.row_count)

## Pull in Comment Column into Python:
output = ['Sentiment:',]
comment = ['Comment:',]
results = worksheet.col_values(1)
for result in results:
#    print(result)
    analysis = TextBlob(result)
#    print(analysis.sentiment)
#    print("\n")
    output.append(analysis.sentiment)
    comment.append(result)

#print(output)
#print(comment)

#pp.pprint(result)

#}}} End of Import Data

################################################################################
# Run Comments through Sentiment Analyzer (Text Blob)

# Updating Cells with Sentiment Scores
## Concepts:
##  1. Create Range that includes all comments pasted into column A
##  2. run for statment through all cells in range
##  3. use textblob to get sentement of each cells comment
##  4. update corresponding row columns B and C with Sentiment and Score

## 1. Create and Select a range
comment_range = worksheet.row_count
row=1
col=1
n = 0

while row <= comment_range:
    resultsheet.update_cell(row,col,comment[row])
    resultsheet.update_cell(row,col + 1, output[row])
    row = row + 1
    n = n + 1
    
# Add Header to sheet:
header = ["Comment:", "Sentiment:"]
index = 1
resultsheet.insert_row(header, index)


################################################################################




# Output results to Results Sheet
#output.update_cell(r, 2, comment)


