'''
pymax.py

An interface for communicating between Python and Max/MSP.
Copyright (c) 2022, Daniel Brown
Contact: daniel@intelligentmusicsystems.com
All rights reserved.

Distributed under the Attribution-NonCommercial-ShareAlike (CC BY-NC-SA) license
(https://creativecommons.org/licenses/by-nc-sa/4.0/):

You are free to:

Share — copy and redistribute the material in any medium or format
Adapt — remix, transform, and build upon the material

(The licensor cannot revoke these freedoms as long as you follow the license terms.)

Under the following terms:

Attribution — You must give appropriate credit, provide a link to the license, 
and indicate if changes were made. You may do so in any reasonable manner, 
but not in any way that suggests the licensor endorses you or your use.

NonCommercial — You MAY NOT use the material for commercial purposes 
without explicit written consent of the author.

ShareAlike — If you remix, transform, or build upon the material, 
you must distribute your contributions under the same license as the original.

No additional restrictions — You may not apply legal terms or technological 
measures that legally restrict others from doing anything the license permits.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''


# GENERATOR -------------------------------------------------------------------

class Generator():

    def __init__(self, gen_cls, gen_cls_args):
        self.gen_cls        = gen_cls
        self.gen_cls_args   = gen_cls_args
        self.gen            = gen_cls(*gen_cls_args)

        self.tempo          = 60
        self.time           = 0
        self.next_event     = None

    def reset(self):
        self.gen        = self.gen_cls(*self.gen_cls_args)
        self.time       = 0
        self.next_event = None

    def update(self, time_type : str, time_incr):
        return [event for event in self.next_events(time_type, time_incr)]

    def next_events(self, time_type : str, time_incr):
        if time_type == 'beats':
            time_incr = time_incr * self.tempo / 60000
        if not self.next_event:
            self.advance()
        while self.next_event and self.next_event[0] < self.time:
            self.advance()
        while self.next_event and self.next_event[0] < self.time + time_incr:
            yield self.next_event.copy()
            self.advance()
        self.time += time_incr
            
    def advance(self):
        try:
            self.next_event = next(self.gen)
        except StopIteration:
            self.next_event = None

# HANDLER ------------------------------------------------------------------------------------------------

class Handler():

    def __init__(self, obj):
        self.obj = obj

    def get_var(self, var_name : str):
        try:
            return getattr(self.obj, var_name)
        except AttributeError:
            raise

    def set_var(self, var_name : str, value):
        try:
            setattr(self.obj, var_name, value)
            #return self.get_var(var_name)
        except AttributeError:
            raise

    def call(self, fcn_name : str, *args):
        try:
            return getattr(self.obj, fcn_name)(*args)
        except AttributeError:
            raise      


# HANDLER SYSTEM ---------------------------------------------------------------------------------------------

class HandlerSystem(dict):

    def __init__(self):
        super().__init__(self)

    def add_handler(self, name : str, obj):
        self[name] = Handler(obj)

    def process_message(self, obj_name : str, fcn_name : str, *args):
        try:
            obj = self[obj_name]
        except AttributeError:
            print("Unknown object " + obj_name + " called with method " + fcn_name + " and args " + " ".join([str(arg) for arg in args]) + ".")
        try:
            fcn = getattr(obj, fcn_name)
        except AttributeError:
            print("Unknown attribute " + args[0] + " called on object " + obj_name + " with args " + " ".join([str(arg) for arg in args[1:]]) + ".")
        return fcn(*args)

# OSC SYSTEM ------------------------------------------------------------------------------------------------------------

from osc4py3.as_eventloop   import *
from osc4py3                import oscmethod, oscbuildparse
from osc4py3.oscmethod      import OSCARG_ADDRESS, OSCARG_DATAUNPACK

import sys

class OSC_System():
    def __init__(self, server_name, client_name, host_ip, receive_port, send_port, receive_addr, send_addr):
        self.client_name = client_name
        self.send_addr   = send_addr
        self.osc_running = False

        osc_startup()
        osc_udp_server(host_ip, receive_port, server_name)
        osc_udp_client(host_ip, send_port, client_name)
        osc_method(receive_addr, self.process_message, argscheme = OSCARG_DATAUNPACK)

    def close(self):
        self.osc_running = False

    def run(self):
        self.osc_running = True
        print("PyMax loop entered. Press Ctrl-C to exit loop.")
        try:
            while self.osc_running:
                osc_process()
        except KeyboardInterrupt:
            self.osc_running = False
        osc_terminate()
        sys.exit("PyMax loop exited. Have a good day.")

    def send(self, msg):
        osc_msg = oscbuildparse.OSCMessage(self.send_addr, None, msg)
        osc_send(osc_msg, self.client_name)
        #print(msg)

    def process_message(self, *msg):
        # override in subclasses
        pass

# LOGGER ---------------------------------------------------------------------------------------------------------------

import pickle

class Logger():

    def __init__(self):
        self.data = []
        self.time = 0
        self.active = 0

    def reset(self):
        self.time = 0

    def update(self, time_incr):
        if self.active:
            self.time += time_incr

    def log(self, addr, item):
        self.data.append((self.time, addr, item))

    def save(self, filepath):
        pickle.dump(self.data, open(filepath, "wb" ))


# MESSAGE FORMATTER ------------------------------------------------------------------------------------------

class MessageFormatter():

    def __init__(self):
        pass

    def format_msg(self, addr, msg):
        if isinstance(msg, list):
            return [addr, *self.format_list_msg(msg)] #[self.format_item(item) for item in msg]
        else:
            return [addr, msg]

    def format_list_msg(self, msg):
        # if the msg is a list, each item must be:
        # - (if it's an atom) just an atom
        # - (if it's a list) a string representing the flattened list of the item
        return [self.format_list_item(item) if isinstance(item, list) else item for item in msg]

    def format_list_item(self, l):
        return " ".join([self.format_list_item(item) if isinstance(item, list) else str(item) for item in l])

# PYMAX SYSTEM --------------------------------------------------------------------------------------------------------

'''
Message types:
['obj_name', 'set_var',     'var_name',     value       ]
['obj_name', 'get_var',     'var_name'                  ] 
['obj_name', 'call'         'method_name',  *method_args]
['gen_name', 'update',                                  ]
['gen_name', 'synchronize', ticks_per_beat, raw_ticks   ]
['sys',      'close']
['sys',      'save']
'''

class PyMaxSystem(OSC_System):

    def __init__(self, receive_port, send_port):

        super().__init__('pymax_server', 'pymax_client', '127.0.0.1', receive_port, send_port, '/pymax', '/pymax')

        self.handlers           = HandlerSystem()
        #elf.handlers['sys']    = self
        self.message_formatter  = MessageFormatter()
        self.logger             = Logger()
        self.add_object('log', self.logger)
    

    def add_object(self, name : str, obj):
        self.handlers.add_handler(name, obj)


    def add_class(self, name : str, cls, *args):
        self.handlers.add_handler(name, cls(*args))


    def add_generator(self, name : str, gen_cls, *arg_names):
        gen_cls_args = [self.handlers[arg_name].obj for arg_name in arg_names]
        self.handlers.add_handler(name, Generator(gen_cls, gen_cls_args))


    def process_message(self, *in_msg):
        [addr, fcn, *args] = in_msg
        result = self.handlers.process_message(addr, fcn, *args)
        if result:
            out_msg = self.message_formatter.format_msg(addr, result)
            self.send(out_msg)
            if self.logger.active:
                self.logger.log(addr, result)

# TOP-LEVEL INTERFACE -------------------------------------------------------------------------------------------------

pymax_system = None
receive_port = 7002
send_port    = 7003

def open_pymax():
    global pymax_system, send_port, receive_port
    pymax_system = PyMaxSystem(receive_port, send_port)

def add_class(obj_name : str, cls, *args):
    global pymax_system
    pymax_system.add_class(obj_name, cls, *args)

def add_object(obj_name : str, obj):
    global pymax_system
    pymax_system.add_object(obj_name, obj)

def add_generator(gen_name : str, gen_cls, *arg_names):
    global pymax_system
    pymax_system.add_generator(gen_name, gen_cls, *arg_names)

def run_pymax():
    global pymax_system
    pymax_system.run()