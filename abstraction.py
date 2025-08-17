"""Abstraction demo: define a clear interface and hide implementation details.

We use Python's `abc` module to declare an abstract base class (ABC) that
specifies what actions are available, without saying how they are done.

- Notifier (abstract): defines `send(message)` that all notifiers must implement
- EmailNotifier / SMSNotifier: provide concrete implementations

This separates the 'what' (interface) from the 'how' (implementation).
"""

from abc import ABC, abstractmethod


class Notifier(ABC):
    """Abstract interface: how clients will interact with any notifier."""

    @abstractmethod
    def send(self, message: str) -> None:
        """Send a message through a specific channel."""
        raise NotImplementedError


class EmailNotifier(Notifier):
    """Concrete implementation that 'sends' an email."""

    def send(self, message: str) -> None:
        # In real code, you'd integrate an email service here.
        print(f"[EMAIL] {message}")


class SMSNotifier(Notifier):
    """Concrete implementation that 'sends' an SMS."""

    def send(self, message: str) -> None:
        # In real code, you'd integrate an SMS gateway here.
        print(f"[SMS] {message}")


def notify_user(notifier: Notifier, message: str) -> None:
    """Function using the abstract interface (works with any Notifier).

    This shows both Abstraction (we depend on the interface) and
    Polymorphism (different notifiers respond in their own way).
    """

    notifier.send(message)


if __name__ == "__main__":
    # Demo (optional): try both implementations via the same interface
    notify_user(EmailNotifier(), "Welcome to OOP!")
    notify_user(SMSNotifier(), "Your code is clean and simple.")
