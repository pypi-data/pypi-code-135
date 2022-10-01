'''
###########################
VTOFG: Vibration Test Object Function Generator
###########################
vtofg.plotter
Author: Zack Ravetz

This file contains VTOFG's "Plotter" class. This defines the class used to
plot the modelled ultrasound output
'''

import numpy as np
import matplotlib as mpl
mpl.use("TkAgg") #necessary so that matplotlib figures can be embedded in tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as anim
from matplotlib.figure import Figure
import tkinter as tk
import time
import threading
import math
from tkinter import TclError

SPEED_OF_SOUND = 154000 #speed of sound in tissue in cm/s

class Plotter(tk.Frame):
    '''
    The class for collecting the relevant parameters and plotting the real time(ish) 
    expected spectral doppler ultrasound 

    Attributes
    ----------
    main: FunctionGenerator
        The function generator object for this Plotter
    show_time: float
        The period of time shown on the spectrum in seconds (this is the length of each frame)
    PRF: int
        The pulse repetition frequency used to model the spectrum in Hz
    n_lines: int
        The number of lines show per show time
    line_period: float
        The length of time each line represents in seconds
    waves: list[SweepWave]
        A list of SweepWave objects to calculate the signal from
    time: float
        A timestamp used to control the rate that each line is shown
    start_time: float
        A timestamp used to control the rate that each frame is shown
    gain: float
        The gain applied to the spectrum after the FFT (fast fourier transform) of the signal is found
    delay: float
        A value used to control the rate that each line is shown
    prev_i: int
        Previous i-th animation
    fft_len: int
        The number of frequencies that are given when the FFT is calculated
    freq_mask: array like
        A mask to remove any frequencies less than the wall frequency
    heatmap_array: array like
        The array used to hold the data that is shown in heatmap
    next_frame_array: array like
        The array used to hold the data for the next frame after the one that is being played
    current_frame_array: array like
        The array used to hold the data for the current frame that heatmap_array is updated from
    zeros: array like
        An array of zeros
    start_line: Int
        The number of lines shown before the next frame
    next_thread: Thread
        The thread used to calculate the next frame
    fig: matplotlib figure
        The matplotlib figure object containing ax
    ax: matplotlib axes
        The matplotlib axes object containing heatmap
    heatmap: matplotlib imshow
        The matplotlib imshow object that shows the spectrum
    canvas: FigureCanvasTkAgg
        The matplotlib canvas object required to show matplotlib figures in tkinter
    trans_freq_var: tkinter IntVar
        The tkinter variable containing the transducer frequency in kHz
    PRF_var: tkinter IntVar
        The tkinter variable containing the pulse repetition frequency in Hz
    max_speed_lab: tkinter Label
        The tkinter label to show the max speed without aliasing for the given PRF/transducer freq
    show_time_var: tkinter DoubleVar
        The tkinter variable containing the show time in seconds
    n_lines_var: tkinter IntVar
        The tkinter variable containing the number of lines per frame
    wall_filt_var: tkinter IntVar
        The tkinter variable containing the wall filter cutoff in Hz
    gain_var: tkinter DoubleVar
        The tkinter variable containing the gain
    delay_time_var: tkinter IntVar
        The tkinter variable containing the delay 
    pos_label: tkinter Label
        The label to show the curser position on the graph
    anim: matplotlib FuncAnimation
        The FuncAnimation object used to update heatmap
    paused: bool
        Used to keep track of if the signal is paused 

    Methods
    -------
    mouse_move(event):
        Updates pos_label with the position of the mouse
    calc_max:
        Updates max_speed_lab with the maximum speed possible to show without aliasing
    update:
        Updates heatmap and current_frame_array, called by anim
    get_next:
        Calculates the next frame, called in next_thread
    toggle_pause(waves):
        plays/pauses the plotting of the spectrum
    '''
    def __init__(self, main) -> None:
        '''
        constructs the Plotter

        Parameters
        ----------
        main: FunctionGenerator
            The function generator object for this Plotter
        '''
        super().__init__(main)
        self.columnconfigure(3, weight = 1)
        self.main = main

        #starting values
        trans_freq = 7000000 #transducer frequency in Hz
        wall_filt = 0 #wall filter in Hz
        self.show_time = 10.0
        self.PRF = 5000
        self.n_lines = 100
        self.line_period = self.show_time/self.n_lines
        self.waves = []
        self.time = time.time()
        self.start_time = time.time()
        self.gain = 1
        self.delay = 0.01
        self.prev_i = 1

        #calculates the length of the FFT and the frequency mask
        self.fft_len = round(self.line_period*self.PRF)
        self.fft_freqs = np.fft.fftshift(np.fft.fftfreq(self.fft_len)*self.PRF)
        self.freq_mask = self.fft_freqs>=wall_filt


        #starting values for the arrays
        self.heatmap_array = np.zeros((self.fft_len, self.n_lines))
        self.next_frame_array = np.zeros((self.fft_len, self.n_lines))
        self.current_frame_array = np.zeros((self.fft_len, self.n_lines))
        self.zeros = np.zeros(self.fft_len)
        self.start_line = 0

        #starts next_thread to calculate the next frame
        self.next_thread = threading.Thread(target = self.get_next)
        self.next_thread.start()

        #creates and formats the figure/axes
        self.fig = Figure(tight_layout=True)
        self.fig.canvas.mpl_connect ('motion_notify_event', self.mouse_move)
        self.ax = self.fig.add_subplot(111)
        self.heatmap = self.ax.imshow(self.heatmap_array,
            vmax = 1,
            vmin = 0,
            cmap='gray',
            aspect='auto')

        self.ax.set_xticks(np.linspace(0, self.n_lines-1, 10))
        xticks = ['' for _ in range(10)]
        xticks[-1] = str(self.show_time)+'s'
        self.ax.set_xticklabels(xticks)

        self.ax.yaxis.set_ticks_position("right")
        self.ax.set_yticks(np.linspace(0, self.fft_len, 7))
        yticks = np.linspace(-np.min(self.fft_freqs), np.min(self.fft_freqs), 7)
        yticks = np.round(SPEED_OF_SOUND*yticks/(2*trans_freq), 1)
        yticks = [str(tick) for tick in yticks]
        yticks[2] = yticks[2]+'cm/s'
        self.ax.set_yticklabels(yticks)
        
        #creates the canvas for embedding the figure in tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=0, row=0, rowspan=7 ,sticky='nsew')

        #tkinter layouts/entries to collect user information
        self.trans_freq_var = tk.IntVar(self)
        self.trans_freq_var.set(int(trans_freq/1000))
        trans_freq_lab = tk.Label(self, text="Transducer Frequency(kHz):")
        trans_freq_input = tk.Entry(self,
            textvariable=self.trans_freq_var,
            validate='all',
            validatecommand=(self.main.vcmd_int, '%P'))
        trans_freq_lab.grid(column=1, row=0, sticky='ew')
        trans_freq_input.grid(column=2, row=0, sticky='ew')
        
        self.PRF_var = tk.IntVar(self)
        self.PRF_var.set(self.PRF)
        PRF_lab = tk.Label(self, text="Pulse Repetition Frequency(Hz):")
        PRF_input = tk.Entry(self,
            textvariable=self.PRF_var,
            validate='all',
            validatecommand=(self.main.vcmd_int, '%P'))
        PRF_lab.grid(column=1, row=1, sticky='ew')
        PRF_input.grid(column=2, row=1, sticky='ew')

        max_speed = np.round(SPEED_OF_SOUND*self.PRF/(4*trans_freq), 1)
        self.max_speed_lab = tk.Label(self, text="(max " + str(max_speed) + "cm/s)")
        self.max_speed_lab.grid(column=3, row=1, sticky='ew')
        self.trans_freq_var.trace_add('write', self.calc_max)
        self.PRF_var.trace_add('write', self.calc_max)

        self.show_time_var = tk.DoubleVar(self)
        self.show_time_var.set(self.show_time)
        show_time_lab = tk.Label(self, text="Display Time(s):")
        show_time_input = tk.Entry(self,
            textvariable=self.show_time_var,
            validate='all',
            validatecommand=(self.main.vcmd_float, '%P'))
        show_time_lab.grid(column=1, row=2, sticky='ew')
        show_time_input.grid(column=2, row=2, sticky='ew')

        self.n_lines_var = tk.IntVar(self)
        self.n_lines_var.set(self.n_lines)
        n_lines_lab = tk.Label(self, text="Display Samples:")
        n_lines_input = tk.Entry(self,
            textvariable=self.n_lines_var,
            validate='all',
            validatecommand=(self.main.vcmd_int, '%P'))
        n_lines_lab.grid(column=1, row=3, sticky='ew')
        n_lines_input.grid(column=2, row=3, sticky='ew')

        self.wall_filt_var = tk.IntVar(self)
        self.wall_filt_var.set(wall_filt)
        wall_filt_lab = tk.Label(self, text="Wall Filter(Hz):")
        wall_filt_input = tk.Entry(self,
            textvariable=self.wall_filt_var,
            validate='all',
            validatecommand=(self.main.vcmd_int, '%P'))
        wall_filt_lab.grid(column=1, row=4, sticky='ew')
        wall_filt_input.grid(column=2, row=4, sticky='ew')

        self.gain_var = tk.DoubleVar(self)
        self.gain_var.set(self.gain)
        gain_lab = tk.Label(self, text="Gain:")
        gain_input = tk.Entry(self,
            textvariable=self.gain_var,
            validate='all',
            validatecommand=(self.main.vcmd_float, '%P'))
        gain_lab.grid(column=1, row=5, sticky='ew')
        gain_input.grid(column=2, row=5, sticky='ew')

        self.delay_time_var = tk.IntVar(self)
        self.delay_time_var.set(int(self.delay*1000))
        delay_time_lab = tk.Label(self, text="Display Speed:")
        delay_time_input = tk.Entry(self,
            textvariable=self.delay_time_var,
            validate='all',
            validatecommand=(self.main.vcmd_int, '%P'))
        delay_time_lab.grid(column=1, row=6, sticky='ew')
        delay_time_input.grid(column=2, row=6, sticky='ew')

        self.pos_label = tk.Label(self, text="Frequency = {}Hz, Speed = {}cm/s".format(0,0))
        self.pos_label.grid(column=0, row=7)

        #creates the animation object
        self.anim = anim.FuncAnimation(self.fig,
            self.update,
            interval=1,
            blit=True,
            save_count=self.n_lines)
        self.paused = True

    def mouse_move(self, event):
        '''
        Updates pos_label with the position of the mouse

        Parameters
        ----------
        event:
            The mouse movement event
        '''
        if event.inaxes:
            index = math.floor(event.ydata)+1
            freq = self.fft_freqs[-index]
            temp_freq = self.trans_freq_var.get()*1000
            speed = round(SPEED_OF_SOUND*freq/(2*temp_freq), 1)
            freq = round(freq, 1)
            self.pos_label['text'] ="Frequency = {}Hz, Speed = {}cm/s".format(freq,speed)
    
    def calc_max(self, *args):
        '''
        Updates max_speed_lab with the maximum speed possible to show without aliasing

        Parameters
        ----------
        *args:
            needed due to the trace of tkinter variables, unused
        '''
        try:
            temp_freq = self.trans_freq_var.get()*1000
            prf = self.PRF_var.get()
            if temp_freq!=0 and prf!=0:
                max_speed = np.round(SPEED_OF_SOUND*prf/(4*temp_freq), 1)
                self.max_speed_lab['text'] = "(max " + str(max_speed) + "cm/s)"
        except TclError:
            self.max_speed_lab['text'] = "(max 0.0cm/s)"

    def update(self, i):
        '''
        Updates heatmap and current_frame_array, called by anim

        Parameters
        ----------
        i: int
            The number of the line to be updated
        '''
        #stops unnecessary animation
        if len(self.waves) == 0:
            self.anim.pause()

        else:
            #keeps time so display is real time (ish)
            time_diff = (time.time()-self.time)+self.delay
            if time_diff < self.line_period:
                time.sleep(self.line_period-time_diff)
            self.time = time.time()

            #updated current_frame_array and resynchronises display and audio
            if i%self.n_lines == 0:
                if i != 0:
                    time_diff = (time.time()-self.start_time)
                    if time_diff < self.show_time:
                        time.sleep(self.show_time-time_diff)
                    else:
                        self.time += self.show_time-time_diff
                    self.start_time = time.time()
                    self.next_thread.join()
                    self.current_frame_array = np.copy(self.next_frame_array)
                    self.next_thread = threading.Thread(target = self.get_next)
                    self.next_thread.start()
                elif self.prev_i == 0:
                    self.start_time = time.time()
                    self.next_thread.join()
                    self.current_frame_array = np.copy(self.next_frame_array)
                    self.next_thread = threading.Thread(target = self.get_next)
                    self.next_thread.start()
                self.prev_i = i
            
            #updates heatmap
            self.heatmap_array[:, int(i%self.n_lines)] = self.current_frame_array[:, int(i%self.n_lines)]
            self.heatmap_array[:, int((i+1)%self.n_lines)] = self.zeros
            self.heatmap.set_array(self.heatmap_array)
        return (self.heatmap,)

    def get_next(self):
        '''
        Calculates the next frame, called in next_thread

        For each line in the next frame times are generated based on the line period and the 
        pulse repetition frequency. The signal at each time is calculated and
        fourier transformed to find the relevant doppler signal.
        '''
        if len(self.waves) > 0: #prevents unnecessary calculations
            times0 = np.arange(0, self.line_period, 1/self.PRF)
            for i in range(self.n_lines):
                times = times0+(i+self.start_line)*self.line_period
                sigs = np.zeros(self.fft_len)
                amps = 0
                for wave in self.waves:
                    sig, amp = wave.get_signal(times)
                    sigs = sigs+sig
                    amps = amps+amp
                if amps != 0:
                    sigs = sigs/amps
                line = np.abs(np.fft.fftshift(np.fft.fft(sigs)))*2*self.gain/self.fft_len
                self.next_frame_array[:, i] = line*self.freq_mask
            self.start_line += self.n_lines

    def toggle_pause(self, waves):
        '''
        plays/pauses the plotting of the spectrum

        Takes the values the user has entered and updates the spectrum in real time according
        to the entered values.
        Pauses the spectrum if already playing

        Parameter
        ---------
        waves: list[SweepWave]
            A list of SweepWave objects
        '''
        if self.paused:
            #Shares a lot of code functionality with the __init__ function
            trans_freq = self.trans_freq_var.get()*1000
            wall_filt = self.wall_filt_var.get()
            self.show_time = self.show_time_var.get()
            self.PRF = self.PRF_var.get()
            self.n_lines = self.n_lines_var.get()
            self.line_period = self.show_time/self.n_lines
            self.waves = waves
            self.time = time.time()
            self.start_time = time.time()
            self.gain = self.gain_var.get()
            self.delay = self.delay_time_var.get()/1000
            self.prev_i = 1
 
            self.fft_len = round(self.line_period*self.PRF)
            self.fft_freqs = np.fft.fftshift(np.fft.fftfreq(self.fft_len)*self.PRF)
            self.freq_mask = np.abs(self.fft_freqs)>=wall_filt

            self.heatmap_array = np.zeros((self.fft_len, self.n_lines))
            self.next_frame_array = np.zeros((self.fft_len, self.n_lines))
            self.current_frame_array = np.zeros((self.fft_len, self.n_lines))
            self.zeros = np.zeros(self.fft_len)
            self.start_line = 0

            self.next_thread.join()
            self.next_thread = threading.Thread(target = self.get_next)
            self.next_thread.start()
            
            #clears and updates the axes
            self.ax.clear()
            self.heatmap = self.ax.imshow(self.heatmap_array,
                vmax = 1,
                vmin = 0,
                cmap='gray',
                aspect='auto')

            self.ax.set_xticks(np.linspace(0, self.n_lines-1, 10))
            ticks = ['' for _ in range(10)]
            ticks[-1] = str(self.show_time)+'s'
            self.ax.set_xticklabels(ticks)

            self.ax.yaxis.set_ticks_position("right")
            self.ax.set_yticks(np.linspace(0, self.fft_len-1, 7))
            yticks = np.linspace(-np.min(self.fft_freqs), np.min(self.fft_freqs), 7)
            yticks = np.round(SPEED_OF_SOUND*yticks/(2*trans_freq), 1)
            yticks = [str(tick) for tick in yticks]
            yticks[2] = yticks[2]+'cm/s'
            self.ax.set_yticklabels(yticks)

            #updates the canvas in tkinter
            self.canvas.get_tk_widget().grid_forget()
            self.canvas.get_tk_widget().grid(column=0, row=0, rowspan=7, sticky='nsew')

            self.anim = anim.FuncAnimation(self.fig,
                self.update,
                interval=1,
                blit=True,
                save_count=self.n_lines)
        else:
            self.anim.pause()
            
        self.paused = not self.paused