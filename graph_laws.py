# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name                 : Mascaret
Description          : Pre and Postprocessing for Mascaret for QGIS
Date                 : June,2017
copyright            : (C) 2017 by Artelia
email                :
***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from .graphCommon import GraphCommon

dico_typ_law = {1: {'name': 'Hydrograph Q(t)',
                    'var': [{'name': 'time', 'leg': 'time', 'unit': 's'},
                            {'name': 'flowrate', 'leg': 'Q', 'unit': 'm3/s'}],
                    'graph': {'x': {'var': 0, 'tit': 'time', 'unit': 's'},
                              'y': {'var': [1], 'tit': 'Q', 'unit': 'm3/s'}},
                    'xIsTime': True},
                2: {'name': 'Rating Curve Z = f(Q)',
                    'var': [{'name': 'flowrate', 'leg': 'Q', 'unit': 'm3/s'},
                            {'name': 'z', 'leg': 'z', 'unit': 'm'}],
                    'graph': {'x': {'var': 0, 'tit': 'Q', 'unit': 'm3/s'},
                              'y': {'var': [1], 'tit': 'z', 'unit': 'm'}},
                    'xIsTime': False},
                3: {'name': 'Limnihydrograph Z,Q(t)',
                    'var': [{'name': 'time', 'leg': 'time', 'unit': 's'},
                            {'name': 'z', 'leg': 'z', 'unit': 'm'},
                            {'name': 'flowrate', 'leg': 'Q', 'unit': 'm3/s'}],
                    'graph': {'x': {'var': 0, 'tit': 'time', 'unit': 's'},
                              'y': {'var': [1, 2], 'tit': None, 'unit': None}},
                    'xIsTime': False}
                }

class GraphLaw(GraphCommon):
    """class Dialog GraphLaw"""
    def __init__(self, mgis=None, lay=None, typ_law=None):
        GraphCommon.__init__(self, mgis)
        self.mdb = self.mgis.mdb
        self.initUI_common_P()
        self.GUI_graph(lay)
        self.initUI()
        self.initCurv(typ_law)

    def initUI(self):
        self.axes = self.fig.add_subplot(111)
        self.fig.canvas.mpl_connect('pick_event', self.onpick)

        self.axes.tick_params(axis='both', labelsize=7.)
        self.axes.grid(True)

    def initCurv(self, typ_law):
        self.axes.cla()
        self.axes.tick_params(axis='both', labelsize=7.)
        self.axes.grid(True)

        self.list_trac = []
        self.courbes = []

        if typ_law:
            self.axeX = dico_typ_law[typ_law]['graph']['x']['var']
            for v, var in enumerate(dico_typ_law[typ_law]['graph']['y']['var']):
                self.list_trac.append({"id": var, "name": dico_typ_law[typ_law]['var'][var]['name']})
                self.courbeTrac, = self.axes.plot([], [], zorder=100 - v, label=dico_typ_law[typ_law]['var'][var]['name'])
                self.courbes.append(self.courbeTrac)


            self.initLegende()

        self.canvas.draw()

    def initGraph(self, id_law, all_vis=False):
        # self.majUnitX("s")
        leglines = self.leg.get_lines()

        sql = "SELECT value FROM {0}.laws_test WHERE id_law = {1} and id_var = {2} ORDER BY idx".format(self.mdb.SCHEMA, id_law, self.axeX)
        rows = self.mdb.run_query(sql, fetch=True)
        lst_x = [r[0] for r in rows]

        for t, trac in enumerate(self.list_trac):
            lst_y = []
            if id_law is not None:
                sql = "SELECT value FROM {0}.laws_test WHERE id_law = {1} and id_var = {2} ORDER BY idx".format(self.mdb.SCHEMA, id_law, trac['id'])
                rows = self.mdb.run_query(sql, fetch=True)
                if len(rows) > 0:
                    lst_y = [r[0] for r in rows]

            self.courbes[t].set_data(lst_x, lst_y)

            if all_vis:
                self.courbes[t].set_visible(True)
                leglines[t].set_alpha(1.0)

        self.majLimites()


