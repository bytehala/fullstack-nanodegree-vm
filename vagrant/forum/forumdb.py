#
# Database access functions for the web forum.
#
import bleach
import psycopg2
import time

## Database connection


## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    DB = psycopg2.connect("dbname=forum")
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM posts")
    results = cursor.fetchall()
    #print(results)
    posts = [{'content': (str(row[0])), 'time': str(row[1])} for row in results]
    posts.sort(key=lambda row: row['time'], reverse=True)
    DB.close();
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    DB = psycopg2.connect("dbname=forum")
    cursor = DB.cursor()
    t = time.strftime('%c', time.localtime())
    disp = bleach.clean(content)
    cursor.execute("INSERT INTO posts values (%s)",(disp,))
    DB.commit()
    DB.close()
