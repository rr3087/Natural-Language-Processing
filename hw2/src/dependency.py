def shift(stack, buff, dgraph):
    
    stack = stack.append(buff[-1]) # last element of buffer moves into stack
    del buff[-1] # buffer updated
    
    dgraph = dgraph # dgraph remains unchanged
    return stack, buff, dgraph
    # raise NotImplementedError


def left_arc(stack, buff, dgraph):
    
	stack = stack 
	buff = buff 
    
	dgraph.append((stack[-2], stack[-1])) 
	del stack[-2] # stack updated, child is removed from the stack 
	
	return stack, buff, dgraph
    # raise NotImplementedError


def right_arc(stack, buff, dgraph):
    
    stack = stack
    buff = buff
    dgraph.append((stack[-1], stack[-2])) ### stack[-1] is the child, gets removed
    
    del stack[-1] # stack updated, child is removed from the stack
    
    return stack, buff, dgraph
    # raise NotImplementedError


def oracle_std(stack, buff, dgraph, gold_arcs):

    transitions=None

    if len(stack)==1:
        transitions='shift'

    elif len(stack)>1:
        
        if ((stack[-2], stack[-1]) in gold_arcs):
            transitions='left_arc'
            
        elif ((stack[-1], stack[-2]) in gold_arcs and stack[-1] not in [x[-1] for x in list(set(gold_arcs)-set(dgraph))]):
            transitions='right_arc'
        
        else:
            transitions='shift'

    else:
        transitions='shift'

    return transitions
    # raise NotImplementedError


def make_transitions(buff, oracle, gold_arcs=None):
    
    stack = []
    dgraph = []	
    configurations = []
    while (len(buff) > 0 or len(stack) > 1):
        choice = oracle(stack, buff, dgraph, gold_arcs)
        # Makes a copy. Else configuration has a reference to buff and stack.
        config_buff = list(buff)
        config_stack = list(stack)
        configurations.append([config_stack,config_buff,choice])
        if choice == 'shift':	shift(stack, buff, dgraph)
        elif choice == 'left_arc': left_arc(stack, buff, dgraph)
        elif choice == 'right_arc': right_arc(stack, buff, dgraph)
        else:
        	return None 
    return dgraph,configurations
