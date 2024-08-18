"""
Abstract factory method - 
        -  creational design pattern 
        -  provides an interface for creating families of related or dependent objects without specifying their concrete classes.
        - Factory of Factories: The abstract factory pattern is essentially a factory that creates other factories. These factories then produce objects of related classes.
        - 

"""
# consider example of UI: Dark theme , Light Theme. Though this is mostly handled from frontend iteself. Consider this as an example only.

from abc import abstractmethod

# Abstract Product: Button
class Button():
    @abstractmethod
    def render(self):
        pass

# Abstract Product: Checkbox
class Checkbox():
    @abstractmethod
    def render(self):
        pass

# Concrete Product: Dark Button
class DarkButton(Button):
    def render(self):
        print("Rendering Dark Button")

# Concrete Product: Light Button
class LightButton(Button):
    def render(self):
        print("Rendering Light Button")

 # Concrete Product: Dark Checkbox
class DarkCheckbox(Checkbox):
    def render(self):
        print("Rendering Dark Checkbox")

# Concrete Product: Light Checkbox
class LightCheckbox(Checkbox):
    def render(self):
        print("Rendering Light Checkbox")


class UIFactory():
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass  

# Abstract Factory
class DarkUIFactory(UIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()
    
class LightUIFactory(UIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()
    
# for client usage 
def build_ui(factory: UIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()



if __name__ == "__main__":
    # User selects the dark theme
    dark_factory = DarkUIFactory()
    print("Building Dark Theme UI:")
    build_ui(dark_factory)

    # User selects the light theme
    light_factory = LightUIFactory()
    print("\nBuilding Light Theme UI:")
    build_ui(light_factory)