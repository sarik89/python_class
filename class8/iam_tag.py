import boto3
def lambda_handler(event, context):
    client = boto3.client('iam')
    #print(dir(client))
    #create empty list
    USERLIST = []
    #get list of users from AWS,and assign it to response
    response = client.list_users()
    #Filter thru json output,and get usernames
    for list_of_users in response ["Users"]:
        print(list_of_users["UserName"])
        #Append each username into an empty list
        USERLIST.append(list_of_users["UserName"])
    print(USERLIST)    


    for list_of_users in USERLIST:
        response = client.tag_user(
            UserName=list_of_users,
            Tags=[
                {
                    'Key': 'Team',
                    'Value': 'DevOps'
                },
                {
                    'Key': 'Dept',
                    'Value': 'IT'
                },
            ]
        )