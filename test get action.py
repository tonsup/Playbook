"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    updated_artifact = {}
    phantom.debug('on_start() called')
  
    
    #iurl =  phantom.build_phantom_rest_url('action_run')
    iurl =  phantom.build_phantom_rest_url('playbook_run/165')
    response = phantom.requests.get(iurl, verify=False).json()
    updated_artifact = response
    updated_artifact['status'] = "success"
    phantom.debug(updated_artifact)
    #params = {"page_size":1000 , "order":"desc" ,"timerange" : "last_30_days"}
    
    #response = phantom.requests.get(iurl, params=params, verify=False).json()
    #response = phantom.requests.get(iurl, verify=False).json()
    response = phantom.requests.post(iurl, json=updated_artifact, verify=False).json()
    phantom.debug(response)
    
    # call 'playbook_community_investigate_1' block
    #playbook_community_investigate_1(container=container)
   
    return

def playbook_community_investigate_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('playbook_community_investigate_1() called')
    
    # call playbook "community/investigate", returns the playbook_run_id
#    playbook_run_id = phantom.playbook(playbook="community/investigate", container=container)

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