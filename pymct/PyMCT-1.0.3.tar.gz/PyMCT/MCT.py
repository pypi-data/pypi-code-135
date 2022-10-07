from abc import ABC, abstractmethod
from math import inf, log, sqrt
from typing import Any, List, Union

from anytree import NodeMixin, RenderTree

from PyMCT.Log import logger


class MCTNode(NodeMixin):
    _state: Any
    _visits: int
    _reward: float
    _uct: float
    _expanded:bool

    def __init__(self, state: Any, parent=None, children=None) -> None:
        super().__init__()
        self._state = state
        self._visits = 0
        self._reward = 0.0
        self._uct = inf
        self.parent = parent
        self._expanded = False
        if children is not None:
            self.children = children

    @property
    def state(self):
        return self._state

    @property
    def visits(self):
        return self._visits

    @property
    def reward(self):
        return self._reward

    @property
    def reward_history(self):
        return self._reward_history

    @property
    def uct(self):
        return self._uct
    
    @property
    def expanded(self):
        return self._expanded


class MCTS(ABC):
    _root: MCTNode
    _c: Union[int, float]
    _max_iter: int
    _complete: bool
    _debug: bool
    _iter: int
    _optimal_path: List[MCTNode]
    _current_chosen_node: MCTNode
    _previous_chosen_node: MCTNode

    def __init__(
        self, root: MCTNode, c: Union[int, float], max_iter: int, debug=False
    ) -> None:
        super().__init__()
        self._root = root
        self._c = c
        self._complete = False
        self._max_iter = max_iter
        self._debug = debug
        self._iter = 0
        self._optimal_path = list()
        self.optimal_path.append(self.root)
        self._current_chosen_node = None
        self._previous_chosen_node = None

    def iterate(self):
        """Iterates until the terminate conditioin is met (set in terminate method), or max number of iterations reached."""
        while self.complete is False:
            
            self._previous_chosen_node = self.current_chosen_node
            
            if self.root.visits == 0:
                self.get_reward(self.root)
                if self.debug:
                    logger.info(
                        f"Node {self.root.state} receives reward {self.root.reward}."
                    )
                self.backpropagation(self.root)
                self.update_uct(self.root)
                new_states = self.expand(self.root)
                if len(new_states) == 0:
                    self._complete = True
                    logger.warning(f"The root can not be extened.")
                self._current_chosen_node = self.root
            else:
                # select the node with highest uct
                max_uct = -inf
                for node in self.root.descendants:
                    if node.uct > max_uct:
                        self._current_chosen_node = node
                        max_uct = node.uct
                if self.debug:
                    logger.info(
                        f"Selected Node {self.current_chosen_node.state}, uct is {self.current_chosen_node.uct}."
                    )

                if self.current_chosen_node.visits == 0:
                    self.get_reward(self.current_chosen_node)
                    if self.debug:
                        logger.info(
                            f"Node {self.current_chosen_node.state} receives reward {self.current_chosen_node.reward}."
                        )
                    self.backpropagation(self.current_chosen_node)
                    self.update_uct(self.current_chosen_node)
                elif self.current_chosen_node.visits >= 1 and self.current_chosen_node.expanded == False:
                    new_states = self.expand(self.current_chosen_node)
                    if len(new_states) == 0:
                        if self.debug:
                            logger.info(f"Node {self.current_chosen_node.state} is a leaf.")

            self._iter = self.iter + 1
            self._complete = self.terminate()
            if self.complete is False and self.iter >= self.max_iter:
                logger.warning(
                    "MCT search is forced to terminate because max number of iterations has reached."
                )
                self._complete = True

    @property
    def root(self):
        return self._root

    @property
    def complete(self):
        return self._complete

    @property
    def c(self):
        return self._c

    @property
    def debug(self):
        return self._debug

    @property
    def max_iter(self):
        return self._max_iter

    @property
    def iter(self):
        return self._iter

    @property
    def optimal_path(self):
        return self._optimal_path
    
    @property
    def current_chosen_node(self):
        return self._current_chosen_node
    
    @property
    def previous_chosen_node(self):
        return self._previous_chosen_node

    @abstractmethod
    def expand(self, node: MCTNode) -> List[MCTNode]:
        """Exapnd the tree at current node. The new discovered nodes must be add as children for this node.

        Args:
            node (MCTNode): the selected node.

        Returns:
            List[MCTNode]: new discovered nodes.
        """
        node._expanded = True

    @abstractmethod
    def get_reward(self, node: MCTNode):
        """Caculate reward for the current node.

        Args:
            node (MCTNode): the current node.
        """
        pass

    @abstractmethod
    def terminate(self) -> bool:
        """Define the terminate condition for the algorithm.

        Returns:
            bool: return True for termination.
        """

    def backpropagation(self, node: MCTNode):
        """Backpropagation for updating rewards of all ancestors.

        Args:
            node (MCTNode): the node where backpropagation starts.
        """
        if node.parent is not None:
            node.parent._reward = node.parent.reward + node.reward
            if self.debug:
                logger.info(
                    f"Node {node.parent.state}'s reward update to {node.parent.reward}."
                )
            self.backpropagation(node.parent)
        else:
            return

    def update_uct(self, node: MCTNode):
        """Update the UCT value for current node and all its ancestors.

        Args:
            node (MCTNode): the node where backpropagation starts.
        """
        node._visits = node.visits + 1
        if self.debug:
            logger.info(f"Node {node.state}'s visits update to {node.visits}.")
        mean = node.reward / node.visits
        node._uct = mean + self.c * sqrt(log(node.visits) / node.visits)
        if self.debug:
            logger.info(f"Node {node.state}'s uct update to {node.uct}.")
        if node.parent is not None:
            self.update_uct(node.parent)

    def find_optimal_path(self) -> List[MCTNode]:
        """Find the optimal path.

        Returns:
            List[MCTNode]: the optimal path of nodes.
        """
        if len(self.optimal_path[-1].children) != 0:
            uct = -inf
            best_child: MCTNode = None
            for child in self.optimal_path[-1].children:
                if child.uct >= uct:
                    uct = child.uct
                    best_child = child
            self.optimal_path.append(best_child)
            self.find_optimal_path()
        else:
            return

    def render_tree(self):
        print(RenderTree(self.root))
