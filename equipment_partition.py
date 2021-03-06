# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Leandro Ezequiel Baldi 
#    <baldileandro@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import addons
import logging
import time
from openerp.osv import fields, osv
from openerp import tools
_logger = logging.getLogger(__name__)

class it_equipment_partition(osv.osv):

    _name = 'it.equipment.partition'

    _description = 'Equipment Partition'

    _columns = {
    
		'equipment_id': fields.many2one('it.equipment','Equipment', ondelete='cascade'),
		'name': fields.char('Identificator',required=True),
		'disks': fields.char('Disks', help="Disks splitted by , "),
		'type': fields.char('Type', placeholder="RAID 1"),
		'format': fields.char('Format', placeholder="ext4"),
		'mount_ids': fields.one2many('it.equipment.partition.mount','partition_id','Mount on this partition'),
    
    }
    
it_equipment_partition()


class it_equipment_partition_mount(osv.osv):
    
    _name = 'it.equipment.partition.mount'

    _description = 'Partition Mounts'

    _columns = {
    
		'partition_id': fields.many2one('it.equipment.partition','Partition', ondelete='cascade'),
		'name': fields.char('Name'),
		'size': fields.char('Size'),
    
    }
    
it_equipment_partition_mount()
