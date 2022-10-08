import queue
import time

def get_fps(seconds):
    if seconds == 0:
        return 99999
    return 1/seconds

def print_average(world):
     print("average FPS: ", round(world.average_fps(),2))
    
def spawn_timer():
    return [('s',spawn_timer,[]), ('i',print,["Time: ", round(time.time(),2)])]

class Stopwatch():
    def __init__(self):
        self.last = time.time()
        self.now = time.time()
        self.elapsed = 0
        pass

    def stop(self):
        self.last = self.now
        self.now = time.time()
        self.elapsed = self.now-self.last

    def time(self):
        self.stop()
        return self.now

    def read(self):
        return time.time()-self.now

    def read_and_set(self):
        self.stop()
        return self.elapsed

class World():
    def __init__(self, fps=None, sample=None):
        # Frame per second
        self.fps = fps if fps is not None else 60
        self.q = queue.Queue()
        # Sample Size
        self.sample = sample if sample is not None else self.fps
        # recn is average of recent several fpses
        self.timer = Stopwatch()

        self.events = queue.Queue()
        self.tasks = queue.Queue()
        self.next_frame = queue.Queue()

        
        self.add_event(('i',self.init_fps, []))
        self.add_event(('r',self.limit_fps, []))
        self.add_event(('r',self.update_fps, []))

    def run(self):
        while True:
            try:
                task = self.events.get(False)
                if '-' in task[0]:
                    residue = task[1]
                else:
                    residue = task[1](*task[2])
                # r: repeat next time
                if 'r' in task[0]:
                    self.next_frame.put(task)
                # j: jump in line
                if 'j' in task[0]:
                    for i in reversed(residue):
                        # self.events.put(i)
                        self.events.queue.insert(0, i)
                # s: spawn
                if 's' in task[0]:
                    for i in residue:
                        self.next_frame.put(i)

            except queue.Empty as e:
                if self.next_frame.empty():
                    break
                # Swap to next frame
                tmp = self.events
                self.events = self.next_frame
                self.next_frame = tmp

    '''
    Usable variables:
        self.elapsed
        self.loop_end
    '''
    def init_fps(self):
        very_beginning = self.timer.time()-self.sample/self.fps
        for i in range(self.sample+1):
            self.q.put(very_beginning+i*self.sample/self.fps/self.fps)

    '''
    TODO: Issue: Setting fps = 100, 99,90,99,90 pattern would occur
    '''
    def limit_fps(self):
        while True:
            if get_fps(self.timer.read()) > self.fps+1:# TODO optimize later!!!
                continue
            break

    def update_fps(self):
        self.q.get()
        self.q.put(self.timer.time())
    
    def average_fps(self):
        return self.sample*get_fps(self.timer.now-self.q.queue[0])

    def add_event(self, new_event):
        self.events.put(new_event)

# # data = World(30)
# data.add_event(('r',print_average, [data]))
# data.add_event(('s',spawn_timer,[], []))
# data.run()

