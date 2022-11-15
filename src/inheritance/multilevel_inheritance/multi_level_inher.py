from src.inheritance.multilevel_inheritance.two_wheeler import TwoWheeler

tw = TwoWheeler('bike', True)
# tw.set_vehicle_object()
print(tw.two_wheeler_object.get_name())
print(tw.two_wheeler_object.get_milage())