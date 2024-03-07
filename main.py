import ThingESP
thing = ThingESP.Client('user_name', 'project_name', 'password')
ThingESP.send_msg('device is back online ')

# this function handles query, add conditions to trigger certain tasks
def handleResponse(query):
    if query == 'are you up?':
        return 'Iam up!'

    else:
        return 'no task is set for [%s]'%query


thing.setCallback(handleResponse).start()

print('END_TASK')




