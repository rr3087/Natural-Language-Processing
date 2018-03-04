Rahul Rana

rr3087@columbia.edu

HW-1

To train the best classifier, simply run the command
$ python classify.py train_newline.txt dev_newline.txt
This trains and saves the best model in the same folder and prints the test prediction accuracy.

To print other measures of the best classifier, simply run the command
$ python analyze.py model.pkl dev_newline.txt
This loads the saved model and tests it on the testset and prints the test prediction accuracy, top-20 features and contingency table.

To print the performance metrics of the all the 4 models simply run the command
$ python hw1.py
This prints the test prediction accuracy, top-20 features and contingency table for all the 4 models.

The best classifier model has a prediction accuracy of 63.62%, but it mis-classifies the tweets based on some of the top features like presence of exclamation marks, presence of the words 'gop' and those indicating a religious sentiment.

