#!/usr/bin/env python3
from abc import ABC
# from machinevisiontoolbox.Camera import P
import numpy as np
import matplotlib.pyplot as plt
from machinevisiontoolbox.base import mkgrid
from machinevisiontoolbox import CentralCamera
import spatialmath.base as smbase
from spatialmath import SE3

#VisualServo  Abstract class for visual servoing
#
# VisualServo(CAMERA, OPTIONS) 

# A concrete class for simulation of image-based visual servoing (IBVS), a subclass of
# VisualServo.  Two windows are shown and animated:
#   - The camera view, showing the desired view (*) and the 
#     current view (o)
#   - The external view, showing the target points and the camera
#
# Methods::
# run            Run the simulation, complete results kept in the object
# step           One simulation step (provided by the concrete class)
# init           Initialized the simulation (provided by the concrete class)
# plot_p         Plot feature values vs time
# plot_vel       Plot camera velocity vs time
# plot    Plot camera pose vs time
# plot_jcond     Plot Jacobian condition vs time 
# plot_z         Plot point depth vs time
# plot_error     Plot feature error vs time
# plot_all       Plot all of the above in separate figures
# char           Convert object to a concise string
# display        Display the object as a string
#
# Properties::
# history     A vector of structs holding simulation results
#
# Notes::
# - Must be subclassed.
#
# See also PBVS, IBVS, IBVS_l, IBVS_e.

