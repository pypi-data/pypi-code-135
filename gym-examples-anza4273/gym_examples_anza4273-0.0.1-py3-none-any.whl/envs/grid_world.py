import gym
from gym import spaces
import pygame
import numpy as np


class GridWorldEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(self, render_mode=None, size=5, 
        start_location=None, terminal_locations=None, obstacles=None,
        policy=None, transition_matrix=None
    ):
        self.size = size  # The size of the square grid
        self.window_size = 512  # The size of the PyGame window

        # we swap the elements in locations using [[1, 0]] because in this gym env column number comes first
        self._user_start_location = None if start_location is None else self._validate_location(start_location) # [[1, 0]]  
        self._obstacles = [] if obstacles is None else [self._validate_location(location) for location in obstacles] #[[1, 0]] for location in obstacles]
        self._obstacles = np.array(self._obstacles)
        assert not self._state_in_list_of_states(self._user_start_location, self._obstacles)

        self._user_terminal_locations = [] if terminal_locations is None else [self._validate_location(location) for location in terminal_locations] # [[1, 0]] for location in terminal_locations]
        self._terminal_locations = np.array(self._user_terminal_locations)
        if len(self._user_terminal_locations):
            if self._user_start_location is not None:
                assert not self._state_in_list_of_states(self._user_start_location, self._user_terminal_locations)
            if len(self._obstacles):
                assert not any([self._state_in_list_of_states(obstacle, self._user_terminal_locations) for obstacle in self._obstacles])

        # Observations are dictionaries with the agent's and the target's location.
        # Each location is encoded as an element of {0, ..., `size`}^2, i.e. MultiDiscrete([size, size]).
        self.observation_space = spaces.Dict(
            {
                "agent": spaces.Box(0, size - 1, shape=(2,), dtype=int),
                "target": spaces.Box(0, size - 1, shape=(2,), dtype=int),
            }
        )

        # We have 4 actions, corresponding to "right", "up", "left", "down", "right"
        self.action_space = spaces.Discrete(4)

        """
        The following dictionary maps abstract actions from `self.action_space` to 
        the direction we will walk in if that action is taken.
        I.e. 0 corresponds to "right", 1 to "up" etc.
        """
        self._action_to_direction = {
            0: np.array([1, 0]),
            1: np.array([-1, 0]),
            2: np.array([0, 1]),
            3: np.array([0, -1]),
        }

        
        self.states = self._init_states()
        self.policy = policy if policy is not None else np.ones((len(self.states), len(self._action_to_direction))) / len(self._action_to_direction)
        self.transition_matrix = transition_matrix
        self._start_id = None if self._user_start_location is None else self._state_location_to_id(self._user_start_location)


        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        """
        If human-rendering is used, `self.window` will be a reference
        to the window that we draw to. `self.clock` will be a clock that is used
        to ensure that the environment is rendered at the correct framerate in
        human-mode. They will remain `None` until human-mode is used for the
        first time.
        """
        self.window = None
        self.clock = None

    def _validate_location(self, location):
        location_np = np.array(location)
        assert len(location_np) == 2
        assert np.all((location_np >= 0) & (location_np < self.size))
        return location_np.astype(int)

    def _state_location_to_id(self, location):
        return np.argwhere(np.all(location == self.states, axis=1)).flatten()[0]

    def _init_states(self):
        return np.array([np.array([row, col]) for row in range(self.size) for col in range(self.size)
                         if not self._state_in_list_of_states(np.array([col, row]), self._obstacles)])

    def _state_in_list_of_states(self, state, states_to_check=None):
        states_to_check = self.states if states_to_check is None else states_to_check
        if not len(states_to_check):
            return False
        return np.any(np.all(state == states_to_check, axis=1))

    def _get_obs(self):
        return {"agent": self._agent_location, "target": self._target_location}

    def _get_info(self):
        return {
            "distance": np.linalg.norm(
                self._agent_location - self._target_location, ord=1
            )
        }

    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        # Choose the agent's location uniformly at random
        if self._user_start_location is None:
            self._state_id = self.np_random.integers(len(self.states), dtype=int)
            self._agent_location = self.states[self._state_id]
            self._start_location = self._agent_location
        else:
            self._agent_location = self._user_start_location
            self._state_id = self._state_location_to_id(self._agent_location)
            self._start_location = self._user_start_location
        # self._agent_location = self._start_location if self._start_location is not None else self.np_random.integers(0, self.size, size=2, dtype=int)
        

        if len(self._user_terminal_locations):
            self._target_location = self._user_terminal_locations[0]
            self._terminal_locations = self._user_terminal_locations
        else:
            # We will sample the target's location randomly until it does not coincide with the agent's location
            # self._target_location = self._agent_location
            target_id = self._state_id
            while self._state_id == target_id:
                target_id = self.np_random.integers(len(self.states), dtype=int)
            self._target_location = self.states[target_id]
            self._terminal_locations = np.array([self._target_location])

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, info

    def step(self, action):
        action_id, direction = self.choose_action() if action is None else (action, self._action_to_direction[action])

        # action_id, direction = action, self._action_to_direction[action]

        # We use `np.clip` to make sure we don't leave the grid
        if self.transition_matrix is None:
            new_location = self._agent_location + direction
            if self._state_in_list_of_states(new_location):
                self._agent_location = new_location
                self._state_id = self._state_location_to_id(new_location)

        else:
            target_probs = self.transition_matrix[action_id][self._state_id]
            target_id = self.np_random.choice(len(target_probs), p=target_probs)
            self._agent_location = self.states[target_id]
            self._state_id = target_id
            
        # An episode is done iff the agent has reached the target
        terminated = self._state_in_list_of_states(self._agent_location, self._terminal_locations)
        reward = 1 if terminated else 0  # Binary sparse rewards
        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, reward, terminated, False, info

    def choose_action(self):
        action_probs = self.policy[self._state_id]
        action_id = self.np_random.choice(len(action_probs), p=action_probs)
        return action_id, self._action_to_direction[action_id]

    def render(self):
        if self.render_mode == "rgb_array":
            return self._render_frame()

    def _render_frame(self):
        if self.window is None and self.render_mode == "human":
            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode((self.window_size, self.window_size))
        if self.clock is None and self.render_mode == "human":
            self.clock = pygame.time.Clock()

        canvas = pygame.Surface((self.window_size, self.window_size))
        canvas.fill((255, 255, 255))
        pix_square_size = (
            self.window_size / self.size
        )  # The size of a single grid square in pixels

        # First we draw the target
        pygame.draw.rect(
            canvas,
            (100, 230, 70),
            pygame.Rect(
                pix_square_size * self._target_location[[1, 0]],
                (pix_square_size, pix_square_size),
            ),
        )

        # Draw the other terminal states, assuming that the "desirable" terminal state is passed first and was drawn before
        ts = self._terminal_locations[1:]
        for index, location in enumerate(ts):
            green_component = 255 - 255 * index / len(ts)
            pygame.draw.rect(
                canvas,
                (255, green_component, 0),
                pygame.Rect(
                    pix_square_size * location[[1, 0]],
                    (pix_square_size, pix_square_size),
                ),
            )


        # Draw the start state
        pygame.draw.rect(
            canvas,
            (0, 150, 255),
            pygame.Rect(
                pix_square_size * self._start_location[[1, 0]],
                (pix_square_size, pix_square_size),
            ),
        )

        # Draw the obstacles
        for obstacle_location in self._obstacles:
            pygame.draw.rect(
                canvas,
                (0, 0, 0),
                pygame.Rect(
                    pix_square_size * obstacle_location[[1, 0]],
                    (pix_square_size, pix_square_size),
                ),
            )

        # Now we draw the agent
        pygame.draw.circle(
            canvas,
            (200, 0, 255),
            (self._agent_location[[1, 0]] + 0.5) * pix_square_size,
            pix_square_size / 3,
        )

        # Finally, add some gridlines
        for x in range(self.size + 1):
            pygame.draw.line(
                canvas,
                0,
                (0, pix_square_size * x),
                (self.window_size, pix_square_size * x),
                width=3,
            )
            pygame.draw.line(
                canvas,
                0,
                (pix_square_size * x, 0),
                (pix_square_size * x, self.window_size),
                width=3,
            )

        if self.render_mode == "human":
            # The following line copies our drawings from `canvas` to the visible window
            self.window.blit(canvas, canvas.get_rect())
            pygame.event.pump()
            pygame.display.update()

            # We need to ensure that human-rendering occurs at the predefined framerate.
            # The following line will automatically add a delay to keep the framerate stable.
            self.clock.tick(self.metadata["render_fps"])
        else:  # rgb_array
            return np.transpose(
                np.array(pygame.surfarray.pixels3d(canvas)), axes=(0, 1, 2)
            )

    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()
