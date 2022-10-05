from abstract_instrument_interface import abstract_classes
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as Qt# QApplication, QWidget, QMainWindow, QPushButton, QHBoxLayout
import PyQt5.QtGui as QtGui
import logging

class ramp(abstract_classes.abstract_interface):
    """
    Many instruments require having a ramp panel in their GUI, which allows to sweep a certain parameter and send a trigger. This class generates a general "ramp panel", which can then be customized 
    by the child instance, and it contains the minimal logic to do a ramp.
    It inherits from abstract_interface, in order to use some of its methods

    Important: the interface object that istantiate this ramp() object needs to have some QtCore.pyqtSignal objects defined as attributes, in order to communicate with this ramp() object
    
    ## SIGNALS that need to be defined as attributes of self.interface, together with their flags

                                                               | Triggered when ...                               | Send as parameter    
                                                                ------------------------------------------------------------------------------------------------
    sig_connected = QtCore.pyqtSignal(int)                     | The connection stateus of interface changed      | self.interface.SIG_CONNECTED, self.interface.SIG_DISCONNECTED, self.interface.SIG_CONNECTING, self.interface.SIG_DISCONNECTING
    sig_change_moving_status = QtCore.pyqtSignal(int)          | The movement status of interface changed         | self.interface.SIG_MOVEMENT_STARTED, self.interface.SIG_MOVEMENT_ENDED
    
    The interface will emit these signals to notify of changes. 
    """
    
    # Identifier codes used for view-model communication. Other general-purpose codes are specified in abstract_instrument_interface
    SIG_RAMP_STARTED = 1
    SIG_RAMP_STEP_STARTED = 3
    SIG_RAMP_STEP_ENDED = 4
    SIG_RAMP_TRIGGER_FIRED = 5
    SIG_RAMP_ENDED = 2
    
    ## SIGNALS THAT WILL BE USED TO COMMUNICATE WITH THE GUI
    #                                                           | Triggered when ...                                        | Sends as parameter    
    #                                                       #   -----------------------------------------------------------------------------------------------------------------------         
    sig_ramp = QtCore.pyqtSignal(int)                       #   | Ramp event                                                | List containing the stage parameters

    ### Default values of settings (might be overlapped by settings saved in .json files later)
    settings = {   
            'ramp_step_size': 1,
            'ramp_wait_1': 1,
            'ramp_wait_2': 1,
            'ramp_numb_steps': 10,
            'ramp_repeat': 1,
            'ramp_reverse': 1,
            'ramp_send_initial_trigger': 1
             }

    def __init__(self, interface):
        super().__init__(app=interface.app)
        self.interface = interface          #Interface object which is using this ramp object
        self.doing_ramp = False             #Flag variable used to keep track of when a ramp is being done
        self.settings = dict()
        #self.interface.sig_change_moving_status.emit()
        
        
    def set_ramp_functions(self, func_move, func_trigger, func_check_step_has_ended, list_functions_step_not_ended=[],  list_functions_step_has_ended=[],  list_functions_ramp_ended =[]):
        '''
        func_move
            function, takes a single parameter as input
        func_trigger
            function, takes no parameter in input
        func_check_step_has_ended
            function, takes no parameter in input, returns true when the step has ended, false othwerwise
        list_functions_step_not_ended
            list, contains functions that takes no parameter in input. 
            When doing a ramp, after each step is executed, we check wheter the step has ended or not. Everytime that the step has not ended, all functions in this list are executed
        list_functions_step_has_ended
            list, contains functions that takes no parameter in input. 
            When doing a ramp, after each step is executed, we check wheter the step has ended or not. When the step has ended, all functions in this list are executed   
        list_functions_ramp_ended 
            list, contains functions that takes no parameter in input. 
            When the ramp is over all these functions are executed
        '''
        self.func_move = func_move
        self.func_trigger = func_trigger
        self.func_check_step_has_ended = func_check_step_has_ended
        self.list_functions_step_not_ended = list_functions_step_not_ended
        self.list_functions_step_has_ended = list_functions_step_has_ended
        self.list_functions_ramp_ended = list_functions_ramp_ended

    def set_ramp_settings(self,settings):
        '''
        initial_trigger
            bool
        stepsize
            float
        wait1
            float, time in seconds
        wait2
            float, time in seconds
        numb_steps
            int, positive
        add_reverse
            bool
        repeat_ramp
            int, positive
        '''
        ###TO ADD: sanity check on input parameters
        self.settings.update(settings)

    def start_ramp(self):
        initial_trigger = self.settings['ramp_send_initial_trigger']
        stepsize = self.settings['ramp_step_size']
        wait1 = self.settings['ramp_wait_1'] 
        wait2 = self.settings['ramp_wait_2'] 
        numb_steps = self.settings['ramp_numb_steps']
        add_reverse = self.settings['ramp_reverse']
        repeat_ramp = self.settings['ramp_repeat']

        actions = self.generate_list_actions(initial_trigger, stepsize, wait1, wait2, numb_steps, add_reverse , repeat_ramp)
        self.interface.logger.info(f"Starting ramp...")
        self.sig_ramp.emit(self.SIG_RAMP_STARTED)
        self.doing_ramp = True
        self.run_sequence(actions)
    
    def stop_ramp(self):
        self.doing_ramp = False
        self.sig_ramp.emit(self.SIG_RAMP_ENDED)
        self.interface.logger.info(f"Ramp stopped.")
        
    def run_sequence(self,sequence):
        self.sequence = sequence
        self._run_sequence(0)
        
    def _run_sequence(self,index):
        if index >= len(self.sequence):
            self.interface.logger.info(f"Sequence terminated.")
            self.doing_ramp = False
            self.sig_ramp.emit(self.SIG_RAMP_ENDED)
            for action in self.list_functions_ramp_ended:
                action() 
            return
        if self.doing_ramp == False:
            return
        # Execute current action
        current_action = self.sequence[index]
        if current_action['action'] == 'move':
            self.interface.logger.info(f"Will move by {current_action['stepsize']}. Begin moving...")
            self.func_move(current_action['stepsize'])
            #Start checking periodically the value of self.func_check_step_has_ended. If it's false, we call all functions defined in the list self.list_functions_step_not_ended 
            # If it's true, we call all functions defined in the list self.list_functions_step_has_ended, plus the function self._run_sequence(index+1) in order to keep the ramp going, and we stop checking
            self.check_property_until(self.func_check_step_has_ended,[False,True],[self.list_functions_step_not_ended, self.list_functions_step_has_ended + [lambda: self._run_sequence(index+1)]])
        if current_action['action'] == 'wait':
            self.interface.logger.info(f"Waiting for {float(current_action['time'])} s...")
            QtCore.QTimer.singleShot(int(current_action['time']*1e3), lambda :  self._run_sequence(index+1))
        if current_action['action'] == 'send_trigger':
            self.interface.logger.info(f"Sending trigger (if any is defined)...")
            self.func_trigger() #the method update is defined in the super class abstract_interface, it will send a trigger to an external function if any trigger was defined
            self._run_sequence(index+1)
    
    def generate_list_actions(self, initial_trigger, stepsize, wait1, wait2, numb_steps, add_reverse = False, repeat_ramp=1):
        #generate a list of actions that define a ramp
        action =[]
        if initial_trigger:
            action.append({'action':'send_trigger'})
            action.append({'action':'wait', 'time':wait2})
        for j in range(repeat_ramp): #when repeat_ramp > 1, the whole ramp is repeated multiple times
            for i in range(numb_steps):
                action.append({'action':'move', 'stepsize':stepsize})
                action.append({'action':'wait', 'time':wait1})
                action.append({'action':'send_trigger'})
                action.append({'action':'wait', 'time':wait2})
            if add_reverse:
                for i in range(numb_steps):
                    action.append({'action':'move', 'stepsize':-stepsize})
                    action.append({'action':'wait', 'time':wait1})
                    action.append({'action':'send_trigger'})
                    action.append({'action':'wait', 'time':wait2})
        return action
            
    
