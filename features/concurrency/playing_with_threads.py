import _thread
import time
import random

def talk_to_me(self, name):
	while True:
		print("%s: Hey, hey, hey" % name)
		time.sleep(random.randint(1, 5))

_thread.start_new_thread(talk_to_me, ("thread1", "thread1"))
_thread.start_new_thread(talk_to_me, ("thread2", "thread2"))
_thread.start_new_thread(talk_to_me, ("thread3", "thread3"))

while True:
	"keep going round"