# class GraphMeteo(GraphCommon):
#     """class Dialog GraphWaterQ"""
#     def __init__(self, mgis=None, lay=None, lst_var=None):
#         GraphCommon.__init__(self, mgis)
#         self.mdb = self.mgis.mdb
#         self.lst_var = lst_var
#         self.initUI_common_P()
#         self.GUI_graph(lay)
#         self.initUI()
#
#     def initUI(self):
#         self.axes = self.fig.add_subplot(111)
#         self.axes.tick_params(axis='both', labelsize=7.)
#         self.axes.grid(True)
#
#         for var in self.lst_var:
#             self.courbeTrac, = self.axes.plot([], [], zorder=100-var["id"], label=var["name"])
#             self.courbes.append(self.courbeTrac)
#
#         self.fig.canvas.mpl_connect('pick_event', self.onpick)
#         self.initLegende()
#
#     def initGraph(self, config, all_vis=False):
#         self.majUnitX("s")
#         leglines = self.leg.get_lines()
#         for v, var in enumerate(self.lst_var):
#             lst = [[], []]
#             if config is not None:
#                 sql = "SELECT time, value FROM {0}.laws_meteo WHERE id_config = {1} and id_var = {2} ORDER BY time".format(self.mdb.SCHEMA,
#                                                                                                                            config,
#                                                                                                                            var["id"])
#                 rows = self.mdb.run_query(sql, fetch=True)
#                 if len(rows) > 0:
#                     lst = list(zip(*rows))
#
#             self.courbes[v].set_data(lst[0], lst[1])
#
#             if all_vis:
#                 self.courbes[v].set_visible(True)
#                 leglines[v].set_alpha(1.0)
#
#         self.majLimites()
#
#
# class GraphInitConc(GraphCommon):
#     """class Dialog GraphWaterQ"""
#     def __init__(self, mgis=None, lay=None):
#         GraphCommon.__init__(self, mgis)
#         self.mdb = self.mgis.mdb
#         self.initUI_common_P()
#         self.GUI_graph(lay)
#         self.initUI()
#
#     def initUI(self):
#         self.axes = self.fig.add_subplot(111)
#         self.fig.canvas.mpl_connect('pick_event', self.onpick)
#
#     def initMdl(self, mod):
#         sql = "SELECT id, sigle FROM {0}.tracer_name WHERE type = '{1}' ORDER BY id".format(self.mdb.SCHEMA, mod)
#         rows = self.mdb.run_query(sql, fetch=True)
#
#         self.axes.cla()
#         self.axes.tick_params(axis='both', labelsize=7.)
#         self.axes.grid(True)
#
#         self.list_trac = []
#         self.courbes = []
#         for row in rows:
#             self.list_trac.append({"id":row[0], "name": row[1]})
#             self.courbeTrac, = self.axes.plot([], [], zorder=100-row[0], label=row[1])
#             self.courbes.append(self.courbeTrac)
#
#         self.initLegende()
#
#     def initGraph(self, config, bief, all_vis=False):
#         # self.majUnitX("s")
#         leglines = self.leg.get_lines()
#         for t, trac in enumerate(self.list_trac):
#             lst = [[], []]
#             if config is not None:
#                 sql = "SELECT abscissa, value FROM {0}.init_conc_wq " \
#                       "WHERE id_config = {1} and bief = {2} and id_trac = {3} ORDER BY abscissa".format(self.mdb.SCHEMA,
#                                                                                                         config,
#                                                                                                         bief,
#                                                                                                         trac["id"])
#                 rows = self.mdb.run_query(sql, fetch=True)
#                 if len(rows) > 0:
#                     lst = list(zip(*rows))
#
#             self.courbes[t].set_data(lst[0], lst[1])
#
#             if all_vis:
#                 self.courbes[t].set_visible(True)
#                 leglines[t].set_alpha(1.0)
#
#         self.majLimites()

