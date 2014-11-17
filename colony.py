from random import shuffle, choice, randint
from stars import stars
from collections import OrderedDict

# The Colony class simulates a human-derivative space colony.
 
class Colony:
    planets = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')
    
    castes = ('laborers', 'artists', 'merchants', 'priests', 'scientists', 'soldiers')
    techTiers = ('pre-industrial technology', 'machine technology', 'ubiquitous technology')
    genesisReasons = ('escape persecution', 'maintain control', 'explore the unknown', 'seed the galaxy with life', 'spread the gospel')
    
    badjectives = ('exiled', 'leprous', 'bankrupt', 'heretical', 'dissident', 'unpublished', 'pacifist', 'child', 'retired', 'blind', 'robot')
    
    preindustrialPreps = ('on', 'on')
    machinePreps = ('on', 'deep below the surface of')
    ubiquitousPreps = ('orbiting', 'on', 'on a miniaturized replica of', 'atop the space elevator on', 'on the surface of the Dyson sphere surrounding')
    techPreps = {'pre-industrial technology' : preindustrialPreps, 'machine technology' : machinePreps, 'ubiquitous technology' : ubiquitousPreps}
    
    preindustrialAdjectives = ('idyllic', 'charming', 'pastoral', 'forested', 'agrarian', 'snowy')
    machineAdjectives = ('smoggy', 'deforested', 'strip-mined', 'the garden planet', 'carefully manicured', 'the office park planet')
    ubiqitousAdjectives = ('utopian', 'the algae blooming lakes of', 'geothermally heated', 'labyrinthine', 'computer simulated', 'the ringworld')
    techAdjectives = {'pre-industrial technology' : preindustrialAdjectives, 'machine technology' : machineAdjectives, 'ubiquitous technology' : ubiqitousAdjectives}
        
    controlAdjectives = ('bureaucratic', 'obsessive-compulsive', 'draconian', 'dour', 'dictatorial')
    exploreAdjectives = ('inquisitive', 'pioneering', 'experimental')
    seedAdjectives =  ('lusty', 'virile', 'narcissistic', 'randy', 'entitled')
    gospelAdjectives = ('fanatical', 'Mormon', 'pacifist', 'polytheistic', 'pantheistic', 'monotheistic')
    genesisAdjectives = {'escape persecution' : badjectives, 'maintain control' : controlAdjectives, 'explore the unknown' : exploreAdjectives, 'seed the galaxy with life' : seedAdjectives, 'spread the gospel' : gospelAdjectives}
    
    laborerAdjectives = ('hard-working', 'socialist', 'simple', 'communist', 'mule-owning')
    artistAdjectives = ('gifted', 'child', 'genius', 'visionary', 'AI')
    merchantAdjectives = ('fat', 'extravagant', 'miserly', 'merchant', 'corrupt')
    priestAdjectives = ('corrupt', 'rabbinical', 'monastic', 'sacerdotal', 'charitable', 'eunuch', 'evangelical')
    scientistAdjectives = ('gifted', 'genius', 'AI', 'methodical', 'academic')
    soldierAdjectives = ('barbaric', 'honorable', 'militant', 'warmongering')
    casteAdjectives = {'laborers' : laborerAdjectives, 'artists' : artistAdjectives, 'merchants' : merchantAdjectives, 'priests' : priestAdjectives, 'scientists' : scientistAdjectives, 'soldiers' : soldierAdjectives}
    
    laborerSynonyms = ('prostitutes', 'space stevedores', 'welders', 'AI therapists', 'bitcoin miners', 'socialists')
    artistSynonyms = ('poets', 'sculptors', 'painters', 'composers', 'dancers', 'pixel artists')
    merchantSynonyms = ('moneychangers', 'shopkeepers', 'spicers', 'merchant-barons', 'capitalists')
    priestSynonyms = ('cultists', 'priests', 'monks', 'cardinals', 'pilgrims', 'anchorites')
    scientistSynonyms = ('astrobiologists', 'botanists', 'particle physicists', 'AI researchers', 'mathematicians', 'cryptographers', 'eugenicists')
    soldierSynonyms = ('ronin', 'warmongers', 'gladiators', 'mercenaries', 'space marines', 'conquistadors')
    casteSynonyms = {'laborers' : laborerSynonyms, 'artists' : artistSynonyms, 'merchants' : merchantSynonyms, 'priests' : priestSynonyms, 'scientists' : scientistSynonyms, 'soldiers' : soldierSynonyms}
        
    preindustrialSettlements = ('winery', 'dairy farm', 'fishing community', 'mud pueblo', 'sawmill')
    machineSettlements = ('walled city', 'mining colony', 'retirement community', 'university annex', 'spa and resort', 'corporate office park')
    ubiqitousSettlements = ('geodesic dome', 'bismuth labyrinth', 'silicon labyrinth', 'fungus farm', 'algae farm', 'spaceport', 'glass arcology', 'computer simulation')
    settlements = {'pre-industrial technology': preindustrialSettlements, 'machine technology' : machineSettlements, 'ubiquitous technology' : ubiqitousSettlements}
    
    explorePlaces = ('laboratories', 'workshops', 'observatories', 'hackerspaces')
    gospelPlaces = ('mausoleums', 'tabernacles', 'monasteries')
    seedPlaces = ('brothels', 'nurseries', 'greenhouses')
    escapePlaces = ('insane asylums', 'museums', 'free-range farms')
    controlPlaces = ('labor camps', 'panopticons', 'sensory deprivation chambers')
    genesisPlaces = {'escape persecution' : escapePlaces, 'maintain control' : controlPlaces, 'explore the unknown' : explorePlaces, 'seed the galaxy with life' : seedPlaces, 'spread the gospel' : gospelPlaces}
    
    escapeIdeals = ('liberty', 'marginalization', 'self-actualization', 'suffrage', 'autonomy')
    controlIdeals = ('marginalization', 'oppression', 'torment', 'omniscience', 'brutality')
    exploreIdeals = ('uncertainty', 'empiricism', 'unknowable forms', 'the limitations of knowledge', 'artificial being', 'quantum indeterminacy')
    seedIdeals = ('virility', 'fertility', 'sexual metaphors', 'self-replication', 'mortality')
    gospelIdeals = ('sacrifice', 'faith and submission to a higher power', 'divinity', 'the afterlife', 'mortality')
    genesisIdeals = {'escape persecution' : escapeIdeals, 'maintain control' : controlIdeals, 'explore the unknown' : exploreIdeals, 'seed the galaxy with life' : seedIdeals, 'spread the gospel' : gospelIdeals}
    
    merchantBooks = ('The Wealth of Nations', 'The Fountainhead', 'Atlas Shrugged', 'The Road to Serfdom', 'Capitalism in the Quantum Age', 'Anthem', 'The Biography of Grover Norquist')
    
    def __init__(self):
        """Intializes and describes a colony"""
        self.name = '{0} {1}'.format(choice(stars), choice(self.__class__.planets))
        self.casteOrder = (list(self.__class__.castes))
        shuffle(self.casteOrder)
        self.tech = choice(self.__class__.techTiers)
        self.genesis = choice(self.__class__.genesisReasons)
        self.description = ''
        self.attributes = '{0}   ~  ruled by {1}   ~   founded to {2}'.format(self.tech, self.casteOrder[0], self.genesis)

    def describe(self):        
        """Procedurally describes a colony from its attributes"""
        branch = randint(0,62)
        
        if 0 <= branch <= 29:            
            if self.casteOrder[0] == 'soldiers':
                if self.genesis == 'escape persecution':                    
                    self.description = '{2}: A full service {3} for retired {1}'.format(choice(self.__class__.badjectives), choice(self.__class__.soldierSynonyms), self.name, choice(self.__class__.settlements[self.tech]))                    
                elif self.genesis == 'maintain control':                    
                    self.description = 'The penal mining colony for {0} {1} on {2}'.format(choice(self.__class__.badjectives), choice(self.__class__.casteSynonyms[self.casteOrder[5]]), self.name, choice(self.__class__.settlements[self.tech]))                    
                elif self.genesis == 'explore the unknown':
                    self.description = 'The frontier garrison and {2} {0} recently conquered {1}'.format(choice(self.__class__.techPreps[self.tech]), self.name, choice(self.__class__.settlements[self.tech]))
                elif self.genesis == 'seed the galaxy with life':
                    self.description = 'The militarized {3} and bonsai garden for the mandatory contemplation of {0} {1} {2}'.format(choice(self.__class__.seedIdeals), choice(self.__class__.techPreps[self.tech]), self.name, choice(self.__class__.settlements[self.tech]))
                elif self.genesis == 'spread the gospel':
                    self.description = 'An outpost for crusaders who took up arms to defend {2} {3} on {0} {1}'.format(choice(self.__class__.techAdjectives[self.tech]), self.name, choice(self.__class__.badjectives), choice(self.__class__.priestSynonyms))                
            elif self.casteOrder[0] == 'scientists':
                if self.genesis == 'escape persecution':                    
                    self.description = 'A sanctuary for {0} who challenged the dogma of powerful {1} {2} {3}'.format(choice(self.__class__.scientistSynonyms), choice(self.__class__.priestSynonyms), choice(self.__class__.techPreps[self.tech]), self.name)                    
                elif self.genesis == 'maintain control':                    
                    self.description = '{0}, home to a coalition of {1} eugenicists and their {2} servants'.format(self.name, choice(self.__class__.scientistAdjectives), choice(self.__class__.casteAdjectives[self.casteOrder[5]]))
                elif self.genesis == 'explore the unknown':
                    self.description = 'An Extremely Large Hadron Collider {0} {1} {2}'.format(choice(self.__class__.techPreps[self.tech]), choice(self.__class__.techAdjectives[self.tech]), self.name)
                elif self.genesis == 'seed the galaxy with life':
                    self.description = 'The research institute and {2} for abiogenesis on {0} {1}'.format(choice(self.__class__.techAdjectives[self.tech]), self.name, choice(self.__class__.settlements[self.tech]))
                elif self.genesis == 'spread the gospel':
                    self.description = 'The Galactic Academy of Sciences founded by {0} {1} {2} {3}'.format(choice(self.__class__.scientistAdjectives), choice(self.__class__.scientistSynonyms), choice(self.__class__.techPreps[self.tech]), self.name)
            elif self.casteOrder[0] == 'laborers':
                if self.genesis == 'escape persecution':
                    self.description = 'The {0} for unionized {1} {2} {3}'.format(choice(self.__class__.settlements[self.tech]), choice(self.__class__.laborerSynonyms), choice(self.__class__.techPreps[self.tech]), self.name)
                elif self.genesis == 'maintain control':
                    self.description = '{0} {1}: divisional headquarters for the communist party in this region of the galaxy (where evidence of {2} has been redacted)'.format(choice(self.__class__.techAdjectives[self.tech]).capitalize(), self.name, choice(self.__class__.controlIdeals))
                elif self.genesis == 'explore the unknown':
                    self.description = 'A team of robot {0} sent to survey {1} {2}'.format(choice(self.__class__.laborerSynonyms), choice(self.__class__.techAdjectives[self.tech]), self.name)
                elif self.genesis == 'seed the galaxy with life':
                    self.description = 'Drones sent to terraform {0} {1} and build {2}'.format(choice(self.__class__.techAdjectives[self.tech]), self.name, choice(self.__class__.seedPlaces))
                elif self.genesis == 'spread the gospel':
                    self.description = 'The {0} {1} {2} where a hard day\'s work is highly valued'.format(choice(self.__class__.settlements[self.tech]), choice(self.__class__.techPreps[self.tech]), self.name)
            elif self.casteOrder[0] == 'merchants':
                if self.genesis == 'escape persecution':
                    self.description = '{0} {1}: a refuge for {2} who fled a communist revolution on their home planet'.format(choice(self.__class__.techAdjectives[self.tech]).capitalize(), self.name, choice(self.__class__.merchantSynonyms))
                elif self.genesis == 'maintain control':
                    self.description = 'The monopolistic conglomerate of {0} {1} {2} {3}'.format(choice(self.__class__.merchantAdjectives), choice(self.__class__.merchantSynonyms), choice(self.__class__.techPreps[self.tech]), self.name)
                elif self.genesis == 'explore the unknown':
                    self.description = '{3} {0}, home to a consortium of {1} seeking to monetize {2}'.format(self.name, choice(self.__class__.merchantSynonyms), choice(self.__class__.genesisIdeals[choice(self.__class__.genesisReasons)]), choice(self.__class__.techAdjectives[self.tech]).capitalize())
                elif self.genesis == 'seed the galaxy with life':
                    self.description = 'An oligarchy of wealthy {0} who recently opened a for-profit {1} on {2}'.format(choice(self.__class__.merchantSynonyms), choice(self.__class__.settlements[self.tech]), self.name)
                elif self.genesis == 'spread the gospel':
                    self.description = 'An orbital printing press that rains down copies of {0} onto {1} {2}'.format(choice(self.__class__.merchantBooks), choice(self.__class__.techAdjectives[self.tech]), self.name)
            elif self.casteOrder[0] == 'artists':
                if self.genesis == 'escape persecution':
                    self.description = 'The {0}\' commune for the free and naked expression of {1} {2} {3}'.format(choice(self.__class__.artistSynonyms), choice(self.__class__.escapeIdeals), choice(self.__class__.techPreps[self.tech]), self.name)
                elif self.genesis == 'maintain control':
                    self.description = 'The {0} with mandatory art classes on {1} {2}'.format(choice(self.__class__.settlements[self.tech]), choice(self.__class__.techAdjectives[self.tech]), self.name)
                elif self.genesis == 'explore the unknown':
                    self.description = '{0} {1}, an observation deck where {2} observe naked and confined {3} to better understand the mysteries of {4}'.format(choice(self.__class__.techPreps[self.tech]).capitalize(), self.name, choice(self.__class__.artistSynonyms), choice(self.__class__.casteSynonyms[self.casteOrder[5]]), choice(self.__class__.genesisIdeals[choice(self.__class__.genesisReasons)]))
                elif self.genesis == 'seed the galaxy with life':
                    self.description = 'The {0} for {1} {2} who choose to better understand their craft through lovemaking on {3}'.format(choice(self.__class__.settlements[self.tech]), choice(self.__class__.seedAdjectives), choice(self.__class__.artistSynonyms), self.name)
                elif self.genesis == 'spread the gospel':
                    self.description = 'A {0} on {1} that hosts an annual conference for pop {2}'.format(choice(self.__class__.settlements[self.tech]), self.name, choice(self.__class__.artistSynonyms))
            elif self.casteOrder[0] == 'priests':
                if self.genesis == 'escape persecution':
                    self.description = '{3} {0}, home to an order of heretical {1} who reject the {2} doctrine of their people'.format(self.name, choice(self.__class__.priestSynonyms), choice(self.__class__.gospelAdjectives), choice(self.__class__.techAdjectives[self.tech]).capitalize())
                elif self.genesis == 'maintain control':
                    self.description = 'The orthodox {0} for {1} {2} {3} {4}'.format(choice(self.__class__.gospelPlaces), choice(self.__class__.gospelAdjectives), choice(self.__class__.priestSynonyms), choice(self.__class__.techPreps[self.tech]), self.name)
                elif self.genesis == 'explore the unknown':
                    self.description = '{0} {1}, a seminary for the metaphysical contemplation of {2}'.format(choice(self.__class__.techPreps[self.tech]).capitalize(), self.name, choice(self.__class__.gospelIdeals))
                elif self.genesis == 'seed the galaxy with life':
                    self.description = 'The marriage counseling clinic and devotional {2} {0} {1}'.format(choice(self.__class__.techPreps[self.tech]), self.name, choice(self.__class__.settlements[self.tech])) 
                elif self.genesis == 'spread the gospel':
                    self.description = 'A {0} mission on {1} {2} for converting {3} natives'.format(choice(self.__class__.gospelAdjectives), choice(self.__class__.techAdjectives[self.tech]), self.name, choice(self.__class__.badjectives))
                                            
        elif 30 <= branch <= 44:
            if self.tech == 'pre-industrial technology':
                if self.genesis == 'explore the unknown':
                     self.description = '{0}, home to a historical reenactment society of {2} {1}'.format(self.name, choice(self.__class__.casteSynonyms[self.casteOrder[0]]), choice(self.__class__.badjectives))
                elif self.genesis == 'escape persecution':
                    self.description = '{1}: a {2} of {0} Luddites'.format(choice(self.__class__.casteAdjectives[self.casteOrder[0]]), self.name, choice(self.__class__.preindustrialSettlements))
                elif self.genesis == 'maintain control':
                    self.description = 'The {0} fiefdoms of {1}, where {2} serve their {3} liege lord'.format(choice(self.__class__.preindustrialAdjectives), self.name, choice(self.__class__.casteSynonyms[self.casteOrder[5]]), choice(self.__class__.casteAdjectives[self.casteOrder[0]]))
                elif self.genesis == 'seed the galaxy with life':
                    self.description = 'A harem of {0} {1} on medieval {2}'.format(choice(self.__class__.seedAdjectives), choice(self.__class__.casteSynonyms[self.casteOrder[0]]), self.name)
                elif self.genesis == 'spread the gospel':
                    self.description = 'The Puritan {0} for evangelical {1} on {2}'.format(choice(self.__class__.preindustrialSettlements), choice(self.__class__.casteSynonyms[self.casteOrder[0]]), self.name)
            elif self.tech == 'machine technology':
                if self.genesis == 'explore the unknown':
                    self.description = 'An array of radio telescopes outside the {0} on {1} {2}'.format(choice(self.__class__.machineSettlements), choice(self.__class__.machineAdjectives), self.name)
                elif self.genesis == 'escape persecution':
                    self.description = 'Public housing for {0} {1} gentrified {2}'.format(choice(self.__class__.casteSynonyms[self.casteOrder[0]]), choice(self.__class__.machinePreps), self.name)                
                elif self.genesis == 'maintain control':
                    self.description = 'The juvenile detention center for {0} children who obsess over {1} on {2}'.format(choice(self.__class__.badjectives), choice(self.__class__.genesisIdeals[choice(self.__class__.genesisReasons)]), self.name)
                elif self.genesis == 'seed the galaxy with life':
                    self.description = 'Just a giant cruise ship full of {0} {1} on {2}'.format(choice(self.__class__.seedAdjectives), choice(self.__class__.casteSynonyms[self.casteOrder[0]]), self.name)
                elif self.genesis == 'spread the gospel':
                    self.description = 'A megachurch run by {0} {1}, broadcasting live from {2}'.format(choice(self.__class__.priestAdjectives), choice(self.__class__.casteSynonyms[self.casteOrder[0]]), self.name)
            elif self.tech == 'ubiquitous technology':
                if self.genesis == 'explore the unknown':
                    self.description = 'A quantum data center for simulating the lives of {0} {1} {2} {3}'.format(choice(self.__class__.casteAdjectives[self.casteOrder[0]]), choice(self.__class__.casteSynonyms[choice(self.__class__.castes)]), choice(self.__class__.techPreps[self.tech]), self.name)
                elif self.genesis == 'escape persecution':
                    self.description = 'The cryogenics facility for the preservation of {0} {1} {2} {3}'.format(choice(self.__class__.badjectives), choice(self.__class__.casteSynonyms[self.casteOrder[0]]), choice(self.__class__.techPreps[self.tech]), self.name)
                elif self.genesis == 'maintain control':
                    self.description = 'Orbiting {0}: a socially stratified {1} governed by {2}'.format(self.name, choice(self.__class__.ubiqitousSettlements), choice(self.__class__.casteSynonyms[self.casteOrder[0]]))
                elif self.genesis == 'seed the galaxy with life':
                    self.description = '{0} {1}, home to an assembly plant for android {2}'.format(choice(self.__class__.ubiqitousAdjectives).capitalize(), self.name, choice(self.__class__.casteSynonyms[self.casteOrder[0]]))
                elif self.genesis == 'spread the gospel':
                    self.description = '{0}, home to an anthropological society of {1} who covertly inject the theme of {2} into the folklore of other civilizations'.format(self.name, choice(self.__class__.casteSynonyms[self.casteOrder[0]]), choice(self.__class__.genesisIdeals[choice(self.__class__.genesisReasons)]))
            
        elif 45 <= branch <= 62:
            if self.casteOrder[0] == 'laborers':
                if self.tech == 'pre-industrial technology':
                    self.description = 'A kibbutz for {0} {1} on {2}'.format(choice(self.__class__.genesisAdjectives[self.genesis]), choice(self.laborerSynonyms), self.name)
                elif self.tech == 'machine technology':
                    self.description = 'The worker-owned and operated {1} of {2} {0}'.format(self.name, choice(self.__class__.genesisPlaces[self.genesis]), choice(self.__class__.machineAdjectives))
                elif self.tech == 'ubiquitous technology':
                    self.description = '{0}, host to a psychic hivemind of {1} {2}'.format(self.name, choice(self.__class__.genesisAdjectives[self.genesis]), choice(self.__class__.laborerSynonyms))
            elif self.casteOrder[0] == 'artists':
                if self.tech == 'pre-industrial technology':
                    self.description = 'The conservatory for neoclassical {0} who explore the theme of {1} on {2}'.format(choice(self.__class__.artistSynonyms), choice(self.__class__.genesisIdeals[self.genesis]), self.name)
                elif self.tech == 'machine technology':
                    self.description = 'A series of art installations conceived by {1} at various {0} on {2}'.format(choice(self.__class__.genesisPlaces[self.genesis]), choice(self.__class__.artistSynonyms), self.name)
                elif self.tech == 'ubiquitous technology':
                    self.description = '{0}: a collective of AI {1} who parody the human theme of {2}'.format(self.name, choice(self.__class__.artistSynonyms), choice(self.__class__.genesisIdeals[self.genesis]))
            elif self.casteOrder[0] == 'priests':
                if self.tech == 'pre-industrial technology':
                    self.description = '{0} {1}, home to a scriptorium dedicated to the penning of meditations on {2}'.format(choice(self.__class__.preindustrialAdjectives).capitalize(), self.name, choice(self.__class__.genesisIdeals[self.genesis]))
                elif self.tech == 'machine technology':
                    self.description = 'Polygamous cultists who live among the {0} of {1} {2}'.format(choice(self.__class__.genesisPlaces[self.genesis]), choice(self.__class__.machineAdjectives), self.name)
                elif self.tech == 'ubiquitous technology':
                    self.description = 'A pyramidic burial chamber and monument to {0} {1} {2}'.format(choice(self.__class__.genesisIdeals[self.genesis]), choice(self.__class__.ubiquitousPreps), self.name)
            elif self.casteOrder[0] == 'scientists':
                if self.tech == 'pre-industrial technology':
                    self.description = '{0}, home to a collective of {1} {2} who reproduce scientific experiments from pre-industrial Earth'.format(self.name, choice(self.genesisAdjectives[self.genesis]), choice(self.__class__.scientistSynonyms))
                elif self.tech == 'machine technology':
                    self.description = 'A society of {0} who work simulated jobs at {1} on {3} to better understand {2}'.format(choice(self.__class__.scientistSynonyms), choice(self.__class__.genesisPlaces[self.genesis]), choice(self.__class__.genesisIdeals[self.genesis]), self.name)
                elif self.tech == 'ubiquitous technology':
                    self.description = 'The postdoctoral program for {0} tenure-track {1} {2} {3}'.format(choice(self.__class__.genesisAdjectives[self.genesis]), choice(self.__class__.scientistSynonyms), choice(self.__class__.ubiquitousPreps), self.name)
            elif self.casteOrder[0] == 'soldiers':
                if self.tech == 'pre-industrial technology':
                    self.description = '{0}, where {1} {2} study their martial arts in the quiet isolation of a {3}'.format(self.name, choice(self.__class__.genesisAdjectives[self.genesis]), choice(self.__class__.soldierSynonyms), choice(self.__class__.preindustrialSettlements))
                elif self.tech == 'machine technology':
                    self.description = '{0}, where {1} {2} spar each other to overcome their frustrations surrounding {3}'.format(self.name, choice(self.__class__.badjectives), choice(self.__class__.soldierSynonyms), choice(self.__class__.genesisIdeals[self.genesis]))
                elif self.tech == 'ubiquitous technology':
                    self.description = 'The highly militarized {0} {1} {2}'.format(choice(self.__class__.genesisPlaces[self.genesis]), choice(self.__class__.ubiquitousPreps), self.name)
            elif self.casteOrder[0] == 'merchants':
                if self.tech == 'pre-industrial technology':
                    self.description = 'An antique fair on {0} where 1% of the proceeds are donated to the study of {1}'.format(self.name, choice(self.__class__.genesisIdeals[self.genesis]))
                elif self.tech == 'machine technology':
                    self.description = 'A chain of retail {0} near the {1} on {2}'.format(choice(self.__class__.genesisPlaces[self.genesis]), choice(self.__class__.machineSettlements), self.name)
                elif self.tech == 'ubiquitous technology':
                    self.description = 'A pay-by-the-hour computer simulation {0} {1} where patrons can experience {2}'.format(choice(self.__class__.ubiquitousPreps), self.name, choice(self.__class__.genesisIdeals[self.genesis]))
                    
    def serialize(self):
        """Serializes a colony object in the specificed order"""
        return OrderedDict([('name', self.name), ('description', self.description), ('attribute summary', self.attributes), ('tech level', self.tech), ('caste hierarchy', self.casteOrder), ('founded to', self.genesis)])