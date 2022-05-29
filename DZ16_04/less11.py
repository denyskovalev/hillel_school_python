#
#
# class Hotel:
#
#     def __init__(self, name):
#         self.name = name
#
#         self.available_rooms = {
#             i: {"visitor": None} for i in range(1, 11)
#         }
#
#     def book_room(self, customer, room):
#
#         if self.check_status(room) and self.check_visitor(customer):
#             self.available_rooms[room]["visitor"] = customer
#             customer.booking_list.append({
#                 "hotel": self.name,
#                 "room": room
#             })
#         else:
#             print("Some error")
#
#     def unbook_room(self, room):
#         if not self.check_status(room):
#             self.available_rooms[room]["visitor"] = None
#
#     def check_visitor(self, customer):
#         for key, value in self.available_rooms.items():
#             if value["visitor"] is customer:
#                 return False
#         return True
#
#     def check_status(self, room):
#         return self.available_rooms[room]["visitor"] is None
#
#
# class Visitor:
#
#     def __init__(self, name):
#         self.name = name
#         self.booking_list = []
#
#     def book_number(self, hotel, room):
#         status = hotel.check_status(room)
#
#         if status:
#             hotel.book_room(customer=self, room=room)
#         else:
#             print("Please book another room!")
#
#
# sirius = Hotel(name="Sirius")
# hilton = Hotel(name="Hilton")
#
# me = Visitor(name="Den")
#
# me.book_number(sirius, 3)
# me.book_number(hilton, 4)
#
# print(me.booking_list)