class ramp_gui(Qt.QGroupBox,abstract_classes.abstract_gui):
    """
    It inherits from abstract_gui, mainly to be able to access general purpose functions such as disable_widget and enable_widget. Might change this in the future
    """
    def __init__(self,ramp):
        super().__init__()
        self.ramp = ramp
        self.initialize()
       
    def initialize(self):
        self.create_widgets()
        ### Connect widgets events to functions
        self.button_StartRamp.clicked.connect(self.click_button_start_ramp)
        ### Connect signals from model to event slots of this GUI
        self.ramp.sig_ramp.connect(self.on_ramp_state_changed)
        self.ramp.interface.sig_change_moving_status.connect(self.on_moving_state_change)
        self.ramp.interface.sig_connected.connect(self.on_connection_status_change)

        ### SET INITIAL STATE OF WIDGETS
        self.checkbox_Initial_trigger.setChecked(bool(self.ramp.settings['ramp_send_initial_trigger']))
        self.edit_StepSize.setText(str(self.ramp.settings['ramp_step_size']))
        self.edit_Wait1.setText(str(self.ramp.settings['ramp_wait_1']))
        self.edit_Wait2.setText(str(self.ramp.settings['ramp_wait_2']))
        self.spinbox_steps.setValue(int(self.ramp.settings[ 'ramp_numb_steps']))
        self.checkbox_Reverse.setChecked(bool(self.ramp.settings['ramp_reverse']))
        self.spinbox_repeat.setValue(int(self.ramp.settings[ 'ramp_repeat']))
        self.on_connection_status_change(self.ramp.interface.SIG_DISCONNECTED) 

    def create_widgets(self):
        self.setTitle(f"Ramp")
        ramp_vbox = Qt.QVBoxLayout()
        ramp_hbox1 = Qt.QHBoxLayout()
        ramp_hbox2 = Qt.QHBoxLayout()
        self.checkbox_Initial_trigger = Qt.QCheckBox("Send initial trigger (+wait)")
        tooltip = 'When this interface is used within a larger software, it can be set to send a trigger (to another function) everytime a step of the ramp is done (see documentation).\nBy ticking this on, a trigger is sent also at the beginning of the ramp.'
        self.checkbox_Initial_trigger.setToolTip(tooltip)
        self.label_Move = Qt.QLabel("Move by")
        self.edit_StepSize = Qt.QLineEdit()
        self.label_Wait1 = Qt.QLabel(",wait for")
        self.edit_Wait1 = Qt.QLineEdit()
        self.edit_Wait1.setMaximumWidth(35)
        self.label_Wait2 = Qt.QLabel("s, send trigger, wait for")
        self.edit_Wait2 = Qt.QLineEdit()
        self.edit_Wait2.setMaximumWidth(35)
        self.label_steps = Qt.QLabel("s, repeat")
        self.spinbox_steps = Qt.QSpinBox()
        self.spinbox_steps.setRange(1, 100000)
        self.label_steps2 = Qt.QLabel("times.")
        self.widgets_row1 = [self.checkbox_Initial_trigger, self.label_Move, self.edit_StepSize, self.label_Wait1,
                                        self.edit_Wait1, self.label_Wait2, self.edit_Wait2,self.label_steps, self.spinbox_steps, self.label_steps2]
        for w in self.widgets_row1:
            ramp_hbox1.addWidget(w)
        ramp_hbox1.addStretch(1) 

        self.checkbox_Reverse = Qt.QCheckBox("and reverse.")
        self.label_repeat = Qt.QLabel(" Repeat ramp")
        self.spinbox_repeat = Qt.QSpinBox()
        self.spinbox_repeat.setRange(1, 100000)
        self.label_repeat2 = Qt.QLabel(" times.")
        self.button_StartRamp = Qt.QPushButton("Start Ramp")
        self.widgets_row2 = [self.checkbox_Reverse, self.label_repeat, self.spinbox_repeat ,
                                        self.label_repeat2, self.button_StartRamp]
        for w in self.widgets_row2:
            ramp_hbox2.addWidget(w)
        ramp_hbox2.addStretch(1) 

        ramp_vbox.addLayout(ramp_hbox1)  
        ramp_vbox.addLayout(ramp_hbox2)  
        self.setLayout(ramp_vbox ) 
        self.list_widgets = self.widgets_row1 + self.widgets_row2

        # Widgets for which we want to constraint the width by using sizeHint()
        widget_list = self.list_widgets
        for w in widget_list:
            w.setMaximumSize(w.sizeHint())


