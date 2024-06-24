from datetime import datetime
from sqlalchemy.orm import Session
from app.config.database import engine
from app.models.category import Category
from app.models.location import Location
from app.models.location_category_reviewed import LocationCategoryReviewed
from app.models.user import User


def initial_seeding(custom_engine=None):
    """
    Populate database tables defined in the application.
    """
    session_engine = custom_engine if custom_engine else engine
    with Session(bind=session_engine) as session:
        member = User(name="Miguel Briceño", email="mbriceno-2024@gmail.com")

        category1 = Category(
            name="Restaurantes",
            description="-----*****-----"
        )
        category2 = Category(
            name="Estaciones de Servicio", description="-----*****-----"
        )
        category3 = Category(name="Parques", description="-----*****-----")
        category4 = Category(name="Museos", description="-----*****-----")

        location1 = Location(
            name="Coma y Beba",
            latitude="7.8877313428941145",
            longitude="-72.49957719536566",
        )
        location2 = Location(
            name="La Salsa Burger",
            latitude="7.83159555765349",
            longitude="-72.5071343772019",
        )
        location3 = Location(
            name="ES Las Cruces",
            latitude="7.866558544842614",
            longitude="-72.49725433906248",
        )
        location4 = Location(
            name="ES Multi Servicios",
            latitude="7.866558544842614",
            longitude="-72.49725433906248",
        )
        location5 = Location(
            name="MET Cucuta",
            latitude="7.884957699142827",
            longitude="-72.50671762480196",
        )
        location6 = Location(
            name="Casa Rosada Cucuta",
            latitude="7.884957699142827",
            longitude="-72.50971762480196",
        )
        location7 = Location(
            name="Parque Lora",
            latitude="7.894957699142827",
            longitude="-72.51971762480196",
        )
        location8 = Location(
            name="Parque Colsag",
            latitude="7.884357619142827",
            longitude="-72.60971962480196",
        )

        location9 = Location(
            name="Pare y Coma",
            latitude="7.8877313428941145",
            longitude="-72.49957719536566",
        )
        location10 = Location(
            name="El Gran Corrientazo",
            latitude="7.8877313428941145",
            longitude="-72.49957719536566",
        )
        location11 = Location(
            name="ES Punto Largo",
            latitude="7.8877313428941145",
            longitude="-72.49957719536566",
        )
        location12 = Location(
            name="ES Las Macarenas",
            latitude="7.8877313428941145",
            longitude="-72.49957719536566",
        )
        location13 = Location(
            name="Parque Paramo",
            latitude="7.8877313428941145",
            longitude="-72.49957719536566",
        )
        location14 = Location(
            name="Parque Nacional El Nevado",
            latitude="7.8877313428941145",
            longitude="-72.49957719536566",
        )
        location15 = Location(
            name="Museo de Arte Contemporaneo",
            latitude="7.8877313428941145",
            longitude="-72.49957719536566",
        )
        location16 = Location(
            name="Sala Zulima",
            latitude="7.8877313428941145",
            longitude="-72.49957719536566",
        )

        session.add_all(
            [
                member,
                category1,
                category2,
                category3,
                category4,
                location1,
                location2,
                location3,
                location4,
                location5,
                location6,
                location7,
                location8,
                location9,
                location10,
                location11,
                location12,
                location13,
                location14,
                location15,
                location16,
            ]
        )

        session.commit()

        session.add_all(
            [
                LocationCategoryReviewed(
                    category_id=category1.id,
                    location_id=location1.id,
                    visit=0,
                    last_visit=None,
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category1.id,
                    location_id=location2.id,
                    visit=0,
                    last_visit=None,
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category2.id,
                    location_id=location3.id,
                    visit=0,
                    last_visit=None,
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category2.id,
                    location_id=location4.id,
                    visit=1,
                    last_visit=datetime.strptime(
                        "06/04/24 13:55:26", "%d/%m/%y %H:%M:%S"
                    ),
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category3.id,
                    location_id=location7.id,
                    visit=1,
                    last_visit=datetime.strptime(
                        "06/04/24 13:55:26", "%d/%m/%y %H:%M:%S"
                    ),
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category3.id,
                    location_id=location8.id,
                    visit=2,
                    last_visit=datetime.strptime(
                        "06/04/24 13:55:26", "%d/%m/%y %H:%M:%S"
                    ),
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category4.id,
                    location_id=location5.id,
                    visit=2,
                    last_visit=datetime.strptime(
                        "26/05/24 18:55:26", "%d/%m/%y %H:%M:%S"
                    ),
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category4.id,
                    location_id=location6.id,
                    visit=3,
                    last_visit=datetime.strptime(
                        "26/05/24 13:55:26", "%d/%m/%y %H:%M:%S"
                    ),
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category1.id,
                    location_id=location9.id,
                    visit=3,
                    last_visit=datetime.strptime(
                        "27/05/24 13:55:26", "%d/%m/%y %H:%M:%S"
                    ),
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category1.id,
                    location_id=location10.id,
                    visit=4,
                    last_visit=datetime.strptime(
                        "29/05/24 13:55:26", "%d/%m/%y %H:%M:%S"
                    ),
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category2.id,
                    location_id=location11.id,
                    visit=4,
                    last_visit=datetime.strptime(
                        "05/06/24 13:55:26", "%d/%m/%y %H:%M:%S"
                    ),
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category2.id,
                    location_id=location12.id,
                    visit=5,
                    last_visit=datetime.strptime(
                        "11/06/24 13:55:26", "%d/%m/%y %H:%M:%S"
                    ),
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category3.id,
                    location_id=location13.id,
                    visit=5,
                    last_visit=datetime.strptime(
                        "18/06/24 13:55:26", "%d/%m/%y %H:%M:%S"
                    ),
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category3.id,
                    location_id=location14.id,
                    visit=6,
                    last_visit=datetime.strptime(
                        "19/06/24 13:55:26", "%d/%m/%y %H:%M:%S"
                    ),
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category4.id,
                    location_id=location15.id,
                    visit=6,
                    last_visit=datetime.strptime(
                        "19/06/24 13:55:26", "%d/%m/%y %H:%M:%S"
                    ),
                    user_id=member.id
                ),
                LocationCategoryReviewed(
                    category_id=category4.id,
                    location_id=location16.id,
                    visit=7,
                    last_visit=datetime.strptime(
                        "19/06/24 13:55:26", "%d/%m/%y %H:%M:%S"
                    ),
                    user_id=member.id
                ),
            ]
        )

        session.commit()
