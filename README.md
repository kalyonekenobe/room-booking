# room-booking
fido

Superuser:\n
username - admin\n
password - admin\n

Routes\n
users/ - Усі користувачі\n
users/create - Створити користувача
users/<user_id> - Інформація про користувача (можливість видалити)
rooms/ - Усі кімнати
rooms/create - Створити кімнату
rooms/<room_id> - Інформація про кімнату (можливість видалити)
rooms/<room_id>/meetings/?start_time=<YYYY-DD-MM>T<HH:MM>&end_time=<YYYY-DD-MM>T<HH:MM> - Усі бронювання для кімнати з id - room_id у проміжку між start_time i end_time
rooms/<room_id>/meetings/create - Створити бронювання для кімнати з room_id
