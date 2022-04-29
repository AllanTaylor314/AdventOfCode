cold='cold'
bludgeoning='bludgeoning'
radiation='radiation'
slashing='slashing'
fire='fire'

immune_system = [
(4082,	2910,	dict(),                                                 5,	cold,	        15),
(2820,	9661,	dict(immune	=	('slashing',))	,		                27,	cold,	        8),
(4004,	4885,	dict(weak	=	('slashing',))	,		                10,	bludgeoning,	13),
(480,	7219,	dict(weak	=	('bludgeoning',))	,		            134,radiation,	    18),
(8734,	4421,	dict(immune	=	('bludgeoning',))	,		            5,	slashing,	    14),
(516,	2410,	dict(weak	=	('slashing',))	,		                46,	bludgeoning,	5),
(2437,	11267,	dict(weak	=	('slashing',))	,		                38,	fire,	        17),
(1815,	7239,	dict(weak	=	('cold',))	,		                    33,	slashing,	    10),
(4941,	10117,	dict(immune	=	('bludgeoning',))	,		            20,	fire,	        9),
(617,	7816,	dict(weak	=	('bludgeoning',	'slashing'))	,		120,bludgeoning,	4),
]
infection = [
(2877,	20620,	dict(weak=('radiation','bludgeoning')),		                        13,	cold,	        11),
(1164,	51797,	dict(immune=('fire',)),                                             63,	fire,	        7),
(160,	31039,	dict(weak=('radiation',), immune=('bludgeoning',)),	                317,bludgeoning,	2),
(779,	24870,	dict(immune=('radiation','bludgeoning'),weak=('slashing',))	,		59,	slashing,	    12),
(1461,	28000,	dict(immune=('radiation',),weak=('bludgeoning',))	,		        37,	slashing,	    16),
(1060,	48827,	dict(),		                                                        73,	slashing,	    3),
(4422,	38291,	dict(),		                                                        14,	slashing,	    1),
(4111,	14339,	dict(immune=('fire', 'bludgeoning', 'cold'))	,		            6,	radiation,	    20),
(4040,	49799,	dict(immune=('bludgeoning', 'cold'),weak=('slashing','fire')),		24,	fire,	        19),
(2198,	41195,	dict(weak=('radiation',)),		                                    36,	slashing,	    6),
]
