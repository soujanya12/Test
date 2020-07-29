def my_handler(event, context):
    message = 'Hello {} {}!'.format(event['payload']['first_name'],
                                    event['payload']['last_name'])
    return {
        'message' : message
    }
event = {"payload":{'first_name':'soujanya','last_name':'gangula'}}
print(my_handler(event,context={}))