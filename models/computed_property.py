from functools import wraps
from typing import Any, Callable


class ComputedProperty:
    """
    Decorator para criar uma propriedade computada com cache automático
    que se atualiza quando os atributos dependentes são modificados.

    Args:
        *dependencies (str): Nomes dos atributos dependentes.

    Raises:
        ValueError: Se nenhuma dependência for fornecida.
    """

    def __init__(self, *dependencies: str) -> None:
        if not dependencies:
            raise ValueError("Deve haver ao menos uma dependência.")
        self._dependencies = dependencies

    def __call__(self, func: Callable) -> property:
        """
        Decora a função como uma propriedade computada.

        Args:
            func (Callable): Função a ser decorada.

        Returns:
            property: Propriedade computada.
        """
        attr_name = f'_{func.__name__}_cache'

        @property
        @wraps(func)
        def wrapper(instance) -> Any:
            cache = getattr(instance, attr_name, None)
            if cache:
                last_values, value = cache
                if not self._dependencies_changed(instance, last_values):
                    return value

            current_values = {dep: getattr(instance, dep, None) for dep in self._dependencies}
            value = func(instance)
            setattr(instance, attr_name, (current_values, value))
            return value

        return wrapper

    def _dependencies_changed(self, instance: Any, last_values: dict) -> bool:
        """
        Verifica se algum dos atributos dependentes foi alterado.

        Args:
            instance (Any): Instância do objeto.
            last_values (dict): Últimos valores cacheados.

        Returns:
            bool: True se houve alteração, False caso contrário.
        """
        return any(
            getattr(instance, dep, None) != last_values.get(dep, None)
            for dep in self._dependencies
        )
