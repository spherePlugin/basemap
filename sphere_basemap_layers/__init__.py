# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SphereBasemap
                                 A QGIS plugin
 This plugin let you to add a variety of thailand basemap from Gistda Sphere Open Platform
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-01-12
        copyright            : (C) 2023 by Gistda Sphere
        email                : info@gistda.or.th
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SphereBasemap class from file SphereBasemap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sphere_basemap import SphereBasemap
    return SphereBasemap(iface)
