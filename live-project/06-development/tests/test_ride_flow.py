def test_guest_booking_with_mobile_only(client) -> None:
    response = client.post(
        "/guest",
        data={
            "mobile": "9876543210",
            "city": "Bengaluru",
            "sport": "Badminton",
            "venue_name": "Guest Court",
            "game_starts_at": "2026-10-03T09:00",
        },
        follow_redirects=False,
    )
    assert response.status_code == 303
    confirm = client.get(response.headers["location"])
    assert confirm.status_code == 200
    assert b"Request cab to venue" in confirm.content


def test_e2e_player_creates_ride_request(client) -> None:
    book = client.post(
        "/",
        data={
            "player_name": "Alex",
            "contact": "9999999999",
            "city": "Bengaluru",
            "sport": "Badminton",
            "venue_name": "Playo Arena",
            "game_starts_at": "2026-10-01T18:00",
        },
        follow_redirects=False,
    )
    assert book.status_code == 303
    booking_id = book.headers["location"].split("/")[-1]

    confirm = client.get(f"/bookings/{booking_id}")
    assert confirm.status_code == 200
    assert b"Request cab to venue" in confirm.content

    ride = client.post(
        f"/bookings/{booking_id}/ride/new",
        data={"pickup_area": "Indiranagar"},
        follow_redirects=False,
    )
    assert ride.status_code == 303
    assert "/ride-requests/" in ride.headers["location"]

    confirmed = client.get(ride.headers["location"])
    assert confirmed.status_code == 200
    assert b"Manual pilot" in confirmed.content


def test_ops_status_update(client) -> None:
    client.post(
        "/",
        data={
            "player_name": "Sam",
            "contact": "8888888888",
            "city": "Bengaluru",
            "sport": "Badminton",
            "venue_name": "Court 1",
            "game_starts_at": "2026-10-02T10:00",
        },
        follow_redirects=True,
    )
    client.post(
        "/bookings/1/ride/new",
        data={"pickup_area": "HSR Layout"},
        follow_redirects=True,
    )

    login = client.post(
        "/ops/login",
        data={"username": "ops", "password": "test-ops-password"},
        follow_redirects=False,
    )
    assert login.status_code == 303

    update = client.post(
        "/ops/requests/1/status",
        data={"action": "whatsapp_sent", "ops_notes": "Driver Raj"},
        follow_redirects=False,
    )
    assert update.status_code == 303

    detail = client.get("/ops/requests/1")
    assert detail.status_code == 200
    assert b"WHATSAPP_SENT" in detail.content
