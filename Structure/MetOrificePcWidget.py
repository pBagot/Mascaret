# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name                 : Mascaret
Description          : Pre and Postprocessing for Mascaret for QGIS
Date                 : December,2017
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
import os
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.uic import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from .ClassTableStructure import ClassTableStructure, ctrl_set_value, \
    ctrl_get_value, fill_qcombobox

if int(qVersion()[0]) < 5:  # qt4
    from qgis.PyQt.QtGui import *
else:  # qt5
    from qgis.PyQt.QtGui import QIcon
    from qgis.PyQt.QtWidgets import *


class MetOrificePcWidget(QWidget):
    def __init__(self, mgis, id_struct=None):
        QWidget.__init__(self)
        self.mgis = mgis
        self.mdb = self.mgis.mdb
        self.tbst = ClassTableStructure()
        self.ui = loadUi(os.path.join(self.mgis.masplugPath,
                                      'ui/structures/ui_orifice_pc.ui'), self)
        self.id_struct = id_struct

        self.completed = 0
        self.progress = self.ui.progressBar
        self.progress.setValue(0)

        self.sb_nb_trav.valueChanged.connect(self.change_ntrav)
        self.dsb_larg_pil.valueChanged.connect(self.update_piles)
        self.dsb_h_pas.valueChanged.connect(self.update_min_h_max)
        self.dsb_h_min.valueChanged.connect(self.update_min_h_max)
        self.tab_trav.itemChanged.connect(self.verif_larg_trav)

        self.dico_ctrl = {'FIRSTWD': [self.dsb_abs_cul_rg],
                          'ZTOPTAB': [self.dsb_cote_tab],
                          'EPAITAB': [self.dsb_epai_tab],
                          'LARGPIL': [self.dsb_larg_pil],
                          'PASH': [self.dsb_h_pas],
                          'MINH': [self.dsb_h_min],
                          'MAXH': [self.dsb_h_max],
                          'PASQ': [self.dsb_q_pas],
                          'NBTRAVE': [self.sb_nb_trav],
                          'COEFDS': [self.dsb_ds],
                          'COEFDO': [self.dsb_do]
                          }

        self.dico_tab = {self.tab_trav: {'type': 0,
                                         'id': '({}*2) + 1',
                                         'col': [{'fld': 'LARGTRA', 'cb': None,
                                                  'valdef': 1.}]},
                         self.tab_pile: {'type': 1,
                                         'id': '({}*2) + 2',
                                         'col': [{'fld': 'LARGPIL', 'cb': None,
                                                  'valdef': self.dsb_larg_pil}]}
                         }

    def change_ntrav(self, nb_trav):
        nb_pile = max(0, nb_trav - 1)
        nrow_trav = self.tab_trav.rowCount()
        nrow_pile = self.tab_pile.rowCount()
        if nb_trav < nrow_trav:
            self.tab_trav.setRowCount(nb_trav)
        else:
            for t in range(nrow_trav, nb_trav):
                self.insert_elem(self.tab_trav, t)
        if nb_pile < nrow_pile:
            self.tab_pile.setRowCount(nb_pile)
        else:
            for p in range(nrow_pile, nb_pile):
                self.insert_elem(self.tab_pile, p)

    def insert_elem(self, tab, row):
        tab.insertRow(row)
        for c, col in enumerate(self.dico_tab[tab]['col']):
            if isinstance(col['valdef'], int) or isinstance(col['valdef'],
                                                            float):
                val = col['valdef']
            else:
                val = ctrl_get_value(col['valdef'])

            if col['cb']:
                cb = QComboBox()
                fill_qcombobox(cb, col['cb'], val_def=val)
                tab.setCellWidget(row, c, cb)
            else:
                itm = QTableWidgetItem()
                itm.setData(0, val)
                tab.setItem(row, c, itm)

    def update_piles(self):
        for row in range(self.tab_pile.rowCount()):
            self.tab_pile.item(row, 0).setData(0, self.dsb_larg_pil.value())

    def update_min_h_max(self):
        self.dsb_h_max.setMinimum(
            self.dsb_h_min.value() + self.dsb_h_pas.value())

    def verif_larg_trav(self, itm):
        if itm.data(0) <= 0.:
            itm.setData(0, 1.)

    def progress_bar(self, val):
        self.completed += val
        if self.completed > 100:
            self.completed = 100
        self.progress.setValue(self.completed)
