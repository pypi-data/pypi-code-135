from uuid import UUID

from dijkstar import Graph, find_path, NoPathError
from django.contrib.contenttypes.models import ContentType
from django.forms import ValidationError
from django.db.models import Count, Q

from nautobot.dcim.choices import CableTypeChoices
from nautobot.dcim.models import Device, FrontPort, RearPort, Rack, Cable


class CablePath:
    def __init__(self, termination_a, termination_a_type, termination_b, termination_b_type, cable_inp):
        self.termination_a = termination_a
        self.termination_b = termination_b
        self.termination_a_type = termination_a_type
        self.termination_b_type = termination_b_type

        rack_list = [self.termination_a.device.rack]
        cable_list = []

        cables_to_pop = [*cable_inp]
        cable_objs = Cable.objects.filter(id__in=cable_inp).prefetch_related("_termination_a_device__rack",
                                                                             "_termination_b_device__rack")
        while len(cables_to_pop) > 0:

            next_cable = None
            is_swapped = False
            for c_id in cables_to_pop:
                c = next(filter(lambda co: co.id == UUID(c_id), cable_objs))
                if c.termination_a.device.rack == rack_list[-1]:
                    next_cable = c
                    is_swapped = False
                elif c.termination_b.device.rack == rack_list[-1]:
                    next_cable = c
                    is_swapped = True

            cable_list.append(next_cable)
            rack_list.append(
                next_cable.termination_a.device.rack if is_swapped else next_cable.termination_b.device.rack)
            cables_to_pop.pop(cables_to_pop.index(str(next_cable.id)))

        self.rack_list = rack_list
        self.cable_list = cable_list

    def get_renderable_path(self):
        needed_cables = self.get_needed_cables()

        # needed_cables and self.cable_list are sorted and only needs to be zipped for a complete cable trace.
        # Afterwards, we only need to add interfaces and devices for a neat trace.

        intermediate_elements = list()

        open_element = {
            "device": self.termination_a.device,
        }

        # We use UUIDs, so we do only compare for the same UUID, we do not care about the type, should fit anyways.

        cable_list = [*self.cable_list]

        if self.termination_a_type.app_label == "dcim" and self.termination_a_type.model == "interface":
            fp_to_interface_cable = needed_cables.pop(0)

            is_swapped = fp_to_interface_cable['termination_b'].device == open_element['device']
            intermediate_elements.append({
                **open_element,
                "attachment_b": fp_to_interface_cable['termination_b'] if is_swapped else fp_to_interface_cable['termination_a'],
            })

            intermediate_elements.append({
                "needed_cable": fp_to_interface_cable,
            })

            next_attachment_point = fp_to_interface_cable['termination_b'] if not is_swapped else fp_to_interface_cable['termination_a']

            open_element = {
                "attachment_a": next_attachment_point,
                "device": next_attachment_point.device,
            }
        elif self.termination_a_type.app_label == "dcim" and self.termination_a_type.model == "frontport":
            open_element["attachment_a"] = self.termination_a

        prepended_cable = None
        if self.termination_b_type.app_label == "dcim" and self.termination_b_type.model == "interface":
            prepended_cable = needed_cables.pop()


        for i, next_existing_cable in enumerate(cable_list):

            is_swapped = next_existing_cable.termination_b.device == open_element['device']

            open_element["attachment_b"] = next_existing_cable.termination_b if is_swapped else \
                next_existing_cable.termination_a

            intermediate_elements.append(open_element)

            intermediate_elements.append({
                "cable": next_existing_cable
            })

            next_attachment_point = next_existing_cable.termination_a if is_swapped else next_existing_cable.termination_b
            open_element = {
                "attachment_a": next_attachment_point,
                "device": next_attachment_point.device,
            }

            if i >= len(needed_cables):
                continue

            needed_cable = needed_cables[i]

            is_swapped = needed_cable['termination_b'].device == open_element['device']
            intermediate_elements.append({
                **open_element,
                "attachment_b": needed_cable['termination_b'] if is_swapped else needed_cable['termination_a'],
            })

            intermediate_elements.append({
                "needed_cable": needed_cable,
            })

            next_attachment_point = needed_cable['termination_b'] if not is_swapped else needed_cable['termination_a']

            open_element = {
                "attachment_a": next_attachment_point,
                "device": next_attachment_point.device,
            }

        if prepended_cable:

            is_swapped = prepended_cable['termination_b'].device == open_element['device']
            intermediate_elements.append({
                **open_element,
                "attachment_b": prepended_cable['termination_b'] if is_swapped else prepended_cable['termination_a'],
            })

            intermediate_elements.append({
                "needed_cable": prepended_cable,
            })

            next_attachment_point = prepended_cable['termination_b'] if not is_swapped else prepended_cable['termination_a']

            open_element = {
                "attachment_a": next_attachment_point,
                "device": next_attachment_point.device,
            }
        else:
            open_element["attachment_b"] = self.termination_b


        if open_element:
            intermediate_elements.append(open_element)

        return intermediate_elements

    def get_needed_cables(self):

        rearport_uuids = list()
        for c in self.cable_list:
            rearport_uuids.append(c.termination_a_id)
            rearport_uuids.append(c.termination_b_id)

        devices = Device.objects.filter(rearports__in=rearport_uuids)
        needed_cables = list()

        for rack in self.rack_list:

            if rack.id == self.termination_a.device.rack.id and self.termination_a_type.app_label == "dcim" and self.termination_a_type.model == "frontport":
                # We need no first cable to the FP, we ware already at the FP.
                continue
            elif rack.id == self.termination_b.device.rack.id and self.termination_b_type.app_label == "dcim" and self.termination_b_type.model == "frontport":
                # We need no first cable to the FP, we ware already at the FP.
                continue
            elif rack.id == self.termination_a.device.rack.id:
                # Start Rack
                pp_device = next(filter(lambda d: d.rack.id == rack.id, devices))
                fp_to_use = pp_device.frontports.filter(cable=None, rear_port__in=rearport_uuids).first()

                if not fp_to_use:
                    raise ValidationError(f"{pp_device} has no free ports.")

                needed_cables.append({
                    "termination_a_type": ContentType.objects.get_for_model(self.termination_a),
                    "termination_a_id": self.termination_a.id,
                    "termination_a": self.termination_a,
                    "termination_b_type": ContentType.objects.get_for_model(fp_to_use),
                    "termination_b_id": fp_to_use.id,
                    "termination_b": fp_to_use
                })
            elif rack.id == self.termination_b.device.rack.id:
                # Destination Rack
                pp_device = next(filter(lambda d: d.rack.id == rack.id, devices))
                fp_to_use = pp_device.frontports.filter(cable=None, rear_port__in=rearport_uuids).first()

                if not fp_to_use:
                    raise ValidationError(f"{pp_device} has no free ports.")

                needed_cables.append({
                    "termination_a_type": ContentType.objects.get_for_model(fp_to_use),
                    "termination_a_id": fp_to_use.id,
                    "termination_a": fp_to_use,
                    "termination_b_type": ContentType.objects.get_for_model(self.termination_b),
                    "termination_b_id": self.termination_b.id,
                    "termination_b": self.termination_b
                })
            else:
                # Hop Rack
                rack_devices = list(filter(lambda d: d.rack.id == rack.id, devices))
                fp1_to_use = FrontPort.objects.filter(cable=None, device=rack_devices[0],
                                                      rear_port__in=rearport_uuids).first()
                fp2_to_use = FrontPort.objects.filter(cable=None, device=rack_devices[1],
                                                      rear_port__in=rearport_uuids).first()

                if not fp1_to_use:
                    raise ValidationError(f"{rack_devices[0]} has no free ports.")
                if not fp2_to_use:
                    raise ValidationError(f"{rack_devices[1]} has no free ports.")

                needed_cables.append({
                    "termination_a_type": ContentType.objects.get_for_model(fp1_to_use),
                    "termination_a_id": fp1_to_use.id,
                    "termination_a": fp1_to_use,
                    "termination_b_type": ContentType.objects.get_for_model(fp2_to_use),
                    "termination_b_id": fp2_to_use.id,
                    "termination_b": fp2_to_use,
                })
        return needed_cables


