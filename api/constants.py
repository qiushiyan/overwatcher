from enum import Enum


class Team(Enum):
    """
    all overwatch league teams
    """

    ATLANTA_REIGN = "atlanta reign"
    BOSTAN_UPRISING = "boston uprising"
    CHENGDU_HUNTERS = "chengdu hunters"
    DALLAS_FUEL = "dallas fuel"
    FLORIDA_MAYHEM = "florida mayhem"
    GUANGZHOU_CHARGE = "guangzhou charge"
    HANGZHOU_SPARK = "hangzhou spark"
    LONDON_SPITEFIRE = "london spitefire"
    LOS_ANGELES_GLADIATROS = "los angeles gladiators"
    LOS_ANGELES_VALIANT = "los angeles valiant"
    NEW_YORK_EXCELSIOR = "new york excelsior"
    PARIS_ETERNAL = "paris eternal"
    PHILADELPHIA_FUSION = "philadelphia fusion"
    SAN_FRANCISCO_SHOCK = "san francisco shock"
    SEOUL_DYNASTY = "seoul dynasty"
    SHANGHAI_DRAGONS = "shanghai dragons"
    TORONTO_DEFIANT = "toronto defiant"
    VANCOUVER_TITANS = "vancouver titans"
    WASHINGTON_JUSTICE = "washington justice"


class Map(Enum):
    """
    all maps
    """

    BLIZZARD_WORLD = "blizzard world"
    BUSAN = "busan"
    DORADO = "dorado"
    EICHENWALDE = "eichenwalde"
    HANAMURA = "hanamura"
    HAVANA = "havana"
    HOLLYWOOD = "hollywood"
    ILIOS = "ilios"
    JUNKERTOWN = "junkertown"
    KINGS_ROW = "king's row"
    LIJIANG_TOWER = "lijiang tower"
    NEPAL = "nepal"
    NUMBANI = "numbani"
    OASIS = "oasis"
    ROUTE_66 = "route 66"
    TEMPLE_OF_ANUBIS = "temple of anubis"
    VOLSKAYA_INDUSTRIES = "volskaya industries"
    WATCHPOINT_GIBRALTAR = "watchpoint: gibraltar"


class MapType(Enum):
    """
    all map types
    """

    ASSULT = "assult"
    CONTROL = "control"
    HYBRID = "hybrid"
    PAYLOAD = "payload"


class Hero(Enum):
    """
    all heroes
    """

    ANA = "ana"
    ASHE = "ashe"
    BAPTISTE = "baptiste"
    BASTION = "bastion"
    BRIGITTE = "brigitte"
    DVA = "d.va"
    DOOMFIST = "doomfist"
    ECHO = "echo"
    GENJI = "genji"
    HANZO = "hanzo"
    JUNKRAT = "junkrat"
    LUCIO = "lucio"
    MCCREE = "mccree"
    MEI = "mei"
    MERCY = "mercy"
    MOIRA = "moira"
    ORISA = "orisa"
    PHARAH = "pharah"
    REAPER = "reaper"
    REINHARDT = "reinhardt"
    ROADHOG = "roadhog"
    SIGMA = "sigma"
    SOLDIER_76 = "soldier: 76"
    SOMBRA = "sombra"
    SYMMETRA = "symmetra"
    TORBJORN = "torbjorn"
    TRACER = "tracer"
    WIDOWMAKER = "widowmaker"
    WINSTON = "winston"
    WRECKING_BALL = "wrecking ball"
    ZARYA = "zarya"
    ZENYATTA = "zenyatta"
