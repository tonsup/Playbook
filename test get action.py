"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    updated_artifact = {}
    phantom.debug('on_start() called')
    phantom.debug(container)
    phantom.debug('print artifact')
    #artifacts = phantom.collect(container, 'artifacts:*', scope='all')
    artifacts = phantom.collect2(container=container, datapath=['artifact:*.cef.*', 'artifact:*.id'])
    phantom.debug(artifacts[0])
    
    #phantom.debug(artifacts[1]["cef"]["app"]
    updated_artifact['cef'] = artifacts[0]['cef']
    updated_artifact['cef_types'] = artifacts[0]['cef_types']
    
    
    #phantom.debug(updated_artifact)
    #updated_artifact['cef'].update({"myname2": "suphachok"})
    #updated_artifact['cef_types'].update({"myname2": ["domain"]})
    key = '_originating_search'
    if key in updated_artifact['cef']:
        del updated_artifact['cef']['_originating_search']
    
    if key in updated_artifact['cef']:
        del updated_artifact['cef_types']['_originating_search']
    
    artifact_id = artifacts[0]["id"]
    phantom.debug('updating artifact {} with the following attributes:\n{}'.format(artifact_id, updated_artifact))
    url = phantom.build_phantom_rest_url('artifact', artifact_id)
    phantom.debug(url)
    response = phantom.requests.post(url, json=updated_artifact, verify=False).json()

    phantom.debug('POST /rest/artifact returned the following response:\n{}'.format(response))
    if 'success' not in response or response['success'] != True:
        raise RuntimeError("POST /rest/artifact failed")
    #update_data = { "severity": "low" }
    #success, message = phantom.update(container, update_data)
    
    #phantom.debug('Update Container')
    #phantom.debug(phantom.get_raw_data(container))
    #phantom.debug(container)
    
    #iurl =  phantom.build_phantom_rest_url('indicator/1018')
    #response = phantom.requests.get(iurl, verify=False).json()
    #params = {"page_size":1000 , "order":"desc" ,"timerange" : "last_30_days"}
    
    #response = phantom.requests.get(iurl, params=params, verify=False).json()
    #response = phantom.requests.get(iurl, verify=False).json()
    #phantom.debug(response)
    
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