from patterns.observer.concrete_observable import YouTubeChanel
from patterns.observer.concrete_observer import YouTubeSubscriber

if __name__ == '__main__':
    # youtube chanel (observable)
    my_chanel = YouTubeChanel('my_chanel')

    # youtube subscribers (observers)
    sub1 = YouTubeSubscriber('sub1', my_chanel)
    sub2 = YouTubeSubscriber('sub2', my_chanel)
    sub3 = YouTubeSubscriber('sub3', my_chanel)

    # registering the subscribers
    my_chanel.add([sub1, sub2, sub3])

    # post a new video and notifying the subscribers
    print('-> NEW VIDEO AND NOTIFYING')
    my_chanel.post_video('THE FIRST VIDEO OF MY CHANEL')
    my_chanel.notify()

    # subscriber number 2, after some time, verifying if the my_chanel posted a new video
    print('-> LOCKING FOR UPDATES (NO VIDEO)')
    sub2.update()

    # removing sub2 from my_chanel
    my_chanel.remove(sub2)

    # post a new video and notifying the subscribers
    my_chanel.post_video('THE SECOND VIDEO OF MY CHANEL')

    # but subscriber 2 can still get the my_chanel state
    print('-> LOCKING FOR UPDATES (WITH VIDEOS)')
    sub2.update()
    sub2.update()
    sub2.update()
    sub3.update()

    # notifying all the subscribers about the new video
    print('-> NOTIFYING')
    my_chanel.notify()
