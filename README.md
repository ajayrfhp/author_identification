# AUTHOR IDENTIFICATION FROM TWITTER DATA

### OVERVIEW

* Components involved 
	1. DATA EXTRACTION  
		* Tweet sequences of 5 football journalists used
		* Removed tweets of less than 3 words, retweets and links  
	  
	2. FEATURE EXTRACTION 
		* Bag of words model using all words with frequency greater than 10
		*  Style features [TO DO]
		*  Word 2 vec ? [ TO DO ]
	3. MODEL BUILDING  
		* Scikit SVM
		* Neural Nets [ To do]
	4. MODEL VALIDATION
		* #### CONFUSION MATRIX FOR BAG OF WORDS WITH 999 FEATURES

			Confusion Matrix for **training** data  
			Predicted * Expected :
			
			Author 1      | Author 2      | Author 3      | Author 4      | Author 5
			------------- | ------------- | ------------- | ------------- | -------------
			**597**           | 20            | 14            | 19            | 7
			11  		    | **744**  | 8  | 5  | 8
			8 | 5  | **686**  | 14  | 6
			9  | 5  | 9  | **700**  | 9
			59  | 78  | 93  | 56  | **654**
			
			Cross Validated Score = 0.8841
			
			Confusion Matrix for **validation** data  
			Predicted * Expected :
			
			Author 1      | Author 2      | Author 3      | Author 4      | Author 5
			------------- | ------------- | ------------- | ------------- | -------------
			**51**           | 3           | 9          | 5           | 7
			11		    | **97** | 13  | 8  | 17
			14| 17 | **93** | 27  | 8
			18  | 6  | 9  | **75**  | 10
			26  | 11  | 19  | 18  | **64**
			
			Cross Validated Score = 0.5941
			

	5. DETERMINE TEST ERROR  [ TO DO ]

### REFERENCES

* [Comparing Frequency- and Style-Based
Features for Twitter Author Identification](https://www.aaai.org/ocs/index.php/FLAIRS/FLAIRS13/paper/viewFile/5917/6043)