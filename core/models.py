from django.db import models


class Pokemon(models.Model):
    """Model for Pokemon records. 
    
    name: Name of the pokemon.
    """

    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self) -> str:
        return self.name
    

class PokemonAbility(models.Model):
    """Model for saving pokemon abilities. 
    
    pokemon: Foreign key to the related pokemon
    name: Name of the ability
    """

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    