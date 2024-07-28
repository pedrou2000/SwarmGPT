
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''


def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Validate the input planets
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    # Get the indexes of the planets
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    # Determine the range of planets between the two planets
    start_index = min(index1, index2) + 1
    end_index = max(index1, index2)
    
    # Get the planets in between
    between_planets = planets[start_index:end_index]
    
    # Return as a tuple
    return tuple(between_planets) if between_planets else ()

# Test cases for validation
print(bf("Jupiter", "Neptune"))  # Expected: ()
print(bf("Earth", "Mercury"))    # Expected: ("Venus",)
print(bf("Mercury", "Uranus"))   # Expected: ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Mars", "Saturn"))       # Expected: ("Jupiter",)
print(bf("Venus", "Earth"))        # Expected: ()
print(bf("Neptune", "Mercury"))   # Expected: ()
print(bf("Pluto", "Earth"))       # Expected: ()
print(bf("Mars", "Pluto"))        # Expected: ()
print(bf("Jupiter", "Mars"))      # Expected: ("Earth",)

def check(candidate):

    # Check some simple cases
    assert candidate("Jupiter", "Neptune") == ("Saturn", "Uranus"), "First test error: " + str(len(candidate("Jupiter", "Neptune")))      
    assert candidate("Earth", "Mercury") == ("Venus",), "Second test error: " + str(candidate("Earth", "Mercury"))  
    assert candidate("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), "Third test error: " + str(candidate("Mercury", "Uranus"))      
    assert candidate("Neptune", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus"), "Fourth test error: " + str(candidate("Neptune", "Venus"))  


    # Check some edge cases that are easy to work out by hand.
    assert candidate("Earth", "Earth") == ()
    assert candidate("Mars", "Earth") == ()
    assert candidate("Jupiter", "Makemake") == ()


check(bf)