###########################################################################################################
### Event Slots. They are normally triggered by signals from the model, and change the GUI accordingly  ###
###########################################################################################################

    def on_ramp_state_changed(self,status):
        if status == self.ramp.SIG_RAMP_STARTED:
            self.set_doingramp_state()
        if status == self.ramp.SIG_RAMP_ENDED:
            self.set_notdoingramp_state()

    def on_connection_status_change(self,status):
        if status in [self.ramp.interface.SIG_DISCONNECTED,self.ramp.interface.SIG_DISCONNECTING,self.ramp.interface.SIG_CONNECTING]:
            self.disable_widget(self.list_widgets)
        if status == self.ramp.interface.SIG_CONNECTED:
            self.enable_widget(self.list_widgets)

    def on_moving_state_change(self,status):
        if status == self.ramp.interface.SIG_MOVEMENT_STARTED:
            self.disable_widget(self.list_widgets)
        if status == self.ramp.interface.SIG_MOVEMENT_ENDED:
            self.enable_widget(self.list_widgets)
    
#######################
### END Event Slots ###
#######################

    def click_button_start_ramp(self):
        if self.ramp.doing_ramp == False:

            settings = {   
                    'ramp_step_size': float(self.edit_StepSize.text()),
                    'ramp_wait_1': float(self.edit_Wait1.text()),
                    'ramp_wait_2': float(self.edit_Wait2.text()),
                    'ramp_numb_steps': int(self.spinbox_steps.value()),
                    'ramp_repeat': int(self.spinbox_repeat.value()),
                    'ramp_reverse': self.checkbox_Reverse.isChecked(),
                    'ramp_send_initial_trigger': (self.checkbox_Initial_trigger.isChecked() == True)
                     }

            self.ramp.set_ramp_settings(settings)
            self.ramp.start_ramp()
        else:
            self.ramp.stop_ramp()

    def set_doingramp_state(self, text = "Stop Ramp"):
        self.disable_widget(self.list_widgets)
        self.enable_widget([self.button_StartRamp])
        self.button_StartRamp.setText("Stop Ramp")
            
    def set_notdoingramp_state(self, text = "Start Ramp"):
        self.enable_widget(self.list_widgets)
        self.button_StartRamp.setText("Start Ramp")

    #def setEnabled(self,state):
    #    if state:
    #        self.enable_widget(self.list_widgets)
    #    else:
    #        self.disable_widget(self.list_widgets)
    #    return
