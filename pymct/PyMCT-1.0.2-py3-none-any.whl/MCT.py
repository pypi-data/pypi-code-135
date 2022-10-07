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

    def __init__(self, state: Any, parent=None, children=None) -> None:
        super().__init__()
        self._state = state
        self._visits = 0
        self._reward = 0.0
        self._uct = inf
        self.parent = parent
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


class MCTS(ABC):
    _root: MCTNode
    _c: Union[int, float]
    _max_iter: int
    _complete: bool
    _debug: bool
    _iter: int
    _optimal_path: List[MCTNode]

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

    def iterate(self):
        """Iterates until the terminate conditioin is met (set in terminate method), or max number of iterations reached."""
        while self.complete is False:
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
            else:
                # select the node with highest uct
                chosen_node = None
                max_uct = -inf
                for node in self.root.descendants:
                    if node.uct > max_uct:
                        chosen_node = node
                        max_uct = node.uct
                if self.debug:
                    logger.info(
                        f"Selected Node {chosen_node.state}, uct is {chosen_node.uct}."
                    )

                if chosen_node.visits == 0:
                    self.get_reward(chosen_node)
                    if self.debug:
                        logger.info(
                            f"Node {chosen_node.state} receives reward {chosen_node.reward}."
                        )
                    self.backpropagation(chosen_node)
                    self.update_uct(chosen_node)
                elif chosen_node.visits >= 1:
                    new_states = self.expand(chosen_node)
                    if len(new_states) == 0:
                        if self.debug:
                            logger.info(f"Node {chosen_node.state} is a leaf.")

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

    @abstractmethod
    def expand(self, node: MCTNode) -> List[MCTNode]:
        """Exapnd the tree at current node. The new discovered nodes must be add as children for this node.

        Args:
            node (MCTNode): the selected node.

        Returns:
            List[MCTNode]: new discovered nodes.
        """
        return node.children

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
        pass

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
