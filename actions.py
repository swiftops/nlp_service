from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import json
import random


def load_data(msgdata):
    testdict = {}
    textdata = ""
    k1 = ""
    attachmentsdata = []
    if msgdata:
        for i in range(0, len(msgdata[0])):
            testdict['title'] = msgdata[0][i]
            for k, v in msgdata[1][i].items():
                if k == "data" and v is not None:
                    for k1, v1 in v.items():
                        if k1 == 'tabulardata':
                            for i in v1[1]:
                                textdata = textdata + '\n' + i[0]
                                if len(i) > 1:
                                    for itr in range(1, len(i)):
                                        textdata = textdata + ' : ' + i[itr]
                        else:
                            textdata = textdata + '\n' + k1 + ' : ' + str(v1)
                elif v is None:
                    textdata = "No Result"
            if textdata:

                if k1 == 'url':
                    testdict['text'] = "Click here to get " + testdict['title']
                    testdict['title_link'] = textdata.split("\nurl : ")[1]
                else:
                    testdict['text'] = textdata
                testdict['color'] = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
                attachmentsdata.append(testdict)
            testdict = {}
            textdata = ""

        return attachmentsdata

class getRelease(Action):
    def name(self):
        return 'get_release'

    def run(self, dispatcher, tracker, domain):
        release_no=''
        build_no=''

        for item in (tracker.latest_message)['entities']:
            if item['entity'] == 'release_no':
                release_no = item['value']
            elif item['entity'] == 'build_no':
                build_no = item['value']
        print(release_no)
        print(build_no)
        if release_no and build_no:
            filter_service = "http://swiftops.digite.com/rootservice/filter"
            data = {'query': 'release ' + release_no + ';' + build_no, 'username': 'vpanda'}
            buildresponse = requests.post(filter_service, data=data)
            msgdata = json.loads(buildresponse.text)
            attachmentsdata = load_data(msgdata)
            print(attachmentsdata[0])
            if attachmentsdata[0]['title'] == 'Change Log':
                # Pass response to calling api of slack using 'dispatcher.utter_message'
                dispatcher.utter_attachment(json.dumps(attachmentsdata))
            else:
                response_data = "No Result found for the specified Release and build no."
                dispatcher.utter_message(response_data)
        elif release_no == '' and build_no == '' :
            response_data = "Specify release and build no."
            dispatcher.utter_message(response_data)
        else:
            response_data ="No Result found for the specified release and build no."
            dispatcher.utter_message(json.dumps({'text':tracker.latest_message}))