from abc import ABC, abstractmethod
from typing import Tuple

from pygame import Surface


class ComponentBase(ABC):
    """
    The ComponentBase class is an abstract base class that defines the interface for a component in a game or application.
    It provides a set of abstract methods that must be implemented by any concrete subclass.
    """

    @abstractmethod
    def render(self, screen: Surface):
        """
        The render method is responsible for drawing the component on the screen.
        It takes a Surface object as a parameter, which represents the screen or a portion of the screen where the component should be rendered.
        This method must be implemented by any concrete subclass.
        """
        pass

    @abstractmethod
    def update(self, delta_milisec: float):
        """
        The update method is called periodically to update the state of the component.
        It takes a float value representing the time elapsed since the last update in milliseconds.
        This method can be used to perform any necessary calculations, update positions, or handle game logic.
        It must be implemented by any concrete subclass.
        """
        pass

    @abstractmethod
    def on_mouse_move(self, mouse_position: Tuple[int, int]):
        """
        The on_mouse_move method is called whenever the mouse is moved over the component.
        It takes a tuple containing the current position of the mouse as (x, y) coordinates.
        This method can be used to handle mouse hover effects or any other actions that should be triggered when the mouse moves over the component.
        It must be implemented by any concrete subclass.
        """
        pass

    @abstractmethod
    def on_mouse_button_down(self):
        """
        The on_mouse_button_down method is called when a mouse button is pressed while the mouse is over the component.
        This method can be used to handle user interactions, such as clicking on a button or selecting an item.
        It must be implemented by any concrete subclass.
        """
        pass

    @abstractmethod
    def on_mouse_button_up(self):
        """
        The on_mouse_button_up method is called when a mouse button is released while the mouse is over the component.
        This method can be used to handle the completion of user interactions, such as releasing a clicked button.
        It must be implemented by any concrete subclass.
        """
        pass