class VisualServo(ABC):

    class _history:
        pass

    def __init__(self, camera, niter=100, fps=5, graphics=True, pose_b=None, pose_0=None, pose_f=None, P=None, targetsize=0.5, p_f=None, title=None, plotvol=None, movie=None, type=None, verbose=False):
        #VisualServo.VisualServo Create IBVS object
        #
        # VS = VisualServo(camera, options) creates an image-based visual servo
        # simulation object.
        #
        # Options::
        # 'niter',N         Maximum number of iterations
        # 'fps',F           Number of simulation frames per second (default t)
        # 'Tf',T            The final pose
        # 'T0',T            The initial pose
        # 'P',p             The set of world points (3xN)
        # 'targetsize',S    The target points are the corners of an SxS
        #                   square in the XY-plane at Z=0 (default S=0.5)
        # 'p_f',p         The desired image plane coordinates
        # 'verbose'         Print out extra information during simulation
        #
        # Notes::
        # - If 'P' is specified it overrides the default square target.
        print('VisualServo constructor')
        self.camera = camera
        self.history = []

        z = 3

        self.niter = niter

        self.graphics = graphics
        self.fps = fps
        self.verbose = verbose
        self.pose_f = pose_f
        self.pose_b = pose_b
        if pose_0 is not None:
            self.pose_0 = pose_0
        else:
            self.pose_0 = camera.pose

        self.P = P
        if P is not None:
            self.npoints = P.shape[1]
        if p_f is None:
            p_f = camera.project_point(P, pose=pose_f)
        self.p_star = p_f
        # self.ax = smbase.plotvol3(plotvol)
        self.movie = movie
        self.type = type
        if graphics:

            fig = plt.figure(figsize=plt.figaspect(0.5))
            self.fig = fig

            # First subplot
            ax = fig.add_subplot(1, 2, 1)
            self.camera._plotcreate(ax=ax)
            self.ax_camera = ax

            # Second subplot
            ax = fig.add_subplot(1, 2, 2, projection='3d')
            ax = smbase.plotvol3(plotvol, ax=ax)
            # smbase.plot_sphere(0.06, self.P, color='r', ax=ax)
            # self.camera.plot(self.pose, label=True, ax=ax)
            ax.view_init(16, 28)
            plt.grid(True)
            self.ax_3dview = ax

            self.camera_args = dict(shape='camera', color='b', scale=0.3, ax=self.ax_3dview)

            fig.patch.set_color('#f0f0f0')
            self.ax_3dview.set_facecolor('#f0f0f0')

            if title is not None:
                self.fig.canvas.manager.set_window_title(title)

    def init(self):

        if self.graphics:
            self.camera.clf()
            self.camera.plot_point(self.P, objpose=self.pose_b, markersize=8, markerfacecolor='none')    # show initial view

            if self.pose_b is not None:
                P = self.pose_b * self.P
            else:
                P = self.P
            smbase.plot_sphere(0.05, P, color='r', ax=self.ax_3dview)
            self.camera.plot(**{**self.camera_args, **dict(color='k')})

        if self.pose_0 is not None:
            self.camera.pose = self.pose_0

        # clear the history
        self.history = []

    def run(self, niter=None):
        #VisualServo.run  Run visual servo simulation
        #
        # self.run(N) run the simulation for N steps
        #
        # self.run[] as above but run it for the number of steps
        # specified in the constructor or Inf.
        #
        # Notes::
        # - Repeatedly calls the subclass step[] method which returns
        #   a flag to indicate if the simulation is complete.
        
        self.init()
        
        if self.movie is not None:
            self.anim = Animate(self.movie)
        
        if niter is None:
            niter = self.niter

        alpha_min = 0.1
        for step in range(niter):
            
            status = self.step()

            if self.graphics:
                if self.type == 'point':
                    self.plot_point(self.history[-1].p, markersize=4)

                self.clear_3dview()
                alpha = alpha_min + (1 - alpha_min) * step / niter
                self.camera.plot(alpha=alpha, **self.camera_args)

                if self.movie is not None:
                    self.anim.add()
                else:
                    plt.pause(1 / self.fps)
            
            if status > 0:
                print('completed on error tolerance')
                break
            elif status < 0:
                print('failed on error\n')
                break

        else:
            # exit on iteration limit
            print('completed on iteration count')
        
        if self.movie is not None:
            self.anim.close()

    def plot_p(self):
        #VisualServo.plot_p Plot feature trajectory
        #
        # self.plot_p[] plots point feature trajectories on the image plane.
        #
        # See also self.plot_vel, self.plot_error, self.plot,
        # self.plot_jcond, self.plot_z, self.plot_error, self.plot_all.
        
        if len(self.history) == 0:
            return

        if self.type != 'point':
            print('Can only plot image plane trajectories for point-based IBVS')
            return

        # result is a vector with row per time step, each row is u1, v1, u2, v2 ...
        for i in range(self.npoints):
            u = [h.p[0, i] for h in self.history]  # get data for i'th point
            v = [h.p[1, i] for h in self.history]
            plt.plot(u, v, 'b')
        
        # mark the initial target shape
        smbase.plot_poly(self.history[0].p, 'o--', close=True, markeredgecolor='k', markerfacecolor='w', label='initial')
        
        # mark the goal target shape
        if isinstance(self, IBVS):
            smbase.plot_poly(self.p_star, 'k*:', close=True, markeredgecolor='k', markerfacecolor='k', label='goal')

        # axis([0 self.camera.npix[0] 0 self.camera.npix[1]])
        # daspect([1 1 1])
        plt.grid(True)
        plt.xlabel('u (pixels)')
        plt.ylabel('v (pixels)')
        plt.xlim(0, self.camera.width)
        plt.ylim(0, self.camera.height)
        plt.legend()
        ax = plt.gca()
        ax.invert_yaxis()
        ax.set_aspect('equal')  
        ax.set_facecolor('lightyellow')
    

    def plot_vel(self):
        #VisualServo.plot_vel Plot camera trajectory
        #
        # self.plot_vel[] plots the camera velocity versus time.
        #
        # See also self.plot_p, self.plot_error, self.plot,
        # self.plot_jcond, self.plot_z, self.plot_error, self.plot_all.
        if len(self.history) == 0:
            return

        vel = np.array([h.vel for h in self.history])
        plt.plot(vel[:, :3], '-')
        plt.plot(vel[:, 3:], '--')
        plt.ylabel('Cartesian velocity')
        plt.grid(True)
        plt.xlabel('Time step')
        plt.xlim(0, len(self.history) - 1)
        plt.legend(['$v_x$', '$v_y$', '$v_z$', r'$\omega_x$', r'$\omega_y$', r'$\omega_z$'], loc='upper right')

    def plot_pose(self):
        #VisualServo.plot Plot camera trajectory
        #
        # self.plot[] plots the camera pose versus time.
        #
        # See also self.plot_p, self.plot_vel, self.plot_error,
        # self.plot_jcond, self.plot_z, self.plot_error, self.plot_all.

        if len(self.history) == 0:
            return

        # Cartesian camera position vs timestep
        T = SE3([h.pose for h in self.history])
        
        plt.subplot(211)
        plt.plot(T.t)
        plt.xlim(0, len(self.history) - 1)
        plt.ylabel('Camera position (m)')
        plt.legend(['x', 'y', 'z'])
        plt.grid(True)
        
        plt.subplot(212)
        plt.plot(T.rpy(order='camera'))
        plt.ylabel('Camera orientation (rad)')
        plt.grid(True)
        plt.xlabel('Time step')
        plt.xlim(0, len(self.history) - 1)
        plt.legend([r'$\alpha$', r'$\beta$', r'$\gamma$'])


    def plot_jcond(self):
        #VisualServo.plot_jcond Plot image Jacobian condition
        #
        # self.plot_jcond[] plots image Jacobian condition versus time.
        # Indicates whether the point configuration is close to
        # singular.
        #
        # See also self.plot_p, self.plot_vel, self.plot_error, self.plot,
        # self.plot_z, self.plot_error, self.plot_all.  
        
        if len(self.history) == 0:
            return
        
        Jcond = [h.jcond for h in self.history]
        # Image Jacobian condition number vs time
        plt.plot(Jcond)
        plt.grid(True)
        plt.ylabel('Jacobian condition number')
        plt.xlabel('Time step')
        plt.xlim(0, len(self.history) - 1)

    def plot_z(self):
        #VisualServo.plot_z Plot feature depth
        #
        # self.plot_z[] plots feature depth versus time.  If a depth estimator is
        # used it shows true and estimated depth.
        #
        # See also self.plot_p, self.plot_vel, self.plot_error, self.plot,
        # self.plot_jcond, self.plot_error, self.plot_all.
        if len(self.history) == 0:
            return
            
        if self.type != 'point':
            print('Z-estimator data only computed for point-based IBVS')
            return

        Z_est = np.array([h.Z_est for h in self.history])
        Z_true = np.array([h.Z_true for h in self.history])
        plt.plot(Z_true, '-', label='true')
        plt.plot(Z_est, '--', label='estimate')
        plt.grid()
        plt.ylabel('Depth (m)')
        plt.xlabel('Time step')
        plt.xlim(0, len(self.history) - 1)
        plt.legend()

    def plot_error(self):
        #VisualServo.plot_error Plot feature error
        #
        # self.plot_error[] plots feature error versus time.
        #
        # See also self.plot_vel, self.plot_error, self.plot,
        # self.plot_jcond, self.plot_z, self.plot_all.
        
        if len(self.history) == 0:
            return
        
        e = [h.e for h in self.history]
        if self.type == 'point':
            plt.plot(e[:,1:2:end], 'r')
            plt.plot(e[:,2:2:end], 'b')
            plt.ylabel('Feature error (pixel)')
            
            plt.legend('u', 'v')
        else:
            plot(e)
            plt.ylabel('Feature error')

        plt.grid(True)
        plt.xlabel('Time')
        plt.xaxis(length(self.history))

        return e

    def plot_all(self):
        #VisualServo.plot_all Plot all trajectory
        #
        # self.plot_all[] plots in separate figures feature values, velocity, 
        # error and camera pose versus time.
        #
        # self.plot_all(DEV, NAME) writes each plot to a separate file.
        # The name is an SPRINTF format specifier with a #s field that
        # is replaced with a unique per plot suffix.  DEV is the device name
        # passed to the MATLAB print function
        #
        # Example::
        #         self.plot_all('-depsc', 'eg1#s.eps')
        #
        # See also self.plot_vel, self.plot_error, self.plot,
        # self.plot_error.

        plt.figure()
        self.plot_p()

        plt.figure()
        self.plot_vel()

        plt.figure()
        self.plotpose()

        plt.figure()
        self.plot_error()

        # optional plots depending on what history was recorded
        if hasattr(history[0], 'Z_est'):
            plt.figure()
            self.plot_z()
        
        if hasattr(self.history[0], 'jcond'):
            plt.figure()
            self.plot_jcond()

    def __str__(self):
        #VisualServo.char Convert to string
        #
        # s = self.char[] is a string showing VisualServo parameters in a compact single line format.
        #
        # See also VisualServo.display.

        s = f"Visual servo object: camera={self.camera.name}\n  {self.niter} iterations, {len(self.history)} history'"

        s += np.array2string(self.P, prefix='P = ')
        # s = strvcat(s, sprintf('  T0:'))
        # s = strvcat(s, [repmat('      ', 4,1) num2str(self.T0)])
        # s = strvcat(s, sprintf('  C*_T_G:'))
        # s = strvcat(s, [repmat('      ', 4,1) num2str(self.Tf)])
        if self.pose_0 is not None:
            s +=  pose_0.printline(label='𝜉_C', orient='camera')
        if self.pose_f is not None:
            s +=  pose_0.printline(label='𝜉_C*_G', orient='camera')

    def __repr__(self):
        return str(self)

    def plot_point(self, *args, **kwargs):
        return self.camera.plot_point(*args, **kwargs)

    def plot(self, *args, **kwargs):
        return self.camera.plot(*args, ax=self.ax_3dview, **kwargs)

    def clear_3dview(self):
        for child in self.ax_3dview.get_children(): # ax.lines:
            if __class__.__name__ == 'Line3DCollection':
                child.remove()


