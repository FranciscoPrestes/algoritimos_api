from fastapi import APIRouter
from models.computed_property import ComputedProperty

router = APIRouter()

class Example:
    def __init__(self, value: float) -> None:
        self.value = value

    @ComputedProperty("value")
    def double(self) -> float:
        """
        Retorna o dobro do valor atual.

        Returns:
            float: O valor multiplicado por 2.
        """
        return self.value * 2


@router.get("/example/{value}")
async def get_computed_property(value: float) -> dict[str, float]:
    """
    Retorna o valor e seu dobro calculado como propriedade computada.

    Args:
        value (float): Valor de entrada.

    Returns:
        dict[str, float]: Valor e dobro.
    """
    example = Example(value)
    return {
        "value": example.value,
        "double": example.double
    }
