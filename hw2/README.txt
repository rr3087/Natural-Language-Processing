HW-2 Writeup

Rahul Rana
rr3087

HW-2


Part 1 - Arc Standard
1. Output of your validate_transitions.py

FORMS : ['ROOT', 'Great', 'graphic', 'design', 'work', '!']
GOLD ARCS : [(1, 4), (2, 4), (3, 4), (4, 0), (5, 4)]
[5, 4, 3, 2, 1, 0]
TRANSITIONS :
shift
shift
shift
shift
shift
left_arc
left_arc
left_arc
shift
right_arc
right_arc

2. List all the feature types you implemented. [Ex: ‘TOP_STK_TOKEN_’ , ‘...’, ‘....’]
For our reference.

•	TOP_STK_LEMMA_....
•	TOP_STK_CPOSTAG_.....lower()
•	TOP_BUFFER_LEMMA_....
•	TOP_BUFFER_CPOSTAG_.....lower()
•	TWO_STK_LEMMA_....
•	TWO_STK_CPOSTAG_.....lower()
•	TWO_BUFFER_LEMMA_....
•	TWO_BUFFER_CPOSTAG_.....lower()
•	THREE_STK_LEMMA_....
•	THREE_STK_CPOSTAG_.....lower()
•	FOUR_BUFFER_LEMMA_....
•	FOUR_BUFFER_CPOSTAG_.....lower()
•	FIVE_STK_LEMMA_....
•	FIVE_STK_CPOSTAG_.....lower()
•	FIVE_BUFFER_LEMMA_....
•	FIVE_BUFFER_CPOSTAG_.....lower()
•	SIX_STK_LEMMA_....
•	SIX_STK_CPOSTAG_.....lower()
•	SIX_BUFFER_LEMMA_....
•	SIX_BUFFER_CPOSTAG_.....lower()

3. Explain any 6 feature types in detail. What does the feature type represent? Why do you think this is useful for transition predictions?

The 6 features that really helped to bump up the F1 to almost 89% were:
1.	TOP_STK_LEMMA_.... This feature includes the LEMMA of the word in the sentence corresponding to the index on the top of the stack, which holds very useful information since it is the first element to be considered for arc formation. The lemma is included and not the actual token, so that the different possible feature values are reduced in total.
2.	TOP_STK_CPOSTAG_.... This features includes the Course Grained POS Tag of the word in the sentence corresponding to the index on the top of the stack, which holds information about the POS tag of the element that is being considered for arc formation, which is useful for relational information about the sentence as a whole. CPOSTAG is used and not POSTAG, so that the possible feature values are reduced in total and it is an easier classification problem for the classifier. The observed metrics were consistent with this hypothesis.
3.	TOP_BUFFER_LEMMA_.... This feature includes the LEMMA of the word in the sentence corresponding to the index on the top of the buffer. Since this is the element that is being pushed first to the stack which would be considered for arc formation, it is quite intuitive that this feature would be important. 
4.	TOP_BUFFER_CPOSTAG_.... This feature includes the Course Grained POS Tag of the word in the sentence corresponding to the index on the top of the buffer. This is the POS tag about the element that is being pushed first to the stack, which would be considered for arc formation. So, it makes sense to include this relational information of the sentence. 
5.	TWO_STK_LEMMA_.... This feature includes the LEMMA of the word in the sentence corresponding to the index on the 2nd from top of the stack. Since, the top and 2nd from top elements are considered in the arc formation, having this information is very useful. 
6.	TWO_STK_CPOSTAG_.... This feature includes the Course Grained POS Tag of the word in the sentence corresponding to the index on the 2nd from top of the stack. Since, the top and 2nd from top elements are considered in the arc formation, having relational information about them is very useful.

The other features also helped, but their total contribution to the F1 was within 3-4 points above 89

4. How do you interpret precision and recall in context of this task?

Total precision :0.9344782886565615
Total recall: 0.9344782886565615

Precision and Recall are high in this case and equal in value, which means that the classifier is learning the arc transitions correctly and predicting many arcs that are accurate. With these respective values of precision and recall, it means that the arc transitions that were actually not accurate, but predicted as being accurate (False Positives) and arc transitions that were actually accurate, but predicted as not being accurate (False Negative) are around 7% of the total predicted accurate arcs and of the total actual accurate arcs, respectively.

5. What is your final F1 score on the dev set?

F1 Measure: 0.9344782886565615


Part 2 - Domain Adaptation
6. Average F1 score from 10 runs of domain_adaptation_eval.py.

Email Results
Total precision :0.8178021978021975
Total recall: 0.8139560439560436
F1 Measure: 0.8158745880693484

Newsgroup Results:
Total precision :0.818840579710145
Total recall: 0.7840579710144928
F1 Measure: 0.8010718872028725

It’s the exact same metrics over 10 runs. And so the averages are:

train_genre : reviews, test_genre : email, Avg F1 : 0.8158745880693484

train_genre : reviews, test_genre : newsgroup, Avg F1 : 0.8010718872028725

Another model, which had a different combination of features and classifier gave average F1 score of 0.90 and 0.71 on email and newsgroups, respectively. But I have reported the model that gave good performance on both domains, rather than on just one domain.

7. Provide an explanation of the performance of the feature types in domain adaptation. What features generalized well?  What features did not?

The classifier used here was Multinomial Naïve Bayes, with alpha=0.2.

A lot of different sets of feature types were experimented with and the ones that allowed the classifier to perform well on both test domains of email and newsgroups were:
•	TOP_STK_LEMMA_.... This feature, as explained earlier, intuitively holds essential information about the arcs. And translates well across domains.
•	TOP_STK_CPOSTAG_.... This feature, as explained earlier, also holds important information about the sentence and hence the transitions. This core information would intuitively translate well across domains and it did. 
Similarly, TOP_BUFFER_LEMMA_ and TOP_BUFFER_CPOSTAG_ features also translated well across domains. 

Some of the features that did not generalize well across the domains were:
•	TWO_STK_LEMMA_.... LEMMA of the word corresponding to the index on the 2nd from TOP on stack.
•	TWO_BUFFER_LEMMA_....LEMMA of the word corresponding to the index on the 2nd from TOP on buffer.
•	THREE_BUFFER_LEMMA_.... LEMMA of the word corresponding to the index on the 3rd from TOP on buffer.
•	FOUR_BUFFER_LEMMA_....LEMMA of the word corresponding to the index on the 4th from TOP on buffer 
Seems like the lemma information from other indices, apart from the top, were adding noise and did not hold useful information because of which the F1 metrics reduced. They did not hold positive information as present in the TOP_STK_LEMMA and TOP_BUFFER_LEMMA, and so they did not translate well across both domains.

It was interesting to observe that some features translated really well across one test domain and did not across the other test domain. So, a trade-off among features had to be made so that a balanced set of features were used that translated well across both the test domains. 


SUBMITTED CODE -

1.	dependency.py - Module with all the functions pertaining to the arc standard algorithm. shift, right_arc, left_arc, oracle_std, make_transition.
2.	feature_extraction.py - Module that defines the feature_extractor function.
3.	domain_adaptation.py - Module with the train function for domain adaptation.
4.	feature_extraction_da.py - Module that defines the feature_extractor for the domain adaptation experiment.
