Congratulations! By finding this file, you've completed the first stage of the assessment.

Somewhere else in the directory structure is a file called data.zip with the data you'll need to complete the second stage.

The zip archive contains three files:
	all_companies.csv - Contains a master database of securities and closing prices. 
	sample_input.csv - Test input with data on recent trades (stock symbol and trade price).
	sample_output.csv - Expected output.

The file sample_input.csv contains a list of stock tickers and trade prices. e.g
AAPL, 1234.00
IBM, 456.3
etc.

Your goal is to map each ticker back to the corresponding security in all_companies.csv (e.g. back to the companyId). For some cases
a direct match on symbol will work - in other cases the symbol names are slightly different. Symbols are not unique identifiers - 
only the combination of symbol and stock exchange is unique. In the case of duplicate symbols, the trade price may help resolve ambiguity.
There is a high correlation between the closing price in all_companies.csv and the trade price in sample_input.csv, however they are 
not identical. As part of your output, include the symbol from the input file, the trade price, closing price, and the slippage - defined
as 100*(tradePrice/closePrice-1) (or the percentage difference between the trade price and closing price).

If you are unable to map a symbol back to a companyId, it is OK to either not include in the output or leave the companyId as blank.

The final product should be a script that can be run from the command-line and accepts the name of a the input CSV file as an argument
(eg python submission.py input.csv). Submissions are accepted in all languages. If you are using a compiled language such as Java or C++,
 please submit your source code and compilation instructions instead of a binary.
Output should be written to a file named output.csv in the current working directory (see sample_output.csv for the output format).
You may assume the file all_companies.csv will be present in the directory where your script is run.

We will run your script on a set of hidden testcases similar to those in sample_input.csv. Evaluation will depend on
the correctness and completeness of the output, as well as overall code quality. The assessment should take 2-3 hours to complete.

Feel free to send any questions to Benjamin Pachev <benjamin.pachev@doubleriver.com>.
Submissions should be sent to John Simmons <johnsimmons@doubleriver.com>
May the Force be with you.