class CableRouter:

    def __init__(self, termination_a, termination_a_type, termination_b, termination_b_type, media_type):
        self.termination_a = termination_a
        self.termination_b = termination_b

        self.allowed_cable_types = None
        if media_type == "fiber_sm":
            self.allowed_cable_types = [
                CableTypeChoices.TYPE_SMF,
                CableTypeChoices.TYPE_SMF_OS1,
                CableTypeChoices.TYPE_SMF_OS2,
            ]
        elif media_type == "fiber_mm":
            self.allowed_cable_types = [
                CableTypeChoices.TYPE_MMF,
                CableTypeChoices.TYPE_MMF_OM1,
                CableTypeChoices.TYPE_MMF_OM2,
                CableTypeChoices.TYPE_MMF_OM3,
                CableTypeChoices.TYPE_MMF_OM4,
            ]
        elif media_type == "copper":
            self.allowed_cable_types = [
                CableTypeChoices.TYPE_CAT3,
                CableTypeChoices.TYPE_CAT5,
                CableTypeChoices.TYPE_CAT5E,
                CableTypeChoices.TYPE_CAT6,
                CableTypeChoices.TYPE_CAT6A,
                CableTypeChoices.TYPE_CAT7,
                CableTypeChoices.TYPE_CAT7A,
                CableTypeChoices.TYPE_CAT8,
            ]

        excluded_cable_ids = list()
        if termination_a_type.app_label == "dcim" and termination_a_type.model == "frontport":
            rps_to_exclude = RearPort.objects.filter(device=self.termination_a.device)
            for rp in rps_to_exclude:
                if termination_a.rear_port != rp and rp.cable:
                    excluded_cable_ids.append(rp.cable.id)

        if termination_b_type.app_label == "dcim" and termination_b_type.model == "frontport":
            rps_to_exclude = RearPort.objects.filter(device=self.termination_b.device)
            for rp in rps_to_exclude:
                if termination_b.rear_port != rp and rp.cable:
                    excluded_cable_ids.append(rp.cable.id)

        possible_edges = Cable.objects.raw(
            '''
                SELECT c.*, d_a.rack_id as termination_a_rack_id, d_b.rack_id as termination_b_rack_id FROM dcim_cable c
                LEFT JOIN django_content_type ct_a ON ct_a.id = termination_a_type_id
                LEFT JOIN django_content_type ct_b ON ct_b.id = termination_b_type_id
                LEFT JOIN dcim_rearport rp_a ON rp_a.id = termination_a_id
                LEFT JOIN dcim_rearport rp_b ON rp_b.id = termination_b_id
                INNER JOIN dcim_frontport fp_a ON fp_a.rear_port_id = rp_a.id AND fp_a.cable_id IS NULL
                INNER JOIN dcim_frontport fp_b ON fp_b.rear_port_id = rp_b.id AND fp_b.cable_id IS NULL
                LEFT JOIN dcim_device d_a ON rp_a.device_id = d_a.id
                LEFT JOIN dcim_device d_b ON rp_b.device_id = d_b.id
                WHERE (
                    c.type = ANY(%s) AND
                    NOT c.id = ANY(%s) AND 
                    ct_a.app_label = 'dcim' AND ct_a.model = 'rearport' AND
                    ct_b.app_label = 'dcim' AND ct_b.model = 'rearport' AND
                    fp_a.cable_id IS NULL and fp_b.cable_id IS NULL
                )
            ''',
            [self.allowed_cable_types, excluded_cable_ids]
        )

        self.graph = Graph()
        for edge in possible_edges:
            self.graph.add_edge(edge.termination_a_rack_id, edge.termination_b_rack_id, edge.id)
            self.graph.add_edge(edge.termination_b_rack_id, edge.termination_a_rack_id, edge.id)

    def get_devices_for_hop_list(self, hop_list):
        devices = Device.objects.filter(id__in=hop_list)
        return list(map(lambda h: next(filter(lambda d: d.id == h, devices)), hop_list))

    def get_path(self):

        if self.termination_a.device.rack.id == self.termination_b.device.rack.id:
            raise ValidationError(
                f"{self.termination_a.device} and {self.termination_b.device} are located within the same rack")

        try:
            path = find_path(
                self.graph,
                self.termination_a.device.rack.id,
                self.termination_b.device.rack.id,
                cost_func=lambda a, b, c, d: 1
            )
        except NoPathError:
            raise ValidationError(
                f"No path available between {self.termination_a.device} and {self.termination_b.device}")

        return path.edges