#PBVS   Implement classical PBVS for point features
#
# A concrete class for simulation of position-based visual servoing (PBVS), a subclass of
# VisualServo.  Two windows are shown and animated:
#   - The camera view, showing the desired view (*) and the 
#     current view (o)
#   - The external view, showing the target points and the camera
#
# Methods::
# run            Run the simulation, complete results kept in the object
# plot_p         Plot image plane coordinates of points vs time
# plot_vel       Plot camera velocity vs time
# plot    Plot camera pose vs time
# plot_z         Plot point depth vs time
# plot_error     Plot feature error vs time
# plot_all       Plot all of the above in separate figures
# char           Convert object to a concise string
# display        Display the object as a string
#
# Example::
#         cam = CentralCamera('default');
#         Tc0 = transl(1,1,-3)*trotz(0.6);
#         TcStar_t = transl(0, 0, 1);
#         pbvs = PBVS(cam, 'T0', Tc0, 'Tf', TcStar_t);
#         pbself.plot_p
#
# References::
# - Robotics, Vision & Control, Chap 15
#   P. Corke, Springer 2011.
#
# Notes::
# - The history property is a vector of structures each of which is a snapshot at
#   each simulation step of information about the image plane, camera pose, error, 
#   Jacobian condition number, error norm, image plane size and desired feature 
#   locations.
#
# See also VisualServo, IBVS, IBVS_l, IBVS_e.

# IMPLEMENTATION NOTE
#
# 1.  The gain, lambda, is always positive



class PBVS(VisualServo):

    def __init__(self, camera, targetsize=0.5, eterm=0, lmbda=0.05, **kwargs):
        #PBself.PBVS Create PBVS visual servo object
        #
        # PB = PBVS(camera, options)
        #
        # Options::
        # 'niter',N         Maximum number of iterations
        # 'eterm',E         Terminate when norm of feature error < E
        # 'lambda',L        Control gain, positive definite scalar or matrix
        # 'T0',T            The initial pose
        # 'Tf',T            The final relative pose
        # 'P',p             The set of world points (3xN)
        # 'targetsize',S    The target points are the corners of an SxS square
        # 'fps',F           Number of simulation frames per second (default t)
        # 'verbose'         Print out extra information during simulation
        # 'axis'            Axis dimensions
        #
        # Notes::
        # - If 'P' is specified it overrides the default square target.
        #
        # See also VisualServo.
        
        # invoke superclass constructor
        super().__init__(camera, type='point', title='PBVS simulation', **kwargs)


        self.targetsize = targetsize
        self.eterm = eterm
        self.lmbda = lmbda

        if self.pose_f is None:
            self.pose_f = SE3(0, 0, 1)
            print('setting Tf to default')

    def init(self):
        #PBself.init Initialize simulation
        #
        # PB.init() initializes the simulation.  Implicitly called by
        # PB.run().
        #
        # See also VisualServo, PBself.run.
        
        # initialize the vservo variables
        #self.camera.clf();

        super().init()
        
        # show the reference location, this is the view we wish to achieve
        # when Tc = T_final
        p_star = self.camera.project_point(self.P, pose=self.pose_f.inv())    # create the camera view

        #hold on
        #plot(p_star(:,1), p_star(:,2), '*');      # show desired view
        #hold off

        #camup([0,-1,0]);


    def step(self):
        #PBself.step Simulate one time step
        #
        # STAT = PB.step() performs one simulation time step of PBself.  It is
        # called implicitly from the superclass run method.  STAT is
        # one if the termination condition is met, else zero.
        
        status = 0;

        # compute the current view
        uv = self.camera.project_point(self.P, objpose=self.pose_b)

        # estimate pose of goal wrt camera
        Te_C_G = self.camera.estpose(self.P, uv, worldframe=False)

        # estimate motion to desired relative pose
        T_delta =  Te_C_G * self.pose_f.inv()
        
        # update the camera pose
        Td = T_delta.interp1(self.lmbda)

        self.camera.pose @= Td      # apply it to current pose

        # update the history variables
        hist = self._history()
        hist.p = uv
        vel = Td.delta()
        hist.vel = vel
        hist.pose = self.camera.pose

        self.history.append(hist)
        
        if np.linalg.norm(vel) < self.eterm:
            status = 1

        return status


#IBVS   Implement classical IBVS for point features
#

#

#
# Example::
#         cam = CentralCamera('default')
#         Tc = trnorm( Tc * delta2tr(v) )
#         Tc0 = transl(1,1,-3)*trotz(0.6)
#         p_f = bsxfun(@plus, 200*[-1 -1 1 1 -1 1 1 -1], cam.pp')
#         ibvs = IBVS(cam, 'T0', Tc0, 'p_f', p_f)
#         self.run[]
#         self.plot_p[]
#
# References::
# - Robotics, Vision & Control, Chap 15
#   P. Corke, Springer 2011.
#
# Notes::
# - The history property is a vector of structures each of which is a snapshot at
#   each simulation step of information about the image plane, camera pose, error, 
#   Jacobian condition number, error norm, image plane size and desired feature 
#   locations.
#
# See also VisualServo, PBVS, IBVS_l, IBVS_e.

# IMPLEMENTATION NOTE
#
# 1.  As per task function notation (Chaumette papers) the error is
#     defined as actual-demand, the reverse of normal control system
#     notation.
# 2.  The gain, lambda, is always positive
# 3.  The negative sign is written into the control law



