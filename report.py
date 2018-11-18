#!/usr/bin/env python
import psycopg2
# this query to select top three articles.
articles_select = """
                select quote_ident(title),count(*) as num
                from articles join log on articles.slug=substr(log.path,10)
                where log.status='200 OK'
                group by articles.title
                order by num desc
                limit 3;
                """  
# this query to select top three authors.
authors_select= """
                select authors.name ,count(*) as num
                from authors join articles on authors.id=articles.author
                join log on articles.slug=substr(log.path,10)
                where log.status='200 OK'
                group by authors.name
                order by num desc
                limit 3;
                """

# this query to select which days did mor than 1% of requests lead to errors.
error_select =  """
                select date,faild_precentage 
                from precentage where faild_precentage >1;
                """


#this def to execute top three articles select and print Information about it.
def top_three_articles():
    db = psycopg2.connect(dbname = 'news')
    c = db.cursor()
    c.execute(articles_select)
    result = c.fetchall()
    db.close()

    print('\n\tTop three articles:\n')

    for title,num in result:
        print(" \n{} -- {} views\n".format(title, num))

#this def to execute top three authors select and print information about it.
def top_three_authors():
    db = psycopg2.connect(dbname = 'news')
    c = db.cursor()
    c.execute(authors_select)
    result = c.fetchall()
    db.close()

    print('\n\tTop three authors:\n')

    for name,num in result:
        print(" \n{} -- {} views\n".format(name, num))

#this def to execute error precentage select and print information about it.
def error_precentage():
    db = psycopg2.connect(dbname = 'news')
    c = db.cursor()
    c.execute(error_select)
    result = c.fetchall()
    db.close()

    print('\n\t Days which more than 1% lead to error:')

    for date,faild_precentage in result:
        print ("\n{} -- {} % errors\n".format(date,round(faild_precentage,2)))


if __name__ == '__main__':
    top_three_articles()
    top_three_authors()
    error_precentage()
