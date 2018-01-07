import logging

from clickstream.consumer import Consumer


if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s] %(message)s',
                        level=logging.INFO)
    loggerSpark = logging.getLogger('py4j')
    loggerSpark.setLevel('WARNING')

    consumer = Consumer()
    ssc = consumer.categories()

    try:
        ssc.start()
        ssc.awaitTermination()
    except KeyboardInterrupt:
        ssc.stop(stopGraceFully=True)
