import praw




def get_reddit():

    reddit = praw.Reddit(client_id='ftEo3O0al4CSCA',
                     client_secret='sHQdYvHTijtinLmXZwh4GwN6tiI',
                     user_agent='ProjectM by BoilingFusion and d3athk1ss')




    for submission in reddit.subreddit('Showerthoughts').new(limit=1):
    
        sub = submission.title
        return sub
    


