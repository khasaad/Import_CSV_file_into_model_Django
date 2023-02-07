import pytest

from django.test import Client
from norme.models import norme

# we only have one model to test. 
# We are going to use the create() function, which precisely returns the instance of the model when inserting the data into the database.

@pytest.mark.django_db  
def test_norm_model():
    client = Client()
    norme1 = Norme.objects.create(
               numdos = "DD237051",
               numdosverling = "DD237051",
               ancart = "LNEN50289-1-3",
               filiere = "ETR",
               etape = "60.62",
               verling = "E",
               formats = "PDFC")

    response = client.get(f"/norms/{norm1.id}/")
    
    assert response.status_code == 200

    assert response.json() == {
        "id": 1,
        "numdos" = "DD237051",
        "numdosverling" = "DD237051",
        "ancart" = "LNEN50289-1-3",
        "filiere" = "ETR",
        "etape" = 60.62,
        "verling" = "E",
        "formats" = "PDFC"
        }
