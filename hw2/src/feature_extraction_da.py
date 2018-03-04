# config {stack,buffer,label}
def get_features_da(config,sent_dict):
    features = []

    # TODO Improve Features
    
    if len(config[0]) > 0:
        # Top of stack.
        top = config[0][-1] 
        
        top_stk_token_feature = 'TOP_STK_TOKEN_'+str(sent_dict['FORM'][top].lower())
        features.append(top_stk_token_feature)
	
        top_stk_lemma = 'TOP_STK_LEMMA_' + str(sent_dict['LEMMA'][top].lower()) # not converting to lower has helped to increase the f1 score slightly
        features.append(top_stk_lemma)

        top_stk_cpostag = 'TOP_STK_CPOSTAG_' + str(sent_dict['CPOSTAG'][top].lower())
        features.append(top_stk_cpostag)
	
      
    if len(config[1]) > 0:
       	top_buffer = config[1][-1]  # top of buffer, since it is in descending order

       	top_buffer_token_feature = 'TOP_BUFFER_TOKEN'+str(sent_dict['FORM'][top_buffer].lower())
       	features.append(top_buffer_token_feature)

       	top_buffer_lemma = 'TOP_BUFFER_LEMMA_' + str(sent_dict['LEMMA'][top_buffer].lower())
       	features.append(top_buffer_lemma)

       	top_buffer_cpostag = 'TOP_BUFFER_CPOSTAG_' + str(sent_dict['CPOSTAG'][top_buffer].lower())
       	features.append(top_buffer_cpostag)
	

    if len(config[0]) > 1:
    	two = config[0][-2] # 2nd from top in stack
    	
    	# two_stk_token = 'two_stk_token_'+str(sent_dict['FORM'][two].lower())
    	# features.append(two_stk_token)

    	# two_stk_lemma = 'TWO_STK_LEMMA_' + str(sent_dict['LEMMA'][two].lower())
    	# features.append(two_stk_lemma)

    	two_stk_cpostag = 'TWO_STK_CPOSTAG_' + str(sent_dict['CPOSTAG'][two].lower())
    	features.append(two_stk_cpostag)

    if len(config[1]) > 1:
    	two_buffer = config[1][-2] # 2nd from top in buffer

    	two_buffer_token = 'TWO_BUFFER_TOKEN_'+str(sent_dict['FORM'][two_buffer].lower())
    	features.append(two_buffer_token)

    	# two_buffer_lemma = 'TWO_BUFFER_LEMMA_' + str(sent_dict['LEMMA'][two_buffer])
    	# features.append(two_buffer_lemma)

    	two_buffer_cpostag = 'TWO_BUFFER_CPOSTAG_' + str(sent_dict['CPOSTAG'][two_buffer].lower())
    	features.append(two_buffer_cpostag)
	

    # if len(config[0]) > 2:
    # 	three = config[0][-3] # 3rd from top in stack

    # 	three_stk_lemma = 'THREE_STACK_LEMMA_' + str(sent_dict['LEMMA'][three])
    # 	features.append(three_stk_lemma)

    # 	three_stk_cpostag = 'THREE_STACK_CPOSTAG_' + str(sent_dict['CPOSTAG'][three].lower())
    # 	features.append(three_stk_cpostag)

    if len(config[1]) > 2:
    	three_buffer = config[1][-3] # 3rd from top in buffer

    	# three_buffer_lemma = 'THREE_BUFFER_LEMMA_' + str(sent_dict['LEMMA'][three_buffer].lower())
    	# features.append(three_buffer_lemma)

    	three_buffer_cpostag = 'THREE_BUFFER_CPOSTAG_' + str(sent_dict['CPOSTAG'][three_buffer].lower())
    	features.append(three_buffer_cpostag)

    # if len(config[0]) > 3:
    # 	four = config[0][-4] # 4th from top in stack

    # 	four_stk_lemma = 'FOUR_STK_LEMMA_' + str(sent_dict['LEMMA'][four].lower())
    # 	features.append(four_stk_lemma)

    # 	four_stk_cpostag = 'FOUR_STK_CPOSTAG_' + str(sent_dict['CPOSTAG'][four].lower())
    # 	features.append(four_stk_cpostag)

    if len(config[1]) > 3:
    	four_buffer = config[1][-4] # 4th from top in buffer

    	# four_buffer_lemma = 'FOUR_BUFFER_LEMMA_' + str(sent_dict['LEMMA'][four_buffer].lower())
    	# features.append(four_buffer_lemma)

    	four_buffer_cpostag = 'FOUR_BUFFER_CPOSTAG_' + str(sent_dict['CPOSTAG'][four_buffer].lower())
    	features.append(four_buffer_cpostag)


    return features