class IBVS(VisualServo):

    def __init__(self, camera, eterm=0.5, lmbda=0.08, depth=None, depthest=False, **kwargs):
        #self.IBVS Create IBVS visual servo object
        #
        # IB = IBVS(camera, options)
        #
        # Options::
        # 'niter',N         Maximum number of iterations
        # 'eterm',E         Terminate when norm of feature error < E
        # 'lambda',L        Control gain, positive definite scalar or matrix
        # 'T0',T            The initial pose
        # 'P',p             The set of world points (3xN)
        # 'targetsize',S    The target points are the corners of an SxS square
        # 'p_f',p         The desired image plane coordinates
        # 'depth',D         Assumed depth of points is D (default true depth
        #                   from simulation is assumed)
        # 'depthest'        Run a simple depth estimator
        # 'fps',F           Number of simulation frames per second (default t)
        # 'verbose'         Print out extra information during simulation
        #
        # Notes::
        # - If 'P' is specified it overrides the default square target.
        #
        # See also VisualServo.

        # invoke superclass constructor
        super().__init__(camera, type='point', title='IBVS simulation', **kwargs)



        self.lmbda = lmbda
        self.eterm = eterm
        self.theta = 0
        self.smoothing = 0.80
        self.depth = depth
        self.depthest = depthest
        
    @classmethod
    def Example(cls):
        # run a canned example
        # fprintf('---------------------------------------------------\n')
        # fprintf('canned example, image-based IBVS with 4 points\n')
        # fprintf('---------------------------------------------------\n')
        # self.P = mkgrid(2, 0.5, 'pose', SE3[-1,-1,2])
        # self.pf = bsxfun(@plus, 200*[-1 -1 1 1 -1 1 1 -1], cam.pp')
        # self.T0 = SE3(1,1,-3)*SE3.Rz(0.6)
        # self.lambda = opt.lambda
        # self.eterm = 0.5
        pass

    def init(self):
        #self.init Initialize simulation
        #
        # IB.init[] initializes the simulation.  Implicitly called by
        # IB.run[].
        #
        # See also VisualServo, self.run.

        # if self.p_star is None:
        #     # final pose is specified in terms of image coords
        #     self.p_star = self.pf
        # else:
        #     if self.pose_f is None:
        #         self.pose_f = SE3(0, 0, 1)
        #         print('setting Tf to default')

        #     # final pose is specified in terms of a camera-target pose
        #     #   convert to image coords


        # initialize the vservo variables
        super().init()

        # show the reference location, this is the view we wish to achieve
        # when Tc = Tct_star

        self.vel_prev = None
        self.uv_prev = None


    def step(self):
        #self.step Simulate one time step
        #
        # STAT = IB.step[] performs one simulation time step of self.  It is
        # called implicitly from the superclass run method.  STAT is
        # one if the termination condition is met, else zero.
        #
        # See also VisualServo, self.run.
        
        status = 0
        Z_est = None
        
        uv = self.camera.project_point(self.P)

        hist = self._history()

        # optionally estimate depth
        if self.depthest:
            # run the depth estimator
            Z_est, Z_true = self.depth_estimator(uv)
            if self.verbose:
                print(f"Z: est={Z_est}, true={Z_true}")
            self.depth = Z_est
            if Z_est is None:
                hist.Z_est = np.zeros((self.P.shape[1],))
            else:
                hist.Z_est = Z_est.ravel()
            if Z_true is None:
                hist.Z_true = Z_true
            else:
                hist.Z_true = Z_true.ravel()

        # compute the Jacobian
        if self.depth is None:
            # exact depth from simulation (not possible in practice)
            pt = self.camera.pose.inv() * self.P
            J = self.camera.visjac_p(uv, pt[2, :])
        elif Z_est is not None:
            # use the estimated depth
            J = self.camera.visjac_p(uv, Z_est)
        else:
            # use the default depth
            J = self.camera.visjac_p(uv, self.depth)

        # compute image plane error as a column
        e = uv - self.p_star  # feature error
        e = e.ravel('F')  # convert columnwise to a 1D vector 

        # compute the velocity of camera in camera frame
        try:
            v = -self.lmbda * np.linalg.pinv(J) @ e
        except np.linalg.LinAlgError:
            return -1

        if self.verbose:
            print(v)

        # update the camera pose
        Td = SE3.Delta(v) # differential motion
        # Td = SE3(trnorm(delta2tr(v)))    
        #Td = expm( skewa(v) )
        #Td = SE3( delta2tr(v) )
        self.camera.pose @= Td       # apply it to current pose

        # update the history variables
        hist.p = uv
        vel = Td.delta()
        hist.vel = vel
        hist.e = e
        hist.enorm = np.linalg.norm(e)
        hist.jcond = np.linalg.cond(J)
        hist.pose = self.camera.pose

        self.history.append(hist)

        #TODO not really needed, its in the history
        self.vel_prev = vel
        self.uv_prev = uv

        if np.linalg.norm(e) < self.eterm:
            status = 1

        return status

    def depth_estimator(self, uv):
        #self.depth_estimator Estimate point depth
        #
        # [ZE,ZT] = IB.depth_estimator(UV) are the estimated and true world 
        # point depth based on current feature coordinates UV (2xN).
        
        if self.uv_prev is None:
            Z_est = None

        else:
            # compute Jacobian for unit depth, z=1
            J = self.camera.visjac_p(uv, 1)
            Jv = J[:, :3]  # velocity part, depends on 1/z
            Jw = J[:, 3:]  # rotational part, indepedent of 1/z

            # estimate image plane velocity
            uv_d =  uv.ravel('F') - self.uv_prev.ravel('F')
            
            # estimate coefficients for A (1/z) = b
            b = uv_d - Jw @ self.vel_prev[3:]
            A = Jv @ self.vel_prev[:3]

            AA = np.zeros((A.shape[0], A.shape[0]//2))
            for i in range(A.shape[0]//2):
                AA[2*i:(i+1)*2, i] = A[2*i:(i+1)*2]

            eta, resid, *_ = np.linalg.lstsq(AA, b.ravel(), rcond=None)         # least squares solution
            # eta2 = A(1:2) \ B(1:2)

            # first order smoothing
            self.theta = (1 - self.smoothing) * 1 / eta + self.smoothing * self.theta
            Z_est = self.theta

        # true depth
        P_CT = self.camera.pose.inv() * self.P
        Z_true = P_CT[2, :]

        if self.verbose:
            print('depth', Z_true)
            print('est depth', Z_est)

        return Z_est, Z_true



#IBVS   Implement classical IBVS for point features
#
# A concrete class for simulation of image-based visual servoing (IBVS), a subclass of
# VisualServo.  Two windows are shown and animated:
#   - The camera view, showing the desired view (*) and the 
#     current view (o)
#   - The external view, showing the target points and the camera
#
# Methods::
# run            Run the simulation, complete results kept in the object
# plot_p         Plot image plane coordinates of points vs time
# plot_vel       Plot camera velocity vs time
# plot    Plot camera pose vs time
# plot_jcond     Plot Jacobian condition vs time 
# plot_z         Plot point depth vs time
# plot_error     Plot feature error vs time
# plot_all       Plot all of the above in separate figures
# char           Convert object to a concise string
# display        Display the object as a string
#
# Example::
#         cam = CentralCamera('default')    
#         ibvs = IBVS_l(cam, 'example') 
#         self.run[]
#
# References::
# - Robotics, Vision & Control, Chap 15
#   P. Corke, Springer 2011.
#
# Notes::
# - The history property is a vector of structures each of which is a snapshot at
#   each simulation step of information about the image plane, camera pose, error, 
#   Jacobian condition number, error norm, image plane size and desired feature 
#   locations.
# - Lines are constructed by joining consecutive point features.
#
# See also VisualServo, PBVS, IBVS_l, IBVS_e.
# IMPLEMENTATION NOTE
#
# 1.  As per task function notation (Chaumette papers) the error is
#     defined as actual-demand, the reverse of normal control system
#     notation.
# 2.  The gain, lambda, is always positive
# 3.  The negative sign is written into the control law

class IBVS_l(VisualServo):

    def __init__(self, camera, eterm=0.01, plane=None, lmbda=0.08, **kwargs):
        #IBVS_l.IBVS_l Create IBVS line visual servo object
        #
        # IB = IBVS_l(camera, options)
        #
        # Options::
        # 'example'         Use set of canned parameters
        # 'niter',N         Maximum number of iterations
        # 'eterm',E         Terminate when norm of feature error < E
        # 'lambda',L        Control gain, positive definite scalar or matrix
        # 'T0',T            The initial pose
        # 'Tf',T            The final camera pose used only to determine desired
        #                   image plane coordinates (default 1m in z-direction)
        # 'P',p             The set of world points (3xN)
        # 'planes',P        The world planes holding the lines (4xN)
        # 'fps',F           Number of simulation frames per second (default t)
        # 'verbose'         Print out extra information during simulation
        #
        # Notes::
        # - If 'P' is specified the lines join points 1-2, 2-3, N-1.
        #
        # See also VisualServo.

        # invoke superclass constructor
        super().__init__(camera, type='line', **kwargs)
        
        self.eterm = eterm
        self.plane = plane
        self.lmbda = lmbda
                
    @classmethod
    def Example(cls, camera):
        # setup for a canned example
        print('Canned example: line-based IBVS with three lines')
        if camera is None:
            camera = CentralCamera.Default(name='')
        self = cls(camera)
        # self.planes = np.tile([0, 0, 1, -3], (3, 1)).T
        self.plane = [0, 0, 1, -3]
        self.P = smbase.circle([0, 0, 3], 1, resolution=3)
        self.pose_0 = SE3(1, 1, -3) * SE3.Rz(0.6)
        self.pose_f = SE3(0, 0, 1)
        return self

    def init(self, pose_f=None):
        #IBVS_l.init Initialize simulation
        #
        # IB.init[] initializes the simulation.  Implicitly called by
        # IB.run[].
        #
        # See also VisualServo, IBVS_l.run.
        super().init()

        # final pose is specified in terms of a camera-target pose
        self.f_star_retinal = self.getlines(self.pose_f, np.linalg.inv(self.camera.K)) # in retinal coordinates
        self.f_star = self.getlines(self.pose_f) # in image coordinates

    def getlines(self, pose, scale=None):
        # one line per column
        #  row 1 theta
        #  row 2 rho
        # project corner points to image plane
        p = self.camera.project_point(self.P, pose=pose)

        if scale is not None:
            p = smbase.homtrans(scale, p)

        # compute lines and their slope and intercept

        lines = []
        for i in range(p.shape[1]):
            j = (i + 1) % p.shape[1]
            theta = np.arctan2(p[0, j] - p[0, i], p[1, i] - p[1, j])
            rho = np.cos(theta) * p[0, i] + np.sin(theta) * p[1, i]
            lines.append((theta, rho))
        return np.array(lines).T

    def step(self):
        #IBVS_l.step Simulate one time step
        #
        # STAT = IB.step[] performs one simulation time step of self.  It is
        # called implicitly from the superclass run method.  STAT is
        # one if the termination condition is met, else zero.
        #
        # See also VisualServo, IBVS_l.run.
        status = 0
        Z_est = []
        
        # compute the lines
        f = self.getlines(self.pose)

        # now plot them
        if self.graphics:
            #self.camera.clf()
            colors = 'rgb'
            for i in range(f.shape[1]):
                # plot current line
                self.plot_line_tr(self.camera, f[:, i], color=colors[i])
                # plot demanded line
                self.plot_line_tr(self.camera, self.f_star[:, i], color=colors[i], linestyle='--')

        f_retinal = self.getlines(self.pose, np.linalg.inv(self.camera.K))

        # compute image plane error as a column
        e = f_retinal - self.f_star_retinal   # feature error on retinal plane
        e = e.ravel('F')
        for i in range(0, len(e), 2):
            e[i] = smbase.angdiff(e[i])
    
        J = self.camera.visjac_l(f_retinal, self.plane)

        # compute the velocity of camera in camera frame
        v = -self.lmbda * np.linalg.pinv(J) @ e
        if self.verbose:
            print('v:', v)

        # update the camera pose
        Td = SE3.Delta(v)    # differential motion

        self.pose = self.pose @ Td       # apply it to current pose

        # update the external view camera pose
        self.camera.pose = self.pose

        # update the history variables
        hist = self._history()
        hist.f = f.ravel()
        hist.vel = v
        hist.e = e
        hist.enorm = np.linalg.norm(e)
        hist.jcond = np.linalg.cond(J)
        hist.pose = self.pose

        self.history.append(hist)
        if np.linalg.norm(e) < self.eterm:
            status = 1

        return status

    @staticmethod
    def plot_line_tr(camera, lines, **kwargs):
    # %CentralCamera.plot_line_tr  Plot line in theta-rho format
    # %
    # % CentralCamera.plot_line_tr(L) plots lines on the camera's image plane that
    # % are described by columns of L with rows theta and rho respectively.
    # %
    # % See also Hough.

        ax = camera._ax
        x = np.r_[ax.get_xlim()]
        y = np.r_[ax.get_ylim()]

        lines = smbase.getmatrix(lines, (2, None))
        # plot it
        for theta, rho in lines.T:
            #print(f'{theta=}, {rho=}')
            if np.abs(np.cos(theta)) > 0.5:
                # horizontalish lines
                ax.plot(x, -x * np.tan(theta) + rho / np.cos(theta), **kwargs)
            else:
                # verticalish lines
                ax.plot(-y / np.tan(theta) + rho / np.sin(theta), y, **kwargs)


#IBVS_e   Implement classical IBVS for ellipse features
#
# A concrete class for simulation of image-based visual servoing (IBVS) with 
# ellipse features, a subclass of VisualServo.  Two windows are shown and
# animated:
#   - The camera view, showing the desired view and the 
#     current view
#   - The external view, showing the target points and the camera
#
#
# Example::
#         cam = CentralCamera('default')    
#         ibvs = IBVS_e(cam, 'example') 
#         self.run[]
#
# You can change various properties of the ibvs object (initial/final pose,
# error tolerance etc. and rerun the simulation using the run[] method.
#
# References::
# - Robotics, Vision & Control, Chap 15
#   P. Corke, Springer 2011.
#
# Notes::
# - The history property is a vector of structures each of which is a snapshot at
#   each simulation step of information about the image plane, camera pose, error, 
#   Jacobian condition number, error norm, image plane size and desired feature 
#   locations.
# - We approximate the ellipse by a number of points on a circle in the
# world and fit an ellipse to the projection of the points.
#
# See also VisualServo, PBVS, IBVS_l, IBVS_e.

# IMPLEMENTATION NOTE
#
# 1.  As per task function notation (Chaumette papers) the error is
#     defined as actual-demand, the reverse of normal control system
#     notation.
# 2.  The gain, lambda, is always positive
# 3.  The negative sign is written into the control law

class IBVS_e(VisualServo):

    def __init__(self, camera, eterm=0.08, plane=None, lmbda=0.04, **kwargs):
        #IBVS_e.IBVS_e Create IBVS visual servo object
        #
        # IB = IBVS_e(camera, options)
        #
        # Options::
        # 'example'         Use set of canned parameters
        # 'niter',N         Maximum number of iterations
        # 'eterm',E         Terminate when norm of feature error < E
        # 'lambda',L        Control gain, positive definite scalar or matrix
        # 'T0',T            The initial camera pose
        # 'Tf',T            The final camera pose used only to determine desired
        #                   image plane coordinates (default 1m in z-direction)
        # 'P',p             The set of world points (3xN)
        # 'plane',P         The world plane holding the ellipse (4x1)
        # 'fps',F           Number of simulation frames per second (default t)
        # 'verbose'         Print out extra information during simulation
        #
        # Notes::
        # - If 'P' is specified it should define a set of points lying
        #   on a 3D world plane.
        #
        # See also VisualServo.
        
        # invoke superclass constructor
        print('IBVS_e constructor')
        super().__init__(camera, type='point', **kwargs)

        self.eterm = eterm
        self.plane = plane
        self.lmbda = lmbda        

    @classmethod
    def Example(cls, camera=None, **kwargs):
        # run a canned example
        print('canned example, ellipse + point-based IBVS')
        if camera is None:
            camera = CentralCamera.Default(name='')
        self = cls(camera, **kwargs)
        self.P = smbase.circle(radius=0.5, centre=[0, 0, 3], resolution=10)
        self.pose_f = SE3(0.5, 0.5, 1)
        self.pose_0 = SE3(0.5, 0.5, 0) * SE3.Rx(0.3)
        #self.T0 = transl(-1,-0.1,-3)#*trotx(0.2)
        self.plane = [0, 0, 1, -3]    # in plane z=3
        return self

    def init(self):
        #IBVS_e.init Initialize simulation
        #
        # IB.init[] initializes the simulation.  Implicitly called by
        # IB.run[].
        #
        # See also VisualServo, IBVS_e.run.

        # desired feature coordinates.  This vector comprises the ellipse
        # parameters (5) and the coordinaes of 1 point
        super().init()

        self.f_star = np.r_[
                self.get_ellipse_parameters(self.pose_f),
                self.camera.project_point(self.P[:, 0], pose=self.pose_f).ravel()
            ]
        
        self.ellipse_star = self.camera.project_point(self.P, pose=self.pose_f)
        # self.ellipse_star = self.camera.project([self.P self.P(:,1)], pose=self.pose_f)


    def get_ellipse_parameters(self, pose):
        p = self.camera.project_point(self.P, pose=pose) #, retinal=True)

        # # convert to normalized image-plane coordinates
        p = smbase.homtrans(np.linalg.inv(self.camera.K), p)
        x, y = p

        # solve for the ellipse parameters
        # x^2 + A1 y^2 - 2 A2 xy + 2 A3 x + 2 A4 y + A5 = 0
        A = np.column_stack([y**2, -2*x*y, 2*x, 2*y, np.ones(x.shape)])
        b = -(x**2)
        theta, resid, *_ = np.linalg.lstsq(A, b, rcond=None)         # least squares solution
        return theta

    def step(self):
        #IBVS_e.step Simulate one time step
        #
        # STAT = IB.step[] performs one simulation time step of self.  It is
        # called implicitly from the superclass run method.  STAT is
        # one if the termination condition is met, else zero.
        #
        # See also VisualServo, IBVS_e.run.
        
        status = 0
        Z_est = []

        # compute feature vector
        f = np.r_[
                self.get_ellipse_parameters(self.pose),
                self.camera.project_point(self.P[:, 0], pose=self.pose).ravel()
            ]
        
        # compute image plane error as a column
        e = f - self.f_star   # feature error
        
        # compute the Jacobians and stack them
        Je = self.camera.visjac_e(f[:5], self.plane)  # ellipse
        Jp = self.camera.visjac_p(f[5:], -self.plane[3]) # point
        J = np.vstack([Je, Jp])

        # compute the velocity of camera in camera frame
        v = -self.lmbda * np.linalg.pinv(J) @ e

        # update the camera pose
        self.pose @= SE3.Delta(v)

        if self.verbose:
            print(f"{cond=}, {v=}")
            self.pose.printline()

        # update the history variables
        hist = self._history()
        hist.f = f
        hist.p = self.camera.project_point(self.P, pose=self.pose)
        hist.vel = v
        hist.e = e
        hist.enorm = np.linalg.norm(e)
        hist.jcond = np.linalg.cond(J)
        hist.pose = self.pose
        self.history.append(hist)
        
        if hist.enorm < self.eterm:
            status = 1

        return status


# %IBVS   Implement classical IBVS for point features
# %
# %  results = ibvs(T)
# %  results = ibvs(T, params)
# %
# %  Simulate IBVS with for a square target comprising 4 points is placed 
# %  in the world XY plane. The camera/robot is initially at pose T and is
# %  driven to the orgin.
# %
# %  Two windows are shown and animated:
# %   1. The camera view, showing the desired view (*) and the 
# %      current view (o)
# %   2. The external view, showing the target points and the camera
# %
# % The results structure contains time-history information about the image
# % plane, camera pose, error, Jacobian condition number, error norm, image
# % plane size and desired feature locations.
# %
# % The params structure can be used to override simulation defaults by
# % providing elements, defaults in parentheses:
# %
# %   target_size    - the side length of the target in world units (0.5)
# %   target_center  - center of the target in world coords (0,0,3)
# %   niter          - the number of iterations to run the simulation (500)
# %   eterm          - a stopping criteria on feature error norm (0)
# %   lambda         - gain, can be scalar or diagonal 6x6 matrix (0.01)
# %   ci             - camera intrinsic structure (camparam)
# %   depth          - depth of points to use for Jacobian, scalar for
# %                    all points, of 4-vector.  If null take actual value
# %                    from simulation      ([])
# %
# % SEE ALSO: ibvsplot

# % IMPLEMENTATION NOTE
# %
# % 1.  As per task function notation (Chaumette papers) the error is
# %     defined as actual-demand, the reverse of normal control system
# %     notation.
# % 2.  The gain, lambda, is always positive
# % 3.  The negative sign is written into the control law

class IBVS_sph(VisualServo):

    def __init__(self, camera, eterm=0.01, lmbda=0.04, depth=None, **kwargs):

        # invoke superclass constructor
        super().__init__(camera, type='point', **kwargs)
        
        self.lmbda = lmbda
        self.eterm = eterm
        self.depth = depth
        
                
    @classmethod
    def Example(cls):
        # run a canned example
        print('canned example, spherical IBVS with 4 points');
        if camera is None:
            camera = SphericalCamera.Default(name='')
        self = cls(camera, **kwargs)
        self.P = mkgrid(2, side=1.5, pose=SE3(0, 0, 0.5))
        self.pose_f = SE3(0, 0, -1.5) * SE3.Rz(1)
        self.pose_0 = SE3(0.3, 0.3, -2) * SE3.Rz(0.2)
        # self.T0 = transl(-1,-0.1,-3);%*trotx(0.2)

    def init(self):

        super().init()

        # final pose is specified in terms of a camera-target pose
        #   convert to image coords
        self.p_star = self.camera.project_point(self.P, pose=self.pose_f)


    def step(self):
        status = 0;
        Z_est = [];
        
        # compute image plane error as a column
        p = self.camera.project_point(self.P)  # (phi, theta)
        print(f"{p=}")

        e = self.p_star - p   # feature error
        e[0, :] = smbase.wrap_mpi_pi(e[1, :])
        e[1, :] = smbase.wrap_0_pi(e[1, :])
        e = e.ravel('F')
    
        # compute the Jacobian
        if self.depth is None:
            # exact depth from simulation (not possible in practice)
            P_C = self.camera.pose.inv() * self.P
            J = self.camera.visjac_p(p, P_C[2, :])
        else:
            J = self.camera.visjac_p(pt, self.depth)

        # compute the velocity of camera in camera frame
        try:
            v = self.lmbda * np.linalg.pinv(J) @ e
        except np.linalg.LinAlgError:
            status = -1

        if self.verbose:
            print(f"{v=}")

        # update the camera pose
        self.camera.pose @= SE3.Delta(v) 

        # draw lines from points to centre of camera
        if self.graphics:
            centre = self.camera.pose.t
            plt.sca(self.ax_3dview)
            for P in self.P.T:
                plt.plot(*[(centre[i], P[i]) for i in range(3)], 'k')

        # update the history variables
        hist = self._history()
        hist.p = p
        hist.vel = v
        hist.e = e
        hist.enorm = np.linalg.norm(e)
        hist.jcond = np.linalg.cond(J)
        hist.pose = self.camera.pose
        self.history.append(hist)

        if hist.enorm < self.eterm:
            status = 1
        return status

    def plot_p(self):
        # result is a vector with row per time step, each row is u1, v1, u2, v2 ...
        for i in range(self.npoints):
            u = [h.p[0, i] for h in self.history]  # get data for i'th point
            v = [h.p[1, i] for h in self.history]
            plt.plot(u, v, 'b')
        
        # mark the initial target shape
        smbase.plot_point(self.history[0].p, 'o', markeredgecolor='k', markerfacecolor='w', label='initial')
        
        # mark the goal target shape
        smbase.plot_point(self.p_star, 'k*', markeredgecolor='k', markerfacecolor='k', label='goal')

        # axis([0 self.camera.npix[0] 0 self.camera.npix[1]])
        # daspect([1 1 1])
        ax = plt.gca()

        plt.grid(True)
        ax.set_xlabel('Azimuth φ (rad)')
        ax.set_ylabel('Colatitude θ (rad)')
        ax.set_xlim(-np.pi, np.pi)
        ax.set_ylim(0, np.pi)
        ax.invert_yaxis()
        plt.legend(loc='lower right')
        ax.set_facecolor('lightyellow')


# %IBVS   Implement classical IBVS for point features
# %
# %  results = ibvs(T)
# %  results = ibvs(T, params)
# %
# %  Simulate IBVS with for a square target comprising 4 points is placed 
# %  in the world XY plane. The camera/robot is initially at pose T and is
# %  driven to the orgin.
# %
# %  Two windows are shown and animated:
# %   1. The camera view, showing the desired view (*) and the 
# %      current view (o)
# %   2. The external view, showing the target points and the camera
# %
# % The results structure contains time-history information about the image
# % plane, camera pose, error, Jacobian condition number, error norm, image
# % plane size and desired feature locations.
# %
# % The params structure can be used to override simulation defaults by
# % providing elements, defaults in parentheses:
# %
# %   target_size    - the side length of the target in world units (0.5)
# %   target_center  - center of the target in world coords (0,0,3)
# %   niter          - the number of iterations to run the simulation (500)
# %   eterm          - a stopping criteria on feature error norm (0)
# %   lambda         - gain, can be scalar or diagonal 6x6 matrix (0.01)
# %   ci             - camera intrinsic structure (camparam)
# %   depth          - depth of points to use for Jacobian, scalar for
# %                    all points, of 4-vector.  If null take actual value
# %                    from simulation      ([])
# %
# % SEE ALSO: ibvsplot

# % IMPLEMENTATION NOTE
# %
# % 1.  As per task function notation (Chaumette papers) the error is
# %     defined as actual-demand, the reverse of normal control system
# %     notation.
# % 2.  The gain, lambda, is always positive
# % 3.  The negative sign is written into the control law

class IBVS_polar(VisualServo):

    def __init__(self, camera, eterm=0.01, lmbda=0.02, depth=None, **kwargs):

        # monkey patch the plot setup for the CentralCamera object
        import types
        camera._plotcreate = types.MethodType(self._plotcreate, camera)
        camera._project_point = camera.project_point
        camera.project_point = types.MethodType(self._project_polar, camera)

        # invoke superclass constructor
        super().__init__(camera, type='point', **kwargs)
        
        self.lmbda = lmbda
        self.eterm = eterm
        self.depth = depth


    def init(self):

        # initialize the vservo variables
        super().init()

        # if 0 % isempty(self.h_rt) || ~ishandle(self.h_rt)
        #     fprintf('create rt axes\n');
        #     self.h_rt = axes;
        #     set(self.h_rt, 'XLimMode', 'manual');
        #     set(self.h_rt, 'YLimMode', 'manual');
        #     set(self.h_rt, 'NextPlot', 'replacechildren');
        #     axis([-pi pi 0 sqrt(2)])
        #     %axis([-pi pi 0 norm(self.camera.npix-self.camera.pp)])
        #     xlabel('\theta (rad)');
        #     ylabel('r (pix)');
        #     title('polar coordinate feature space');
        #     grid
        # end
        # %axes(self.h_rt)
        # %cla


        # final pose is specified in terms of a camera-target pose
        #  convert to image coords
        self.th_r_star = self.camera.project_point(self.P, pose=self.pose_f)

        self.plot_point(self.p_star, '*')

        if smbase.isscalar(self.lmbda):
            self.lmbda = np.diag([self.lmbda] * 6)

        # show the reference location, this is the view we wish to achieve
        # when Tc = Tct_star
        # if 0
        # self.camera.clf()
        # self.camera.plot(self.p_star, '*'); % create the camera view
        # self.camera.hold(true);
        # self.camera.plot(self.P, 'pose', self.T0, 'o'); % create the camera view
        # pause(2)
        # self.camera.hold(false);
        # self.camera.clf();
        # end

        # %self.camera.plot(self.P);    % show initial view

        # % this is the 'external' view of the points and the camera
        # %plot_sphere(self.P, 0.05, 'b')
        # %cam2 = showcamera(T0);
        # clf
        # self.camera.plot_camera(self.P, 'label');
        # # %camup([0,-1,0]);

        self.history = [];


    def step(self):
        status = 0;
        Zest = [];
        
        hist = self._history()

        # compute the polar projection view (phi, r)
        p = self.camera.project_point(self.P)

        # compute image plane error as a column
        e = self.p_star - p  # feature error

        e[0, :] = smbase.wrap_mpi_pi(e[0, :])
        e = e.ravel('F')  # convert columnwise to a 1D vector 
        
        # compute the Jacobian
        if self.depth is None:
            # exact depth from simulation (not possible in practice)
            pt = self.camera.pose.inv() * self.P
            J = self.camera.visjac_p_polar(p, pt[2, :])
        else:
            # use the default depth
            J = self.camera.visjac_p_polar(p, self.depth)

        # compute the velocity of camera in camera frame
        try:
            v = -self.lmbda @ np.linalg.pinv(J) @ e
        except np.linalg.LinAlgError:
            return -1

        if self.verbose:
            print(v)

        vmax = 0.02
        if np.linalg.norm(v) > vmax:
            v = smbase.unitvec(v) * vmax

        # update the camera pose
        Td = SE3.Delta(v) # differential motion
        # Td = SE3(trnorm(delta2tr(v)))    
        #Td = expm( skewa(v) )
        #Td = SE3( delta2tr(v) )
        self.camera.pose @= Td       # apply it to current pose

        # update the history variables
        hist.p = p
        vel = Td.delta()
        hist.vel = vel
        hist.e = e
        hist.enorm = np.linalg.norm(e)
        hist.jcond = np.linalg.cond(J)
        hist.pose = self.camera.pose

        self.history.append(hist)

        if np.linalg.norm(e) < self.eterm:
            status = 1

        return status

    def plot_p(self):
        # result is a vector with row per time step, each row is u1, v1, u2, v2 ...
        for i in range(self.npoints):
            u = [h.p[0, i] for h in self.history]  # get data for i'th point
            v = [h.p[1, i] for h in self.history]
            plt.plot(u, v, 'b')
        
        # mark the initial target shape
        smbase.plot_point(self.history[0].p, 'o', markeredgecolor='k', markerfacecolor='w', label='initial')
        
        # mark the goal target shape
        smbase.plot_point(self.p_star, 'k*', markeredgecolor='k', markerfacecolor='k', label='goal')

        # axis([0 self.camera.npix[0] 0 self.camera.npix[1]])
        # daspect([1 1 1])
        ax = plt.gca()

        plt.grid(True)
        ax.set_xlabel('Azimuth φ (rad)')
        ax.set_ylabel('normalized radius')
        ax.set_xlim(-np.pi, np.pi)
        rmax = np.linalg.norm(np.r_[self.camera.width, self.camera.height] - self.camera.pp) * 2 / self.camera.width
        ax.set_ylim(0, rmax)
        plt.legend()
        ax.set_facecolor('lightyellow')

    @staticmethod
    def _project_polar(self, P, pose=None, objpose=None):
        # bound to project_point()

        # overloaded projection method, projects to polar coordinates

        p = self._project_point(P, pose=pose, objpose=objpose)
        # %p = homtrans( inv(self.camera.K), p);

        pp = self.pp
        u = p[0, :] - pp[0]
        v = p[1, :] - pp[1]
        th_r = np.array([np.arctan2(v,u),
                         np.sqrt(u**2 + v**2) / self.width * 2])

        # %line(rt(:,2), rt(:,1), 'Marker', 'o', 'MarkerFaceColor', 'k', 'Parent', self.h_rt)
        # % plot points on rt plane

        return th_r

    @staticmethod
    def _plotcreate(self, fig=None, ax=None):
        if self._newplot(fig, ax):
            return

        ax = self._ax

        ax.set_xlim(-np.pi, np.pi)
        rmax = np.linalg.norm(np.r_[self.width, self.height] - self.pp) * 2 / self.width
        ax.set_ylim(0, rmax)

        ax.autoscale(False)
        ax.grid(True)

        ax.set_xlabel('Azimuth φ (rad)')
        ax.set_ylabel('normalized radius')

        ax.set_title(self.name)
        ax.set_facecolor('lightyellow')
        ax.figure.canvas.set_window_title('Machine Vision Toolbox for Python')

        # TODO figure out axes ticks, etc
        return ax  # likely this return is not necessary
