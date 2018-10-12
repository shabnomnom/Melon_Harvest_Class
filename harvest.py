############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        # when initiating the attrebutes when can name them whatever we want 
        self.code = code
        self.harvest = first_harvest 
        self.color = color
        self.is_seedless = is_seedless
        self.best_seller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)



    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    #all_melon_types = []

    # code, first_harvest, color, is_seedless, is_bestseller, name = melon_info

    musk = MelonType("musk","1998", "green",True, True,"Muskmelon")
    musk.add_pairing("mint")
    # all_melon_types.append(musk)

    cas = MelonType('cas', '2003', 'orange', False, False, 'Casaba')
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    # all_melon_types.append(cas)

    yw = MelonType('yw', '2013', 'yellow', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    # all_melon_types.append(yw)

    cren = MelonType('cren', '1996', 'green', True, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    # all_melon_types.append(cren)

    melons = [musk,cas,yw,cren]
    return melons

def print_pairing_info(melons):
    """Prints information about each melon type's pairings."""

    for melon in melons:
        print(" {} pairs with".format(melon.name))
        for pairs in melon.pairings:
            print("- {}".format(pairs))
        print() 

def make_melon_type_lookup(melons):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_lookup ={}

    for melon in melons: 
        melon_lookup[melon.code] = melon
            # "year of harvest" : melon.harvest,
            # "Color:" : melon.color,
            # "Is_seedless" : melon.is_seedless,
            # "Best_seller:": melon.best_seller,
            # "Name:" : melon.name, }

    for key,value in melon_lookup.items():
        print(key,value)


melons = make_melon_types() 

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



