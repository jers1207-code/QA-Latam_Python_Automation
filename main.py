import helpers
import data
class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
           print ('Conectado al servidor de Urban Routes')
        else:
            print ('No se puede conectar a Urban Routes, verifica que el servidor esté encendido.')
    def test_set_route (self):
        # Agregar en S9
        pass
    def test_select_plan (self):
        # Agregar en S9
        pass
    def test_fill_phone_number (self):
        # Agregar en S9
        pass
    def test_fill_card (self):
        # Agregar en S9
        pass
    def test_comment_for_driver (self):
        # Agregar en S9
        pass
    def test_order_blanket_and_handkerchiefs (self):
        # Agregar en S9
        pass
    def test_order_2_ice_creams (self):
        for j in range(2):
            # Agregar en S9
            pass
    def test_car_search_model_appears (self):
        # Agregar en S9
        pass
