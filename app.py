from aifc import Error

import pika, sys, os,re,json
from pika import channel
result = None

def resive():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rmq.esphere.local'))
    channel = connection.channel()
    channel.queue_declare(queue='notif_lkk_11.12',durable=True)

    def callback(ch, method, properties, body):
        global result
        result=body.decode()

        try:
            prepare_date=(body.decode())
       # print (type(prepare_date))
            if '79214199530' in prepare_date:

              json_date= json.loads(prepare_date)
              print(json_date['message']['text'])
            else:
               pass
        except (Exception, Error) as error:
            print(' нет номера '+ str(error))
    channel.basic_consume('notif_lkk_11.12', on_message_callback=callback ,auto_ack=True)
    channel.start_consuming()
resive()
