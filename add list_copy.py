"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'cf_local_ADD_IOC_Containment_LIST_1' block
    cf_local_ADD_IOC_Containment_LIST_1(container=container)

    return

def cf_local_ADD_IOC_Containment_LIST_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('cf_local_ADD_IOC_Containment_LIST_1() called')
    
    literal_values_0 = [
        [
            "user",
            "Seree",
            4,
        ],
    ]

    parameters = []

    for item0 in literal_values_0:
        parameters.append({
            'IOC_Type': item0[0],
            'input_IOC': item0[1],
            'Container_id': item0[2],
        })
    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "local/ADD_IOC_Containment_LIST", returns the custom_function_run_id
    phantom.custom_function(custom_function='local/ADD_IOC_Containment_LIST', parameters=parameters, name='cf_local_ADD_IOC_Containment_LIST_1', callback=custom_function_1)

    return

def add_note_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_note_2() called')

    note_title = "Containment Result  najaj"
    note_content = "Success"
    note_format = "markdown"
    phantom.add_note(container=container, note_type="general", title=note_title, content=note_content, note_format=note_format)

    return

def decision_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('decision_2() called')

    # check for 'if' condition 1
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["cf_local_ADD_IOC_Containment_LIST_1:custom_function_result.data.0.Results", "==", "success"],
        ],
        case_sensitive=False)

    # call connected blocks if condition 1 matched
    if matched:
        add_note_2(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    # check for 'elif' condition 2
    matched = phantom.decision(
        container=container,
        action_results=results,
        conditions=[
            ["cf_local_ADD_IOC_Containment_LIST_1:custom_function_result.data.0.Results", "==", "Exists"],
        ],
        case_sensitive=False)

    # call connected blocks if condition 2 matched
    if matched:
        add_note_3(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function)
        return

    return

def add_note_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_note_3() called')
    phantom.debug(results)
    note_title = "Containment Result"
    note_content = "Exists"
    note_format = "markdown"
    phantom.add_note(container=container, note_type="general", title=note_title, content=note_content, note_format=note_format)

    return

def custom_function_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('custom_function_1() called')
    
    custom_function_results_data_1 = phantom.collect2(container=container, datapath=['cf_local_ADD_IOC_Containment_LIST_1:custom_function_result.data.0.Results'], action_results=results)
    custom_function_results_item_1_0 = [item[0] for item in custom_function_results_data_1]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    phantom.debug(custom_function_results_data_1)
    phantom.debug(custom_function_results_item_1_0)
    
    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################
    decision_2(container=container)

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return