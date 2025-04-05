# MadeBySobyDamn
import bs
from bsMap import *
import bsMap
import bsInternal
import json
import cmdsetg
import logger

num = 0

def __init__(self, vrOverlayCenterOffset=None):
    """
    Instantiate a map.
    """
    import bsInternal
    bs.Actor.__init__(self)
    self.preloadData = self.preload(onDemand=True)

    def stats_shower():
        px=-110
        offset=str(7*" ")
        #separator ="--"*len(columnas)
        tabla= ""+ "       Name"+offset + "         Kills\n" 
        t = bs.newNode('text',
                        attrs={ 'text':str(tabla),
                                'scale': 0.6,
                                'maxWidth': 0,
                                'position': (400, -90),
                                'shadow': 0,
                                'flatness': 1.0,
                                'color': (0.7,0.7,0.7),
                                'hAlign': 'left',
                                'vAttach': 'top'})
        """ print "  Nombre: {}".format(name)
            print "  Puntaje: {}".format(stats['scores'])
            print "  Eliminaciones: {}".format(stats['kills'])
            print "  Muertes: {}".format(stats['deaths'])
            print "  Juegos jugados: {}".format(sta
                                'position': (-100,ts['games'])
            print
        """
        f = open(logger.stats, "r")
        stats = json.loads(f.read())

        #print(stats)
        # Ordenar por la metrica deseada (ejemplo: puntaje 'scores')
        # Convertimos los valores de 'scores' a enteros para que se ordenen correctamente.
        jugadores_ordenados = sorted(
            stats.items(),
            key=lambda item: int(item[1]['scores']),
            reverse=True # Orden descendente
        )

        # Imprimir los top 5 (o menos si no hay suficientes jugadores)
        top_5 = jugadores_ordenados[:5]  # Obtener solo los primeros 5
        for i, (id_jugador, stats) in enumerate(top_5, start=1):
            name = stats['name_html'].split(">")[-1]  # Extraer el nombre del jugador
            nameident=len(name)
            name=name.capitalize()
            name=name[:15]

            t = bs.newNode('text',
                        attrs={'text':u" {} | ".format(i)+u" {}".format(name),
                                'scale': 0.5,
                                'maxWidth': 0,
                                'position': (400, px),
                                'shadow': 1,
                                'flatness': 1.0,
                                'color': (1,1,1),
                                'hAlign': 'left',
                                'vAttach': 'top'})
            t = bs.newNode('text',
                        attrs={'text':"  "*19+"{}".format(stats['kills']),
                                'scale': 0.5,
                                'maxWidth': 0,
                                'position': (400, px),
                                'shadow': 1,
                                'flatness': 1.0,
                                'color': (1,1,1),
                                'hAlign': 'left',
                                'vAttach': 'top'})
            px=px-20
        """ print "  Nombre: {}".format(name)
            print "  Puntaje: {}".format(stats['scores'])
            print "  Eliminaciones: {}".format(stats['kills'])
            print "  Muertes: {}".format(stats['deaths'])
            print "  Juegos jugados: {}".format(sta
                                'position': (-100,ts['games'])
            print
        """
    stats_shower()

    # set some defaults
    bsGlobals = bs.getSharedObject('globals')
    # area-of-interest bounds
    aoiBounds = self.getDefBoundBox("areaOfInterestBounds")
    if aoiBounds is None:
        print 'WARNING: no "aoiBounds" found for map:', self.getName()
        aoiBounds = (-1, -1, -1, 1, 1, 1)
    bsGlobals.areaOfInterestBounds = aoiBounds
    # map bounds
    mapBounds = self.getDefBoundBox("levelBounds")
    if mapBounds is None:
        print 'WARNING: no "levelBounds" found for map:', self.getName()
        mapBounds = (-30, -10, -30, 30, 100, 30)
    bsInternal._setMapBounds(mapBounds)
    # shadow ranges
    try:
        bsGlobals.shadowRange = [
            self.defs.points[v][1] for v in
            ['shadowLowerBottom', 'shadowLowerTop',
             'shadowUpperBottom', 'shadowUpperTop']]
    except Exception:
        pass
    # in vr, set a fixed point in space for the overlay to show up at..
    # by default we use the bounds center but allow the map to override it
    center = ((aoiBounds[0]+aoiBounds[3])*0.5,
              (aoiBounds[1]+aoiBounds[4])*0.5,
              (aoiBounds[2]+aoiBounds[5])*0.5)
    if vrOverlayCenterOffset is not None:
        center = (center[0]+vrOverlayCenterOffset[0],
                  center[1]+vrOverlayCenterOffset[1],
                  center[2]+vrOverlayCenterOffset[2])
    bsGlobals.vrOverlayCenter = center
    bsGlobals.vrOverlayCenterEnabled = True
    self.spawnPoints = self.getDefPoints("spawn") or [(0, 0, 0, 0, 0, 0)]
    self.ffaSpawnPoints = self.getDefPoints("ffaSpawn") or [(0, 0, 0, 0, 0, 0)]
    self.spawnByFlagPoints = (self.getDefPoints("spawnByFlag")
                              or [(0, 0, 0, 0, 0, 0)])
    self.flagPoints = self.getDefPoints("flag") or [(0, 0, 0)]
    self.flagPoints = [p[:3] for p in self.flagPoints]  # just want points
    self.flagPointDefault = self.getDefPoint("flagDefault") or (0, 1, 0)
    self.powerupSpawnPoints = self.getDefPoints("powerupSpawn") or [(0, 0, 0)]
    self.powerupSpawnPoints = \
        [p[:3] for p in self.powerupSpawnPoints]  # just want points
    self.tntPoints = self.getDefPoints("tnt") or []
    self.tntPoints = [p[:3] for p in self.tntPoints]  # just want points
    self.isHockey = False
    self.isFlying = False
    self._nextFFAStartIndex = 0


bsMap.Map.__init__ = __init__
